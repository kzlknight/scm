先看下效果图：

![](https://img.jbzj.com/file_images/article/202012/20201228105557530.png?2020112810566)

用到的模块：

  * PyMySQL 
  * requests 
  * threading 
  * wxpy 

要实现上面的示例，首先是有两大块地方

  * 获取天气信息 
  * 通过微信将天气信息发送出去   

而获取天气信息又包括几个小的需要注意的地方

获取天气信息

  * 获取天气信息的接口 
  * 获取天气信息的城市 
  * 获取所在城市的城市码 

假如我们给多个人发送天气情况，这几个人来自不同的城市，那么我们不可能每次都要输入城市名，然后查找城市码，然后再访问接口，获取天气情况，这样会非常的麻烦，所以我们需要考虑将城市名跟城市码一一对应起来，说到一一对应，首先想到的数据结构便是字典，所以我们可以将这些信息存入一个字典里，然后持久化到一个文件中，这样便方便很多

首先我们获取最新的 city 表，这个表是一个 list 类型，大体格式如下：

```python

    [
     {
      "id": 1,
      "pid": 0,
      "city_code": "101010100",
      "city_name": "北京",
      "post_code": "100000",
      "area_code": "010",
      "ctime": "2019-07-11 17:30:06"
     },
     {
      "id": 2,
      "pid": 0,
      "city_code": "",
      "city_name": "安徽",
      "post_code": null,
      "area_code": null,
      "ctime": null
     }
    ]
```

我们就简单的粘贴复制，放到一个空的列表中，如下所示，将所有的城市信息放到列表 citycode 中

```python

    citycode = [
     {
      "id": 1,
      "pid": 0,
      "city_code": "101010100",
      "city_name": "北京",
      "post_code": "100000",
      "area_code": "010",
      "ctime": "2019-07-11 17:30:06"
     },
    ...
    ...
    ...
    ...
    ...
    ...
     {
      "id": 2,
      "pid": 0,
      "city_code": "None",
      "city_name": "安徽",
      "post_code": "null",
      "area_code": "null",
      "ctime": "null"
     }
    ]
    
    cityinfo = {}
    #将城市名和城市代码写入json文件中
    with open('city_for_code.json','w',encoding='utf-8') as f:
      for i in citycode:
        name = i["city_name"]
        code = i["city_code"]
        cityinfo[name] = code
      f.write(str(cityinfo))
    
    #测试是否能读取
    with open('city_for_code.json','r+',encoding='utf-8') as file:
      data_dst = file.readlines()
      d = eval(data_dst[0])
```

然后就是一顿处理，只把我们所需的 city_name 和 city_code
这俩字段取出即可，随后写入文件中。如果读取的话就按照上面方法去读取，需要注意的是，使用 open()方法读取文件，得到的内容是一个列表，我们需要通过
eval()方法转化成 dict 类型。

这是把 city_name 和 city_code 放到一个文件中的方法，另外我们也可以放到数据库中，这里以 MySQL 为例，安装 PyMySQL 模块

```python

    import pymysql
    
    db_parames = {
      'host': 'localhost',
      'user': 'root',
      'password': '123456',
      'database': 'city_code_info'
    }
    #连接数据库
    conn = pymysql.connect(**db_parames)
    
    #创建游标对象，增删改查都在游标上进行
    cursor = conn.cursor()
    
    #表存在，就删除
    cursor.execute("DROP TABLE IF EXISTS city_code")
    
    #建表语句
    create_table_sql = """CREATE TABLE `city_code` (
     `city_name` varchar(20) DEFAULT NULL,
     `city_code` varchar(25) DEFAULT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    """
    #建表
    cursor.execute(create_table_sql)
    
    #插入数据
    with open('city_for_code.json','r+',encoding='utf-8') as f:
      origin_data = f.readlines()
      current_data = eval(origin_data[0])  #读取的内容是一个列表，且只包含一个元素
      #print(current_data.get('北京','Not Exists.'))
      for name, code in current_data.items():
        sql = """INSERT INTO city_code(city_name, city_code) VALUES ('%s', '%s')""" % (name, code)
        try:
          cursor.execute(sql)
        except:
          conn.rollback()
      conn.commit()
      conn.close()
```

执行这个 python
程序就可以将文件中的城市名跟城市码存到库中，当然我们也可以直接获取到城市名和城市码，然后跳过文件持久化这一步，直接把这两个字段取出存进去，但是考虑着代码要多练多写，就多此一举了一下。

下面是输入城市名就能得到城市码的代码块：

```python

    import pymysql
    
    def get_city_code(city_name):
      db_parames = {
      'host': 'localhost',
      'user': 'root',
      'password': '123456',
      'database': 'city_code_info'
      }
      #连接数据库
      conn = pymysql.connect(**db_parames)
    
      #创建游标对象，增删改查都在游标上进行
      cursor = conn.cursor()
    
      #创建查询语句
      select_sql = "SELECT * FROM city_code where city_name='%s'"%(city_name)
      try:
        cursor.execute(select_sql)
        result = cursor.fetchall()
        for row in result:
          city_code = row[1]
        return city_code
      except:
        return "Error: unable fetch data!"
```

然后是根据输入的城市码来获取天气情况：

```python

    import requests
    
    def get_weather(city_name,get_date_time=3):
      city_code = get_city_code(city_name)
      url = 'http://t.weather.sojson.com/api/weather/city/%s'%(city_code)
      header = {
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
      }
      response = requests.get(url,header)
      response.encoding = 'utf-8'
      weather = response.json()
      day = {1: '明天', 2: '后天', 3: '大后天'}
      weather_lst = []
      for num in range(get_date_time):
        City = weather["cityInfo"]["city"]
        Weatherganmao = weather["data"]["ganmao"]
        Weatherquality = weather["data"]["quality"]
        Weathershidu = weather["data"]["shidu"]
        Weatherwendu = weather["data"]["wendu"]
        Weatherpm25 = str(weather["data"]["pm25"])
        Weatherpm10 = str(weather["data"]["pm10"])
        Dateymd = weather["data"]["forecast"][num]["ymd"]
        Dateweek = weather["data"]["forecast"][num]["week"]
        Sunrise = weather["data"]["forecast"][num]["sunrise"]
        Sunset = weather["data"]["forecast"][num]["sunset"]
        Windfx = weather["data"]["forecast"][num]["fx"]
        Windf1 = weather["data"]["forecast"][num]["fl"]
        Weathertype = weather["data"]["forecast"][num]["type"]
        Weathernotice = weather["data"]["forecast"][num]["notice"]
        Weatherhigh = weather["data"]["forecast"][num]["high"]
        Weatherlow = weather["data"]["forecast"][num]["low"]
        if num == 0:
          result = '今日天气预报' + '\n' \
            + '日期： ' + Dateymd + ' ' + Dateweek + ' ' + City + '\n' \
            + '天气： ' + Weathertype + ' ' + Windfx + ' ' + Windf1 + ' ' + Weathernotice + '\n' \
            + '当前温度： ' + Weatherwendu + '℃' + '\n' \
            + '空气湿度： ' + Weathershidu + '\n' \
            + '温度范围： ' + Weatherlow + '' + '~' + '' + Weatherhigh + '\n' \
            + '污染指数： ' + 'PM2.5: ' + Weatherpm25 + ' ' + 'PM10: ' + Weatherpm10 + '\n' \
            + '空气质量： ' + Weatherquality + '\n' \
            + '日出时间： ' + Sunrise + '\n' \
            + '日落时间： ' + Sunset + '\n' \
            + '温馨提示： ' + Weatherganmao
        else:
          which_day = day.get(num,'超出范围')
          result = '\n' + which_day + ' ' + '天气预报' + '\n' \
            + '日期： ' + Dateymd + ' ' + Dateweek + ' ' + City + '\n' \
            + '天气： ' + Weathertype + ' ' + Windfx + ' ' + Windf1 + ' ' + Weathernotice + '\n' \
            + '温度范围： ' + Weatherlow + '' + '~' + '' + Weatherhigh + '\n' \
            + '日出时间： ' + Sunrise + '\n' \
            + '日落时间： ' + Sunset + '\n' \
            + '温馨提示： ' + Weatherganmao
        weather_lst.append(result)
        weather_str = ''   #因为默认要输出三天的天气情况，所以我们需要创建一个空字符串，然后每迭代一次，就将天气情况拼接到空字符串中。
        for msg in weather_lst:
          weather_str += msg + '\n'
    
      return weather_str
```

下面是发送微信消息

```python

    from wxpy import *
    
    def send_wx(city_name, who):
      bot = Bot(cache_path=True)
      #bot = Bot(console_qr=2, cache_path='botoo.pkl')
      my_friend = bot.friends().search(who)[0]
      msg = get_weather(city_name)
      try:
        my_friend.send(msg)
      except:
        my_friend = bot.friends().search('fei')[0]
        my_friend.send(u"发送失败")
```

然后我们还需要写一个定时器，每隔一段时间便要发送一次

```python

    from threading import Timer
    
    def auto_send():
      city_name = '设置要发送的城市'
      friend_list = ['要发送的人']
    
      for who in friend_list:
        send_wx(city_name,who)
      global timer
      timer = Timer(1,auto_send)
      timer.start()
```

最后执行程序

```python

    if __name__ == '__main__':
      timer = Timer(1,auto_send)
      timer.start()
```

以上就是python获取天气接口给指定微信好友发天气预报的详细内容，更多关于python获取天气接口的资料请关注脚本之家其它相关文章！

