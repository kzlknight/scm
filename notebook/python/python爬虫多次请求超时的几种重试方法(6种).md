**第一种方法**  

```python

    headers = Dict()
    url = 'https://www.baidu.com'
    try:
     proxies = None
     response = requests.get(url, headers=headers, verify=False, proxies=None, timeout=3)
    except:
     # logdebug('requests failed one time')
     try:
      proxies = None
      response = requests.get(url, headers=headers, verify=False, proxies=None, timeout=3)
     except:
      # logdebug('requests failed two time')
      print('requests failed two time')
    
```

总结 ：代码比较冗余，重试try的次数越多，代码行数越多，但是打印日志比较方便

**第二种方法**  

```python

    def requestDemo(url，):
     headers = Dict()
     trytimes = 3 # 重试的次数
     for i in range(trytimes):
     try:
      proxies = None
      response = requests.get(url, headers=headers, verify=False, proxies=None, timeout=3)
      # 注意此处也可能是302等状态码
      if response.status_code == 200:
      break
     except:
      # logdebug(f'requests failed {i}time')
       print(f'requests failed {i} time')
    
```

总结 ：遍历代码明显比第一个简化了很多，打印日志也方便

**第三种方法**  

```python

    def requestDemo(url， times=1):
     headers = Dict()
     try:
      proxies = None
      response = requests.get(url, headers=headers, verify=False, proxies=None, timeout=3)
      html = response.text()
      # todo 此处处理代码正常逻辑
      pass
      return html
     except:
      # logdebug(f'requests failed {i}time')
      trytimes = 3 # 重试的次数
      if times < trytimes:
      times += 1
       return requestDemo(url， times)
      return 'out of maxtimes'
    
```

总结 ：迭代 显得比较高大上，中间处理代码时有其它错误照样可以进行重试； 缺点 不太好理解，容易出错，另外try包含的内容过多时，对代码运行速度不利。

**第四种方法  
**

```python

    @retry(3) # 重试的次数 3
    def requestDemo(url):
     headers = Dict()
     proxies = None
     response = requests.get(url, headers=headers, verify=False, proxies=None, timeout=3)
     html = response.text()
     # todo 此处处理代码正常逻辑
     pass
     return html
     
    def retry(times):
     def wrapper(func):
      def inner_wrapper(*args, **kwargs):
       i = 0
       while i < times:
        try:
         print(i)
         return func(*args, **kwargs)
        except:
         # 此处打印日志 func.__name__ 为say函数
         print("logdebug: {}()".format(func.__name__))
         i += 1
      return inner_wrapper
     return wrapper
    
```

总结 ：装饰器优点 多种函数复用，使用十分方便

**第五种方法**  

```python

    #!/usr/bin/python
    # -*-coding='utf-8' -*-
    import requests
    import time
    import json
    from lxml import etree
    import warnings
    warnings.filterwarnings("ignore")
    
    def get_xiaomi():
     try:
      # for n in range(5): # 重试5次
      #  print("第"+str(n)+"次")
      for a in range(5): # 重试5次
       print(a)
       url = "https://www.mi.com/"
       headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        # "Cookie": "xmuuid=XMGUEST-D80D9CE0-910B-11EA-8EE0-3131E8FF9940; Hm_lvt_c3e3e8b3ea48955284516b186acf0f4e=1588929065; XM_agreement=0; pageid=81190ccc4d52f577; lastsource=www.baidu.com; mstuid=1588929065187_5718; log_code=81190ccc4d52f577-e0f893c4337cbe4d|https%3A%2F%2Fwww.mi.com%2F; Hm_lpvt_c3e3e8b3ea48955284516b186acf0f4e=1588929099; mstz=||1156285732.7|||; xm_vistor=1588929065187_5718_1588929065187-1588929100964",
        "Host": "www.mi.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36"
       }
       response = requests.get(url,headers=headers,timeout=10,verify=False)
       html = etree.HTML(response.text)
       # print(html)
       result = etree.tostring(html)
       # print(result)
       print(result.decode("utf-8"))
       title = html.xpath('//head/title/text()')[0]
       print("title==",title)
       if "左左" in title:
       # print(response.status_code)
       # if response.status_code ==200:
        break
      return title
    
     except:
      result = "异常"
      return result
    
    if __name__ == '__main__':
     print(get_xiaomi())
```

**第六种方法**  

Python重试模块retrying

```python

    # 设置最大重试次数
    @retry(stop_max_attempt_number=5)
    def get_proxies(self):
     r = requests.get('代理地址')
     print('正在获取')
     raise Exception("异常")
     print('获取到最新代理 = %s' % r.text)
     params = dict()
     if r and r.status_code == 200:
      proxy = str(r.content, encoding='utf-8')
      params['http'] = 'http://' + proxy
      params['https'] = 'https://' + proxy
    
    
```

```python

    # 设置方法的最大延迟时间，默认为100毫秒(是执行这个方法重试的总时间)
    @retry(stop_max_attempt_number=5,stop_max_delay=50)
    # 通过设置为50，我们会发现，任务并没有执行5次才结束！
    
    # 添加每次方法执行之间的等待时间
    @retry(stop_max_attempt_number=5,wait_fixed=2000)
    # 随机的等待时间
    @retry(stop_max_attempt_number=5,wait_random_min=100,wait_random_max=2000)
    # 每调用一次增加固定时长
    @retry(stop_max_attempt_number=5,wait_incrementing_increment=1000)
    
    # 根据异常重试，先看个简单的例子
    def retry_if_io_error(exception):
     return isinstance(exception, IOError)
    
    @retry(retry_on_exception=retry_if_io_error)
    def read_a_file():
     with open("file", "r") as f:
      return f.read()
    
```

read_a_file函数如果抛出了异常，会去retry_on_exception指向的函数去判断返回的是True还是False，如果是True则运行指定的重试次数后，抛出异常，False的话直接抛出异常。  

当时自己测试的时候网上一大堆抄来抄去的，意思是retry_on_exception指定一个函数，函数返回指定异常，会重试，不是异常会退出。真坑人啊！  

来看看获取代理的应用(仅仅是为了测试retrying模块)  

到此这篇关于python爬虫多次请求超时的几种重试方法的文章就介绍到这了,更多相关python爬虫多次请求超时内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

