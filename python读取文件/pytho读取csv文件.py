import csv
import pymysql
db = pymysql.connect(host='192.2.2.102', user ='root', password = 'superman', database = 'test',port = 3306)
mycursor = db.cursor()
sql = '''
      drop table if exists my_database_stats;
      create table if not exists my_database_stats (database_name varchar(10),
      table_name varchar(10),
      index_name varchar(10),
      last_update datatime,
      stat_name varchar(10),
      stat_value int(5),
      sample_size int(5),
      stat_description varchar(20))
      '''
print(sql)
# 打印当前时间的年份
with open("E:\\study\\python\\python读取文件\\innodb_index_stats.csv",'r') as f:
    # reader = csv.reader(f) 此时reader返回的值是csv文件中每行的列表，将每行读取的值作为列表返回,此时reader是一个列表
    # reader = csv.reader(f)
    reader = f.reader()
    rows = [row for row in reader]
# 打印内容
    print(rows[0])
    print(rows[1])
# 建表

