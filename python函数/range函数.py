# python2中使用range返回时list；python3中返回是<class 'range'>
'''
一、语法：
 range(stop)
 range(start,stop,step)  # 左闭右开
 start:计数从start开始，默认是从0开始。eg：range(5)等价于range(0,5)
 stop:计数到stop结束，但不包括stop。eg：range(0,5)是[0,1,2,3,4],没有5
 step:步长，默认为1。eg:range(0,5)等价于range(0,5,1)

注意：
返回值：一个可迭代对象（类型是对象），不是列表，所以打印的时候不会打印列表
list() 函数[对象迭代器]可以把range()返回的可迭代对象转为一个列表，返回的变量类型为列表
'''
for i in range(10):
    print(i)
print(type(range(10))) # <class 'range'>
print(type(list(range(10)))) # 使用list()将range生成的对象转换成列表
print(type(tuple(range(10))))
print(type(set(range(10))))