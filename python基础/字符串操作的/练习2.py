# random 随机数
import random

s = "知识点要记牢达到能详细口述的程度，并想一个方法将知识点串联起来，去解决问题；\
学习某样东西的时候也要想到可以解决哪些问题 \
并且需要及时的去复习，重新操作，已达到将知识运用解决问题，从而促进能力的提升"

# random.randint()方法里面的取值区间是前闭后闭区间
# np.random.randint()方法的取值区间是前闭后开区间
'''
random.randint(a,b[,c])
#用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b。c是步幅。

numpy.random.randint(low, high=None, size=None, dtype='l')
#这个方法产生离散均匀分布的整数，这些整数大于等于low，小于high。
low : int        #产生随机数的最小值
high : int, optional    #给随机数设置个上限，即产生的随机数必须小于high
size : int or tuple of ints, optional    #整数，生成随机元素的个数或者元组，数组的行和列
dtype : dtype, optional    #期望结果的类型

'''

print(random.randint(1000, 9999))
print(round(1.2501, 1))
print(round(1.251, 1))
