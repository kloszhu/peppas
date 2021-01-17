# import MySQLdb python3不支持MySQLdb
import pymysql

#打开数据库，数据库可自己创建，create database test;
con = pymysql.connect(host='121.4.203.2',  user='admin', passwd='admin1234', db='peppa', port=3306, charset='utf8')
#通过cursor()创建一个游标对象
cur = con.cursor()

#建表
cur.execute('''CREATE TABLE If Not Exists person (id int not null auto_increment primary key,name varchar(20),age int, sex varchar(2))''')

#插入数据
data="'Alice',16,'女'"
cur.execute(' INSERT INTO person (name,age,sex) VALUES (%s)'%data)

cur.execute(' INSERT INTO person (name,age,sex) VALUES (%s,%s,%s)',('Alex',20,'男'))

cur.execute(' INSERT INTO person (name,age,sex) VALUES ({a},{b},{c})'.format(a="'Alice'",b=12,c="'否'"))

cur.executemany(' INSERT INTO person (name,age,sex) VALUES (%s,%s,%s)',[('sara',24,'女'),('开心麻花',30,'男')])

#提交操作
con.commit()

#查询表中的数据
cur.execute('SELECT * FROM person')

#fetchall()获取所有数据，返回一个二维的列表
res = cur.fetchall()
for line in res:
    print(line)

    # fetchone()获取其中的一个结果，返回一个元组
    cur.execute('SELECT * FROM person')
    res = cur.fetchone()
    print(res)

#修改数据
cur.execute('UPDATE person SET name=%s WHERE id=%s', ('小明',12,'男'))

#删除数据
cur.execute('DELETE FROM person WHERE id=%s', (0,))

con.commit()
con.close()