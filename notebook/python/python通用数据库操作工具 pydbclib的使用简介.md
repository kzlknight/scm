pydbclib是一个通用的python关系型数据库操作工具包，使用统一的接口操作各种关系型数据库（如
oracle、mysql、postgres、hive、impala等）进行增删改查，它是对各个python数据库连接驱动包（如sqlalchemy、pymysql、cx_Oracle、pyhive、pyodbc、impala等）的封装，依照python最简原则SQL占位符统一成
':[name]' 这一种形式，这点和sqlalchemy是一样的

##  安装

```python

    pip3 install pydbclib
```

##  简单使用  

看下简单的查询示例

```python

    from pydbclib import connect
    # 使用with上下文，可以自动提交，自动关闭连接
    with connect("sqlite:///:memory:") as db:
      db.execute('create table foo(a integer, b varchar(20))')
      # 统一使用':[name]'形式的SQL的占位符
      db.execute("insert into foo(a,b) values(:a,:b)", [{"a": 1, "b": "one"}]*4)
      print(db.read("select * from foo").get_one())
      print(db.read("select * from foo").get_all())
      print(db.read("select * from foo").to_df())
      db.get_table("foo").insert({"a": 2, "b": "two"})
      print(db.get_table("foo").find_one({"a": 2}))
      print(db.get_table("foo").find().get_all())
      print(db.get_table("foo").find().to_df())
```

查询结果记录是以字典形式展现，向库里写入记录也是字典形式，如果要使用原生元祖形式，查询函数read里添加as_dict=False参数

##  接口文档  

数据库连接，更多常用数据库连接方式参考文章结尾

```python

    # connect函数有个driver参数决定你是通过哪个数据库驱动包去连接的
    # driver参数默认值是sqlalchemy，即通过sqlalchemy驱动包连接数据库
    >>> db = pydbclib.connect("sqlite:///:memory:")
    >>> db = pydbclib.connect(":memory:", driver='sqlite3')
    # 也可以传入驱动包连接对象
    >>> import sqlite3
    >>> db = pydbclib.connect(driver=sqlite3.connect(":memory:"))
    >>> from sqlalchemy import create_engine
    >>> db = pydbclib.connect(driver=create_engine("sqlite:///:memory:"))
```

###  原生SQL接口  

1. 使用execute方法执行SQL，和各数据库连接包基本一致，不同点是它既可以单条执行，也可以批量执行(相当于executemany)，另外该方法的SQL占位符是':[name]'形式 
```python

    >>> record = {"a": 1, "b": "one"}
    >>> db.execute('create table foo(a integer, b varchar(20))')
    # 插入单条记录，结果返回影响行数
    >>> db.execute("insert into foo(a,b) values(:a,:b)", record)
    1
    # 插入多条记录
    >>> db.execute("insert into foo(a,b) values(:a,:b)", [record, record])
    2
```

2. 查询数据 
```python

    # 查询结果只返回一条记录
    >>> db.read_one("select * from foo")
    {'a': 1, 'b': 'one'}
    #read返回迭代器类型，用get方法获取前几条记录，使用map对每条记录进行数据清洗
    >>> db.read("select * from foo").map(lambda x: {f"foo.{k}": v for k,v in x.items()}).get(2)
    # as_dict=False返回原生元祖记录
    >>> db.read("select * from foo", as_dict=False).get(2)
    [(1, 'one'), (1, 'one')]
    # 也可以直接for遍历
    >>> for r in db.read("select * from foo"):
    ...   print(r)
    ... 
    {'a': 1, 'b': 'one'}
    {'a': 1, 'b': 'one'}
    {'a': 1, 'b': 'one'}
    # 转换成pandas dataframe对象, 前提已经安装了pandas
    >>> db.read("select * from foo").to_df()
      a  b
    0 1 one
    1 1 one
    2 1 one
```

3. 提交、回滚、关闭连接 
```python

    >>> db.rollback()
    >>> db.commit()
    >>> db.close()
```

###  表级别操作的SQL接口封装  

1. 插入记录 
```python

    # 插入单条和插入多条，输入参数字典的键值必须和表中字段同名
    >>> db.get_table("foo").insert({"a": 1, "b": "one"})
    1
    >>> db.get_table("foo").insert([{"a": 1, "b": "one"}]*10)
    10
```

2. 查询记录 
```python

    # 查询字段a=1第一条记录
    >>> db.get_table("foo").find_one({"a": 1})
    {'a': 1, 'b': 'one'}
    # 也可以直接写成sql条件表达式，其他接口的条件参数类似都可以是表达式
    >>> db.get_table("foo").find_one("a=1")
    {'a': 1, 'b': 'one'}
    # 查询字段a=1所有记录，find返回迭代器对象同上面read方法
    >>> db.get_table("foo").find({"a": 1}).get_all()
    [{'a': 1, 'b': 'one'},...{'a': 1, 'b': 'one'}]
```

3. 更新记录 
```python

    # 将a=1那条记录的b字段值更新为"first"
    >>> db.get_table("foo").update({"a": 1}, {"b": "first"})
    11
    >>> db.get_table("foo").find({"a": 1}).get_one()
    {'a': 1, 'b': 'first'}
```

4. 删除记录 
```python

    # 将a=1那条记录删除
    >>> db.get_table("foo").delete({"a": 1})
    11
    >>> db.get_table("foo").find({"a": 1}).get_all()
    []
```

##  常用数据库连接  

1. Common Driver 
```python

    # 使用普通数据库驱动连接，driver参数指定驱动包名称
    # 例如pymysql包driver='pymysql',connect函数其余的参数和driver参数指定的包的创建连接参数一致
    # 连接mysql
    db = pydbclib.connect(user="user", password="password", database="test", driver="pymysql")
    # 连接oracle
    db = pydbclib.connect('user/password@local:1521/xe', driver="cx_Oracle")
    # 通过odbc方式连接
    db = pydbclib.connect('DSN=mysqldb;UID=user;PWD=password', driver="pyodbc") 
    # 通过已有驱动连接方式连接
    import pymysql
    con = pymysql.connect(user="user", password="password", database="test")
    db = pydbclib.connect(driver=con)
```

2. Sqlalchemy Driver 
```python

    # 使用Sqlalchemy包来连接数据库，drvier参数默认为'sqlalchemy'
    # 连接oracle
    db = pydbclib.connect("oracle://user:password@local:1521/xe")
    # 连接mysql
    db = pydbclib.connect("mysql+pyodbc://:@mysqldb")
    # 通过已有engine连接
    from sqlalchemy import create_engine
    engine = create_engine("mysql+pymysql://user:password@localhost:3306/test")
    db = pydbclib.connect(driver=engine)
```

使用过程中有任何疑问，欢迎评论交流  
项目地址 [ pydbclib ](https://github.com/taogeYT/pydbclib)

以上就是python通用数据库操作工具 pydbclib的使用简介的详细内容，更多关于python
数据库操作工具pydbclib的资料请关注脚本之家其它相关文章！

