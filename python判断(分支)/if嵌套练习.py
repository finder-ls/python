'''
1. 定义布尔型变量 has_ticket 表示是否有车票
2. 定义整型变量 knife_length 表示刀的长度，单位：厘米
3. 首先检查是否有车票，如果有，才允许进行 安检
4. 安检时，需要检查刀的长度，判断是否超过 20 厘米
   如果超过 20 厘米，提示刀的长度，不允许上车
   如果不超过 20 厘米，安检通过
5. 如果没有车票，不允许进门
'''
has_ticket = True
knife_length = 25

if has_ticket is True:
    print('有车票请进行安检')
    if knife_length < 20:
        print('安检通过')
    else:
        print('刀具长度为%d厘米，超过20厘米不允许携带上车' % (knife_length))
else:
    print('没有车票不允许进站')

# 别的写法

# 定义布尔型变量 has_ticket 表示是否有车票
has_ticket = True

# 定义整数型变量 knife_length 表示刀的长度，单位：厘米
knife_length = 20

# 首先检查是否有车票，如果有，才允许进行 安检
if has_ticket:
    print("有车票，可以开始安检...")

    # 安检时，需要检查刀的长度，判断是否超过 20 厘米
    # 如果超过 20 厘米，提示刀的长度，不允许上车
    if knife_length >= 20:
        print("不允许携带 %d 厘米长的刀上车" % knife_length)
    # 如果不超过 20 厘米，安检通过
    else:
        print("安检通过，祝您旅途愉快……")

# 如果没有车票，不允许进门
else:
    print("大哥，您要先买票啊")
