# 冒泡排序
lis = [1, 100, 3, 89, 44, 22, 19, 98, 4]
for i in range(len(lis)-1):
    for j in range(len(lis)-1-i):
        if lis[j] > lis[j+1]:
            lis[j+1], lis[j] = lis[j], lis[j+1]
print(lis)
