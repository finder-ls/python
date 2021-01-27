import pymysql
# 导入pymysql方法

# 连接数据库
config = {'host': '192.2.2.102',
          'port': 3306,
          'user': 'root',
          'passwd': 'superman',
          'charset': 'utf8mb4',
          'database': 'test',
          'local_infile': 1
          }
conn = pymysql.connect(**config)
cur = conn.cursor()


def testconnect():
    test_sql = 'select * from users1'
    # 将sql语句通过游标执行
    cur.execute(test_sql)
    # 打印execute执行后的返回结果，因为知道数据量小，使用了fetchall【faichiall】；fetchone；fetchmany
    print(cur.fetchall())
    # 记得提交，保持个好习惯
    conn.commit()

    # 关闭游标与数据库连接
    # conn.close()
    # cur.close()
# 调用写的测试连接的函数


testconnect()

# load_csv函数，参数分别为csv文件路径，表名称，数据库名称
# def load_csv(csv_file_path,table_name,database='test'):


def load_csv(csv_file_path, table_name):
    # 打开csv文件
    file = open(csv_file_path, 'r', encoding='utf-8')
    # 读取csv文件第一行字段名，创建表
    reader = file.readline()
    print(type(reader))  # readline返回一个字符串类型，<class 'str'>
    print(reader)
    # "database_name","table_name","index_name","last_update","stat_name","stat_value","sample_size","stat_description"
    # print(eval(reader)) # 字符串转换为一个元组
    # print(type(eval(reader))) # <class 'tuple'>
    b = reader.split(',')
    b = [{0}.format(eval(stra)) for stra in b]
    print(b)
    # print(type(b)) # <class 'list'> 使用split后,生成一个list，
    # print(b)
    '''
    ['"database_name"', '"table_name"', '"index_name"', '"last_update"'
    ,'"stat_name"',  '"stat_value"', '"sample_size"', '"stat_description"\n']
    '''
    # 生成的list，自动给元素增加了''，所以拼接成的create sql 语句执行报错。
    # create table xx("a" varchar(20));对于 "a" 格式报错。
    # 对list循环，拼接数据建表语句。
    colum = ''
    for a in b:
        colum = colum + a + ' varchar(255),'
        print(colum)
    colum = colum[:-1]  # slice 切片，从0到-1 且不包括-1索引的值。
    print(type(colum))
    # 编写sql，create_sql负责创建表，data_sql负责导入数据
    create_sql = 'create table if not exists ' + table_name + \
        ' ' + '(' + colum + ')' + ' DEFAULT CHARSET=utf8'
    data_sql = ("load data local infile '%s' into table %s fields "
                "terminated by ','lines terminated by '\\r\\n' ignore 1 lines"
                % (csv_file_path, table_name)
                )
    '''
    mysql的load data的用法：
    LOAD DATA LOCAL INFILE 'csv_file_path' INTO TABLE table_name FIELDS \
    TERMINATED BY ',' LINES TERMINATED BY '\\r\\n' IGNORE 1 LINES

    csv_file_path 指文件绝对路径
    table_name 指表名称
    FIELDS TERMINATED BY ',' 指以逗号分隔
    LINES TERMINATED BY '\\r\\n' 指换行
    IGNORE 1 LINES 指跳过第一行，因为第一行是表的字段名
'''
    print(create_sql)
    print(data_sql)
    # 使用数据库
    # cur.execute('use %s' % database)
    # 设置编码格式
    cur.execute('SET NAMES utf8;')
    cur.execute('SET character_set_connection=utf8;')
    # 执行create_sql，创建表
    cur.execute(create_sql)
    # 执行data_sql，导入数据
    cur.execute(data_sql)
    conn.commit()
    # 关闭连接
    conn.close()
    cur.close()


load_csv("E:\\study\\python\\python读取文件\\innodb_index_stats.csv",
         "my_database_stats")
