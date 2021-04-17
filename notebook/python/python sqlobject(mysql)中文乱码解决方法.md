UnicodeEncodeError: 'latin-1' codec can't encode characters in position；  
找了一天终于搞明白了，默认情况下，mysql连接的编码是latin-1，你需要指定使用什么编码方式:  
connectionForURI(mysql://user:password@localhost:3306/eflow?use_unicode=1&charset=utf8)  
  

Python mysql 中文乱码 的解决方法，有需要的朋友不妨看看。  
  
先来看一段代码：  

_复制代码_ 代码如下:

  
import MySQLdb  
db_user = "tiger"  
db_pw = "tiger"  
db = MySQLdb.connect(host="localhost", user=db_user, passwd=db_pw
,db="finaltldw",charset="gb2312")  
c = db.cursor()  
c.execute("""select id, name from NODES""")  
i=0;  
for id, name in c.fetchall():  
print "%2d %s" % (id, name)  
i=i+1  
if i==100:  
break  

返回结果:  
1 TOP  
2 教育  
3 机构  
4 人  
5 地区  
6 单位  
7 科学研究  
8 实验室  
9 类型  
  
如果编码是UTF-8  
转载一个解决方案: 其中的use db  
  
Python操作MySQL以及中文乱码的问题  
Python操作MySQL需要安装Python-MySQL  
可以从网上搜索一下，和一般的Python包一样安装  
  
安装好之后，模块名字叫做MySQLdb ，在Window和Linux环境下都可以使用，试验了一下挺好用，  
不过又发现了烦人的乱麻问题，最后用了几个办法，解决了！  
  
我用了下面几个措施，保证MySQL的输出没有乱麻：  
1 Python文件设置编码 utf-8 （文件前面加上 #encoding=utf-8)  
2 MySQL数据库charset=utf-8  
3 Python连接MySQL是加上参数 charset=utf8  
4 设置Python的默认编码为 utf-8 (sys.setdefaultencoding(utf-8)  
mysql_test.py

_复制代码_ 代码如下:

  
#encoding=utf-8  
import sys  
import MySQLdb  
  
reload(sys)  
sys.setdefaultencoding('utf-8')  
  
db=MySQLdb.connect(user='root',charset='utf8')  
cur=db.cursor()  
cur.execute('use mydb')  
cur.execute('select * from mytb limit 100')  
  
f=file("/home/user/work/tem.txt",'w')  
  
for i in cur.fetchall():  
f.write(str(i))  
f.write(" ")  
  
f.close()  
cur.close()  

上面是linux上的脚本,windows下运行正常!  
  
注：MySQL的配置文件设置也必须配置成utf8  
  
设置 MySQL 的 my.cnf 文件，在 [client]/[mysqld]部分都设置默认的字符集（通常在/etc/mysql/my.cnf)：  
[client]  
default-character-set = utf8  
[mysqld]  
default-character-set = utf8

