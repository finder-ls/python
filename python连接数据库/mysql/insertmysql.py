import pymysql
db = pymysql.connect(host='192.2.2.102', user='root', password='superman',
                     port=3306, database='test', charset='utf8')
mycursor = db.cursor()
# sql数据
sql = "insert into users(name,age) values('小明',20)"
selectsql = "select * from users"
# 执行
mycursor.execute(sql)
mycursor.execute(selectsql)
# 查询返回结果
data = mycursor.fetchall()
print(data)
# 后续操作
db.commit()
mycursor.close()
db.close()
