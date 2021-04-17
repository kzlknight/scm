实例1、取得MYSQL版本

_复制代码_ 代码如下:

  
# -*- coding: UTF-8 -*-  
#安装MYSQL DB for python  
import MySQLdb as mdb  
con = None  
try:  
#连接mysql的方法：connect('ip','user','password','dbname')  
con = mdb.connect('localhost', 'root',  
'root', 'test');  
#所有的查询，都在连接con的一个模块cursor上面运行的  
cur = con.cursor()  
#执行一个查询  
cur.execute("SELECT VERSION()")  
#取得上个查询的结果，是单个结果  
data = cur.fetchone()  
print "Database version : %s " % data  
finally:  
if con:  
#无论如何，连接记得关闭  
con.close()  

执行结果：  
Database version : 5.5.25

实例2、创建一个表并且插入数据

_复制代码_ 代码如下:

  
# -*- coding: UTF-8 -*-  
import MySQLdb as mdb  
import sys  
#将con设定为全局连接  
con = mdb.connect('localhost', 'root', 'root', 'test');  
with con:  
#获取连接的cursor，只有获取了cursor，我们才能进行各种操作  
cur = con.cursor()  
#创建一个数据表 writers(id,name)  
cur.execute("CREATE TABLE IF NOT EXISTS \  
Writers(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(25))")  
#以下插入了5条数据  
cur.execute("INSERT INTO Writers(Name) VALUES('Jack London')")  
cur.execute("INSERT INTO Writers(Name) VALUES('Honore de Balzac')")  
cur.execute("INSERT INTO Writers(Name) VALUES('Lion Feuchtwanger')")  
cur.execute("INSERT INTO Writers(Name) VALUES('Emile Zola')")  
cur.execute("INSERT INTO Writers(Name) VALUES('Truman Capote')")  

实例3、python使用slect获取mysql的数据并遍历

_复制代码_ 代码如下:

  
# -*- coding: UTF-8 -*-  
import MySQLdb as mdb  
import sys  
#连接mysql，获取连接的对象  
con = mdb.connect('localhost', 'root', 'root', 'test');  
with con:  
#仍然是，第一步要获取连接的cursor对象，用于执行查询  
cur = con.cursor()  
#类似于其他语言的query函数，execute是python中的执行查询函数  
cur.execute("SELECT * FROM Writers")  
#使用fetchall函数，将结果集（多维元组）存入rows里面  
rows = cur.fetchall()  
#依次遍历结果集，发现每个元素，就是表中的一条记录，用一个元组来显示  
for row in rows:  
print row  

_复制代码_ 代码如下:

  
执行结果：  
(1L, ‘Jack London')  
(2L, ‘Honore de Balzac')  
(3L, ‘Lion Feuchtwanger')  
(4L, ‘Emile Zola')  
(5L, ‘Truman Capote')  

实例4、使用字典cursor取得结果集（可以使用表字段名字访问值）

_复制代码_ 代码如下:

  
# -*- coding: UTF-8 -*-  
# 来源：疯狂的蚂蚁的博客www.server110.com总结整理  
import MySQLdb as mdb  
import sys  
#获得mysql查询的链接对象  
con = mdb.connect('localhost', 'root', 'root', 'test')  
with con:  
#获取连接上的字典cursor，注意获取的方法，  
#每一个cursor其实都是cursor的子类  
cur = con.cursor(mdb.cursors.DictCursor)  
#执行语句不变  
cur.execute("SELECT * FROM Writers")  
#获取数据方法不变  
rows = cur.fetchall()  
#遍历数据也不变（比上一个更直接一点）  
for row in rows:  
#这里，可以使用键值对的方法，由键名字来获取数据  
print "%s %s" % (row["Id"], row["Name"])  

实例5、获取单个表的字段名和信息的方法

_复制代码_ 代码如下:

  
# -*- coding: UTF-8 -*-  
# 来源：疯狂的蚂蚁的博客www.server110.com总结整理  
import MySQLdb as mdb  
import sys  
#获取数据库的链接对象  
con = mdb.connect('localhost', 'root', 'root', 'test')  
with con:  
#获取普通的查询cursor  
cur = con.cursor()  
cur.execute("SELECT * FROM Writers")  
rows = cur.fetchall()  
#获取连接对象的描述信息  
desc = cur.description  
print 'cur.description:',desc  
#打印表头，就是字段名字  
print "%s %3s" % (desc[0][0], desc[1][0])  
for row in rows:  
#打印结果  
print "%2s %3s" % row  

_复制代码_ 代码如下:

  
运行结果： cur.description: ((‘Id', 3, 1, 11, 11, 0, 0), (‘Name', 253, 17, 25, 25,
0, 1))  
Id Name  
1 Jack London  
2 Honore de Balzac  
3 Lion Feuchtwanger  
4 Emile Zola  
5 Truman Capote  

  
实例6、使用Prepared statements执行查询（更安全方便）

_复制代码_ 代码如下:

  
# -*- coding: UTF-8 -*-  
# 来源：疯狂的蚂蚁的博客www.server110.com总结整理  
import MySQLdb as mdb  
import sys  
con = mdb.connect('localhost', 'root', 'root', 'test')  
with con:  
cur = con.cursor()  
#我们看到，这里可以通过写一个可以组装的sql语句来进行  
cur.execute("UPDATE Writers SET Name = %s WHERE Id = %s",  
("Guy de Maupasant", "4"))  
#使用cur.rowcount获取影响了多少行  
print "Number of rows updated: %d" % cur.rowcount  

  
结果：  

_复制代码_ 代码如下:

  
Number of rows updated: 1  

