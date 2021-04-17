例如 具有如下结构的html文件  
  

_复制代码_ 代码如下:

  
<div class='entry-content'>  
<p>感兴趣内容1</p>  
<p>感兴趣内容2</p>  
……  
<p>感兴趣内容n</p>  
</div>  
<div class='content'>  
<p>内容1</p>  
<p>内容2</p>  
……  
<p>内容n</p>  
</div>  

  
  
**我们尝试获得'感兴趣内容'  
**  
对于文本内容,我们保存到IDList中。  
可是如何标记我们遇到的文本是感兴趣的内容呢，也就是，处于  

_复制代码_ 代码如下:

  
<div class='entry-content'>  
<p>这里的内容</p>  
<p>还有这里</p>  
……  
<p>以及这里的内容</p>  
</div>  

  
  
**思路如下**  

  1. 遇到<div class='entry-content'> 设置标记flag = True 
  2. 遇到</div>后 设置标记flag = False 
  3. 当flag 为True时遇到<p> 设置标记getdata = True 
  4. 遇到</p> 且getdata = True,设置getdata = False 

python为我们提供了SGMLParser类，SGMLParser 将 HTML 分析成 8 类数据 **[1]**
，然后对每一类调用单独的方法:使用时只需继承SGMLParser 类，并编写页面信息的处理函数。

**可用的处理函数如下** ：

****

  * **开始标记 (Start tag)**

> 是一个开始一个块的 HTML 标记，象 <html>，<head>，<body> 或 <pre> 等，或是一个独一的标记，象 <br> 或 <img>
> 等。当它找到一个开始标记 tagname，SGMLParser 将查找名为 _**start_tagname** _ 或 **_do_tagname_
> ** 的方法。例如，当它找到一个 <pre> 标记，它将查找一个 start_pre 或 do_pre 的方法。如果找到了，SGMLParser
> 会使用这个标记的属性列表来调用这个方法；否则，它用这个标记的名字和属性列表来调用 **_unknown_starttag_ ** 方法。

  * **结束标记 (End tag)**

> 是结束一个块的 HTML 标记，象 </html>，</head>，</body> 或 </pre> 等。当找到一个结束标记时，SGMLParser
> 将查找名为 **_end_tagname_ ** 的方法。如果找到，SGMLParser 调用这个方法，否则它使用标记的名字来调用
> **_unknown_endtag_ ** 。

  * **字符引用 (Character reference)**

> 用字符的十进制或等同的十六进制来表示的转义字符，象 &#160;。当找到，SGMLParser 使用十进制或等同的十六进制字符文本来调用
> **_handle_charref_ ** 。

  * **实体引用 (Entity reference)**

> HTML 实体，象 &copy;。当找到，SGMLParser 使用 HTML 实体的名字来调用 **_handle_entityref_ ** 。

  * **注释 (Comment)**

> HTML 注释, 包括在 <!-- ... -->之间。当找到，SGMLParser 用注释内容来调用 **_handle_comment_ ** 。

  * **_处理指令 (Processing instruction)_ **

> HTML 处理指令，包括在 <? ... > 之间。当找到，SGMLParser 用处理指令内容来调用 **_handle_pi_ ** 。

  * **声明 (Declaration)**

> HTML 声明，如 DOCTYPE，包括在 <! ... >之间。当找到，SGMLParser 用声明内容来调用 **_handle_decl_ **
> 。

  * **文本数据 (Text data)**

> 文本块。不满足其它 7 种类别的任何东西。当找到，SGMLParser 用文本来调用 **_handle_data_ ** 。

  

**综上** ，的到如下代码  
  
  

_复制代码_ 代码如下:

  
from sgmllib import SGMLParser  
class GetIdList(SGMLParser):  
def reset(self):  
self.IDlist = []  
self.flag = False  
self.getdata = False  
SGMLParser.reset(self)  
  
def start_div(self, attrs):  
for k,v in attrs:#遍历div的所有属性以及其值  
if k == 'class' and v == 'entry-content':#确定进入了<div class='entry-content'>  
self.flag = True  
return

def end_div(self):#遇到</div>  
self.flag = False  
  
def start_p(self, attrs):  
if self.flag == False:  
return  
self.getdata = True  

_复制代码_ 代码如下:

  
def end_p(self):#遇到</p>  
if self.getdata:  
self.getdata = False

def handle_data(self, text):#处理文本  
if self.getdata:  
self.IDlist.append(text)  

_复制代码_ 代码如下:

  
def printID(self):  
for i in self.IDlist:  
print i  

上面的思路存在一个bug  
遇到</div>后 设置标记flag = False  
如果遇到div嵌套怎么办？

_复制代码_ 代码如下:

  
<div class='entry-content'><div>我是来捣乱的</div><p>感兴趣</p></div>  

在遇到第一个</div>之后标记flag = False，导致无法的到‘感兴趣内容'。  
怎么办呢？如何判断遇到的</div>是和<div class='entry-content'>匹配的哪个呢？  
很简单，</div>和<div>是对应的，我们可以记录他所处的层数。进入子层div verbatim加1,退出子层div
verbatim减1.这样就可以判断是否是同一层了。

修改后 如下

_复制代码_ 代码如下:

  
from sgmllib import SGMLParser  
class GetIdList(SGMLParser):  
def reset(self):  
self.IDlist = []  
self.flag = False  
self.getdata = False  
self.verbatim = 0  
SGMLParser.reset(self)  
  
def start_div(self, attrs):  
if self.flag == True:  
self.verbatim +=1 #进入子层div了，层数加1  
return  
for k,v in attrs:#遍历div的所有属性以及其值  
if k == 'class' and v == 'entry-content':#确定进入了<div class='entry-content'>  
self.flag = True  
return

def end_div(self):#遇到</div>  
if self.verbatim == 0:  
self.flag = False  
if self.flag == True:#退出子层div了，层数减1  
self.verbatim -=1

def start_p(self, attrs):  
if self.flag == False:  
return  
self.getdata = True  
  
def end_p(self):#遇到</p>  
if self.getdata:  
self.getdata = False

def handle_data(self, text):#处理文本  
if self.getdata:  
self.IDlist.append(text)  
  
def printID(self):  
for i in self.IDlist:  
print i  

最后 建立了我们自己的类GetIdList后如何使用呢？  
简单建立实例 t = GetIdList()  
the_page为字符串，内容为html  
t.feed(the_page)#对html解析

t.printID()打印出结果

全部测试代码为

_复制代码_ 代码如下:

  
from sgmllib import SGMLParser  
class GetIdList(SGMLParser):  
def reset(self):  
self.IDlist = []  
self.flag = False  
self.getdata = False  
self.verbatim = 0  
SGMLParser.reset(self)  
  
def start_div(self, attrs):  
if self.flag == True:  
self.verbatim +=1 #进入子层div了，层数加1  
return  
for k,v in attrs:#遍历div的所有属性以及其值  
if k == 'class' and v == 'entry-content':#确定进入了<div class='entry-content'>  
self.flag = True  
return

def end_div(self):#遇到</div>  
if self.verbatim == 0:  
self.flag = False  
if self.flag == True:#退出子层div了，层数减1  
self.verbatim -=1

def start_p(self, attrs):  
if self.flag == False:  
return  
self.getdata = True  
  
def end_p(self):#遇到</p>  
if self.getdata:  
self.getdata = False

def handle_data(self, text):#处理文本  
if self.getdata:  
self.IDlist.append(text)  
  
def printID(self):  
for i in self.IDlist:  
print i

  
##import urllib2  
##import datetime  
##vrg = (datetime.date(2012,2,19) - datetime.date.today()).days  
##strUrl = 'http://www.nod32id.org/nod32id/%d.html'%(200+vrg)  
##req = urllib2.Request(strUrl)#通过网络获取网页  
##response = urllib2.urlopen(req)  
##the_page = response.read()

the_page ='''<html>  
<head>  
<title>test</title>  
</head>  
<body>  
<h1>title</h1>  
<div class='entry-content'>  
<div class= 'ooxx'>我是来捣乱的</div>  
<p>感兴趣内容1</p>  
<p>感兴趣内容2</p>  
……  
<p>感兴趣内容n</p>  
<div class= 'ooxx'>我是来捣乱的2<div class= 'ooxx'>我是来捣乱的3</div></div>  
</div>  
<div class='content'>  
<p>内容1</p>  
<p>内容2</p>  
……  
<p>内容n</p>  
</div>  
</body>  
</html>  
'''  
lister = GetIdList()  
lister.feed(the_page)  
lister.printID()  

执行后 输出为  

_复制代码_ 代码如下:

  
感兴趣内容1  
感兴趣内容2  
感兴趣内容n  

  
  
参考文献  
  
[1] [ 深入 Python:Dive Into Python 中文版
](http://help.jb51.net/diveintopython/toc/index.html)

