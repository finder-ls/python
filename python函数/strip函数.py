'''
用途：删除首尾字符串
例如：删除从csv中取到数据后的/n 换行符。
它的函数原型：string.strip(s[, chars])，它返回的是字符串的副本，并删除前导和后缀字符。
（意思就是你想去掉字符串里面的哪些字符，那么你就把这些字符当参数传入。此函数只会删除头和尾的字符，中间的不会删除。）
如果strip()的参数为空，那么会默认删除字符串头和尾的空白字符(包括\n，\r，\t这些)。
lstrip()：去除左边
rstrip()：去除右边

1.Python strip()函数 介绍
函数原型
声明：s为字符串，rm为要删除的字符序列
s.strip(rm)       删除s字符串中开头、结尾处，位于 rm删除序列的字符
s.lstrip(rm)      删除s字符串中开头处，位于 rm删除序列的字符
s.rstrip(rm)     删除s字符串中结尾处，位于 rm删除序列的字符
注意：
(1)当rm为空时，默认删除空白符(包括‘\n‘, ‘\r‘, ‘\t‘,  ‘ ‘)
(2)这里的rm删除序列是只要边(开头或结尾)上的字符在删除序列内，就删除掉。
(2)这里的rm删除序列是只要边(开头或结尾)上的字符在删除序列内，就删除掉。
结果是一样的。
'''

str = ' ab cd '
print(str) # ' ab cd '
print(str.strip()) #删除头尾空格 #'ab cd'
print(str.lstrip()) #删除开头空格 #'ab cd '
print(str.rstrip()) #删除结尾空格 #' ab cd'


str2 = '1a2b12c21'
print(str2.strip('12')) #删除头尾的1和2 'a2b12c'
print(str2.lstrip('12')) #删除开头的1和2 'a2b12c21'
print(str2.rstrip('12')) #删除结尾的1和2  '1a2b12c'


示例三：
# 当传的参数不管是“abc”还是abc的其他排列形式，这都不重要，重要的是函数只知道你要删除的字符是”a”，”b”，”c”。
# 函数会把你传的参数拆解成一个个的字符，然后把头尾的这些字符去掉。
a="aabcacb1111acbba"
print(a.strip("abc"))
print(a.strip("acb"))
print(a.strip("bac"))
print(a.strip("bca"))
print(a.strip("cab"))
print(a.strip("cba"))

# 输出：
# 1111
# 1111
# 1111
# 1111
# 1111
# 1111
