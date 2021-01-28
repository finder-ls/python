import keyword
# for 循环内部使用的变量名字 in 列表
for name in keyword.kwlist:
    # 循环内部针对列表的每个变量做的操作
    # print(name)
    # print(name + "这是关键字")
    # title()方法返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())。
    # print(name.title() + "这是关键字")
    # istitle() 方法检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写。
    # 如果字符串中所有的单词拼写首字母是否为大写，且其他字母为小写则返回 True，否则返回 False
    # print(name.istitle())
    # "\n" 换行
    print(name.title() + "\n")
