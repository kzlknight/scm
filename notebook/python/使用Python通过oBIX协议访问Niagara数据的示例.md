oBIX 全称是 Open Building Information Exchange，它是基于 RESTful Web Service
的接口的标准，用于构建控制系统。oBIX是在专为楼宇自动化设计的框架内，使用XML和URI在设备网络上读写数据的。

因项目需要使用 Python 对 Niagara 软件中的数据进行读写和控制，所以写了一个该协议的Python版本包，发布在这里： [
https://pypi.org/project/oBIX/ ](https://pypi.org/project/oBIX/)

使用 pip 安装使用即可：

```python

    pip install oBIX
```

本文主要介绍使用 Python 通过 oBIX 协议对 Niagara 软件中的点进行读、写操作。

**一、准备工作**

1. 在 Niagara 软件中配置好 oBIX 协议，确保已经可以正常访问； 

（1）Palette 搜 oBIX, 添加一个 ObixNetwork 到 Drivers中

（2）Palette 搜 baja, 将 AuthenticationSchemes/WebServicesSchemes/的
HTTPBasicScheme 拖拽到 Services/AuthenticationService/Authentication Schemes/

（3）UserServices 右键 View, AX User Manager下新建一个用户，配置如下：

* 用户名：oBIX   
* 密码：oBIX.12345   
* Authentication Schemes Name 选：HTTPBasicScheme   
* Admin 权限   
2. Niagara 中新建一个数值类型的可读写的点，命名为：temp1，完整路径是：/config/AHU/temp1/，后面以此为例进行访问 

3. 安装python的oBIX包： ` pip install oBIX `

**二、快速开始**

```python

    from oBIX.common import Point, DataType
    from oBIX import Client
    
    
    if __name__ == '__main__':
      # ip, userName, password
      # 可选项:
      #  port: 端口号，如：8080
      #  https: 是否使用 https，默认：True
      client = Client("127.0.0.1", "oBIX", "oBIX.12345")
    
      # 点的路径
      point_path = "/config/AHU/temp1/"
    
      # 读取一个点的值
      point_value = client.read_point_value(point_path)
      print("point value is {0}".format(point_value))
```

**三、基本实例**

3.1 读取点

```python

    # 点的路径
      point_path = "/config/AHU/temp1/"
    
      # 读取一个点的值
      point_value = client.read_point_value(point_path)
      print("point value is {0}".format(point_value))
    
      # 读取一个点实例
      # 然后就能获取到这个点所包含的常用属性
      # 例如：name, val, status, display, href, in1, in2 ... in16, fallback, out
      point_obj = client.read_point(point_path)
      print("name is {0}".format(point_obj.name))
      print("fallback is {0}".format(point_obj.fallback))
      print("in10 is {0}".format(point_obj.in10))
      
      # 也可以使用下面代码直接获取
      point_in10_value = client.read_point_slot(point_path, "in10")
      print("in10 is {0}".format(point_in10_value))
```

3.2 写入点

```python

    # 点的路径
      point_path = "/config/AHU/temp1/"
    
      # set 一个点的值
      client.write_point(point_path, 15.2, DataType.real)
      # set point auto
      client.set_point_auto(point_path, DataType.real)
      # override a point
      client.override_point(point_path, 14, DataType.real)
      # emergency override a point
      client.emergency_override_point(point_path, 15, DataType.real)
      # set a point emergency auto
      client.set_point_emergency_auto(point_path, DataType.real)
```

**四、高级应用**

4.1 读取历史数据

```python

    # 起始时间
      start_time = datetime.now(tz=timezone(timedelta(hours=8))) - timedelta(minutes=10)
      # 结束时间
      end_time = datetime.now(tz=timezone(timedelta(hours=8)))
    
      # 读取该断时间内的历史数据
      history = client.read_history("Station01", "OutDoorTemp", start_time, end_time)
    
      # 取起始时间往后指定个数的历史数据
      limit_num = 1
      history = client.read_history("Station01", "OutDoorTemp", start_time=start_time, limit=limit_num)
```

4.2 读取报警数据

```python

    # 起始时间
      start_time = datetime.now(tz=timezone(timedelta(hours=8))) - timedelta(minutes=10)
      # 结束时间
      end_time = datetime.now(tz=timezone(timedelta(hours=8)))
    
      # 读取该段时间内的报警数据
      alarms = client.read_alarms("Station01", "OutDoorTemp", start_time, end_time)
    
      # 取起始时间往后指定个数的报警数据
      limit_num = 1
      alarms = client.read_alarms("Station01", "OutDoorTemp", start_time=start_time, limit=limit_num)
```

4.3 监控点的数据变化  
监控点的数据变化时 oBIX 协议的一部分。添加想要监控的点，然后当 Niagara 中点的值发生变化后，会自动触发相应的函数。

```python

    from oBIX.common import Point, DataType
    from oBIX import Client
    
    
    def init_watch():
      global client, point_path
      # 添加监控
      point_path_list = [point_path] # 这里可以是多个点
      result = client.add_watch_points(point_path_list)
      client.watch_changed_handler.on_change += on_watch_changed
    
    
    # Niagara 里改点的值发生变化时，会自动触发改函数
    def on_watch_changed(points: [Point]):
      for point in points:
        val = point.val
        print(f"on_watch_changed: {val}")
    
    
    if __name__ == '__main__':
      # ip, userName, password
      # 可选项:
      # port: 端口号，如：8080
      # https: 是否使用 https，默认：True
      client = Client("127.0.0.1", "oBIX", "oBIX.12345")
      
      # 点的路径
      point_path = "/config/AHU/temp1/"
    
      init_watch()
      client.start_watch()
      while True:
        i = 0
```

4.4 导出所有点的信息  
如果一个项目中有大量的目录和点，手动挨个去写比较麻烦，所以这里提供了一个导出点信息的函数。将点的信息保存文件后，再直接从文件中读取点的信息就会方便很多。

```python

    # 导出所有点的信息
    export_result = client.export_points()
    
    # folder_path [optional]: 想要导出的目录，如： "/config/xxx/"，默认会导出所有点的信息
    # export_file_name [optional]: 导出文件的名称，默认： "all_points.json"
    # export_type [optional]:
    #   0: JSON格式，嵌套格式并保留目录信息
    #   1: JSON格式, 只保留点的信息，不保留目录信息
    #   2: 字符串列表格式, 只输出点的路径信息
    
    export_result = client.export_points(folder_path="/config/AHU/", export_file_name="output.json", export_type=1)
```

以上就是使用Python通过oBIX协议访问Niagara数据的示例的详细内容，更多关于Python通过oBIX协议访问Niagara数据的资料请关注脚本之家其它相关文章！

