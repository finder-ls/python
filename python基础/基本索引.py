# 区别于切片概念的区间取值，基本索引是取单个值。
# 超过索引范围使用会报错，切片则不会报错，切片是返回【求的索引范围与实际存在的索引范围】交集部分。
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[-1])
print(a[0])
# 超过下标范围报错,IndexError: list index out of range
print(a[-11])
print(a[10])
