# def add(a,b):
#     result=a+b
#     return result
# print(add(1,2))


"""
无返回值函数
"""
# def say_hi():
#     print("hello world")
# result=say_hi()
# print(f"无返回值函数，返回的内容是:{result}")
# print(f"无返回值函数，返回的内容是:{type(result)}")

#主动返回none的函数
# def say_hi2():
#     print("hello world")
#     return None


# result=say_hi2()
# print(f"无返回值函数，返回的内容是:{result}")
# print(f"无返回值函数，返回的内容是:{type(result)}")


# def check_age(age):
#     if age>=18:
#         return "success"
#     else:
#         return None


# result=check_age(16)
# if not result:
#     print("未成年，不可以进入")


# def func_b():
#     print("----2----")
# def func_a():
#     print("----1----")
#     func_b()
#     print("----3----")
# func_a()


#演示全局变量
# num=200
# def test_a():
#     print(f"test_a:{num}")
# def test_b():
#     print(f"test_b:{num}")
# test_a()
# test_b()
# print(num)



#在全局中改局部
# num=200
# def test_a():
#     print(f"test_a:{num}")
# def test_b():
#     global num
#     num=300
#     print(f"test_b:{num}")
# test_a()
# test_b()
# print(num)



#ATM
# money=5000000
# name=None
# #要求客户输入姓名
# name=input("请输入你的姓名：")
# #定义查询函数
# def query(show_header):
#     if show_header:
#         print("查询余额")
#     print(f"{name}，你的余额是：{money}")

# #定义存款函数
# def saving(num):
#     global money
#     money+=num
#     print("存款")
#     print(f"{name},您好，您存款{num}元成功，当前余额为：{money}")
#     query(False)


# #定义取款函数
# def get_money(num):
#     global money
#     money-=num
#     print("取款")
#     print(f"{name},您好，您取款{num}元成功，当前余额为：{money}")

#     query(False)
# def main():
#    print("主菜单")
#    print(f"{name},您好，欢迎使用ATM系统")
#    print("查询余额\t[输入1]")
#    print("存款\t\t[输入2]")
#    print("取款\t\t[输入3]")
#    print("退出系统\t[输入4]")
#    return input("请输入您的选择：")
# while True:
#     keyboard_input=main()
#     if keyboard_input=="1":
#         query(True)
#         continue
#     elif keyboard_input=="2":
#         num=int(input("请输入存款金额："))
#         saving(num)
#         continue
#     elif keyboard_input=="3":
#         num=int(input("请输入取款金额："))
#         get_money(num)
#         continue
#     else:
#         print("退出系统")
#         print("欢迎下次光临")
#         break


#数据容器
# name_list=["张三","李四","王五"]
# print(name_list)


# 列表
# name_list=["张三","李四","王五"]
# print(name_list)
# print(type(name_list))


# #定义一个列表
# my_list=[1,2,3,4,5]
# print(my_list)
# print(type(my_list))
# my_list=[8,9,10]
# print(my_list)
# print(type(my_list))
# #定义一个嵌套的列表
# my_list=[[1,2,3],[4,5,6],[7,8,9]]
# print(my_list)
# print(type(my_list))


#通过索引访问列表元素，
# name_list=["张三","李四","王五"]
# print(name_list[0])
# print(name_list[1])
# print(name_list[2])
# print(name_list[-1])
# print(name_list[-2])
# print(name_list[-3])

#取出嵌套列表的元素
# my_list=[[1,2,3],[4,5,6],[7,8,9]]
# print(my_list[0][0])
# print(my_list[1][1])
# print(my_list[2][2])


# from operator import index


# mylist=["itcast","python","itheima"]
#1、查询列表中元素的索引
# index=mylist.index("python")
# print(f"python在列表中的索引是：{index}")
# index=mylist.index("hello")
# print(f"hello在列表中的索引是：{index}")
#2、修改特定下标索引的值
# mylist[0]="奶龙"
# print(f"修改后的列表是:{mylist}")
#3、在列表中插入新元素
# mylist.insert(1,"hello")
# print(f"插入后的列表是:{mylist}")
#4、在列表的尾部追加一个新元素
# mylist.append("yuansu")
# print("列表在追加元素后的结果是：",mylist)
#5、在列表的尾部追加一批新元素
# mylist2=[1,2,3]
# mylist.extend(mylist2)
# print(f"列表在追加元素后的结果是：{mylist}")
# 6、删除列表中的元素（2种方式）
#6.1、通过下标索引删除元素
# del mylist[3]
# print(f"删除列表元素后的结果是：{mylist}")
#6.2、列表pop（下标）
# mylist.pop(4)
# print(f"通过pop方法取出元素后列表内容:{mylist}")
#7、删除某元素在列表中的第一个匹配项
# mylist.remove("itcast")
# print(f"删除列表元素后的结果是：{mylist}")
#8、清空列表
# mylist.clear()
# print(f"清空列表后的结果是：{mylist}")
#9、统计列表内某元素的数量
# mylist=[1,1,1,2]
# count=mylist.count(1)
# print(f"列表中1的数量是:{count}")
#10、列表中全部的元素数量
# mylist=[1,1,1,2]
# count=len(mylist)
# print(f"列表中元素数量是:{count}")



"""
列表的使用
"""
# mylist=[21,25,21,23,22,20]
# mylist.append(31)
# mylist.extend([29,33,30])
# num1=mylist[0]
# print(f"从列表中取出第一个元素是：{num1}")
# num2=mylist[-1]
# print(f"从列表中取出最后一个元素是：{num2}")
# index=mylist.index(31)
# print(f"31在列表中的索引是:{index}")
# print(f"最后列表的内容是：{mylist}")



# 列表的遍历

# def list_while_func():
#     """
#     while循环遍历列表
#     """
#     my_list=[1,2,3,4,5]
#     index=0

#     while index<len(my_list):
#         element=my_list[index]
#         print(f"列表中的元素是：{element}")
#         index+=1 
# list_while_func()

# def list_for_func():
#     """
#     for循环遍历列表
#     """
#     mylist=[1,2,3,4,5]
#     for item in mylist:
#        print(f"列表中的元素是：{item}")
# list_for_func()


#取出列表中偶数
# def list_func():
#     """
#     取出列表中偶数
#     """
#     mylist=[1,2,3,4,5,6,7,8,9]
#     even_list=[]
#     for item in mylist:
#         if item%2==0:
#             even_list.append(item)
#             print(f"列表中的偶数是：{item}") 
# list_func()


#元组
# creature=("牛魔王","铁扇公主","红孩儿")
# print(creature)
# color=("red","green","blue",creature)
# print(color[2])
# print(color[3][1])



# 演示tuple元组的定义和操作

# t1=(1,"hello",True)
# t2=()
# t3=tuple()
# print(f"t1的类型是:{type(t1)}")
# print(f"t2的类型是:{type(t2)}")
# print(f"t3的类型是:{type(t3)}")

# t4=("hello",)
# print(f"t4的类型是:{type(t4)},t4的内容是:{t4}")  
#元组的嵌套
# t5=(1,2,3,(4,5,6))  
# print(f"t5的类型是:{type(t5)},t5的内容是:{t5}")
#下标索引去取出内容
# num=t5[3][2] 
# print(f"从嵌套元组中去除的数据是:{num}")
#元组的操作：index查找方法
# t6=(1,2,3,4,5,6)
# index=t6.index(4)
# print(f"在元组t6中查找4，的下标是:{index}")
# #元组的操作：count计数方法
# t7=(1,2,3,4,5,6,4,4,4)
# count=t7.count(4)
# print(f"在元组t7中查找4，出现的次数是:{count}")
# #元组的操作：len()函数
# t8=(1,2,3,4,5,6)
# count=len(t8)
# print(f"元组t8的长度是:{count}")
# #元组的遍历：while
# index=0
# while index<len(t8):
#     element=t8[index]
#     print(f"元组t8中的元素是:{element}")
#     index+=1
# #元组的遍历：for
# for item in t8:
#     print(f"元组t8中的元素是:{item}")
# #修改元组的内容
# t8[0]=100   
# print(f"修改元组t8后的结果是:{t8}")



#定义一个元组:元组不可修改但嵌套里列表中元素可以修改
# t9=(1,2,3,["hello","world"])
# print(f"t9的内容是:{t9}")
# t9[3][0]="helloworld"
# print(f"t9的内容是:{t9}")
# ls=[[2,3,7],[[3,5],25],[0,9]]
# print(len(ls))

