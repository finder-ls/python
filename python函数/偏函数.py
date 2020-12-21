'''
def int2(x, base=2):
    return int(x, base) # 定义函数的方式


print(int2('100'))
print(int2('1000000'))
'''
# 引入functools模块
# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
import functools
int2 = functools.partial(int, base=2)
print(int2('100'))
