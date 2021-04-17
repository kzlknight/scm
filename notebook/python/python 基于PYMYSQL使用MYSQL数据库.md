在做测试的时候都会用到数据库，今天写一篇通过python连接MYSQL数据库

##  什么是MYSQL数据库  

MySQL是一个关系型数据库管理系统，由瑞典MySQL AB 公司开发，目前属于 Oracle 旗下产品。MySQL 是最流行的关系型数据库管理系统之一，在
WEB 应用方面，MySQL是最好的 RDBMS (Relational Database Management System，关系数据库管理系统)
应用软件之一。

##  什么是PYMYSQL  

PyMySQL 是在 Python3.x 版本中用于连接 MySQL 服务器的一个库，Python2中则使用mysqldb。

PyMySQL 遵循 Python 数据库 API v2.0 规范，并包含了 pure-Python MySQL 客户端库。

###  PyMySQL安装

```python

    pip install pymysql
```

##  PyMySQL使用  

###  连接数据库  

1、首先导入PyMySQL模块

2、连接数据库（通过connect()）

3、创建一个数据库对象 （通过cursor()）

4、进行对数据库做增删改查

```python

    # coding:utf-8
    import pymysql
    # 连接数据库
    count = pymysql.connect(
          host = 'xx.xxx.xxx.xx', # 数据库地址
          port = 3306,  # 数据库端口号
          user='xxxx',  # 数据库账号
          password='XXXX',  # 数据库密码
          db = 'test_sll')  # 数据库表名# 创建数据库对象
    db = count.cursor()
```

###  查找数据  

db.fetchone()获取一条数据

db.fetchall()获取全部数据

```python

    # coding:utf-8
    import pymysql
    # 连接数据库
    count = pymysql.connect(
          host = 'xx.xxx.xxx.xx', # 数据库地址
          port = 3306,  # 数据库端口号
          user='xxxx',  # 数据库账号
          password='xxxx',  # 数据库密码
          db = 'test_sll')  # 数据库名称
    # 创建数据库对象
    db = count.cursor()
    # 写入SQL语句
    sql = "select * from students "
    # 执行sql命令
    db.execute(sql)
    # 获取一个查询
    # restul = db.fetchone()
    # 获取全部的查询内容
    restul = db.fetchall()
    print(restul)
    db.close()
```

###  修改数据  

commit() 执行完SQL后需要提交保存内容

```python

    # coding:utf-8
    import pymysql
    # 连接数据库
    count = pymysql.connect(
          host = 'xx.xxx.xxx.xx', # 数据库地址
          port = 3306,  # 数据库端口号
          user='xxx',  # 数据库账号
          password='xxx',  # 数据库密码
          db = 'test_sll')  # 数据库表名
    # 创建数据库对象
    db = count.cursor()
    # 写入SQL语句
    sql = "update students set age = '12' WHERE id=1"
    # 执行sql命令
    db.execute(sql)
    # 保存操作
    count.commit()
    db.close()
```

###  删除数据

```python

    # coding:utf-8
    import pymysql
    # 连接数据库
    count = pymysql.connect(
          host = 'xx.xxx.xxx.xx', # 数据库地址
          port = 3306,  # 数据库端口号
          user='xxxx',  # 数据库账号
          password='xxx',  # 数据库密码
          db = 'test_sll')  # 数据库表名
    # 创建数据库对象
    db = count.cursor()
    # 写入SQL语句
    sql = "delete from students where age = 12"
    # 执行sql命令
    db.execute(sql)
    # 保存提交
    count.commit()
    db.close()
```

###  新增数据  

新增数据这里涉及到一个事务问题，事物机制可以保证数据的一致性，比如插入一个数据，不会存在插入一半的情况，要么全部插入，要么都不插入

```python

    # coding:utf-8
    import pymysql
    # 连接数据库
    count = pymysql.connect(
          host = 'xx.xxx.xxx.xx', # 数据库地址
          port = 3306,  # 数据库端口号
          user='xxxx',  # 数据库账号
          password='xxx',  # 数据库密码
          db = 'test_sll')  # 数据库表名
    # 创建数据库对象
    db = count.cursor()
    # 写入SQL语句
    sql = "insert INTO students(id,name,age)VALUES (2,'安静','26')"
    # 执行sql命令
    db.execute(sql)
    # 保存提交
    count.commit()
    db.close()
```

到这可以发现除了查询不需要保存，其他操作都要提交保存，并且还会发现删除，修改，新增，只是修改了SQL，其他的没什么变化

###  创建表  

创建表首先我们先定义下表内容的字段

字段名  |  含义  |  类型  
---|---|---  
id  |  id  |  varchar  
name  |  姓名  |  varchar  
age  |  年龄  |  int

```python

    # coding:utf-8
    import pymysql
    # 连接数据库
    count = pymysql.connect(
          host = 'xx.xxx.xxx.xx', # 数据库地址
          port = 3306,  # 数据库端口号
          user='xxxx',  # 数据库账号
          password='xxx',  # 数据库密码
          db = 'test_sll')  # 数据库表名
    # 创建数据库对象
    db = count.cursor()
    # 写入SQL语句
    sql = 'CREATE TABLE students (id VARCHAR(255) ,name VARCHAR(255) ,age INT)'
    # 执行sql命令
    db.execute(sql)
    db.close()
```  
  
以上就是python 基于PYMYSQL使用MYSQL数据库的详细内容，更多关于python 使用MySQL的资料请关注脚本之家其它相关文章！

