# 使用reader函数，接收一个可迭代的对象（比如csv文件），能返回一个生成器，就可以从其中解析出csv的内容：
import csv


with open("E:\\study\\python\\python读取文件\\innodb_index_stats.csv", "r") as f:
    reader = csv.reader(f)
    rows = [row for row in reader]
print(rows[0])  # 打印标题
print(rows[1])
