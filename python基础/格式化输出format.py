'''
用法：
字符串格式化方法调用：'...{}...'.format(values) 或者 f'...{xx}...'

str.format( ) 方法通过字符串中的花括号  { } 来识别需要替换的字段，从而完成字符串的格式化。
相对基本格式化输出采用‘%’的方法，format()功能更强大，该函数把字符串当成一个模板，通过传入的参数进行格式化，\
并且使用大括号‘{}’作为特殊字符代替‘%’；大括号与大括号之间可任意写东西

位置匹配
(1)不带编号，即“{}”
(2)带数字编号，可调换顺序，即“{1}”、“{2}”
(3)带关键字，即“{a}”、“{tom}”

'''
import datetime


print('不带字段：{} {}'.format("hello", "world"))  # 不带字段
print("带数字编号：{0} {1}".format("hello", "world"))  # 带数字编号
print("带关键字：{a} {b}".format(a="hello", b="world"))  # 带关键字
# ####通过位置匹配
print("位置匹配：{} {} {}".format("a", "b", "c"))
# IndexError: Replacement index 3 out of range for positional args tuple
# 使用下角标超过范围会报错，下角标从0开始
# print("{1}, {2}, {3}".format("a", "b", "c"))
print("通过索引做位置匹配：{1}, {2}, {0}".format("a", "b", "c"))
# 下角标使用小于范围时，不会报错，但是会提示哪个索引没有使用
# '...'.format(...) has unused arguments at position(s): 3cornflakes(F523)
# print("{1}, {2}, {0}".format("a", "b", "c", "d"))
print("可打乱顺序：{2},{0},{1}".format(*"abc"))
print("可重复：{0}{1}{0}".format("abc", "def"))

# ####通过名字匹配
myword = {"aa": "hello", "bb": "world"}
print("myword:{aa},{bb}".format(**myword))

# 通过对象属性匹配
# 通过下标或者key匹配参数

# ========在字符串前加f，在{}中加入对象。达到格式化。 f"xx{}xx"
a1 = "hello"
b1 = "world"
print(f"{a1} {b1}")

# ==  时间格式化
dtime = datetime.datetime(2021, 1, 27, 13, 49, 50)
print("{:%Y-%m-%d %H:%M:%S}".format(dtime))
print("{:%Y/%m/%d %H/%M/%S}".format(dtime))
# == 百分数表示
allnum = 19
finishnum = 2
print("进度为：{:.2f}".format(finishnum/allnum))
print("进度为：{:.2%}".format(finishnum/allnum))
# == 进制转换
'''
'b' - 二进制。将数字以2为基数进行输出。(binary system 二进制)
'c' - 字符。在打印之前将整数转换成对应的Unicode字符串。
'd' - 十进制整数。将数字以10为基数进行输出。(decimal system 十进制)
'o' - 八进制。将数字以8为基数进行输出。(octal number system 八进制)
'x' - 十六进制。将数字以16为基数进行输出，9以上的位数用小写字母。(hexadecimal 十六进制hex)
'e' - 幂符号。用科学计数法打印数字。用'e'表示幂。
'g' - 一般格式。将数值以fixed-point格式输出。当数值特别大的时候，用幂形式打印。
'n' - 数字。当值为整数时和'd'相同，值为浮点数时和'g'相同。不同的是它会根据区域设置插入数字分隔符。
'%' - 百分数。将数值乘以100然后以fixed-point('f')格式打印，值后面会有一个百分号。
'''
print("int:{0:d}; hex:{0:x}; cot:{0:o}; bin:{0:b}".format(42))
# 在前面加“#”，则带进制前缀
print("int:{0:d}; hex:{0:#x}; oct:{0:#o}; bin:{0:#b}".format(42))
# == 格式转换
print("{:b}".format(20))  # 二进制
print("{0:b}".format(20))  # 这里的{0:b}中的0表示取format中的第一参数。
print("{:o}".format(20))  # 八进制
print("{:d}".format(20))  # 十进制
print("{:x}".format(20))  # 十六进制
print("{:c}".format(20))  # 转换为Unicode字符串

# == 左中右对齐及位数补全
# < (默认)左对齐、 >右对齐、^中间对齐、= (只用于数字)在小数点后进行补齐
# 取位数 "{:4s}" 、"{:.2f}" 等
print("{}and {}".format("hello", "world"))
