##  **起源**  

当同一个远程服务器有多个人使用的时候，想知道服务器是否有人在用，我们不能直接的去登录，因为这样可能会把对方挤下来，这并不友好，所以这里提供一个监控远程服务器是否有人连接的方式

##  **思路**  

遇到这个问题，想着如何去解决

刚开始的时候，我是想通过一个主动的方式，去监控到服务器是否有人连接，就是说当我想要知道服务器是否有人连接，我通过一个运行一个脚本程序，然后返回给我一个结果，事实证明，我并没有通过这样的思路解决这个问题

后来想以一个被动的方式来监控，比如在服务器上装载一个脚本，每5分钟运行一次脚本，来确定服务器上是否有人连接，不过这也比较消耗资源，后来想到一个方式，就是监控服务器连接和断开的行为，在每次服务器连接和断开的时候，运行脚本来知道服务器是否有人连接

放个流程图

![](https://img.jbzj.com/file_images/article/202012/20201218101357328.png?2020111810146)

这里是一整套的监控流程图，包括服务器监控和界面展示

##  实现  

我们有了思路，接下来就是实现的问题

实现起来也比较简单

但是我们需要解决几个问题

  1. 如何知道服务器有没有人连接？ 
  2. 如何监控远程服务器的连接和断开？ 

###  cmd命令netstat监控3389端口  

对于第一个问题，如何知道服务器有没有人连接？

这里可以了解一下 [ 3389端口 ](https://baike.baidu.com/item/3389%E7%AB%AF%E5%8F%A3) （ [
远程桌面 ](https://baike.baidu.com/item/%E8%BF%9C%E7%A8%8B%E6%A1%8C%E9%9D%A2)
的服务端口）和netstat
命令，在windons服务器中，一般是一个远程连接的端口，就是说你可以监控这个端口，来知道服务器有没有人远程连接；而netstat （显示协议统计和当前
TCP/IP 网络连接）是一个cmd命令，我们可以通过它来监控端口情况

比如这里我们要监控3389端口

我们先连接远程连接服务器，打开cmd命令窗口，输入命令：netstat -n -p tcp | find ":3389"

我们就得到一个类似如这样的结果

> TCP 10.11.174.373:55311 16.21.315.55:3389 ESTABLISHED

这里有2个ip，一个10.11.174.373，这个是你本地的ip，一个16.21.315.55，这个就是你服务器的ip

但你在服务器上运行这个命令的时候，如果有远程连接，那么就会得到这样的一个结果（当然，你自己连接的也算），当没有人连接的时候，就会得到一个空的，没有任何连接情况

###  python脚本实现  

这里的脚本，我们要实现3个功能：

  1. 获取本地ip 
  2. 获取服务器连接状态（ip） 
  3. 相关数据存储到数据库 

虽然我们使用netstat命令监控3389端口的时候有本地的ip，但是这只是有远程连接的时候有ip信息，但是如果无人连接，那么就获取不到，当然，你也可以自填本地ip，不过这样并不是很好

获取本地ip，这里我们是用python中的socket函数来实现

```python

    socket.getaddrinfo(socket.gethostname(),None)[-1][-1][0]
```

后面的服务器连接，上面有说

数据库存储，也就不多做说明了，直接上下代码（这里数据库，请自行建好）

```python

    #!/usr/bin/env python
    # -*- encoding: utf-8 -*-
    '''
    @File  :  server_ip.py
    @Time  :  2020/04/23 10:08:15
    @Author :  吉祥鸟
    @GitHub :  https://github.com/jixn-hu
    @CSDN  :  https://me.csdn.net/qq_37462361
    '''
    
    
    import os
    import re
    import pyodbc
    import time
    import socket
    
    def now_time():
      """
      格式化返回当前时间
      :return:
      """
      now = int(time.time())
      local_time = time.localtime(now)
      format_now = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
      return format_now
    
    def open_184_db(db="rreporttask"):
      """
      开启本地数据库
      :param db: 数据库（默认为rreporttask）
      :return: 创建好的数据库连接
      """
      print(now_time(), '连接184数据库%s' % db)
      driver = 'SQL Server'
      # 数据库ip
      serverName = '******'
      # 登陆用户名和密码
      userName = '******'
      passWord = '******'
      # 建立连接并获取cursor
      conn = pyodbc.connect(driver=driver, server=serverName,
                 user=userName, password=passWord, database=db, charset="gbk")
      return conn
    
    
    def insert_many(conn, items, table_name):
      """
      多条数据插入到数据库（注：插入的数据包含表里的关键字）
      :param conn:数据库
      :param items:插入的数据列表字典（列表内包含字典类型）
      :param table_name:数据库表名
      :return:无
      """
      print(now_time(), "更新数据表{}...".format(table_name))
      # print(now_time(),"item:", items)
      if items:
        cursor = conn.cursor()
        sql1 = "insert into %s" % table_name
        sql2 = "("
        sql3 = ") values("
        sql4 = ")"
        for key in items[0].keys(): # 拼接sql语句
          sql2 += "%s," % key
          sql3 += "?,"
          # sql4 += "%s=values(%s)," % (key, key)
        sql = sql1 + sql2[:-1] + sql3[:-1] + sql4
        item_values = []
        for item in items:
          item_values.append(list(item.values()))
        num = len(item_values)
        # print(num)
        print(now_time(), '一共需要处理数据%s条' % num)
        # print(now_time(),"sql:", sql)
    
        try:
          for i in range(0, num, 1000):
            a = min(num, 1000 + i)
            # print(item_values[i:a])
            cursor.executemany(sql, item_values[i:a])
            conn.commit()
            print(now_time(), "当前已经处理%s条数据" % a)
        except Exception as e:
          print(now_time(), '更新数据失败，回滚')
          print(e)
          conn.rollback()
      conn.close()
    
    
    def main():
      items = []
      item = {}
      time.sleep(1)
      cmd = 'netstat -n -p tcp | find ":3389"'
      command = os.popen(cmd)
      r = command.read()
      print(r)
      zz = r.split("\n")[0].split()
      if r=='':
        ip = "0000"
      else:
        local_ip = zz[1]
        local_ip = re.sub(r":.*$",'',local_ip)
        ip = zz[2]
      item["server_ip"]=socket.getaddrinfo(socket.gethostname(),None)[-1][-1][0] # 本地ip
      item["sign_ip"] = ip
      item["entrytime"] = now_time()
      items.append(item)
      print(item)
      conn = open_184_db()
      insert_many(conn,items,"server_sign")
      
    
    if __name__ == "__main__":
      main()
```

你可以把这个python脚本，打包成exe，然后放到服务器上，设置触发条件，当有人连接和断开服务器的时候，运行这个脚本

至于如何设置这个触发器，这就是第二个问题了，如何监控远程服务器的连接和断开？

这里可以百度下，windons自带的任务计划程序，通过这个我们可以设置exe服务器连接和断开的时，运行exe脚本，放个图，之后的自行摸索下

![](https://img.jbzj.com/file_images/article/202012/20201218101645851.png?20201118101656)

其实到这里，基本就是结束了，详细的思路和主要的实现，也都有了，我们可以直接查询数据库就能的知道服务器连接的情况

##  展示  

不过后面为了更方便看，后面我自己又使用flask做了一个界面展示

就不多说明了

先放个成果图

![](https://img.jbzj.com/file_images/article/202012/20201218101731810.png?20201118101739)

直接上代码

server_sign.py:

```python

    #!/usr/bin/env python
    # -*- encoding: utf-8 -*-
    '''
    @File  :  server_sign.py
    @Time  :  2020/04/07 10:47:52
    @Author :  吉祥鸟
    @GitHub :  https://github.com/jixn-hu
    @CSDN  :  https://me.csdn.net/qq_37462361
    '''
    
    import re
    import pyodbc
    import time
    from flask import Flask,render_template
    
    app=Flask(__name__)
    
    def now_time():
      """
      格式化返回当前时间
      :return:
      """
      now = int(time.time())
      local_time = time.localtime(now)
      format_now = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
      return format_now
    
    def open_184_db(db="rreporttask"):
      """
      开启本地数据库
      :param db: 数据库（默认为rreporttask）
      :return: 创建好的数据库连接
      """
      print(now_time(), '连接184数据库%s' % db)
      driver = 'SQL Server'
      serverName = '******'
      # 登陆用户名和密码
      userName = '******'
      passWord = '******'
      # 建立连接并获取cursor
      conn = pyodbc.connect(driver=driver, server=serverName,
                 user=userName, password=passWord, database=db, charset="gbk")
      return conn
    
    
    def select_one(conn, sql="select ios_id from ios_main"):
      """
      查询信息
      :param time:
      :param type:
      :return:
      """
      print(now_time(), "正在查询数据库......")
      cursor = conn.cursor()
      try:
        cursor.execute(sql)
        result = cursor.fetchall()
        conn.commit()
        print(now_time(), "数据查询成功")
        return result
      except:
        print(now_time(), '更新数据失败，回滚')
        conn.rollback()
      conn.close()
    
    
    
    @app.route('/admin/<name>') # route() 装饰器告诉 Flask 什么样的URL 能触发我们的函数
    def hello_world(name):
      conn = open_184_db()
      data_back = {}
      datas = select_one(conn,"select server_ip,sign_ip,entrytime from(select *,ROW_NUMBER()over(partition by server_ip order by entrytime desc)rank from rreporttask..server_sign) as z where rank=1 order by server_ip")
      for data in datas:
        if data[1]=='0000' or '3389' in data[1]:
          data_back[data[0]]="未连接"
          data[1]="无"
        else:
          data_back[data[0]]="连接ing"
      # print(datas)
      return render_template("login.html",name=name,datas=datas,data_back=data_back)
    
    
    @app.route('/hal/<name>') # route() 装饰器告诉 Flask 什么样的URL 能触发我们的函数
    def hello_world1(name):
      return "hellodd {}".format(name)
    
    if __name__ == "__main__":
      app.run(debug = True,host='0.0.0.0') # 用 run() 函数来让应用运行在本地服务器上
```

login.html:

```python

    <html>
      <!-- CSS goes in the document HEAD or added to your external stylesheet -->
    <style type="text/css">
      table.hovertable {
      font-family: verdana,arial,sans-serif;
      font-size:11px;
      color:#333333;
      border-width: 1px;
      border-color: #999999;
      border-collapse: collapse;
      }
      table.hovertable th {
      background-color:#c3dde0;
      border-width: 1px;
      padding: 8px;
      border-style: solid;
      border-color: #a9c6c9;
      }
      table.hovertable tr {
      background-color:#d4e3e5;
      }
      table.hovertable td {
      border-width: 1px;
      padding: 8px;
      border-style: solid;
      border-color: #a9c6c9;
      }
      </style>
      <body>
       <h1>服务器登录状态查看</h1>
       <table class="hovertable">
         <tr>
          <th>服务器ip</th>
          <th>登录ip</th>
          <th>连接时间</th>
          <th>连接状态</th>
         </tr>
         {% for data in datas %}
          <tr>
            <td>{{ data[0] }}</td>
            <td>{{ data[1] }}</td>
            <td>{{ data[2] }}</td>
            <td>{{ data_back[data[0]] }}</td>
          </tr>
         {% endfor %}
       </table>
    
      </body>
      
    </html>
```

##  思维导图  

最后，放一个思维导图，供参考

![](https://img.jbzj.com/file_images/article/202012/20201218101835523.png?20201118101843)

以上就是python 监控服务器是否有人远程登录（详细思路+代码）的详细内容，更多关于python 监控服务器的资料请关注脚本之家其它相关文章！

