# 列表中的列表
# 取出1个元素 与 取出多个元素的 区别
list1 = [[1, 2, 3, 4], ["a", "b", "c", "d"]]
print(list1[0][1])  # 取索引为0的数据中 索引为1的数据
print(type(list1[0][1]))  # <class 'int'>
print(list1[1][2])  # 取索引为1的数据中 索引为2的数据
print(list1[1][0:2])  # ['a', 'b']
print(type(list1[1][0:2]))  # <class 'list'>
