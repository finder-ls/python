# 引入pymongo模块
import pymongo
# 连接到mongo服务器，创建客户端
'''
有账号密码的方式连接mongodb
# 账号密码方式连接MongoDB | "mongodb://用户名:密码@公网ip:端口/"
client = pymongo.MongoClient("mongodb://root:root@127.0.0.1:27017/")
client = pymongo.MongoClient("192.2.2.99", 27017)
'''
client = pymongo.MongoClient("mongodb://root:abc123@192.2.2.99:27017/")
# 选择数据库
db = client.mydb
# 选择用哪个集合
coll = db.users
# 查看单个文档
rs = coll.find_one()
# 打印单个查询
print(rs)
