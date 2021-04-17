我就废话不多说了，大家还是直接看代码吧~

```python

    import pymysql
    from sshtunnel import SSHTunnelForwarder
    import pymysql.cursors #以dict形式输出
    
    def dbconnect_ssh(ssh_host,ssh_port,keyfile,ssh_user,db_host,db_name,sql,db_port,db_user,db_passwd):
     with SSHTunnelForwarder(
       (ssh_host, ssh_port),
       #ssh_password="sshpasswd",
       ssh_pkey=keyfile,
       ssh_username=ssh_user,
       remote_bind_address=(db_host, db_port)
     ) as server:
    
      db = pymysql.connect(
       host='127.0.0.1',
       port=server.local_bind_port,
       user=db_user,
       passwd=db_passwd,
       db=db_name,
       charset="utf8",
       cursorclass=pymysql.cursors.DictCursor)
    
      cursor = db.cursor()
    
      try:
       cursor.execute(sql)
       data = cursor.fetchall()
       db.commit()
      except:
       db.rollback()
    
      collect = []
      for result in data:
       collect.append(result)
    
      db.close()
      cursor.close()
    
      return collect
    
    if __name__ == "__main__":
     ssh_host = "10.10.2.13"   #SSH服务器地址
     ssh_port = 22     #SSH端口
     keyfile = xxxx.key" #SSH密钥
     ssh_user = "root"   #SSH用户名
     db_host = "127.0.0.1"  #数据库地址
     db_name = 'DBname'    #数据库名
     sql = 'show tables;'  #SQL
     db_port = 3306     #数据库端口
     db_user = 'root'    #数据库用户名
     db_passwd = '33333'   #数据库密码
     result = dbconnect_ssh(ssh_host,ssh_port,keyfile,ssh_user,db_host,db_name,sql,db_port,db_user,db_passwd)
     print (result)
    
```

**补充知识：** **Python 使用SSHTunnel 连接内网mysql数据库**

**准备：**

主要模块 sshtunnel， pip install sshtunnel

其余模块 pymysql，playhouse，configparser

**简介：**

这里用的是数据库连接池和自动的链接断开重连机制，其实最主要的就是sshtunner的建立，所以可以只看service建立的 部分

**配置文件：**

```python

    [mysql]
    database=ad_insight
    max_connections=10
    stale_timeout=1000
    host=localhost
    user=数据库用户名
    password=数据库密码
    port=3306
```

python 代码

```python

    from playhouse.pool import PooledMySQLDatabase
    from playhouse.shortcuts import ReconnectMixin
    from configparser import ConfigParser
    from sshtunnel import SSHTunnelForwarder
     
    class RetryMySQLDatabase(ReconnectMixin,PooledMySQLDatabase):
     _instance = None
     
     @staticmethod
     def get_db_instance():
      if not RetryMySQLDatabase._instance:
       server = SSHTunnelForwarder(
        ssh_address_or_host='ssh域名或者地址',
        ssh_port=ssh端口,
        ssh_password='ssh密码',
        ssh_username='ssh名称',
        remote_bind_address=('数据库地址',数据库端口)
     
       )
       server.start()
       config = ConfigParser()
       config.read("./default.cfg",encoding="utf-8")
       RetryMySQLDatabase._instance = RetryMySQLDatabase(
        str(config['mysql']['database']),
        max_connections=int(config['mysql']['max_connections']),
        stale_timeout=int(config['mysql']['stale_timeout']),
        host=str(config['mysql']['host']),
        user=str(config['mysql']['user']),
        password=str(config['mysql']['password']),
        port=server.local_bind_port
        # port=int(config['mysql']['port'])
       )
      return RetryMySQLDatabase._instance
```

其实主要是在server对象的建立和server.start

希望能给大家一个参考，本人亲测有效。也希望大家多多支持脚本之家。

