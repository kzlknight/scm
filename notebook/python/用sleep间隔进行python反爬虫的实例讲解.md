在找寻材料的时候，会看到一些暂时用不到但是内容不错的网页，就这样关闭未免浪费掉了，下次也不一定能再次搜索到。有些小伙伴会提出可以保存网页链接，但这种基本的做法并不能在网页打不开后还能看到内容。我们完全可以用爬虫获取这方面的数据，不过操作过程中会遇到一些阻拦，今天小编就教大家用sleep间隔进行python反爬虫，这样就可以得到我们想到的数据啦。

###  步骤

要利用headers拉动请求，模拟成浏览器去访问网站，跳过最简单的反爬虫机制。

获取网页内容，保存在一个字符串content中。

构造正则表达式，从content中匹配关键词pattern获取下载链接。需要注意的是，网页中的关键词出现了两遍（如下图），所以我们要利用set()函数清除重复元素。

第三步是遍历set之后的结果，下载链接。

设置time.sleep(t)，无sleep间隔的话，网站认定这种行为是攻击，所以我们隔一段时间下载一个，反反爬虫。

具体代码

```python

    import urllib.request# url request
    import re      # regular expression
    import os      # dirs
    import time
    '''
    url 下载网址
    pattern 正则化的匹配关键词
    Directory 下载目录
    def BatchDownload(url,pattern,Directory):
       
      # 拉动请求，模拟成浏览器去访问网站->跳过反爬虫机制
      headers = {'User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
      opener = urllib.request.build_opener()
      opener.addheaders = [headers]
      # 获取网页内容
      content = opener.open(url).read().decode('utf8')
      # 构造正则表达式，从content中匹配关键词pattern
      raw_hrefs = re.findall(pattern, content, 0)
      # set函数消除重复元素
      hset = set(raw_hrefs)
         
      # 下载链接
      for href in hset:
        # 之所以if else 是为了区别只有一个链接的特别情况
        if(len(hset)>1):
          link = url + href[0]
          filename = os.path.join(Directory, href[0])
          print("正在下载",filename)
          urllib.request.urlretrieve(link, filename)
          print("成功下载！")
        else:
          link = url +href
          filename = os.path.join(Directory, href)
           
        # 无sleep间隔，网站认定这种行为是攻击，反反爬虫
        time.sleep(1)
     
    #BatchDownload('https://www1.ncdc.noaa.gov/pub/data/swdi/stormevents/csvfiles/',
    #       '(Storm-Data-Export-Format.docx)',
    #       'E:\stormevents\csvfiles')
         
    #       '(Storm-Data-Export-Format.pdf)',
    #       '(StormEvents_details-ftp_v1.0_d(\d*)_c(\d*).csv.gz)',
    #       '(StormEvents_fatalities-ftp_v1.0_d(\d*)_c(\d*).csv.gz)',
    #       '(StormEvents_locations-ftp_v1.0_d(\d*)_c(\d*).csv.gz)',
    #BatchDownload('https://www1.ncdc.noaa.gov/pub/data/swdi/stormevents/csvfiles/legacy/',
    #       '(ugc_areas.csv)',
    #       'E:\stormevents\csvfiles\legacy')
```

###  结果展示

为了让大家能够清楚的知道整个反爬过程，这里小编把思路和代码都罗列了出来。其中可以time.sleep(t)解除网站对于爬虫的阻拦问题，着重标记了出来

![](https://img.jbzj.com/file_images/article/202011/20201130163431.png)

到此这篇关于用sleep间隔进行python反爬虫的实例讲解的文章就介绍到这了,更多相关如何使用sleep间隔进行python反爬虫内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

