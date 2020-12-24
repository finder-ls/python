# 引入pymysql
import pymysql
# 连接mysql数据库
db = pymysql.connect(host='192.2.2.102', user='root',
                     password='superman', database='test', charset='utf8')
# 创建游标
link = db.cursor
# 编写slq
sql = "select * from users"

# 打印sql结果
print(sql)
