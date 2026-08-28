"""嵌套 for 循环练习。"""

# for day in range(1, 101):
#     print(f"今天是向小美表白的第 {day} 天，加油坚持")

#     for rose in range(1, 11):
#         print(f"给小美送第 {rose} 朵玫瑰花")

#     print(f"小美，我喜欢你（第 {day} 天的表白结束）")

# print("坚持 100 天，表白成功！")


# for i in range(1,10):
#     for j in range(i,i+1):
#         print(f"{j}*{i}={j*i}\t",end='')
#     print()



# for i in range(1,6):
#     print("语句1")
#     continue
#     print("语句2")


# for i in range(1,101):
#     print("语句1")
#     break
#     print("语句2")
# print("语句3")

# for i in range(1,6):
#     print("语句1")
#     for j in range(1,6):
#         print("语句2")
#         break
#         print("语句3")
#     print("语句4")


# 综合案例：
#定义账户余额变量
# money=10000
# num=range
# i=1
# #for循环对员工发放工资
# for i in range(1,21):
#     import random
#     score=random.randint(1,10)


#     if score<5:
#         print(f"员工{i}绩效{score},不满足，不发工资，下一位")
#         continue
#     #要判断余额足不足
#     if money >=1000:
#         money -=1000
#         print(f"员工{i},满足条件发放工资1000,公司账户余额:{money}")
#     else:
#         print(f"余额不足，")
#         break

# try-else语句
# try:
#     num=eval(input("请输入一个整数："))
#     print(num**2)
# except NameError:
#     print("输入错误，请输入一个整数！")


#函数封装避免重复编写
# def happy():
#     print("Happy birthday to you!")
# def happyB(name):
#     happy()
#     happy()
#     print("Happy birthday,dear {}!".format(name))
#     happy()
# happyB("Mike")
# print()
# happyB("Lily")



# name="xushuang"
# length=len(name)
# print(length)


# str1="itheima"
# str2="itcast"
# str3="python"
# count=0
# for i in str1:
#     count +=1
# print(f"字符串{str1}的长度是：{count}")
# count=0
# for i in str2:
#     count +=1
# print(f"字符串{str2}的长度是：{count}")
# count=0
# for i in str3:
#     count +=1
# print(f"字符串{str3}的长度是：{count}")


# def my_len(data):
#     count=0
#     for i in data:
#         count +=1
#     print(f"字符串{data}的长度是{count}")


# my_len(str1)
# my_len(str2)
# my_len(str3)



# def say_hi():
#     print("hello world")
# say_hi() 


# def check():
#     print("欢迎来到python世界")
# check()   


# def add(x,y):
#     result=x+y
#     print(f"{x}+{y}的计算结果是：{result}")
# add(1,2)



#自动查核酸
# def check(num):
#     print("欢迎来到腾讯健康排查系统")
#     if num<=37.5:
#         print(f"体温测量中，您的体温是:{num}度，体温正常")
#     else:
#         print(f"体温测量中，您的体温是:{num}度，体温异常，需要隔离14天")
# check(36.5)    
    




        
    


