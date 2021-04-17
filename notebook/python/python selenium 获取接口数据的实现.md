python selenium 获取接口数据。

selenium没有直接提供查询的函数，但是可以通过webdriver提供的API查询，使用的函数是Network.getResponseBody

webdriver提供的API文档： [ https://chromedevtools.github.io/devtools-
protocol/tot/Network/ ](https://chromedevtools.github.io/devtools-
protocol/tot/Network/)

Network.getResponseBody文档说明：

![](https://img.jbzj.com/file_images/article/202012/2020120714225745.png)

Network.getResponseBody的参数是requestid，requestid是webdriver每个请求自动生成的惟一ID，拿到requestid就能拿到请求返回的内容。

如何获取requestid？创建webdriver对象时配置信息设置获取performance，即可获取每个请求的日志信息，然后通过对日志信息的检索找到对应的requestid。

获取日志信息的webdriver创建代码（注意，必须传入配置信息才能获取日志信息）：

```python

    from selenium import webdriver
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    import time
     
    caps = {
      'browserName': 'chrome',
      'loggingPrefs': {
        'browser': 'ALL',
        'driver': 'ALL',
        'performance': 'ALL',
      },
      'goog:chromeOptions': {
        'perfLoggingPrefs': {
          'enableNetwork': True,
        },
        'w3c': False, 
      },
    }
    driver = webdriver.Chrome(desired_capabilities=caps)
     
    driver.get('https://partner.oceanengine.com/union/media/login/')
    # 必须等待一定的时间，不然会报错提示获取不到日志信息，因为絮叨等所有请求结束才能获取日志信息
    time.sleep(3)
     
    request_log = driver.get_log('performance')
```

打印request_log是一个数组，然后遍历request_log检索需要获取的url对应的requestid，比如需要获取 [
https://s3.pstatp.com/bytecom/resource/union_web2/media/manifest.json对应的requestid
](https://s3.pstatp.com/bytecom/resource/union_web2/media/manifest.json对应的requestid)
，并且获取接口内容：

```python

    for i in range(len(request_log)):
      message = json.loads(request_log[i]['message'])
      message = message['message']['params']
      # .get() 方式获取是了避免字段不存在时报错
      request = message.get('request')
      if(request is None):
        continue
     
      url = request.get('url')
      if(url == "https://s3.pstatp.com/bytecom/resource/union_web2/media/manifest.json"):
        # 得到requestId
        print(message['requestId'])
        # 通过requestId获取接口内容
        content = driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': message['requestId']})
        print(content)
        break
```

完整代码：

```python

    import json
    from selenium import webdriver
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    import time
     
    caps = {
      'browserName': 'chrome',
      'loggingPrefs': {
        'browser': 'ALL',
        'driver': 'ALL',
        'performance': 'ALL',
      },
      'goog:chromeOptions': {
        'perfLoggingPrefs': {
          'enableNetwork': True,
        },
        'w3c': False, 
      },
    }
    driver = webdriver.Chrome(desired_capabilities=caps)
     
    driver.get('https://partner.oceanengine.com/union/media/login/')
    # 必须等待一定的时间，不然会报错提示获取不到日志信息，因为絮叨等所有请求结束才能获取日志信息
    time.sleep(3)
     
    request_log = driver.get_log('performance')
    print(request_log)
     
    for i in range(len(request_log)):
      message = json.loads(request_log[i]['message'])
      message = message['message']['params']
      # .get() 方式获取是了避免字段不存在时报错
      request = message.get('request')
      if(request is None):
        continue
     
      url = request.get('url')
      if(url == "https://s3.pstatp.com/bytecom/resource/union_web2/media/manifest.json"):
        # 得到requestId
        print(message['requestId'])
        # 通过requestId获取接口内容
        content = driver.execute_cdp_cmd('Network.getResponseBody', {'requestId': message['requestId']})
        print(content)
        break
```

到此这篇关于python selenium 获取接口数据的实现的文章就介绍到这了,更多相关python selenium
获取接口数据内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

