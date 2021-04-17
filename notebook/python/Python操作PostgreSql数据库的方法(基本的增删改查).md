##  Python操作PostgreSql数据库（基本的增删改查）

操作数据库最快的方式当然是直接用使用SQL语言直接对数据库进行操作，但是偶尔我们也会碰到在代码中操作数据库的情况，我们可能用ORM类的库对数控库进行操作，但是当需要操作大量的数据时，ORM的数据显的太慢了。在python中，遇到这样的情况，我推荐使用
` psycopg2 ` 操作 ` postgresql ` 数据库

##  psycopg2

> 官方文档传送门： http://initd.org/psycopg/docs/index.html

##  简单的增删改查

###  连接

连接pg并创建表

```python

    PG_SQL_LOCAL = {
     'database': 'postgres',
     'user': 'postgres',
     'password': "8dsa581",
     # 'host':'10.27.78.1',
     'host': 'localhost'
    }
    
    def connectPostgreSQL():
     conn = psycopg2.connect(**PG_SQL_LOCAL)
     print('connect successful!')
     cursor = conn.cursor()
     cursor.execute('''
     create table public.members(
     id integer not null primary key,
     name varchar(32) not null,
     password varchar(32) not null,
     singal varchar(128)
     )''')
     conn.commit()
     conn.close()
     print('table public.member is created!')
```

###  增

一条一条的增加数据

```python

    def insertOperate():
     conn = psycopg2.connect(**PG_SQL_LOCAL)
     cursor = conn.cursor()
     cursor.execute("insert into public.member(id,name,password,singal)\
    values(1,'member0','password0','signal0')")
     cursor.execute("insert into public.member(id,name,password,singal)\
    values(2,'member1','password1','signal1')")
     cursor.execute("insert into public.member(id,name,password,singal)\
    values(3,'member2','password2','signal2')")
     cursor.execute("insert into public.member(id,name,password,singal)\
    values(4,'member3','password3','signal3')")
     row = conn.fetchone()
     print(row)
     conn.commit()
     conn.close()
    
     print('insert records into public.memmber successfully')
```

###  查

  * fetchall() 一次性获取所有数据 
  * fetchmany() 一次值提取2000条数据（使用服务端的游标） 

```python

    def selectOperate():
     conn = psycopg2.connect(**PG_SQL_LOCAL)
     cursor = conn.cursor()
     cursor.execute("select id,name,password,singal from public.member where id>2")
     # rows = cursor.fetchall()
     # for row in rows:
     # print('id=', row[0], ',name=', row[1], ',pwd=', row[2], ',singal=', row[3],)
    
     while True:
     rows = cursor.fetchmany(2000)
     if not rows:
      break
     for row in rows:
      # print('id=', row['id'], ',name=', row['name'], ',pwd=', row['pwd'], ',singal=', row['singal'],)
      rid,name,pwd,singal = row
      print(rid,name,pwd,singal)
      # print('id=', row[0], ',name=', row[1], ',pwd=', row[2], ',singal=', row[3], )
     conn.close()
```

###  改

更新数据

```python

    def updateOperate():
     conn = psycopg2.connect(**PG_SQL_LOCAL)
     cursor=conn.cursor()
     result = cursor.execute("update public.member set name='member X' where id=3")
     print(result)
     conn.commit()
     print("Total number of rows updated :", cursor.rowcount)
    
     cursor.execute("select id,name,password,singal from public.member")
     rows=cursor.fetchall()
     for row in rows:
     print('id=',row[0], ',name=',row[1],',pwd=',row[2],',singal=',row[3],'\n')
     conn.close()
```

###  删

删除数据

```python

    def deleteOperate():
     conn = psycopg2.connect(**PG_SQL_LOCAL)
     cursor = conn.cursor()
    
     cursor.execute("select id,name,password,singal from public.member")
     rows = cursor.fetchall()
     for row in rows:
     print('id=', row[0], ',name=', row[1], ',pwd=', row[2], ',singal=', row[3], '\n')
    
     print('begin delete')
     cursor.execute("delete from public.member where id=2")
     conn.commit()
     print('end delete')
     print("Total number of rows deleted :", cursor.rowcount)
    
     cursor.execute("select id,name,password,singal from public.member")
     rows = cursor.fetchall()
     for row in rows:
     print('id=', row[0], ',name=', row[1], ',pwd=', row[2], ',singal=', row[3], '\n')
     conn.close()
```

###  补充，增加的字段带有时间格式

带有时间格式是，只需要传入时间格式的字符串（‘2017-05-27'）即可，PG会自动识别

```python

    cur.execute("INSERT INTO Employee "
      "VALUES('Gopher', 'China Beijing', 100, '2017-05-27')")
    # 查询数据
    cur.execute("SELECT * FROM Employee")
    rows = cur.fetchall()
    for row in rows:
     print('name=' + str(row[0]) + ' address=' + str(row[1]) +
      ' age=' + str(row[2]) + ' date=' + str(row[3]), type(row[3]))
    
     # 插入数据
     sql = """INSERT INTO Employees VALUES(%s, %s, %s,%s) """
     var = []
     var.append([row[0], row[1], row[2], row[3]])
     cur.executemany(sql, var)
    
    # 提交事务
    conn.commit()
    
    # 关闭连接
    conn.close()
```

到此这篇关于Python操作PostgreSql数据库(基本的增删改查)的文章就介绍到这了,更多相关Python操作PostgreSql数据库内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

