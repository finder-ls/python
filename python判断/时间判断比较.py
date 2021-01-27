from datetime import datetime
'''
datetime是一个模块，它提供了日期格式和字符串格式相互转化的函数，datetime模块还包含一个datetime类，
通过from datetime import datetime导入的才是datetime这个类。
'''
# 定义一个函数，将字符串格式的时间转换为时间格式
# strptime()，功能：按照特定时间格式将字符串转换（解析）为时间类型。


def ftime(t):
    return datetime.strptime(t, '%Y-%m-%d %H:%M:%S')


a = '2021-01-01 00:00:00'
b = '2021-02-01 00:00:00'
c = '2021-04-01 00:00:00'
d = '2021-05-01 00:00:00'
e = '2021-02-12 00:00:00'
n_time = datetime.now()
print(n_time)
print(ftime(a))
# 时间格式 直接尽心比较
if ftime(e) < ftime(a):
    print("活动未开始")
elif ftime(e) > ftime(d):
    print("本次活动已结束")
elif ftime(b) < ftime(e) < ftime(c):
    print("上次活动已结束，本次活动未开始")
    print("上次活动结束时间为:%s,\n本次活动开始时间为:%s,\n当前时间为:%s" % (b, c, e))
