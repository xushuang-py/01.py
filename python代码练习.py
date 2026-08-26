#循环语句
#if循环
# import random

# num = random.randint(1, 10)
# guess_num=int(input("输入你要猜测的数字："))
# if guess_num==num:
#     print("恭喜，第一次就猜对了")
# else:
#     if guess_num>num:
#         print("你猜测的数字太大了")
#     else:
#         print("你猜测的数字太小了")


#     guess_num=int(input("再次输入你要猜测的数字："))

#     if guess_num==num:
#         print("恭喜，第二次猜对了")
#     else:
#         if guess_num>num:
#                 print("你猜测的数字太大了")
#         else:
#             print("你猜测的数字太小了")

# height,weight=eval(input("请输入身高(米)和体重(公斤)[逗号隔开]:"))
# bmi=weight / pow(height,2)
# print("BMI数值为:{:.2f}".format(bmi))
# who,dom="",""
# if bmi<18.5:
#     who="偏瘦"
# elif bmi<25:
#     who="正常"
# elif bmi<30:
#     who="偏胖"
# else:
#     who="肥胖"
# if bmi<18.5:
#     dom="偏瘦"
# elif bmi<24:
#     dom="正常"
# elif bmi<28:
#     dom="偏胖"
# else:
#     dom="肥胖"
# print("BMI指标为:国际‘{0}',国内'{1}'".format(who,dom))



# while循环:
# i=1
# while i <100:
#     print("小美，我喜欢你")
#     i +=1
# sum=0


# i=1
# while i<=100:
#     sum +=i
#     i +=1
# print(f"1-100累加的和是:{sum}")


# 获取范围在1-100的随机数字
# import random
# num=random.randint(1,100)
# #定义一个变量，总共猜测了多少次
# count=0
# #通过一个布尔类型的变量，做循环是否继续的标记
# flag=True
# while flag:
#     guess_num=int(input("请输入你猜测的数字："))
#     count +=1
#     if guess_num==num:
#         print("猜中了")
#         flag=False
#     else:
#         if guess_num>num:
#             print("你猜的大了")  
#         else:
#             print("你猜的小了")   
# print(f"你总共猜测了{count}次")


##while循环的嵌套
# i=1
# while i <=100:
#     print(f"今天是第{i}天,准备表白")
#     i+=1
#     print("小美，我喜欢你")
#     j=1
#     while j<=10:
#         print(f"送给小美第{j}只玫瑰花")
#         j+=1
# print(f"坚持到第{i-1}天，表白成功")


# name="itheima"
# for x in name:
#     print(x)


# name="itheima is a brand of itcast"
# count=0
# # for循环统计
# #for临时变量in被统计的数据
# for x in name:
#     if x=="a":
#         count +=1
# print(f"被统计的字符串中有{count}个a")


# range语句
# for i in range(5):
#     print(i)


