'''
集合用{}定义
集合属于序列类型
所谓序列，指的是一块可存放多个值的连续内存空间，这些值按一定顺序排列，可通过每个值所在位置的编号（称为索引）访问它们
1.值不重复
2.存储不可变数据类型
'''
seta = {1, 2, 3, 4}
print(seta)
# dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表
print(dir(set)) # 获得集合set的方法
print(dir()) # 获得当前模块的属性列表

