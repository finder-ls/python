# 需求，写一个打招呼的函数，封装三行打招呼代码，并在函数下方调用打招呼函数。
name = '小明'


def hello():  # 定义函数
    """这是函数的文档注释"""
    print('hello world 1')
    print('hello world 2')
    print('hello world 3')


print(name)
hello()
print(name)
