# 定义一个可变参数的求和函数
def c_sum(*args):
    x = 0
    for n in args:
        x = x + n
    return x


# 定义一个可变参数求和函数，不返回求和结果而是根据后面代码需要再计算。因此返回一个求和的函数：
# 在c_sum函数的基础上，将计算部分包装为一个函数，并在求和结果后返回该函数


def ca_sum(*args):
    def ca_s():
        x = 0
        for n in args:
            x = x + n
        return x
    return ca_s


print(c_sum(1, 2, 3, 4, 5, 6))
# 使用ca_sum
print(ca_sum(1, 2, 3, 4))
print(ca_sum(1, 2, 3, 4)())
