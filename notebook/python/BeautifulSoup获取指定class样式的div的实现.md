如何获取指定的标签的内容是解析网页爬取数据的必要手段，比如想获取<div class='xxx'> ...<div>这样的div标签，通常有三种办法，

1）用字符串查找方法,然后切分字符串（或切片操作），如str.index(patternStr)或str.find(patternStr)，这种方法快，但步骤多，因为要去头去尾。

2）用正则表达式，比如'<div
class="result_info">([\s\S]+?)</div>'，通过正则表达式的括号，可以获取匹配的内容，即<div
..></div>之间的内容：

```python

    import re
    
    def getTags(html):
     reg = r'<div class="result_info">([\s\S]+?)</div>'
     pattern= re.compile(reg)
     tags= re.findall(pattern, html)
     return tags
    
    
```

  

不过正则表达式仍有缺点，例如'<div
class="result_info">([\s\S]+?)</div>'括号中的问号表示非贪婪匹配，正常情况下可以匹配到所需要的内容，但如果class="result_info"的div中还嵌套了子的div，那么正则表达式的后半部分"</div>"将会匹配子div的结尾部分</div>，而不是希望的父div.

假如有这样一个html：

```python

     <div class="result_info">
      <p>some paragraph test 1
      </p>
      <p>some paragraph test 2
      </p>
      <div id="div_sub" class="sub_div_style">
      some contents in sub div
      </div>
      backend content here
     </div>
    
```

那么backend contents here这段内容将会匹配不到，正则表达式将会将id为div_sub的</div>作为结尾。

3）使用第三方库，比如BeautifulSoup，优点是准确，缺点是速度会比字符串切分、正则表达式慢，下面说说BeautifulSoup的用法。

按照BeautifulSoup官方文档的说明怎么都不能成功，后来在百度知道（ [
http://zhidao.baidu.com/question/433247968620775644.html
](http://zhidao.baidu.com/question/433247968620775644.html) ）找到答案，真是扯淡，附上有效代码：

```python

    soup=BeautifulSoup(html)
    print soup.find_all(name='div',attrs={"class":"footer"})#按照字典的形式给attrs参数赋值
    
```

完整的：

```python

    from bs4 import BeautifulSoup
    import urllib2
    
    def getTargetDiv(url,myAttrs):
     html=urllib2.urlopen(url).read()
     soup=BeautifulSoup(html)
     return soup.find_all(name='div',attrs=myAttrs)
    
    if __name__=="__main__":
     url=r'http://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/'
     myAttrs={'class':'footer'}
     print getTargetDiv(url, myAttrs)
    
    
```

按照官方文档( [ http://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/
](http://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/) )的做法：

```python

    #1.soup.find_all("a", class_="sister")
    #2.css_soup.find_all("p", class_="body")
    #3.soup.find_all(href=re.compile("elsie"))
    
```

改成

```python

    soup.find_all(name='div',class_=re.compile('info_item'))
    
```

或者  

```python

    soup.find_all('div',class_='info_item')
    
```

都没有匹配结果，经测试需要soup.find_all(name='div',attrs={"class":"footer"})这样以字典的形式给attrs参数赋值才可以。

另一个例子，获取指定样式的div内的所有图片url，并下载保存:

```python

    urls=[]
    for img in soup.find('div',attrs={'class':'wrap'}).find_all('img'):#找到class="wrap"的div里面的所有<img>标签
     urls.append(img.attrs['src'])#获取img标签的src属性，即图片网址
    
    i=0
    savedir=r'C:\Users\hp\Desktop\Images'#路径中不能包含中文
    for url in urls:
     urllib.urlretrieve(url, '%s\%s.jpg'%(savedir,i))
     i+=1
    print 'Done'
    
    
```

更多用法，可参考： [ https://www.jb51.net/article/184386.htm
](https://www.jb51.net/article/184386.htm)

到此这篇关于BeautifulSoup获取指定class样式的div的实现的文章就介绍到这了,更多相关BeautifulSoup获取class样式的div内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

