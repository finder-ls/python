# 使用%或者format进行字符串的格式化输出
# 定义(str)字符变量name，输出 我的名字叫 小明，请多关照
name = '小明'
print('我的名字叫 %s，请多关照！' % name)

# 定义(int)整数变量 student_no，输出 我的学号是 000001
student_no = 0o1  # 十进制数不允许0开头，01会报错。
print('我的学号是 %06d' % student_no)

# 定义(float)小数price，weight，money
# 输出 苹果单价 9.00元/斤 ，购买了5.00斤，需要支付 45.00元
# 留意保留小数的写法
price = 9.213
weight = 5.1237
money = 45.12
print('苹果单价 %.2f元/斤，购买了 %.3f斤，需要支付%.4f元' % (price, weight, money))
print('苹果单价 %f元/斤，购买了 %f斤，需要支付%f元' % (price, weight, money))


# 定义一个小数 scale,输出 数据比例为 10.00%
scale = 0.1
print('数据比例是%0.2f%%' % (scale*100))
print('%0.2f%%' % scale)

# 格式化输出字典中的内容
data = {"name": "John", "age": 18, "height": 180}
print(
    "The boy named {0[name]:s} is {0[age]:d}-year-old "
    "and {0[height]:g} tall.".format(data)
     )

"""
%% 百分号标记 #就是输出一个%
%c 字符及其ASCII码
%s 字符串
%d 有符号整数(十进制)
%u 无符号整数(十进制)
%o 无符号整数(八进制)
%x 无符号整数(十六进制)
%X 无符号整数(十六进制大写字符)
%e 浮点数字(科学计数法)
%E 浮点数字(科学计数法，用E代替e)
%f 浮点数字(用小数点符号)
%g 浮点数字(根据值的大小采用%e或%f)
%G 浮点数字(类似于%g)
%p 指针(用十六进制打印值的内存地址)
%n 存储输出字符的数量放进参数列表的下一个变量中
"""
