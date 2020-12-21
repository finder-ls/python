# len() 方法返回对象（字符、列表、元组等）长度或项目个数。
s = "人生苦短，我用python"
print(len(s))
# 字段字符串占用的字节数 默认的utf-8编码模式下
print(len(s.encode()))
# gbk 编码中的字节数
print(len(s.encode('gbk')))
