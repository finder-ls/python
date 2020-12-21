# 使用while中嵌套while的方法打印九九乘法表
'''
思路：
1*1
1*2 2*2
1*3 2*3 3*3
1*4 2*4 3*4 4*4
...
右侧每次循环增加1，只要右侧比左侧小循环就会继续，知道左侧=右侧 continue
print('*' * 5, end='不换行，可增加的内容')并且需要增加判断，当a=b是换行

'''
# 定义计数器a与b，b为右侧数据，a为左侧数据
a = 1
b = 1
while b <= 9:
    # b值固定时，a进行自增循环
    while a <= b:
        # 判断如果a != b 则打印不自动换行
        if a != b:
            print('%d*%d' % (a, b), end=' ')
        else:
            # 当a == b 时，自动换行
            print('%d*%d' % (a, b))
        # 处理计数器
        a += 1
    # 重置计数器a = 1，以便参与b的自增循环时能从1开始。
    a = 1
    b += 1

# 将结果打印出来
a = 1
b = 1
c = 1
while b <= 9:
    # b值固定时，a进行自增循环
    while a <= b:
        c = a * b
        # 判断如果a != b 则打印不自动换行
        if a != b:
            print('%d*%d=%d' % (a, b, c), end=' ')
        else:
            # 当a == b 时，自动换行
            print('%d*%d=%d' % (a, b, c))
        # 处理计数器
        a += 1
    # 重置计数器a = 1，以便参与b的自增循环时能从1开始。
    a = 1
    b += 1
