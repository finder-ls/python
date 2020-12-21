card_list = {"张三": {"name": "张三", "qq": "12345", "phone": "12"},
             "李四": {"name": "李四",  "qq": "1321", "phone": "13"}
             }
print(card_list)
if "张三" in card_list:
    print(card_list["张三"])
else:
    print("张三不在列表中")
