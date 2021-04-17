爬虫简单说来包括两个步骤：获得网页文本、过滤得到数据。  
**1、获得html文本。  
** python在获取html方面十分方便，寥寥数行代码就可以实现我们需要的功能。  

_复制代码_ 代码如下:

  
def getHtml(url):  
page = urllib.urlopen(url)  
html = page.read()  
page.close()  
return html  

  
这么几行代码相信不用注释都能大概知道它的意思。  
  
**2、根据正则表达式等获得需要的内容。  
**  
使用正则表达式时需要仔细观察该网页信息的结构，并写出正确的正则表达式。  
python正则表达式的使用也很简洁。我的上一篇文章《 [ Python的一些用法
](https://www.jb51.net/article/31472.htm) 》介绍了一点正则的用法。这里需要一个新的用法：  

_复制代码_ 代码如下:

  
def getWeather(html):  
reg = '<a title=.*?>(.*?)</a>.*?<span>(.*?)</span>.*?<b>(.*?)</b>'  
weatherList = re.compile(reg).findall(html)  
return weatherList  

  
其中reg是正则表达式，html是第一步获得的文本。findall的作用是找到html中所有符合正则匹配的字符串并存放到weatherList中。之后再枚举weatheList中的数据输出即可。  
这里的正则表达式reg有两个地方要注意。  
一个是“(.*?)”。只要是（）中的内容都是我们将要获得的内容，如果有多个括号，那么findall的每个结果就都包含这几个括号中的内容。上面有三个括号，分别对应城市、最低温和最高温。  
另一个是“.*?”。python的正则匹配默认是贪婪的，即默认尽可能多地匹配字符串。如果在末尾加上问号，则表示非贪婪模式，即尽可能少地匹配字符串。在这里，由于有多个城市的信息需要匹配，所以需要使用非贪婪模式，否则匹配结果只剩下一个，且是不正确的。  
  
python的使用确实十分方便：）

