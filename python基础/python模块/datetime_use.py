import datetime
'''
1.strptime():
由字符串格式转化为日期格式的函数为: datetime.datetime.strptime()。我们输入的日期和时间是字符串，
要处理日期和时间，首先必须把str转换为datetime。转换方法是通过datetime.strptime()实现，
需要一个日期和时间的格式化字符串：
2.strftime():
由日期格式转化为字符串格式的函数为: datetime.datetime.strftime()。后台提取到datetime对象后，
要把它格式化为字符串显示给用户，就需要转换为str，转换方法是通过strftime()实现的，
同样需要一个日期和时间的格式化字符串:
3.datetime加减：
对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符，
不过需要导入timedelta这个类, 如以下例子：

---python中时间日期格式化符号：
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身

'''
print(datetime.date.today()) # 获取当前日期，不显示时间
print(datetime.datetime.today()) # 获取当前日期，显示时间
print(datetime.datetime.now()) # 获取当前日期，显示时间(同上)

print(datetime.datetime.now().strftime('%Y-%m-%d')) # 精确到年月日
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) # 精确到年月日时分秒
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %A')) # 精确到年月日时分秒并且输出星期(全写)
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %a')) # 精确到年月日时分秒并且输出星期(缩写)
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %A %B')) # 年月日时分秒 星期 月份(全写)
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %A %b')) # 年月日时分秒 星期 月份(缩写)

# 倒计时计算
day2021 = datetime.datetime.strptime('2021-1-1 0:0:0', '%Y-%m-%d %H:%M:%S')
now = datetime.datetime.today()
delta = day2021 - now # delta存储两个时间的时间,差精确到毫秒
day = delta.days # 获取两个时间之间的天数

hour = int(delta.seconds/60/60)
minute = int((delta.seconds-hour *60*60)/60)
second = int(delta.seconds-hour *60*60 -minute*60)

print('到2021年元旦还有:' + str(day) +'天'+ str(hour) +'小时'+ str(minute) +'分'+ str(second) +'秒')
# end

# 计算未来时间
print(datetime.datetime.today() + datetime.timedelta(days=5)) # 5天后
print(datetime.datetime.today() + datetime.timedelta(hours=5*24)) # 5*24小时后
print(datetime.datetime.today() + datetime.timedelta(minutes=5*24*60)) # 5*24*60分钟后
print(datetime.datetime.today() + datetime.timedelta(seconds=5*24*60*60)) #5*24*60*60秒后
