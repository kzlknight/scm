用Python写脚本也有一段时间了，经常操作数据库（MySQL），现在就整理下对各类数据库的操作，如后面有新的参数会补进来，慢慢完善。

一， **python 操作 MySQL** :详情见：  
【apt-get install python-mysqldb】

_复制代码_ 代码如下:

  
#!/bin/env python  
# -*- encoding: utf-8 -*-  
#-------------------------------------------------------------------------------  
# Purpose: example for python_to_mysql  
# Author: zhoujy  
# Created: 2013-06-14  
# update: 2013-06-14  
#-------------------------------------------------------------------------------  
import MySQLdb  
import os

#建立和数据库系统的连接，格式  
#conn =
MySQLdb.connect(host='localhost',user='root',passwd='123456',db='test',port=3306,charset='utf8')

#指定配置文件，确定目录,或则写绝对路径  
cwd = os.path.realpath(os.path.dirname(__file__))  
db_conf = os.path.join(cwd, 'db.conf')  
conn =
MySQLdb.connect(read_default_file=db_conf,host='localhost',db='test',port=3306,charset='utf8')

#要执行的sql语句  
query = 'select id from t1'

#获取操作游标  
cursor = conn.cursor()

#执行SQL  
cursor.execute(query)

#获取一条记录,每条记录做为一个元组返回,返回3，游标指到第2条记录。  
result1 = cursor.fetchone()  
for i in result1:  
print i  
#返回影响的行数  
print cursor.rowcount

#获取指定数量记录,每条记录做为一个元组返回,返回1，2，游标从第2条记录开始，游标指到第4条记录。  
result2 = cursor.fetchmany(2)  
for i in result2:  
for ii in i:  
print ii

  
#获取所有记录,每条记录做为一个元组返回,返回3，4，7，6,游标从第4条记录开始到最后。  
result3 = cursor.fetchall()  
for i in result3:  
for ii in i:  
print ii

#获取所有记录,每条记录做为一个元组返回,返回3，4，7，6,游标从第1条记录开始  
#重置游标位置，0为偏移量，mode＝absolute | relative,默认为relative  
cursor.scroll(0,mode='absolute')  
result3 = cursor.fetchall()  
for i in result3:  
for ii in i:  
print ii

#以下2种方法都可以把数据插入数据库：  
#(one)  
for i in range (10,20):  
query2 = 'insert into t1 values("%d",now())' %i  
cursor.execute(query2)  
#提交  
conn.rollback()  
#(two)  
rows = []  
for i in range (10,20):  
rows.append(i)  
query2 = 'insert into t1 values("%s",now())'  
#executemany 2个参数,第2个参数是变量。  
cursor.executemany(query2,rows)  
#提交  
conn.commit()

#选择数据库  
query3 = 'select id from dba_hospital'  
#重新选择数据库  
conn.select_db('chushihua')

cursor.execute(query3)

result4 = cursor.fetchall()  
for i in result4:  
for ii in i:  
print ii  
#不定义query，直接执行：  
cursor.execute("set session binlog_format='mixed'")

#关闭游标，释放资源  
cursor.close()

'''  
+------+---------------------+  
| id | modifyT |  
+------+---------------------+  
| 3 | 2010-01-01 00:00:00 |  
| 1 | 2010-01-01 00:00:00 |  
| 2 | 2010-01-01 00:00:00 |  
| 3 | 2010-01-01 00:00:00 |  
| 4 | 2013-06-04 17:04:54 |  
| 7 | 2013-06-04 17:05:36 |  
| 6 | 2013-06-04 17:05:17 |  
+------+---------------------+

'''  

注意：在脚本中，密码写在脚本里面很容易暴露，这样可以用一个配置文件的方式来存密码，如db.conf：

_复制代码_ 代码如下:

  
[client]  
user=root  
password=123456  

二， **python 操作 MongoDB** :

_复制代码_ 代码如下:

  
#!/bin/env python  
# -*- encoding: utf-8 -*-  
#-------------------------------------------------------------------------------  
# Purpose: example for python_to_mongodb  
# Author: zhoujy  
# Created: 2013-06-14  
# update: 2013-06-14  
#-------------------------------------------------------------------------------  
import pymongo  
import os

#建立和数据库系统的连接,创建Connection时，指定host及port参数  
conn = pymongo.Connection(host='127.0.0.1',port=27017)

#admin 数据库有帐号，连接-认证-切换库  
db_auth = conn.admin  
db_auth.authenticate('sa','sa')  
#连接数据库  
db = conn.abc

#连接表  
collection = db.stu

#查看全部表名称  
db.collection_names()  
#print db.collection_names()

#访问表的数据，指定列  
item = collection.find({},{"sname":1,"course":1,"_id":0})  
for rows in item:  
print rows.values()

#访问表的一行数据  
print collection.find_one()

#得到所有的列  
for rows in collection.find_one():  
print rows

#插入  
collection.insert({"sno":100,"sname":"jl","course":{"D":80,"S":85}})  
#或  
u = dict(sno=102,sname='zjjj',course={"D":80,"S":85})  
collection.insert(u)

#得到行数  
print collection.find().count()  
print collection.find({"sno":100})

#排序，按照某一列的值。pymongo.DESCENDING:倒序；pymongo.ASCENDING:升序。按照sno倒序  
item = collection.find().sort('sno',pymongo.DESCENDING)  
for rows in item:  
print rows.values()

#多列排序  
item =
collection.find().sort([('sno',pymongo.DESCENDING),('A',pymongo.ASCENDING)])

#更新，第一个参数是条件，第二个参数是更新操作，$set,%inc,$push,$ne,$addToSet,$rename 等  
collection.update({"sno":100},{"$set":{"sno":101}})  
#更新多行和多列  
collection.update({"sno":102},{"$set":{"sno":105,"sname":"SSSS"}},multi=True)

#删除，第一个参数是条件，第二个参数是删除操作。  
collection.remove({"sno":101})

'''  
sno:学号；sname：姓名；course：科目

db.stu.insert({"sno":1,"sname":"张三","course":{"A":95,"B":90,"C":65,"D":74,"E":100}})  
db.stu.insert({"sno":2,"sname":"李四","course":{"A":90,"B":85,"X":75,"Y":64,"Z":95}})  
db.stu.insert({"sno":3,"sname":"赵五","course":{"A":70,"B":56,"F":85,"G":84,"H":80}})  
db.stu.insert({"sno":4,"sname":"zhoujy","course":{"A":64,"B":60,"C":95,"T":94,"Y":85}})  
db.stu.insert({"sno":5,"sname":"abc","course":{"A":87,"B":70,"Z":56,"G":54,"H":75}})  
db.stu.insert({"sno":6,"sname":"杨六","course":{"A":65,"U":80,"C":78,"R":75,"N":90}})  
db.stu.insert({"sno":7,"sname":"陈二","course":{"A":95,"M":68,"N":84,"S":79,"K":89}})  
db.stu.insert({"sno":8,"sname":"zhoujj","course":{"P":90,"B":77,"J":85,"K":68,"L":80}})  
db.stu.insert({"sno":9,"sname":"ccc","course":{"Q":85,"B":86,"C":90,"V":87,"U":85}})

'''  

计算Mongodb文档中各集合的数目：

_复制代码_ 代码如下:

  
import pymongo

conn = pymongo.Connection(host='127.0.0.1',port=27017)  
db = conn.abc #abc文档  
for tb_name in db.collection_names(): #循环出各集合名  
Count = db[tb_name].count() #计算各集合的数量  
if Count > 2: #过滤条件  
print tb_name + ':' + str(Count)

'''  
conn = pymongo.Connection(host='127.0.0.1',port=27017)  
db = conn.abc  
for tb_name in db.collection_names():  
print tb_name + ':'  
exec('print ' + 'db.'+tb_name+'.count()') #变量当集合的处理方式

OR

conn = pymongo.Connection(host='127.0.0.1',port=27017)  
db = conn.abc  
for tb_name in db.collection_names():  
mon_dic=db.command("collStats", tb_name) #以字典形式返回  
print mon_dic.get('ns'),mon_dic.get('count')

'''  

三， **python 操作 Redis** :

_复制代码_ 代码如下:

  
#!/bin/env python  
# -*- encoding: utf-8 -*-  
#-------------------------------------------------------------------------------  
# Purpose: example for python_to_mongodb  
# Author: zhoujy  
# Created: 2013-06-14  
# update: 2013-06-14  
#-------------------------------------------------------------------------------

import redis

f = open('aa.txt')  
while True:  
line = f.readline().strip().split(' # ')  
if line == ['']:  
break  
UserName,Pwd,Email = line  
# print name.strip(),pwd.strip(),email.strip()  
rc = redis.StrictRedis(host='127.0.0.1',port=6379,db=15)  
rc.hset('Name:' + UserName,'Email',Email)  
rc.hset('Name:' + UserName,'Password',Pwd)  
f.close()

alluser = rc.keys('*')  
#print alluser  
print
"===================================读出存进去的数据==================================="  
for user in alluser:  
print ' #
'.join((user.split(':')[1],rc.hget(user,'Password'),rc.hget(user,'Email')))  

四， **python 操作 memcache** :

_复制代码_ 代码如下:

  
import memcache  
mc = memcache.Client(['127.0.0.1:11211'],debug=1)  

_复制代码_ 代码如下:

  
#!/usr/bin/env python  
#coding=utf-8  
import MySQLdb  
import memcache  
import sys  
import time

def get_data(mysql_conn):  
# nn = raw_input("press string name:")  
mc = memcache.Client(['127.0.0.1:11211'],debug=1)  
t1 =time.time()  
value = mc.get('zhoujinyia')  
if value == None:  
t1 = time.time()  
print t1  
query = "select company,email,sex,address from uc_user_offline where realName
= 'zhoujinyia'"  
cursor= mysql_conn.cursor()  
cursor.execute(query)  
item = cursor.fetchone()  
t2 = time.time()  
print t2  
t = round(t2-t1)  
print "from mysql cost %s sec" %t  
print item  
mc.set('zhoujinyia',item,60)  
else :  
t2 = time.time()  
t=round(t2-t1)  
print "from memcache cost %s sec" %t  
print value  
if __name__ =='__main__':  
mysql_conn =
MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456',db='member',port=3306,charset='utf8')  
get_data(mysql_conn)  

