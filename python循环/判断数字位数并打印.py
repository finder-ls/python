'''
随意给出一个5位以内的正整数，判断位数并分别打印出各个位上的数字

1.可能输入1,2,3,4,5种位数，通过二分法进行位数判断。
2.数字除以10看余数知道个位数
number = int(input("输入一个5位数："))
number *= 10  # 解决初始进入
while (number//10)!=0:
    number //=10   # 对10取正并赋值
    print(number%10) #对10取余数并打印

3.相减54321

54321//10 =5432; 54321-5432*10=1
5432//10 =543;5432-543*10=2
543//10 =54;543-54*10=3
54//10 =5;54-5*10=4
5//10 =0;5-0*10=5



'''
i = int(input("请输入一个5位以内的整数："))
if i >= 1000:
    if i >= 10000:
        print("5位数")
    else:
        print("4位数")
elif i < 1000:
    if i >= 10:
        if i >= 100:
            print("3位数")
        else:
            print("2位数")
    else:
        print("1位数")
# 循环打印各个位数
c = i
while c//10 > 0:
    print(c - c//10*10)
    c = c//10
    if c//10 == 0:
        print(c - c//10*10)
        break
