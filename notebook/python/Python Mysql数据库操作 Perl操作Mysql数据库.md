首先下载 MySQLdb  
#encoding=GBK  
import MySQLdb  
#import sys  
#  
#reload(sys)  
#sys.setdefaultencoding('utf-8')  
print 'Connection ...'  
host='192.168.1.77'  
user='root'  
passwd='123456'  
db='test'  
conn = MySQLdb.connect(host,user,passwd,db,charset='gbk')  
print 'Connection success'  
cursor = conn.cursor()  
#query = "insert into test(id,name) values(%s , %s)"  
#param = ("1","汉字")  
#cursor.execute(query,param)  
#  
#conn.commit()  
cursor.execute('select * from test')  
rows = cursor.fetchall()  
for row in rows:  
print row[1]  
cursor.close()  
conn.close()  
Perl操作Mysql数据库 网上的比较详细的方法  
一. 安装DBI模块  
步骤1：  
从TOOLS栏目中下载DBI.zip,下载完后用winzip解开到一个temp目录,共有三个文件：  
Readme  
DBI.ppd  
DBI.tar.gz  
步骤2：  
在DOS窗口下，temp目录中运行下面的DOS命令：  
ppm install DBI.ppd  
如果提示无效命令,可在perl/bin目录下运行  
二. 安装DBD-Mysql模块  
从软件下载中下载DBD-Mysql.zip,安装方法同一.  
三. 准备数据库  
启动mysql,首先创建一个数据库mydata,然后创建一个表address  
mysql> create database mydata;  
Query OK, 1 row affected (0.00 sec)  
mysql> use mydata;  
Database changed  
mysql> create table address (  
-> id int(5) not null,   
-> name varchar(40) not null,   
-> email varchar(50) not null,   
-> telephone int(12) null);   
Query OK, 0 rows affected (0.05 sec)  
输入些数据:  
mysql> insert into address values (  
-> 1,'Nighthawk','nighthawk@163.net',92384092);   
Query OK, 1 row affected (0.00 sec)  
四. 下面用perl程序来插入若干记录并做查询.  
use DBI;  
#连接数据库mydata  
my $dbh = DBI->connect('DBI:mysql:mydata') or die "无法连接数据库: " . DBI->errstr;  
print "插入若干记录\n";  
my $sth = $dbh->prepare(q{  
INSERT INTO address (id, name,email,telephone) VALUES (?, ?, ?, ?)  
}) });  
print "输入记录,回车结束:";  
while ($inputdata =<>) {  
chop $inputdata;  
last unless($inputdata);  
my ($id, $name,$email, $tel) = split( /,/, $inputdata);  
$sth->execute($id, $name, $email,$tel)  
}  
# $dbh->commit;  
print "下面根据输入的名字打印出EMAIL地址和电话\n";  
my $sth = $dbh->prepare('SELECT * FROM address WHERE name=?')  
or die $dbh->errstr;  
print "请输入姓名,回车结束:";  
while ($inputname =<>) {  
my @data;  
chomp $inputname;  
last unless($inputname);  
$sth->execute($inputname) or die "错误: " . $sth->errstr;  
while (@data = $sth->fetchrow_array()) {  
print "Email:$data[2]\t Telephone:$data[3]\n";  
}  
}  
#断开连接  
$dbh->disconnect;  
Nighthawk  

