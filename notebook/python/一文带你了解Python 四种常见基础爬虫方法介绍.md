**一、Urllib方法**  

Urllib是python内置的HTTP请求库  

```python

    import urllib.request
    #1.定位抓取的url
    url='http://www.baidu.com/'
    #2.向目标url发送请求
    response=urllib.request.urlopen(url)
    #3.读取数据
    data=response.read()
    # print(data) #打印出来的数据有ASCII码
    print(data.decode('utf-8')) #decode将相应编码格式的数据转换成字符串
```

```python

    #post请求
    import urllib.parse
    url='http://www.iqianyue.com/mypost/'
    #构建上传的data
    postdata=urllib.parse.urlencode({
     'name':'Jack',
     'pass':'123456'
    }).encode('utf-8') #字符串转化成字节流数据
    html=urllib.request.urlopen(url,data=postdata).read()
    print(html)
```

```python

    #headers针对检验头信息的反爬机制
    import urllib.request
    headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    request1=urllib.request.Request('https://www.dianping.com/',headers=headers)#Request类构建了一个完整的请求
    response1=urllib.request.urlopen(request1).read()
    print(response1.decode('utf-8'))
    
    
```

```python

    #超时设置+异常处理
    import urllib.request
    import urllib.error
    for i in range(20):
     try:
      response1=urllib.request.urlopen('http://www.ibeifeng.com/',timeout=0.01)
      print('a')
     except urllib.error.URLError as e:
      print(e)
     except BaseException as a: #所有异常的基类
      print(a)
```

**二、requests方法**  

