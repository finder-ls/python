# index方法
list1 = ["a", "b", "c", 1]
print(list1.index("c"))  # 返回字符c 的索引位置


list2 = ["a", "b", "c", 1, ["a", "b", 1]]
print(list2.index(1))  # 结果为3，只是第一个1 的索引位置

list3 = ["a", "a", "b", "c"]
print(list3.index("a"))  # 结果为0 ，只是第一个索引的位置
