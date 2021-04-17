本文实例讲述了python实现根据主机名字获得所有ip地址的方法。分享给大家供大家参考。具体实现方法如下：

```python

    # -*- coding: utf-8 -*-
    import sys, socket
    result = socket.getaddrinfo('www.google.com', None, 0, socket.SOCK_STREAM)
    counter = 0
    for item in result:
      print "%-2d: %s" % (counter, item[4])
      counter += 1
    
    
```

运行结果：

```python

    0 : ('74.125.128.106', 0)
    1 : ('74.125.128.147', 0)
    2 : ('74.125.128.99', 0)
    3 : ('74.125.128.103', 0)
    4 : ('74.125.128.104', 0)
    5 : ('74.125.128.105', 0)
    
    
```

希望本文所述对大家的Python程序设计有所帮助。

