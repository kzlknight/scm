**HTTP格式**  
HTTP GET请求的格式：

```python

    GET /path HTTP/1.1
    Header1: Value1
    Header2: Value2
    Header3: Value3
```

每个Header一行一个，换行符是 ` \r\n ` 。

HTTP POST请求的格式：

```python

    POST /path HTTP/1.1
    Header1: Value1
    Header2: Value2
    Header3: Value3
    
    body data goes here...
```

当遇到连续两个\r\n时，Header部分结束，后面的数据全部是Body。

HTTP响应的格式：

```python

    200 OK
    Header1: Value1
    Header2: Value2
    Header3: Value3
    
    body data goes here...
```

HTTP响应如果包含body，也是通过 ` \r\n\r\n ` 来分隔的。需注意，Body的数据类型由 ` Content-Type `
头来确定，如果是网页，Body就是文本，如果是图片，Body就是图片的二进制数据。

当存在 ` Content-Encoding ` 时，Body数据是被压缩的，最常见的压缩方式是gzip。

**WSGI接口**  
WSGI：Web Server Gateway Interface。

WSGI接口定义非常简单，只需要实现一个函数，就可以响应HTTP请求。

```python

    # hello.py
    
    def application(environ, start_response):
      start_response('200 OK', [('Content-Type', 'text/html')])
      body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
      return [body.encode('utf-8')]
```

函数接收两个参数：

  * environ：一个包含所有HTTP请求信息的 ` dict ` 对象； 
  * start_response：一个发送HTTP响应的函数。 

**运行WSGI服务**  
Python内置了一个WSGI服务器，这个模块叫wsgiref，它是用纯Python编写的WSGI服务器的参考实现。

```python

    # server.py
    
    from wsgiref.simple_server import make_server
    from hello import application
    
    # 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
    httpd = make_server('', 8000, application)
    print('Serving HTTP on port 8000...')
    # 开始监听HTTP请求:
    httpd.serve_forever()
```

在命令行输入 ` python server.py ` 即可启动WSGI服务器。

启动成功后，打开浏览器，输入 ` http://localhost:8000/ ` ，即可看到结果。

按 ` Ctrl+C ` 可以终止服务器。

以上就是浅析Python 中的 WSGI 接口和 WSGI 服务的运行的详细内容，更多关于Python
WSGI接口和WSGI服务的资料请关注脚本之家其它相关文章！

