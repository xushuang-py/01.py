# print(666)
# print(pow(2, 3))
# print("祖国，你好")
# radius=25
# area=3.14*radius*radius
# print(area)
# print("{:.2f}".format(area))
# 斐波那契数列
# a,b=0,1
# while a<1000:
#     print(a)
#     a,b=b,a+b
# 同心圆
# import turtle
# turtle.pencolor("red")
# turtle.pensize(5)
# turtle.circle(10) 
# turtle.circle(40)
# turtle.circle(80)
# turtle.circle(160)
# 日期和时间的输出
# from datetime import datetime
# now = datetime.now()
# print(now)
# print(now.strftime("%x"))
# print(now.strftime("%X"))
# import turtle

# # 设置画笔
# t = turtle.Turtle()
# t.speed(2)
# t.color("red", "pink")  # 画笔红色，填充粉色

# t.begin_fill()
# # 爱心公式轨迹
# t.left(50)
# t.forward(133)
# t.circle(50, 200)
# t.right(140)
# t.circle(50, 200)
# t.forward(133)
# t.end_fill()

# # 文字
# t.penup()
# t.goto(0, -80)
# t.color("red")
# t.write("I love you", align="center", font=("Arial", 20, "bold"))

# turtle.done()  # 保持窗口打开
# str1=input("请输入一个人的名字：")
# str2=input("请输入一个国家的名字：")
# print("世界这么大，{}想去{}看看".format(str1,str2))
# n=input("请输入一个整数：")
# sum=0
# 九九乘法表
# for i in range(1,int(n)):
#     sum +=i+1
# print("1到N求和结果:",sum)
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{}x{}={}".format(i,j,i*j),end="\t")
#     print('')
# 1-10的阶乘和
# sum, temp = 0, 1
# for i  in range(1, 11):
#     temp *= i
#     sum += temp
# print("运算结果是:{}".format(sum))
# 猴子吃桃问题
# n=1
# for i in range(4,0,-1):
#     n=(n+1)<<1
# print(n)
# 字符串
# Tempstr="1200c"
# print(Tempstr[-1])
# print(Tempstr[0:-1])
# a=1
# a=2
# print(a)
# base,insr=20.7,50
# print("下个月的播放量是:",base+insr)
# 标识符
# 倒水案例实现两杯水里不同饮料互换   
# a=10
# b=20

# c=a#c=10
# a=b#a=20
# b=c#b=10
# print("a的值是:",a)
# print("b的值是:",b)
# a=100
# b=200
# c=300
# d=a
# a=c
# c=b
# b=d
# print(a,b,c,)






       