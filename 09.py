# my_str = "itheima and itcast"
# # 通过下标索引取值
# value = my_str[2]
# value2 = my_str[-16]
# print(f"从字符串{my_str}取下标为2的元素，值是：{value}")
# # index方法
# value = my_str.index("and")
# print(f"从字符串{my_str}中查找and，其起始下标是：{value}")
# # replace方法
# # new_str = my_str.replace("it", "程序")
# print(f"将字符串{my_str}中的it替换为程序,结果是:{new_my_str}")
#split方法
# my_str = "itheima and itcast"
# my_str_list = my_str.split(" ")
# print(f"将字符串{my_str}通过空格进行切割，结果是：{my_str_list}")
# #strip方法
# my_str="  itheima  and  itcast  "
# new_str = my_str.strip()
# print(f"字符串{my_str}被strip()后，结果是：{new_str}")

# my_str = "12itheima and itcast21"
# new_str = my_str.strip("12")
# print(f"字符串{my_str}被strip(12)后，结果是：{new_str}")
# #统计字符串中某字符串的出现次数，count
# my_str = "itheima and itcast"
# count = my_str.count("it")
# print(f"字符串{my_str}中it出现的次数是：{count}")
# #统计字符串的长度
# my_str = "itheima and itcast"
# length = len(my_str)
# print(f"字符串{my_str}的长度是：{length}")

#计算标准差和中位数
# from math import sqrt


# def get_num():  # 获取用户输入
#     numbers = []
#     while True:
#         value = input("请输入数字（直接回车结束）：").strip()
#         if value == "":
#             return numbers

#         try:
#             numbers.append(float(value))
#         except ValueError:
#             print("输入无效，请输入一个数字。")


# def mean(numbers):  # 计算平均值
#     return sum(numbers) / len(numbers)


# def dev(numbers, average):  # 计算样本标准差
#     squared_deviation_sum = 0.0
#     for number in numbers:
#         squared_deviation_sum += (number - average) ** 2
#     return sqrt(squared_deviation_sum / (len(numbers) - 1))


# def median(numbers):  # 计算中位数
#     new_numbers = sorted(numbers)
#     size = len(new_numbers)
#     if size % 2 == 0:
#         return (new_numbers[size // 2 - 1] + new_numbers[size // 2]) / 2
#     return new_numbers[size // 2]


# numbers = get_num()
# if not numbers:
#     print("没有输入数字，程序退出。")
# elif len(numbers) == 1:
#     print(
#         "平均数：{:.2f}，样本标准差：无法计算（至少需要两个数字），中位数：{:.2f}。"
#         .format(mean(numbers), median(numbers))
#     )
# else:
#     average = mean(numbers)
#     print(
#         "平均数：{:.2f}，样本标准差：{:.2f}，中位数：{:.2f}。"
#         .format(average, dev(numbers, average), median(numbers))
#     )




#对list进行切片，从1开始，4结束，步长1
# my_list=[0,1,2,3,4,5,6]
# result1=my_list[1:4:1]
# print(f"结果1:{result1}")
# #对tuple进行切片，从1开始，4结束，步长1
# my_tuple=(0,1,2,3,4,5,6)
# result2=my_tuple[:]
# print(f"结果2:{result2}")
# #对str进行切片，从1开始，4结束，步长2
# my_str="01234567"
# result3=my_str[::2]
# print(f"结果3:{result3}")
# #对str进行切片，从1开始，4结束，步长-1
# my_str="01234567"
# result4=my_str[::-1]
# print(f"结果4:{result4}")
# #对列表进行切片，从3开始，到1结束，步长-1
# my_list=[0,1,2,3,4,5,6]
# result5=my_list[3:1:-1]
# print(f"结果5:{result5}")
# #对元组进行切片，从头开始，到尾结束，步长-2
# my_tuple=(0,1,2,3,4,5,6)
# result6=my_tuple[::-2]
# print(f"结果6:{result6}")
#切片实战
# my_str = "万过薪月,员序程马黑来,nohtyp学"
# result1 = my_str[::-1][9:14]
# print(f"结果1:{result1}")
# result2 = my_str[5:10][::-1]
# print(f"结果2:{result2}")
# result3 = my_str.split(",")[1].replace("来", "")[::-1]
# print(f"结果3:{result3}")


#集合
# my_set={"传智教育","黑马程序员",}
# my_set_empty=set()
# print(f"my_set:{my_set},类型是:{type(my_set)}")
# print(f"my_set_empty:{my_set_empty},类型是:{type(my_set_empty)}")
#添加新元素
# my_set.add("传智")
# my_set.add("黑马")
# print(f"my_set的内容是:{my_set},类型是:{type(my_set)}")
# print(f"my_set_empty的内容是:{my_set_empty},类型是:{type(my_set_empty)}")
# #添加新元素
# my_set.add("传智")
# my_set.add("黑马")
# print(f"my_set添加元素后的结果是:{my_set}")
# #移除元素
# my_set.remove("传智")
# print(f"my_set移除元素后的结果是:{my_set}")
# #随机取出一个元素
# my_set={"黑马"}
# element=my_set.pop()
# print(f"集合被取出的元素是:{element},取出元素后:{my_set}")

#清空集合
# my_set={"黑马"}
# my_set.clear()
# print(f"清空集合后的结果是:{my_set}")
#取2个集合的差集
# set1={1,2,3}
# set2={1,5,6}
# set3=set1.difference(set2)
# print(f"取出差集的结果是:{set3}")
# print(f"取差集后,原有set1的内容:{set1}")
# print(f"取差集后,原有set2的内容:{set2}")


# #消除2个集合的差集
# set1={1,2,3}
# set2={1,5,6}
# set1.difference_update(set2)
# print(f"消除差集后的结果是:{set1}")
# #2个集合的交集
# set1={1,2,3}
# set1={1,5,6}
# set3=set1.union(set2)
# print(f"取交集的结果是:{set3}")
# #统计集合中元素的数量len()
# set1={1,2,3}
# num=len(set1)
# print(f"集合中元素数量是:{num}")
# #集合的遍历
# set1={1,2,3}
# for element in set1:
#     print(f"集合中的元素是:{element}")


# my_list=['黑马程序员','传智播客','黑马程序员','传智博客','itheima','itcast','itheima','itcast','best']
# my_set=set(my_list)
# for element in my_list:
#     my_set.add(element)
# print(f"列表的内容是:{my_list}")
# print(f"通过for循环后,得到的集合对象是:{my_set}")



# #字典
# dcountry1={"中国":"北京","美国":"华盛顿","日本":"东京"}
# dcountry2={}
# dcountry3=dict()
# print(f"dcountry1的内容是:{dcountry1}")
# print(f"fcountry2的内容是:{dcountry2}")
# print(f"dcountry3的内容是:{dcountry3}")
# dcountry1["英国"]="伦敦"
# print(f"dcountry的内容是:{dcountry1}")
# #定义重复key的字典
# my_dict={"王力红":99,"王力红":98,"林俊杰":77}
# print(f"my_dict的内容是:{my_dict}")
# #从字典中基于keyy获取value
# my_dict={"王力红":99,"王力洪":98,"林俊杰":77}
# value=my_dict["王力红"]
# print(f"王力红对应的value是:{value}")
# #定义嵌套字典
# stu_score_dict={
#     "王力洪":{
#         "语文":98,
#         "数学":90,
#         "英语":100
#     },
#     "林俊杰":{
#         "语文":100,
#         "数学":100,
#         "英语":100
#     }
# }
# print(f"学生的考试信息是：{stu_score_dict}")
# print(f"王力洪的语文成绩是：{stu_score_dict['王力洪']['语文']}")
# print(f"林俊杰的英语成绩是：{stu_score_dict['林俊杰']['英语']}")
#字典的常见操作
# my_dict={"周杰伦":99,"王力宏":98,"林俊杰":77}
# #新增元素
# my_dict["张学友"]=100
# print(f"新增元素后的结果是:{my_dict}")
# #更新元素
# my_dict["张学友"]=1000
# print(f"更新元素后的结果是:{my_dict}")
# #删除元素
# score=my_dict.pop("张学友")
# print(f"删除后字典的结果是:{my_dict}")
# #清空字典
# my_dict.clear()
# print(f"清空字典后的结果是:{my_dict}")
# #获取全部的key
# my_dict={"周杰伦":99,"王力宏":98,"林俊杰":77}
# keys=my_dict.keys()
# print(f"字典的key是:{keys}")
# #字典的遍历
# # 方式1:通过获取到全部的key来完成遍历
# for key in keys:
#     print(f"字典的key是{keys}")
#     print(f"字典的value是{my_dict[key]}")
# #方法2：直接对字典进行forr循环,每一次循环都是直接得到key
# for key in my_dict:
#     print(f"字典的key是{key}")
#     print(f"字典的value是{my_dict[key]}")
# #统计字典中元素数量len()
# my_dict={"周杰伦":99,"王力宏":98,"林俊杰":77}
# num=len(my_dict)
# print(f"字典中元素数量是:{num}")
