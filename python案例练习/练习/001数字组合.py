'''
实例001：数字组合
题目 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

思路：
两位数 4次i循环下嵌套4次j；但是有重复数据
三位数 三个for循环，不会有重复数据，比2位数简单
'''
m = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            m += 1
            print(100*i+10*j+k)
print("总数为{}".format(m))
