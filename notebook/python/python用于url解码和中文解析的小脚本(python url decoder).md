_复制代码_ 代码如下:

  
# -*- coding: utf8 -*-  
#! python  
print(repr("测试报警，xxxx是大猪头".decode("UTF8").encode("GBK")).replace("\\x","%"))  

  
  
注意第一个 decode("UTF8") 要与文件声明的编码一样。  
  

最开始对这个问题的接触，来自于一个Javascript解谜闯关的小游戏，某一关的提示如下：

刚开始的几关都是很简单很简单的哦～～这一关只是简单的字符串变形而已…..

后面是一大长串开头是%5Cu4e0b%5Cu4e00%5Cu5173%5Cu7684这样的字符串。  
这种东西以前经常在浏览器的地址栏见到，就是一直不知道怎么转换成能看懂的东东，  
网上google了一下，结合python的url解码和unicode解码，解决方式如下:

_复制代码_ 代码如下:

  
import urllib
escaped_str="%5Cu4e0b%5Cu4e00%5Cu5173%5Cu7684%5Cu9875%5Cu9762%5Cu540d%5Cu5b57%5Cu662f%5Cx20%5Cx69%5Cx32%5Cx6a%5Cx62%5Cx6a%5Cx33%5Cx69%5Cx34%5Cx62%5Cx62%5Cx35%5Cx34%5Cx62%5Cx35%5Cx32%5Cx69%5Cx62%5Cx33%5Cx2e%5Cx68%5Cx74%5Cx6d"  
print urllib.unquote(escaped_str).decode('unicode-escape')  

最近，我对firefox的autoproxy插件中的gfwlist中的中文词汇（用过代理的同学们，你们懂的）产生了兴趣，然而这些网址都是用url编码的，比如http://zh.wikipedia.org/wiki/%E9%97%A8，需要使用正则表达式将被url编码的中文字符提取出来，写了个小脚本如下：

_复制代码_ 代码如下:

  
import urllib  
import re  
with open("listfile","r") as f:  
for url_str in f:  
match=re.compile("((%\w{2}){3,})").findall(url_str)  
#汉字url编码的样式是：百分号+2个十六进制数，重复3次  
  
if match!=None:  
#如果匹配成功，则将提取出的部分转换为中文  
for trans in match:  
print urllib.unquote(trans[0]),  

然而这个脚本仍有一些缺点，对于列表文件中的某些中文字符仍然不能正常解码，比如下面这几行测试代码

_复制代码_ 代码如下:

  
import urllib  
a="http://zh.wikipedia.org/wiki/%BD%F0%B6"  
b="http://zh.wikipedia.org/wiki/%E9%97%A8"  
de=urllib.unquote  
print de(a),de(b)  

输出结果就是前者可以正确解码，而后者不可以，个人觉得原因可能和big5编码有关，如果谁知道什么解决办法，还请告诉我一下~  
  
以下是补充：  
  
de(a).decode(“gbk”,”ignore”)  
de(b).decode(“utf8″,”ignore”)

