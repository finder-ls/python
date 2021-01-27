# DictReader函数，和reader函数类似，接收一个可迭代的对象，能返回一个生成器，
# 但是返回的每一个单元格都放在一个字典的值内，而这个字典的键则是这个单元格的标题（即列头）
import csv


with open("E:\\study\\python\\python读取文件\\innodb_index_stats.csv", "r") as f:
    # reader = csv.dictreader(f)# python区分大小写
    # AttributeError: module 'csv' has no attribute 'dictreader'
    reader = csv.DictReader(f)
    rows = [row for row in reader]
# 输出全部数据数据
print(rows)
# 输出第一行数据
print(rows[1])
