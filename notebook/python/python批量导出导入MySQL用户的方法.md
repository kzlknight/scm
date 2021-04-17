数据库迁移(A -> B)，需要把用户也迁移过去，而用户表（mysql.user）有上百个用户。有2种方法进行快速迁移：  
1，在同版本的条件下，直接备份A服务器的mysql数据库，还原到B服务器。  
2，要是不同版本的数据(5.1 ->
5.5)，很可能mysql数据库下面的一些表结构，甚至表数据的默认值都不一样，按照1的方法进行迁移，虽然最后也是可以正常访问，但是还是有些不太放心，很可能会影响到了B服务器上的MySQL，这样就需要用命令行来生成帐号了，这样是最安全和放心的。下面用python脚本来进行批量导出：

_复制代码_ 代码如下:

  
#!/bin/env python  
# -*- encoding: utf-8 -*-  
#-----------------------------------------  
# Name: mysql_user_dump.py  
# Purpose: 批量导出用户  
# Author: zhoujy  
# Created: 2013-05-28  
#-----------------------------------------  
import MySQLdb

def get_data(conn):  
query = 'select user,host from mysql.user order by user'  
cursor = conn.cursor()  
cursor.execute(query)  
lines = cursor.fetchall()  
return lines

def output_data(conn,rows):  
for user,host in rows:  
query = "show grants for '%s'@'%s'" %(user,host)  
cursor = conn.cursor()  
cursor.execute(query)  
show_pri = cursor.fetchall()  
for grants_command in show_pri:  
print ''.join(grants_command)+';'  
print ''

if __name__ =='__main__':  
conn =
MySQLdb.connect(host='localhost',user='root',passwd='123456',db='mysql',port=3306,charset='utf8')  
rows = get_data(conn)  
output_data(conn,rows)  

运行：python mysql_user_dump.py

_复制代码_ 代码如下:

  
GRANT REPLICATION SLAVE ON *.* TO 'rep'@'192.168.234.%' IDENTIFIED BY PASSWORD
'*6BB4837EB74329105EE4568DDA7DC67ED2CA2AD9';

GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' IDENTIFIED BY PASSWORD
'*6BB4837EB74329105EE4568DDA7DC67ED2CA2AD9' WITH GRANT OPTION;

GRANT ALL PRIVILEGES ON *.* TO 'root'@'192.168.234.%' IDENTIFIED BY PASSWORD
'*6BB4837EB74329105EE4568DDA7DC67ED2CA2AD9';

GRANT USAGE ON *.* TO 'test'@'192.168.234.%' IDENTIFIED BY PASSWORD
'*2A032F7C5BA932872F0F045E0CF6B53CF702F2C5';  
GRANT SELECT, INSERT, UPDATE, DELETE ON `test`.* TO 'test'@'192.168.234.%';

GRANT USAGE ON *.* TO 'zzz_test'@'192.168.234.%' IDENTIFIED BY PASSWORD
'*2A032F7C5BA932872F0F045E0CF6B53CF702F2C5';  
GRANT SELECT, INSERT, UPDATE, DELETE ON `zzz%`.* TO
'zzz_test'@'192.168.234.%';  

最后把这些命令在B上面执行就好了，也可以在执行脚本的时候重定向到一个sql文件：如:user.sql，在到B服务器的数据库里面执行source
user.sql 就完成了导入工作。  
第2个方法最好，不需要1里面的删表和重建表的操作，最安全。

