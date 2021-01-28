# ===常用
'''
join() 方法的语法格式如下：
newstr = str.join(iterable)
此方法中各参数的含义如下：
newstr：表示合并后生成的新字符串；
str：用于指定合并时的分隔符；
iterable：做合并操作的源字符串数据，允许以列表、元组等形式提供。

'''
# 列表中数据拼接为字符串
list1 = ["知识", "能力", "技能"]
list2 = "".join(list1)
list3 = "/".join(list1)
list4 = "与".join(list1)
print(list2)
print(list3)
print(list4)

# 元组中数据拼接成字符串
tuple1 = ("知识", "能力", "技能", "工作", "薪水")
tuple2 = "".join(tuple1)
print(tuple2)
