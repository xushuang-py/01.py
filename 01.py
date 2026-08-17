# # 导入mysql第三方库
# import pymysql

# def mysql_connect_demo():
#     # 1. 数据库连接配置（和你本地信息一一对应）
#     config = {
#         "host": "127.0.0.1",       # 本机地址
#         "port": 3306,               # mysql默认端口
#         "user": "root",             # 你的mysql账号，默认root
#         "password": "123456",  # 替换成你安装mysql设置的密码
#         "database": "my_test",      # 刚刚创建的数据库名
#         "charset": "utf8mb4"        # 编码，和建库保持一致
#     }

#     # 2. 建立数据库连接
#     try:
#         conn = pymysql.connect(**config)
#         # 创建游标：用来执行sql语句
#         cursor = conn.cursor()
#         print("✅ 数据库连接成功！")

#         # ========== 示例1：查询user_info全部数据 ==========
#         sql_select = "SELECT * FROM user_info;"
#         cursor.execute(sql_select)
#         # fetchall() 取出所有查询结果
#         result = cursor.fetchall()
#         print("\n查询到的全部用户数据：")
#         for row in result:
#             print(f"编号:{row[0]}  用户名:{row[1]}  密码:{row[2]}  创建时间:{row[3]}")

#         # ========== 示例2：新增一条用户数据 ==========
#         sql_insert = "INSERT INTO user_info(username,password) VALUES(%s,%s);"
#         # %s是占位符，防止SQL注入，不要直接拼接字符串
#         data = ("wangwu", "888888")
#         cursor.execute(sql_insert, data)
#         # 增删改操作必须提交事务，数据才会真正存入数据库
#         conn.commit()
#         print("\n✅ 新增用户成功！")

#         # ========== 示例3：条件查询 ==========
#         sql_find = "SELECT * FROM user_info WHERE username=%s;"
#         cursor.execute(sql_find, ("student",))
#         one_data = cursor.fetchone()
#         print(f"\n精准查询student：{one_data}")

#     except Exception as e:
#         # 出错回滚，撤销操作
#         conn.rollback()
#         print("❌ 连接/执行出错：", e)
#     finally:
#         # 无论成功失败，最后必须关闭游标和连接，释放资源
#         if "conn" in locals() and conn.open:
#             cursor.close()
#             conn.close()
#             print("\n🔒 数据库连接已关闭")


# # 调用函数运行
# if __name__ == "__main__":
#     mysql_connect_demo()