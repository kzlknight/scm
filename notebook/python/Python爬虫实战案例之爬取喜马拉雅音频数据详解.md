**前言**

喜马拉雅是专业的音频分享平台，汇集了有声小说,有声读物,有声书,FM电台,儿童睡前故事,相声小品,鬼故事等数亿条音频，我最喜欢听民间故事和德云社相声集，你呢？

今天带大家爬取喜马拉雅音频数据，一起期待吧！！

这个案例的视频地址在这里

[ https://v.douyu.com/show/a2JEMJj3e3mMNxml
](https://v.douyu.com/show/a2JEMJj3e3mMNxml)

**项目目标**

爬取喜马拉雅音频数据

受害者地址

[ https://www.ximalaya.com/ ](https://www.ximalaya.com/)

![](https://img.jbzj.com/file_images/article/202012/2020120710224749.png)

本文知识点：

1、系统分析网页性质

2、多层数据解析

3、海量音频数据保存

环境：

1.确定数据所在的链接地址(url)  
2.通过代码发送url地址的请求  
3.解析数据(要的, 筛选不要的)  
4.数据持久化(保存)

**案例思路：**

1. 在静态数据中获取音频的id值 

2. 发送指定id值json数据请求(src) 

3. 从json数据中解析音频所对应的URL地址 开始写代码 

**先导入所需的模块**

```python

    import requests
    import parsel # 数据解析模块
    import re
```

1.确定数据所在的链接地址(url) 逆向分析 网页性质(静态网页/动态网页)

打开开发者工具，播放一个音频，在Madie里面可以找到一个数据包

![](https://img.jbzj.com/file_images/article/202012/2020120710224850.png)

复制URL，搜索

![](https://img.jbzj.com/file_images/article/202012/2020120710224851.png)

找到ID值

![](https://img.jbzj.com/file_images/article/202012/2020120710224852.png)

继续搜索，找到请求头参数

![](https://img.jbzj.com/file_images/article/202012/2020120710224853.png)

```python

    url = 'https://www.ximalaya.com/youshengshu/4256765/p{}/'.format(page)
    headers = {
     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
```

2.通过代码发送url地址的请求

```python

    response = requests.get(url=url, headers=headers)
    html_data = response.text
```

3.解析数据(要的, 筛选不要的) 解析音频的 id值

```python

    selector = parsel.Selector(html_data)
    lis = selector.xpath('//div[@class="sound-list _is"]/ul/li')
    
    for li in lis:
     try:
      title = li.xpath('.//a/@title').get() + '.m4a'
      href = li.xpath('.//a/@href').get()
      # print(title, href)
    
      m4a_id = href.split('/')[-1]
      # print(href, m4a_id)
    
      # 发送指定id值json数据请求(src)
      json_url = 'https://www.ximalaya.com/revision/play/v1/audio?id={}&ptype=1'.format(m4a_id)
      json_data = requests.get(url=json_url, headers=headers).json()
      # print(json_data)
    
      # 提取音频地址
      m4a_url = json_data['data']['src']
      # print(m4a_url)
    
      # 请求音频数据
      m4a_data = requests.get(url=m4a_url, headers=headers).content
    
      new_title = change_title(title)
```

4.数据持久化(保存)

```python

    with open('video\\' + new_title, mode='wb') as f:
     f.write(m4a_data)
     print('保存完成:', title)
```

最后还要处理文件名非法字符

```python

    def change_title(title):
     pattern = re.compile(r"[\/\\\:\*\?\"\<\>\|]") # '/ \ : * ? " < > |'
     new_title = re.sub(pattern, "_", title) # 替换为下划线
     return new_title
```

完整代码

```python

    import re
    
    import requests
    import parsel # 数据解析模块
    
    
    def change_title(title):
     """处理文件名非法字符的方法"""
     pattern = re.compile(r"[\/\\\:\*\?\"\<\>\|]") # '/ \ : * ? " < > |'
     new_title = re.sub(pattern, "_", title) # 替换为下划线
     return new_title
    
    
    for page in range(13, 33):
     print('---------------正在爬取第{}页的数据----------------'.format(page))
     # 1.确定数据所在的链接地址(url) 逆向分析 网页性质(静态网页/动态网页)
     url = 'https://www.ximalaya.com/youshengshu/4256765/p{}/'.format(page)
     headers = {
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
    
     # 2.通过代码发送url地址的请求
     response = requests.get(url=url, headers=headers)
     html_data = response.text
     # print(html_data)
    
     # 3.解析数据(要的, 筛选不要的) 解析音频的 id值
     selector = parsel.Selector(html_data)
     lis = selector.xpath('//div[@class="sound-list _is"]/ul/li')
    
     for li in lis:
      try:
       title = li.xpath('.//a/@title').get() + '.m4a'
       href = li.xpath('.//a/@href').get()
       # print(title, href)
    
       m4a_id = href.split('/')[-1]
       # print(href, m4a_id)
    
       # 发送指定id值json数据请求(src)
       json_url = 'https://www.ximalaya.com/revision/play/v1/audio?id={}&ptype=1'.format(m4a_id)
       json_data = requests.get(url=json_url, headers=headers).json()
       # print(json_data)
    
       # 提取音频地址
       m4a_url = json_data['data']['src']
       # print(m4a_url)
    
       # 请求音频数据
       m4a_data = requests.get(url=m4a_url, headers=headers).content
    
       new_title = change_title(title)
       # print(new_title)
    
       # 4.数据持久化(保存)
       with open('video\\' + new_title, mode='wb') as f:
        f.write(m4a_data)
        print('保存完成:', title)
      except:
       pass
```

运行代码，效果如下图

![](https://img.jbzj.com/file_images/article/202012/2020120710224954.png)

到此这篇关于Python爬虫实战案例之取喜马拉雅音频数据详解的文章就介绍到这了,更多相关Python爬取喜马拉雅音频数据内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

