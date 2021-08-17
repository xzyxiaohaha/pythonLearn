# -*- codeing = utf-8 -*-
# @Time : 2021/8/17 15:57
# @Author : zyxiao
# @File : testSqlite.py
# @Software : {PyCharm}

#-----------1.新建表--------------
# import sqlite3   #一个轻型的数据库
# conn = sqlite3.connect("test.db")    #打开或创建数据库文件
# print("打开数据库")
# c = conn.cursor()  #获取游标
# sql = '''
#     create table company
#         (id int primary  key not null,
#         name text not null,
#         age int not null,
#         adress char(50),
#         salary real)
# '''
# #上面的'''     ''' 可以用来写段落
#
# c.execute(sql)  #执行sql语句
# conn.commit()   #提交数据库操作
# conn.close()    #关闭连接
# print("新建表成功")


#------2.插入语句---------
# import sqlite3   #一个轻型的数据库
# conn = sqlite3.connect("test.db")    #打开或创建数据库文件
# print("打开数据库")
# c = conn.cursor()  #获取游标
# sql = '''
#     insert into company (id,name,age,adress,salary)
#     values (2,"张三",18,"安徽合肥",90000)
# '''
# c.execute(sql)  #执行sql语句
# conn.commit()   #提交数据库操作
# conn.close()    #关闭连接
# print("插入成功")


#------3.查询语句---------
import sqlite3   #一个轻型的数据库
conn = sqlite3.connect("test.db")    #打开或创建数据库文件
print("打开数据库")
c = conn.cursor()  #获取游标
sql = "select * from company"
cursor=c.execute(sql)  #执行sql语句,查询时不需要commit
for row in cursor:
    print("id=",row[0],"name=",row[1],"address=",row[3],"salary=",row[4])
conn.close()    #关闭连接
print("插入成功")


