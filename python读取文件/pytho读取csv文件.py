import csv
with open("E:\\study\\python\\python读取文件\\innodb_index_stats.csv") as f:
    reader = csv.reader(f)
    rows = [row for row in reader]
    print(rows)

