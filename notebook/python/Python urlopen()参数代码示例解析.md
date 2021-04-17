**1.data参数**  

data是可选的，需要使用bytes()方法将参数转化为字节编码格式的内容。如果传递了这个参数，请求方式就不是GET方式，而是POST方式。

```python

    import urllib.parse
    import urllib.request
    
    data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf8')#使用bytes()方法将参数word(值是hello)，转换为字节流（bytes），#该方法的第一个参数需要str类型，需要用urllib.parse模块里的urlencode()方法将参数字典转化为字符串。response = urllib.request.urlopen('http://httpbin.org/post',data = data)
    print(response.read())
```

**2.timeout参数  
**

用于设置超时时间，单位为秒，如果超出了设置的这个时间，还没有得到响应，就会抛出异常。可以通过设置这个超时时间来控制一个页面长时间未响应时，就跳过它的抓取。

```python

    import socket
    import urllib.request
    import urllib.error
    
    try:
      response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)#设置超时时间为0.1s
    except urllib.error.URLError as e:
      if isinstance(e.reason,socket.timeout):
        print('TIME OUT')#如果超时，输出TIME OUT
```

**3.其他参数  
**

context参数，类型必须是ssl.SSLContext类型。

cafile和capath这两个参数分别指定CA证书和它的路径，在请求HTTPS链接时候有用。

cadefault参数已经弃用了，其默认值为False。

以上就是本文的全部内容，希望对大家的学习有所帮助，也希望大家多多支持脚本之家。

