网站的大框架下有定义的字体，包括字体大小和颜色等，用户发布文章的时候可能是从其他网站复制过来的文本，复制的过程也保留了字体描述信息。当文章在页面上显示的时候，默认先会使用文章中定义的字体，如果文章中字体不存在的话才显示大框架下定义的全局字体。因此网站的内容就会显得很乱，有的文章字体很大，有的文章字体很小，不美观。能统一的话就好了！

我对html和css等不是很熟，不知道是否能设置一下让文章中定义的字体内容失效。

笨人有笨办法，统一修改文章，将用户的对字体的定义全部删除！哈哈！如果手工完成的话，这可是一个相当繁重的任务，要首先预览页面，如果不统一的话就修改字体，幸好编辑器里面有个“清除格式”选项，全选文本，点一下就OK了，然后再保存……也很麻烦

如果仅仅是修改字体的话，最省事的方法当然是直接修改数据库，从数据库将文章提取出来，删除和字体相关的标签，然后再写回数据库。

专门查了一下html参考手册，对字体的定义有两种方法：

1.是用<font>标签，例如：

_复制代码_ 代码如下:

  
<p>  
<font size="2" face="Verdana">  
This is a paragraph.  
</font>  
</p>

<p>  
<font size="3" face="Times">  
This is another paragraph.  
</font>  
</p>  

  
这种方法是不推荐使用的

2.使用style定义，例如：  

_复制代码_ 代码如下:

  
<p style="font-family:verdana;font-size:80%;color:green">  
This is a paragraph with some text in it. This is a paragraph with some text
in it. This is a paragraph with some text in it. This is a paragraph with some
text in it.  
</p>  

  
只要将字体的定义部分删除就可以了，用python的正则表达式模块进行替换无压力：

_复制代码_ 代码如下:

  
def format(data):  
'''将font标签和style标签全部删除'''  
p = re.compile(r'<font .*?>|</font>|style=\".*?\"')  
ret = p.sub('',data)  
if ret != data:  
return retelse:  
return None  

  
python处理数据库相关操作时要注意更新数据方法，可以参考这篇文章：http://www.cnblogs.com/ma6174/archive/2013/02/21/2920126.html

