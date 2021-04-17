**一、前言**

最近做web网站的测试，遇到很多需要批量造数据的功能；比如某个页面展示数据条数需要达到10000条进行测试，此时手动构造数据肯定是不可能的，此时只能通过python脚本进行自动构造数据；本次构造数据主要涉及到在某个表里面批量添加数据、在关联的几个表中同步批量添加数据、批量查询某个表中符合条件的数据、批量更新某个表中符合条件的数据等。

**二、数据添加**

即批量添加数据到某个表中。

insert_data.py

```python

    import pymysql
    import random
    import time
    from get_userinfo import get_userinfo
    from get_info import get_info
    from get_tags import get_tags
    from get_tuser_id import get_utag
    
    
    class DatabaseAccess():
      def __init__(self):
        self.__db_host = "xxxxx"
        self.__db_port = 3307
        self.__db_user = "root"
        self.__db_password = "123456"
        self.__db_database = "xxxxxx"
      # 连接数据库
      def isConnectionOpen(self):
        self.__db = pymysql.connect(
          host=self.__db_host,
          port=self.__db_port,
          user=self.__db_user,
          password=self.__db_password,
          database=self.__db_database,
          charset='utf8'
        )
      
      # 插入数据
      def linesinsert(self,n,user_id,tags_id,created_at):
     
        self.isConnectionOpen()
        # 创建游标
        global cursor
        conn = self.__db.cursor()
        try:
          sql1 = '''
          INSERT INTO `codeforge_new`.`cf_user_tag`(`id`, `user_id`, 
          `tag_id`, `created_at`, `updated_at`) VALUES ({}, {}, 
          {}, '{}', '{}');
          '''.format(n,user_id,tags_id,created_at,created_at)
          
          # 执行SQL  
          conn.execute(sql1,)
        except Exception as e:
          print(e)
        finally:
          # 关闭游标
          conn.close()
          self.__db.commit()
          
          self.__db.close()
      
      def get_data(self):
        
        # 生成对应数据 1000条
        for i in range(0,1001):
          created_at = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
          # print(create_at)
          # 用户id
          tuserids = []
          tuserid_list = get_utag()
          for tuserid in tuserid_list:
            tuserids.append(tuserid[0])
          # print(tuserids)
          userid_list = get_userinfo()
          user_id = random.choice(userid_list)[0]
          if user_id not in tuserids:
            user_id=user_id
          
            # 标签id
            tagsid_list = get_tags()
            tags_id = random.choice(tagsid_list)[0]
            self.linesinsert(i,user_id,tags_id,created_at)
    
    
    if __name__ == "__main__":
      # 实例化对象
      db=DatabaseAccess()
      db.get_data()
```

**二、数据批量查询**

select_data.py

```python

    import pymysql
    import pandas as pd
    import numpy as np
    
    
    def get_tags():
      # 连接数据库，地址，端口，用户名，密码，数据库名称，数据格式
      conn = pymysql.connect(host='xxx.xxx.xxx.xxx',port=3307,user='root',passwd='123456',db='xxxx',charset='utf8')
      cur = conn.cursor()
      # 表cf_users中获取所有用户id
      sql = 'select id from cf_tags where id between 204 and 298'
      # 将user_id列转成列表输出
      df = pd.read_sql(sql,con=conn)
      # 先使用array()将DataFrame转换一下
      df1 = np.array(df)
      # 再将转换后的数据用tolist()转成列表
      df2 = df1.tolist()
      # cur.execute(sql)
      # data = cur.fetchone()
      # print(df)
      # print(df1)
      # print(df2)
      return df2
      conn.close()
```

**三、批量更新数据**

select_data.py

```python

    import pymysql
    import pandas as pd
    import numpy as np
    
    
    def get_tags():
      # 连接数据库，地址，端口，用户名，密码，数据库名称，数据格式
      conn = pymysql.connect(host='xxx.xxx.xxx.xxx',port=3307,user='root',passwd='123456',db='xxxx',charset='utf8')
      cur = conn.cursor()
      # 表cf_users中获取所有用户id
      sql = 'select id from cf_tags where id between 204 and 298'
      # 将user_id列转成列表输出
      df = pd.read_sql(sql,con=conn)
      # 先使用array()将DataFrame转换一下
      df1 = np.array(df)
      # 再将转换后的数据用tolist()转成列表
      df2 = df1.tolist()
      # cur.execute(sql)
      # data = cur.fetchone()
      # print(df)
      # print(df1)
      # print(df2)
      return df2
      conn.close()
```

以上就是python 实现数据库中数据添加、查询与更新的示例代码的详细内容，更多关于python 数据库添加、查询与更新的资料请关注脚本之家其它相关文章！

