'''
python内置函数
eval()函数将字符串str当成有效的表达式来求值并返回计算结果也可以用于把list,tuple,dict和string相互转化
eval(<字符串>) 能够以Python表达式的方式解析并执行字符串，并将返回结果输出。
eval()函数将去掉字符串的两个引号，将其解释为一个变量。
单引号，双引号，eval()函数都将其解释为int类型；三引号则解释为str类型。


需求如下：
从csv文件中通过readline函数提取表头获得一个字符串格式如下：
"database_name","table_name","index_name","last_update","stat_name","stat_value","sample_size","stat_description"
对字符串通过split函数以 逗号 分割，获得一个list列表：
 ['"database_name"', '"table_name"', '"index_name"', '"last_update"',
     '"stat_name"', '"stat_value"', '"sample_size"', '"stat_description"\n']

'''
# eval转换的时候：字符串的格式必须和字典，元组，列表格式相同，才能进行转换
# 字符串转换为列表
a = '[1,2,3,4]'
print(type(a))
print(type(eval(a)))

# 字符串转换为元组
b = '(1,2,3,4)'
print(type(b))
print(type(eval(b)))

# 字符串转换为集合
c = '{1,2,3,4}'
print(type(c))
print(type(eval(c)))

# 字符串转换为字典
d = '{"name":"张三","age":18}'
print(type(d))
print(type(eval(d)))
print("=================使用eval()转换字符串验证结束===================")
# eval()返回表达式值
print("eval()函数返回字符串表达式结果验证开始========")
e = 2
print(eval("2*e"))  # 结果为4

print("========分割===========")
abc = '"这是一个字符串"'
print(abc)
print(eval(abc))  # 执行结果：这是一个字符串

line = ['"201903"', '"201904"', '"201905"', '"201906"', '"201907"']
print(line)
linea = ['{0}'.format(eval(seg)) for seg in line]
print(linea)  # ['201903', '201904', '201905', '201906', '201907']
lineb = ['{0}'.format(seg.replace('\"', '')) for seg in line]
print(lineb)

# 对列表进行去除
list1 = ['hello', 'xxx', 'world', '123']
print(' '.join(list1))  # 空格分开 hello xxx world 123
print(','.join(list1))  # 逗号隔开 hello,xxx,world,123
# print('[', ', '.join(list), ']')  # 保留括号，执行报错

strs = "database_name", "table_name", "index_name", "last_update", "stat_name", "stat_value", "sample_size", "stat_description"
# tuple元组没有split方法，所以转换为list
strs = list(strs)
# ['database_name', 'table_name', 'index_name', 'last_update', 'stat_name', 'stat_value', 'sample_size', 'stat_description']
print(strs)
print(strs.split(','))
