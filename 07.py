"""主机自动巡检与安全的临时文件清理工具。

仅使用 Python 标准库，适合在 Windows/Linux/macOS 上运行。
默认只读检查；清理操作必须显式传入 ``--cleanup-temp``。

设计参考（仅借鉴公开项目的通用实践，未复制其代码）：
* https://github.com/giampaolo/psutil
* https://github.com/pablomenino/server-health-check
* https://github.com/StackStorm/st2
"""

from __future__ import annotations

import argparse
import ctypes
import csv
import json
import logging
import os
import platform
import shutil
import socket
import subprocess
import sys
import tempfile
import time
import urllib.request
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

LOGGER = logging.getLogger("ops-check")


@dataclass
class CheckResult:
    name: str
    status: str
    value: Any
    message: str


def _memory_usage() -> tuple[float | None, int | None, int | None]:
    """返回 (使用率, 已用字节, 总字节)，无法读取时返回 None。"""
    if sys.platform == "win32":
        class MemoryStatus(ctypes.Structure):
            _fields_ = [("length", ctypes.c_ulong), ("memory_load", ctypes.c_ulong),
                        ("total_phys", ctypes.c_ulonglong), ("avail_phys", ctypes.c_ulonglong),
                        ("total_page", ctypes.c_ulonglong), ("avail_page", ctypes.c_ulonglong),
                        ("total_virtual", ctypes.c_ulonglong), ("avail_virtual", ctypes.c_ulonglong),
                        ("avail_extended", ctypes.c_ulonglong)]
        status = MemoryStatus()
        status.length = ctypes.sizeof(status)
        if ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(status)):
            used = status.total_phys - status.avail_phys
            return status.memory_load, used, status.total_phys
    else:
        try:
            values: dict[str, int] = {}
            with open("/proc/meminfo", encoding="utf-8") as stream:
                for line in stream:
                    key, value = line.split(":", 1)
                    values[key] = int(value.strip().split()[0]) * 1024
            total = values["MemTotal"]
            available = values.get("MemAvailable", values.get("MemFree", 0))
            return (total - available) * 100 / total, total - available, total
        except (FileNotFoundError, KeyError, ValueError, OSError):
            pass
    return None, None, None


def _cpu_usage() -> float | None:
    """优先使用 psutil；Windows 上回退到 PowerShell/WMI。"""
    try:
        import psutil  # type: ignore
        return float(psutil.cpu_percent(interval=0.2))
    except (ImportError, OSError):
        pass
    if sys.platform == "win32":
        command = ["powershell", "-NoProfile", "-NonInteractive", "-Command",
                   "(Get-CimInstance Win32_Processor | Measure-Object -Property LoadPercentage -Average).Average"]
        try:
            result = subprocess.run(command, capture_output=True, text=True, timeout=5, check=False)
            return float(result.stdout.strip())
        except (OSError, ValueError, subprocess.TimeoutExpired):
            return None
    try:
        return min(100.0, os.getloadavg()[0] * 100 / max(os.cpu_count() or 1, 1))
    except (AttributeError, OSError):
        return None


def check_disk(path: Path, threshold: float) -> CheckResult:
    try:
        usage = shutil.disk_usage(path)
        percent = usage.used * 100 / usage.total
        return CheckResult("disk", "FAIL" if percent >= threshold else "PASS", round(percent, 1),
                           f"{path} 已使用 {percent:.1f}% ({usage.free / 2**30:.1f} GiB 可用)")
    except OSError as exc:
        return CheckResult("disk", "ERROR", None, f"无法读取 {path}: {exc}")


def check_memory(threshold: float) -> CheckResult:
    percent, used, total = _memory_usage()
    if percent is None:
        return CheckResult("memory", "SKIP", None, "当前平台无法读取物理内存信息")
    return CheckResult("memory", "FAIL" if percent >= threshold else "PASS",
                       {"percent": round(percent, 1), "used_bytes": used, "total_bytes": total},
                       f"内存已使用 {percent:.1f}%")


def check_cpu(threshold: float) -> CheckResult:
    percent = _cpu_usage()
    if percent is None:
        return CheckResult("cpu", "SKIP", None, "无法获取 CPU 使用率（可安装 psutil 提升兼容性）")
    return CheckResult("cpu", "FAIL" if percent >= threshold else "PASS", round(percent, 1),
                       f"CPU 使用率 {percent:.1f}%")


def check_network(url: str, timeout: float) -> CheckResult:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        return CheckResult("network", "ERROR", None, f"URL 必须是 http/https 地址: {url}")
    started = time.perf_counter()
    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            elapsed = (time.perf_counter() - started) * 1000
            return CheckResult("network", "PASS", {"status_code": response.status, "latency_ms": round(elapsed, 1)},
                               f"{url} 响应 {response.status}，延迟 {elapsed:.0f} ms")
    except Exception as exc:  # 网络检查不应中断其他巡检项
        return CheckResult("network", "FAIL", None, f"无法访问 {url}: {exc}")


def check_tcp(target: str, timeout: float) -> CheckResult:
    try:
        host, port_text = target.rsplit(":", 1)
        port = int(port_text)
        if not host or not 1 <= port <= 65535:
            raise ValueError
    except ValueError:
        return CheckResult("tcp", "ERROR", target, f"目标格式应为 host:port: {target}")
    started = time.perf_counter()
    try:
        with socket.create_connection((host, port), timeout=timeout):
            elapsed = (time.perf_counter() - started) * 1000
        return CheckResult("tcp", "PASS", {"target": target, "latency_ms": round(elapsed, 1)},
                           f"TCP {target} 连接成功，耗时 {elapsed:.0f} ms")
    except OSError as exc:
        return CheckResult("tcp", "FAIL", target, f"TCP {target} 连接失败: {exc}")


def check_process(name: str) -> CheckResult:
    wanted = name.casefold()
    try:
        import psutil  # type: ignore
        for process in psutil.process_iter(["name", "exe"]):
            current = (process.info.get("name") or "").casefold()
            if current == wanted or Path(current).name == wanted:
                return CheckResult("process", "PASS", name, f"进程正在运行: {name}")
        return CheckResult("process", "FAIL", name, f"未找到进程: {name}")
    except ImportError:
        command = ["tasklist", "/fo", "csv", "/nh"] if sys.platform == "win32" else ["ps", "-A", "-o", "comm="]
        try:
            result = subprocess.run(command, capture_output=True, text=True, timeout=5, check=False)
            names = ([row[0].casefold() for row in csv.reader(result.stdout.splitlines()) if row]
                     if sys.platform == "win32" else
                     [line.strip().casefold() for line in result.stdout.splitlines() if line.strip()])
            found = any(current == wanted or Path(current).name == wanted for current in names)
            return CheckResult("process", "PASS" if found else "FAIL", name,
                               f"进程正在运行: {name}" if found else f"未找到进程: {name}")
        except (OSError, subprocess.TimeoutExpired) as exc:
            return CheckResult("process", "ERROR", name, f"进程检查失败: {exc}")


def check_paths(paths: list[Path]) -> list[CheckResult]:
    return [CheckResult("path", "PASS" if path.exists() else "FAIL", str(path),
                         f"路径存在: {path}" if path.exists() else f"路径不存在: {path}") for path in paths]


def cleanup_temp(older_than_hours: float, dry_run: bool) -> tuple[int, int, list[str]]:
    cutoff = time.time() - older_than_hours * 3600
    scanned = removed = 0
    errors: list[str] = []
    for item in Path(tempfile.gettempdir()).resolve().rglob("*"):
        try:
            if not item.is_file() or item.is_symlink() or item.stat().st_mtime >= cutoff:
                continue
            scanned += 1
            if not dry_run:
                item.unlink()
            removed += 1
        except OSError as exc:
            errors.append(f"{item}: {exc}")
    return scanned, removed, errors


def run_checks(args: argparse.Namespace) -> list[CheckResult]:
    results = [CheckResult("host", "PASS", platform.node(), f"主机 {platform.node()}，系统 {platform.platform()}"),
               check_disk(Path(args.disk_path), args.disk_threshold), check_memory(args.memory_threshold),
               check_cpu(args.cpu_threshold)]
    if not args.skip_network:
        results.append(check_network(args.url, args.timeout))
    results.extend(check_tcp(target, args.timeout) for target in args.tcp)
    results.extend(check_process(name) for name in args.process)
    results.extend(check_paths([Path(p) for p in args.path]))
    return results


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="标准库实现的主机自动巡检工具")
    parser.add_argument("--disk-path", default=Path.cwd(), help="磁盘检查路径，默认当前目录")
    parser.add_argument("--disk-threshold", type=float, default=90, help="磁盘使用率告警阈值（%%）")
    parser.add_argument("--memory-threshold", type=float, default=90, help="内存使用率告警阈值（%%）")
    parser.add_argument("--cpu-threshold", type=float, default=90, help="CPU 使用率告警阈值（%%）")
    parser.add_argument("--url", default="https://www.baidu.com", help="网络连通性检查地址")
    parser.add_argument("--timeout", type=float, default=5, help="网络超时时间（秒）")
    parser.add_argument("--skip-network", action="store_true", help="跳过网络检查")
    parser.add_argument("--path", action="append", default=[], help="要确认存在的路径，可重复传入")
    parser.add_argument("--tcp", action="append", default=[], metavar="HOST:PORT", help="检查 TCP 端口，可重复传入")
    parser.add_argument("--process", action="append", default=[], metavar="NAME", help="检查进程名，可重复传入")
    parser.add_argument("--json", action="store_true", help="以 JSON 输出结果")
    parser.add_argument("--watch", type=float, metavar="SECONDS", help="按间隔持续巡检")
    parser.add_argument("--cleanup-temp", action="store_true", help="清理系统临时目录中的旧文件")
    parser.add_argument("--older-than-hours", type=float, default=24, help="清理文件年龄，默认 24 小时")
    parser.add_argument("--dry-run", action="store_true", help="仅显示将清理的文件数量，不实际删除")
    parser.add_argument("--log-file", type=Path, help="可选日志文件路径")
    parser.add_argument("--report-file", type=Path, help="将最近一次 JSON 报告写入文件")
    parser.add_argument("--version", action="version", version="07.py 2.0")
    return parser


def write_report(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp-{os.getpid()}")
    temporary.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    os.replace(temporary, path)


def main() -> int:
    args = build_parser().parse_args()
    if any(value <= 0 for value in (args.timeout, args.older_than_hours)):
        raise SystemExit("--timeout 和 --older-than-hours 必须大于 0")
    if args.watch is not None and args.watch <= 0:
        raise SystemExit("--watch 必须大于 0")
    if any(not 0 < value <= 100 for value in (args.disk_threshold, args.memory_threshold, args.cpu_threshold)):
        raise SystemExit("资源使用率阈值必须在 0 到 100 之间")
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s", filename=args.log_file)
    while True:
        started = time.perf_counter()
        results = run_checks(args)
        cleanup_info = cleanup_temp(args.older_than_hours, args.dry_run) if args.cleanup_temp else None
        failed = any(result.status in {"FAIL", "ERROR"} for result in results)
        payload = {"timestamp": datetime.now(timezone.utc).isoformat(), "host": platform.node(),
                   "duration_ms": round((time.perf_counter() - started) * 1000, 1),
                   "summary": {"total": len(results), "passed": sum(r.status == "PASS" for r in results),
                               "failed": sum(r.status in {"FAIL", "ERROR"} for r in results),
                               "skipped": sum(r.status == "SKIP" for r in results)},
                   "results": [asdict(r) for r in results]}
        if cleanup_info is not None:
            scanned, removed, errors = cleanup_info
            payload["cleanup"] = {"candidates": scanned, "removed": removed, "errors": errors}
        if args.report_file:
            try:
                write_report(args.report_file, payload)
            except OSError as exc:
                LOGGER.error("报告写入失败: %s", exc)
                failed = True
        if args.json:
            print(json.dumps(payload, ensure_ascii=False))
        else:
            print(f"\n巡检时间: {payload['timestamp']}")
            for result in results:
                print(f"[{result.status:5}] {result.message}")
            if cleanup_info is not None:
                mode = "预览" if args.dry_run else "清理"
                print(f"[{mode}] 扫描 {cleanup_info[0]} 个文件，处理 {cleanup_info[1]} 个")
                for error in cleanup_info[2]:
                    LOGGER.warning("清理失败: %s", error)
        if not args.watch:
            return 1 if failed else 0
        try:
            time.sleep(args.watch)
        except KeyboardInterrupt:
            print("\n已停止持续巡检。")
            return 0


if __name__ == "__main__":
    sys.exit(main())
