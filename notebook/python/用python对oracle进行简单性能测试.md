**一、概述**

dba在工作中避不开的两个问题，sql使用绑定变量到底会有多少的性能提升？数据库的审计功能如果打开对数据库的性能会产生多大的影响？最近恰好都碰到了，索性做个实验。

  1. sql使用绑定变量对性能的影响 
  2. 开通数据库审计功能对性能的影响 

实验采用的办法很简单，就是通过python读取csv文件，然后将其导入到数据库中，最后统计程序执行完成所需要的时间

**二、准备脚本**

python脚本dataimporttest.py

```python

    # author: yangbao
    # function: 通过导入csv，测试数据库性能
    
    import cx_Oracle
    import time
    
    
    # 数据库连接串
    DATABASE_URL = 'user/password@ip:1521/servicename'
    
    
    class CsvDataImport:
    
     def __init__(self, use_bind):
      self.csv_name = 'test.csv'
      self.use_bind = use_bind
      if use_bind == 1:
       self.insert_sql = "insert into testtb values(:0, " \
            "to_date(:1,'yyyy-mm-dd hh24:mi:ss'), " \
            "to_date(:2,'yyyy-mm-dd hh24:mi:ss'), " \
            ":3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14, " \
            ":15, :16, :17, :18, :19, :20, :21)" # 使用绑定变量的sql
      else:
       self.insert_sql = "insert into testtb values({0}, " \
            "to_date('{1}','yyyy-mm-dd hh24:mi:ss'), " \
            "to_date('{2}','yyyy-mm-dd hh24:mi:ss'), " \
            "{3}, {4}, '{5}', {6}, '{7}', {8}, {9}, {10}, {11}, {12}, {13}, {14}, " \
            "{15}, {16}, {17}, {18}, {19}, {20}, {21})" # 不使用绑定变量的sql
    
     def data_import(self):
    
       begin_time = time.perf_counter()
    
       try:
        conn = cx_Oracle.connect(DATABASE_URL)
        curs = conn.cursor()
    
        with open(self.csv_name) as f:
         csv_contents = f.readlines()
    
        import_rows = 0
    
        message = '{} start to import'.format(self.csv_name)
        print(message)
    
        for line, csv_content in enumerate(csv_contents[1:]):
    
         data = csv_content.split(',')
         if self.use_bind == 1:
          data = map(lambda x: None if x == '' else x, data)
         else:
          data = map(lambda x: 'null' if x == '' else x, data)
         data = list(data)
         data[-1] = data[-1].replace('\n', '')
    
         if self.use_bind == 1:
          curs.execute(self.insert_sql, data) # 使用绑定变量的方式插入数据
         else:
          # print(self.insert_sql.format(*data))
          curs.execute(self.insert_sql.format(*data)) # 使用非绑定变量的方式插入数据
         import_rows += 1
         if import_rows % 10000 == 0:
          curs.execute('commit')
          message = '{} has imported {} lines'.format(self.csv_name, import_rows)
          print(message)
    
        conn.commit()
        curs.close()
        conn.close()
    
        end_time = time.perf_counter()
    
        elapsed = round(end_time - begin_time, 2)
        message = '{}, import rows: {}, use_bind: {}, elapsed: {}'.format(
         self.csv_name, import_rows, self.use_bind, elapsed)
        print(message)
    
       except Exception as e:
        message = '{} import failed, reason: {}'.format(self.csv_name, str(e))
        print(message)
    
    
    if __name__ == '__main__':
     CsvDataImport(use_bind=1).data_import()
```

csv文件  
test.csv(内容略)

**三、测试sql使用绑定变量对性能的影响**  
a. 使用绑定变量  
对库进行重启，目的是清空数据库内的所有缓存，避免对实验结果产生干扰

```python

    SQL> startup force;
    SQL> drop table yang.testtb purge;
    SQL> create table yang.testtb as select * from yang.test where 1=0;
```

运行脚本python dataimporttest.py

结果：test.csv, import rows: 227795, use_bind: 1, elapsed: 260.31

b. 不使用绑定变量  
对库进行重启

```python

    SQL> startup force;
    SQL> drop table yang.testtb purge;
    SQL> create table yang.testtb as select * from yang.test where 1=0;
```

将脚本的最后一行CsvDataImport(use_bind=1).data_import()改为CsvDataImport(use_bind=0).data_import()

运行脚本python dataimporttest.py

结果：test.csv, import rows: 227795, use_bind: 0, elapsed: 662.82

可以看到同样的条件下，程序运行的时间，不使用绑定变量是使用绑定变量的2.54倍

**四、测试数据库开启审计功能对性能的影响**  
查看数据库审计功能是否开启

```python

    SQL> show parameter audit 
    NAME   TYPE  VALUE
    -------------- ----------- ----------
    audit_trail string  NONE
```

统计sys.aud$这张表的行数

```python

    SQL> select count(*) from sys.aud$;
    
     COUNT(*)
    ----------
       0
```

所以可以直接拿第三步中的（a. 使用绑定变量）的结果作为没开通审计功能程序运行的时间

对库开通审计功能，并进行重启

```python

    SQL> alter system set audit_trail=db,extended scope=spfile; # 如果设置成db，那么在sys.aud$里面sqltext将为空，也就是说看不到用户执行的sql语句，审计毫无意义
    SQL> startup force;
    SQL> drop table yang.testtb purge;
    SQL> create table yang.testtb as select * from yang.test where 1=0;
    SQL> audit insert table by yang; # 开通对用户yang的insert操作审计
```

将脚本的最后一行CsvDataImport(use_bind=0).data_import()改为CsvDataImport(use_bind=1).data_import()

运行脚本python dataimporttest.py

结果：test.csv, import rows: 227795, use_bind: 1, elapsed: 604.23

与前面使用绑定变量但没有开通数据库审计功能，程序运行的时间，开通数据库审计功能是不开通数据库审计功能的2.32倍

再来看看sys.aud$这张表的大小

```python

    SQL> select count(*) from sys.aud$;
    
     COUNT(*)
    ----------
     227798
```

因sys.aud$这张表中的sqltext与sqlbind都是clob字段，因此需要通过下面的sql去统计该表所占用的空间

```python

    SQL> select sum(bytes) from dba_extents where segment_name in (
    select distinct name from (select table_name, segment_name from dba_lobs where table_name='AUD$') 
    unpivot(name for i in(table_name, segment_name)));
    
    SUM(BYTES)
    ----------
     369229824
```

查看testtb这张表占用的空间

```python

    SQL> select sum(bytes) from dba_extents where segment_name in ('TESTTB');
    
    SUM(BYTES)
    ----------
     37748736
```

可以看到对一个22万行的csv数据导入到数据库，审计的表占用的空间就达到了惊人的360M，而testtb这张表本身也才37M而已

通过上面的实验可以得出，对于数据库的审计功能，开通后会严重拖慢数据库的性能以及消耗system表空间！

**五、总结**

  1. 代码中尽量使用绑定变量 
  2. 最好不要开通数据库的审计，可以通过堡垒机去实现对用户操作审计（ps：还请大家推荐个堡垒机厂商，这个才是本文最主要的目的_） 

实验存在不严谨的地方，相关对比数据也仅作为参考

以上就是用python对oracle进行简单性能测试的示例的详细内容，更多关于python 对Oracle进行性能测试的资料请关注脚本之家其它相关文章！

