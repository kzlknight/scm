**场景描述**

线上mysql数据库里面有张表保存有每天的统计结果，每天有1千多万条，这是我们意想不到的，统计结果咋有这么多。运维找过来，磁盘占了200G，最后问了运营，可以只保留最近3天的，前面的数据，只能删了。删，怎么删？  
因为这是线上数据库，里面存放有很多其它数据表，如果直接删除这张表的数据，肯定不行，可能会对其它表有影响。尝试每次只删除一天的数据，还是卡顿的厉害，没办法，写个Python脚本批量删除吧。  
具体思路是：

  * 每次只删除一天的数据； 
  * 删除一天的数据，每次删除50000条； 
  * 一天的数据删除完，开始删除下一天的数据；   

**Python代码**

```python

    # -*-coding:utf-8 -*-
    
    import sys
    
    # 这是我们内部封装的Python Module
    sys.path.append('/var/lib/hadoop-hdfs/scripts/python_module2')
    import keguang.commons as commons
    import keguang.timedef as timedef
    import keguang.sql.mysqlclient as mysql
    
    def run(starttime, endtime, regx):
     tb_name = 'statistic_ad_image_final_count'
     days = timedef.getDays(starttime,endtime,regx)
     # 遍历删除所有天的数据
     for day in days:
      print '%s 数据删除开始'%(day)
      mclient = getConn()
      sql = '''
      select 1 from %s where date = '%s' limit 1
      '''%(tb_name, day)
      print sql
      result = mclient.query(sql)
      # 如果查询到了这一天的数据，继续删除
      while result is not ():
       sql = 'delete from %s where date = "%s" limit 50000'%(tb_name, day)
       print sql
       mclient.execute(sql)
       sql = '''
       select 1 from %s where date = '%s' limit 1
       '''%(tb_name, day)
       print sql
       result = mclient.query(sql)
      print '%s 数据删除完成'%(day)
      mclient.close()
    
    # 返回mysql 连接
    def getConn():
     return mysql.MysqlClient(host = '0.0.0.0', user = 'test', passwd = 'test', db= 'statistic')
    
    if __name__ == '__main__':
     regx = '%Y-%m-%d'
     yesday = timedef.getYes(regx, -1)
     starttime = '2019-08-17'
     endtime ='2019-08-30'
     run(starttime, endtime, regx)
```

以上就是Python批量删除mysql中千万级大量数据的脚本的详细内容，更多关于python 删除MySQL数据的资料请关注脚本之家其它相关文章！

