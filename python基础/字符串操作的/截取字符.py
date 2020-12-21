s = "截取字符串"
# 获取索引为0的字符
print(s[0])
# 获取索引为-1的字符
print(s[-1])
# 利用索引截取前两个字符 strname[start : end : step]
# 包含start不包含end，step不写默认为最小值1，且不写step时可省略最后一个冒号
print(s[0:2:1])
print(s[0:2])
# 从索引2开始，每2个字符取一次，直到索引10为止
s1 = "https://www.python.org/"
print(s1[2:10:2])

# 获取从索引5开始直到末尾的子串
print(s1[5:])
# 获取从从索引-10开始直到末尾的字串
print(s1[-10:])
# 获取从开头到索引15为止的子串
print(s1[0:15])
# 每3个字符取出一个字符
print(s1[::3])
