# 对简单的列表查询
list_1 = ["1", "2", "3", "4"]
if "1" in list_1:
    print("1存在")
else:
    print("1不存在")
# 对列表中嵌套了字典的情况进行查询，出了问题
list_2 = [{"name": "张三", "phone": 123}, {"name": "赵四", "phone": 123}]
if "张三" in list_2:
    print("张三存在")
else:
    print("张三不存在")
# 对列表中嵌套了字典的，增加for循环
list_2 = [{"name": "张三", "phone": 123}, {"name": "赵四", "phone": 123}]
