# split函数通常对字符串进行操作
# split分割函数经常与strip函数连用
val = 'a,b, c'
# split 结合strip(用于修剪空白符(包括换行符))
vala = [x.strip() for x in val.split(',')]
print(vala)
