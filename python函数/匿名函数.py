# 目的：1.不担心函数名称重复 2.不需要返回函数名
# 样例：lambda x: x*x
# 配合map函数使用
print(map(lambda x: x*x, [1, 2, 3, 4]))
print(list(map(lambda x: x*x, [1, 2, 3, 4])))
