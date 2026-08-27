# s1="人生苦短”  “我用Python"  ",ok"
# print(s1)#字符串拼接
# msgs1="人生苦短"
# msgs2="我用Python"
# msgs3=",ok"
# print(msgs1+msgs2+msgs3) 

# 字符串格式化 %占位符
# s1="张三"
# s2=18
# s3="程序员"
# s4="编程"
# print("我是%s,今年%d岁,职业是%s,爱好是%s"%(s1,s2,s3,s4))#格式化输出
# name="爽哥"
# print(f"大家好，我是{name} ")#格式化输出
# s1="人生苦短" 
# s2="我用Python"
# print(f"{s1}{s2}")



# input()和int()函数
# name=input("请输入你的名字：")
# age=int(input("请输入你的年龄："))
# print(f"大家好，我是{name},今年{age}岁")

# 案例：银行卡ATM取钱
#账号总金额
# total=10000  # 账户初始余额（单位：元）

#输入密码
# password=input("请输入密码：")
# print(f"密码正确，{password}，请取钱")
#输入取钱金额
# number=int(input("请输入取钱金额："))
# print(f"取钱成功，取钱金额是：{number}")
#输出总金额
# print(f"总金额是：{total-number}")

# num1=int(input("请输入第一个数字："))
# num2=int(input("请输入第二个数字："))
# print(f"{num1}+{num2}={num1+num2}")

# 算术运算符
# x=int(input("请输入第一个数字："))
# y=int(input("请输入第二个数字："))
# print(f"{x}+{y}={x+y}")
# print(f"{x}-{y}={x-y}")

# 赋值运算符
# num=85
# num+=10
# print("num=num+10后,num的值=",num)#95

# num-=10
# print("num=num-10后,num的值=",num)#85

# num*=10
# print("num=num*10后,num的值=",num)#850

# num/=10
# print("num=num/10后,num的值=",num)#85.0

# num//=10
# print("num=num//10后,num的值=",num)#8.0

# num%=3
# print("num=num%10后,num的值=",num)#2.0

# num**=3
# print("num=num**10后,num的值=",num)#8.0

# 比较运算符
# 判断一个数是否为偶数还是奇数
# num=int(input("请输入一个数字："))
# if num%2==0:
#     print("偶数")
# else:
#     print("奇数")

# 逻辑运算符
# num=int(input("请输入一个数字："))
# print(f"{num}在1-10之间:",0<=num<=10)

#if语句
# age=int(input("请输入你的年龄："))
# print(f"你今年{age}岁")
# if age>=18:
#     print("我已经成年了")
#     print("即将步入大学")
# print("时间过得真快呀")

# input("欢迎来到黑马儿童游乐园，儿童免费，成人收费。")
# age=int(input("请输入你的年龄："))
# if age>=18:
#     print("您已成年，游玩需要补票10元")
# print("祝你游玩愉快")


# age=int(input("请输入你的年龄："))
# if age>=18:
#     print("您已成年，游玩需要补票10元")
# elif age>=6:
#     print("您已进入儿童游园，请勿bring any thing")
# else:
#     print("您未成年，请勿进入游园")


# 嵌套if语句不
# print("欢迎来到黑马动物园")
# if int(input("请输入你的身高："))>120:
#     print("你的身高大于120cm,不可以免费")
#     print("不过你的vip等级高于3级，可以免费")
#     if int(input("请输入你的vip等级："))>3:
#         print("恭喜你，可以免费")
#     else:
#         print("请支付10元")
# else:
#     print("欢迎你小朋友，可以免费游玩")


# 循环语句



