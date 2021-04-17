本文实例讲述了python中getaddrinfo()基本用法。分享给大家供大家参考。具体如下：

```python

    import sys, socket
    result = socket.getaddrinfo("192.1.1.100", None)
    print result[0][4]
    print result
    
    
```

输出结果：

```python

    ('172.20.53.102', 0)
    [(2, 0, 0, '', ('172.20.53.102', 0))]
    
    
```

希望本文所述对大家的Python程序设计有所帮助。

