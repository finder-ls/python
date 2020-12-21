import os


def lsa(x):
    return x*x


def lsb(x, y):
    return x*y


def lsn(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


def calb(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


def prod(*numbers):
    m = 1
    for n in numbers:
        m = m * n
    return m


def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)


L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']


def trim(s):
    if 0 == len(s):
        return s

    while ' ' == s[0]:
        s = s[1:]
        if 0 == len(s):
            return s

    while ' ' == s[-1]:
        s = s[:-1]
        if 0 == len(s):
            return s
    return s


# 测试trim代码
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')


print(lsn(2, 2))
print(lsn(2))
print(calc([1, 2, 3]))
print(calc((1, 2, 3)))
print(calb(1, 2, 3))
print(prod(1, 2, 3))
print(fact(5))
print(L[1:3])
print((0, 1, 2, 3, 4, 5)[:3])
print(L[:])
print('same'[1:2])

#############################
# 元组、字典、字符串
list1 = (1, 2, 3, 4, 5, 6, 7)
d = {'a': 1, 'b': 2, 'c': 3}
c = "ABCD"
for key in d:
    print(key)
# 迭代字典的value
for value in d.values():
    print(value)
# 同时迭代字典的key和value
for k, v in d.items():
    print(k, v)
# 元组的迭代
for i in list1:
    print(i)
for m in c:
    print(m)
# 通过collections模块的Iterable类型判断一个对象是可迭代对象
# from collections import Iterable
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
print(list(range(1, 11)))

L1 = []
for x in range(1, 11):
    L1.append(x*x)
print(L1)
print([x * x for x in range(1, 11)])
print([d for d in os.listdir('.')])
