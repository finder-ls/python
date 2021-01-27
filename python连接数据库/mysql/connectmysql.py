# 引入pymysql
import pymysql
# 连接mysql数据库
db = pymysql.connect(host='192.2.2.102', user='root',
                     password='superman', database='test', charset='utf8')
# mydb = pymysql.connect('192.2.2.102','root','superman','test')
# 创建游标
link = db.cursor()
# 编写slq
version = "select version()"
sql = "select * from users"
link.execute(version)
dbversion = link.fetchone()
link.execute(sql)
data = link.fetchone()  # 通过fetchone获取返回的一条数据，fetchall获取全部数据，fetchmany获取多条数据
print("数据库版本为：%s" % dbversion)
print("查询sql为： %s" % sql)
print(data)
# 提交
# db.commit()
# 释放内存空间，先关闭游标，在关闭数据库连接
