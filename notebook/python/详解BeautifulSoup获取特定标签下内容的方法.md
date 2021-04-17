以下是个人在学习beautifulSoup过程中的一些总结，目前我在使用爬虫数据时使用的方法的是：先用find_all()找出需要内容所在的标签，如果所需内容一个find_all()不能满足，那就用两个或者多个。接下来遍历find_all的结果，用get_txt（）、get(‘href')、得到文本或者链接，然后放入各自的列表中。这样做有一个缺点就是txt的数据是一个单独的列表，链接的数据也是一个单独的列表，一方面不能体现这些数据之间的结构性，另一方面当想要获得更多的内容时，就要创建更多的空列表。

遍历所有标签：

```python

    soup.find_all('a')
    
```

找出所有页面中含有标签a的html语句，结果以列表形式存储。对找到的标签可以进一步处理，如用for对结果遍历，可以对结果进行purify，得到如链接，字符等结果。

```python

    # 创建空列表
    links=[] 
    txts=[]
    tags=soup.find_all('a')
    for tag in tags:
      links.append(tag.get('href')
      txts.append(tag.txt)         #或者txts.append(tag.get_txt())
    
```

得到html的属性名：

```python

    atr=[]
    tags=soup.find_all('a')
    for tag in tags:
      atr.append(tag.p('class')) # 得到a 标签下，子标签p的class名称 
    
```

find_all()的相关用法实例：  

实例来自 [ BeautifulSoup中文文档
](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#id11)  

**1. 字符串**  

最简单的过滤器是字符串.在搜索方法中传入一个字符串参数,Beautiful Soup会查找与字符串完整匹配的内容,下面的例子用于查找文档中所有的标签:

```python

    soup.find_all('b')
    # [<b>The Dormouse's story</b>]
```

**2.正则表达式**  

如果传入正则表达式作为参数,Beautiful Soup会通过正则表达式的 match()
来匹配内容.下面例子中找出所有以b开头的标签,这表示和标签都应该被找到:

```python

    import re
    for tag in soup.find_all(re.compile("^b")):
      print(tag.name)
    # body
    # b
    
```

下面代码找出所有名字中包含”t”的标签:

```python

    for tag in soup.find_all(re.compile("t")):
      print(tag.name)
    # html
    # title
```

**3.列表  
**

如果传入列表参数,Beautiful Soup会将与列表中任一元素匹配的内容返回.下面代码找到文档中所有标签和标签:

```python

    soup.find_all(["a", "b"])
    # [<b>The Dormouse's story</b>,
    # <a class="sister" href="http://example.com/elsie" rel="external nofollow" rel="external nofollow" rel="external nofollow" rel="external nofollow" id="link1">Elsie</a>,
    # <a class="sister" href="http://example.com/lacie" rel="external nofollow" rel="external nofollow" rel="external nofollow" id="link2">Lacie</a>,
    # <a class="sister" href="http://example.com/tillie" rel="external nofollow" rel="external nofollow" rel="external nofollow" id="link3">Tillie</a>]
    
```

**4.方法（自定义函数，传入find_all）**  

如果没有合适过滤器,那么还可以定义一个方法,方法只接受一个元素参数 [4] ,如果这个方法返回 True 表示当前元素匹配并且被找到,如果不是则反回
False  
下面方法校验了当前元素,如果包含 class 属性却不包含 id 属性,那么将返回 True:

```python

    def has_class_but_no_id(tag):
      return tag.has_attr('class') and not tag.has_attr('id')```
    
```

返回结果中只有

标签没有标签,因为标签还定义了”id”,没有返回和,因为和中没有定义”class”属性.  
下面代码找到所有被文字包含的节点内容:

```python

    from bs4 import NavigableString
    def surrounded_by_strings(tag):
      return (isinstance(tag.next_element, NavigableString)
          and isinstance(tag.previous_element, NavigableString))
    
    for tag in soup.find_all(surrounded_by_strings):
      print tag.name
    # p
    # a
    # a
    # a
    # p
```

**5.按照CSS搜索**  

按照CSS类名搜索tag的功能非常实用,但标识CSS类名的关键字 class 在Python中是保留字,使用 class
做参数会导致语法错误.从Beautiful Soup的4.1.1版本开始,可以通过 class_ 参数搜索有指定CSS类名的tag:

```python

    soup.find_all("a", class_="sister")
    # [<a class="sister" href="http://example.com/elsie" rel="external nofollow" rel="external nofollow" rel="external nofollow" rel="external nofollow" id="link1">Elsie</a>,
    # <a class="sister" href="http://example.com/lacie" rel="external nofollow" rel="external nofollow" rel="external nofollow" id="link2">Lacie</a>,
    # <a class="sister" href="http://example.com/tillie" rel="external nofollow" rel="external nofollow" rel="external nofollow" id="link3">Tillie</a>]
    
```

或者：

```python

    soup.find_all("a", attrs={"class": "sister"})
    # [<a class="sister" href="http://example.com/elsie" rel="external nofollow" rel="external nofollow" rel="external nofollow" rel="external nofollow" id="link1">Elsie</a>,
    # <a class="sister" href="http://example.com/lacie" rel="external nofollow" rel="external nofollow" rel="external nofollow" id="link2">Lacie</a>,
    # <a class="sister" href="http://example.com/tillie" rel="external nofollow" rel="external nofollow" rel="external nofollow" id="link3">Tillie</a>]
    
```

**6.按照text参数查找**  

通过 text 参数可以搜搜文档中的字符串内容.与 name 参数的可选值一样, text 参数接受 字符串 , 正则表达式 , 列表, True .
看例子:

```python

    soup.find_all(text="Elsie")
    # [u'Elsie']
    
    soup.find_all(text=["Tillie", "Elsie", "Lacie"])
    # [u'Elsie', u'Lacie', u'Tillie']
    
    soup.find_all(text=re.compile("Dormouse"))
    [u"The Dormouse's story", u"The Dormouse's story"]
    
    def is_the_only_string_within_a_tag(s):
      ""Return True if this string is the only child of its parent tag.""
      return (s == s.parent.string)
    
    soup.find_all(text=is_the_only_string_within_a_tag)
    # [u"The Dormouse's story", u"The Dormouse's story", u'Elsie', u'Lacie', u'Tillie', u'...']
    
    
```

虽然 text 参数用于搜索字符串,还可以与其它参数混合使用来过滤tag.Beautiful Soup会找到 .string 方法与 text
参数值相符的tag.下面代码用来搜索内容里面包含“Elsie”的标签:

```python

    soup.find_all("a", text="Elsie")
    # [<a href="http://example.com/elsie" rel="external nofollow" rel="external nofollow" rel="external nofollow" rel="external nofollow" class="sister" id="link1">Elsie</a>]
    
```

**7.只查找当前标签的子节点**  

调用tag的 find_all() 方法时,Beautiful Soup会检索当前tag的所有子孙节点,如果只想搜索tag的直接子节点,可以使用参数
recursive=False .

一段简单的文档:

```python

    <html>
     <head>
     <title>
      The Dormouse's story
     </title>
     </head>
    ...
    
```

是否使用 recursive 参数的搜索结果:

```python

    soup.html.find_all("title")
    # [<title>The Dormouse's story</title>]
    
    soup.html.find_all("title", recursive=False)
    # []
    
```

到此这篇关于详解BeautifulSoup获取特定标签下内容的方法的文章就介绍到这了,更多相关BeautifulSoup获取特定标签内容内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！  

