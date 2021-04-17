最近无聊,下了个visual studio
2005的furture,发现里面多了对动态语言的支持.其实很早就想摆弄下python,正好是个机会.一开始是想学ironpython,但后来发现还是实在的学python吧.  
下面是我昨天一天的学习结果,记录一下,方便和我一样的python初学者.  
  
**python是什么?**  
  
Python，是一种面向对象的解释性的计算机程序设计语言，也是一种功能强大而完善的通用型语言，已经具有十多年的发展历史，成熟且稳定。Python
具有脚本语言中最丰富和强大的类库，足以支持绝大多数日常应用。这种语言具有非常简捷而清晰的语法特点，适合完成各种高层任务，几乎可以在所有的操作系统中运行。目前，基于这种语言的相关技术正在飞速的发展，用户数量急剧扩大，相关的资源非常多。  
更多介绍:  
[ http://baike.baidu.com/view/21087.htm
](http://baike.baidu.com/view/21087.htm)  
官方网站:  
[ http://www.python.org/ ](http://www.python.org/)  
  
**python能做什么?**  
  
我比较关注的web领域开发,python就可以做.其他的cs程序,相信也不出成问题.  
  
**为什么要学python?**  
  
按照我的理解,python是和现在流行的java c#
c等相比都不同的语言.多学点不同的东西,不仅可以开拓视野,也会帮助你现在使用的语言(比如我在用c#).而且,说不定一发不可收拾,你的下一份工作就是python!  
  
  
**如何安装python.**  
  
到官方网站 [ http://www.python.org/ ](http://www.python.org/)
来下载最新版本的python(我下的是2.5),根据你的操作系统(我是windows xp)选择相应的下载点.下载完成后安装.  
安装的包括python的运行环境,库,和其他组件.其中比较重要的是一个用来编写python的ide,IDLE,在开始-程序-python2.5下可以看到它.  
  
**学习python**  
  
这里有一个很好的教程,可以帮助你快速的掌握python  
简明Python教程:  
[ http://www.woodpecker.org.cn:908 ... /chinese/index.html
](http://www.woodpecker.org.cn:9081/doc/abyteofpython_cn/chinese/index.html)  
这是稍微复杂些的  
Dive Into Python:  
[ http://www.woodpecker.org.cn/diveintopython/toc/index.html
](http://www.woodpecker.org.cn/diveintopython/toc/index.html)  
我昨天下午看了看简明Python教程,python的一些语法非常的有意思!  
  
**怎么运行python?**  
  
最简单的是用IDLE进行python程序的编写,完成后按F5就会打开python shell看到程序的结果.  
打开IDLE后,File-New Window,就可以开始一个新python程序的编写.  
  
**编写python的IDE都有哪些?**  
  
除了上面提到的IDLE,还有一个比较好的选择是Active Python,这个也是免费下载的软件.你可以到这里来下载  
Active Pytho: [ http://www.activestate.com/Products/activepython/
](http://www.activestate.com/Products/activepython/)  
  
**想要多一些关于python的资源**  
  
Python chm版电子书籍列表  
[ http://bound0.xinwen365.com/python/ ](http://bound0.xinwen365.com/python/)  
  
  
到这里,基本上就可以开始python的学习与实践了.实际上,大体了解了语法后,你肯定想知道怎么用python来编写一个更复杂的程序.  
  
**怎么用python开发网站?**  
  
现在有一些支持python开发网站的框架可选.  
入门级的Karrigell:  
[ http://karrigell.sourceforge.net/en/front.htm
](http://karrigell.sourceforge.net/en/front.htm)  
高级的Django:  
[ http://www.woodpecker.org.cn/obp ... bystep/newtest/doc/
](http://www.woodpecker.org.cn/obp/django/django-stepbystep/newtest/doc/)  
  
  
我现在是做.net开发的,所以也比较关注python和.net的一些结合.现在python在.net上通过ironpython实现.下面是这个的一些问题.  
  
**ironpython是什么?**  
  
简单理解就是一个.net可用的组件,或者说是.net框架下和c#等平行的另一种语言.(这样理解其实有问题,但可以帮助你快速的进入ironpython的世界).  
官方网站: [ http://www.codeplex.com/Wiki/View.aspx?ProjectName=IronPython
](http://www.codeplex.com/Wiki/View.aspx?ProjectName=IronPython)  
但是,如果抛去vs和.net,ironpython和python没有什么特别的不同.我们可以把此时的vs看成一个开发python程序的IDE或框架.  
  
**怎么在.net环境下使用ironpython?**  
  
使用ironpython当然是指用visual studio.net进行开发.要使用ironpython,需要给你的vs打个补丁.  
  
下载这个Microsoft ASP.NET Futures安装,可以让你的vs支持ironpython  
[ http://www.microsoft.com/downloa ... &displaylang=en
](http://www.microsoft.com/downloads/details.aspx?FamilyId=A5189BCB-
EF81-4C12-9733-E294D13A58E6&displaylang=en)  
通过下面的介绍,可以简单的了解如何在vs中使用ironpython  
[ http://quickstarts.asp.net/Futur ... miclanguage_wt.aspx
](http://quickstarts.asp.net/Futures/dlr/doc/dynamiclanguage_wt.aspx)  
另外的五个教程  
为了帮助初学者尽快地使用，开发小组提供了如下五个教程：  
1．Creating a Basic Web Page with IronPython.doc  
[ http://static.asp.net/asp.net/fi ... with-IronPython.doc
](http://static.asp.net/asp.net/files/IronPython/Creating-a-Basic-Web-Page-
with-IronPython.doc)  
2．Using Shared Code with IronPython for ASP.NET.doc  
[ http://static.asp.net/asp.net/fi ... hon-for-ASP.NET.doc
](http://static.asp.net/asp.net/files/IronPython/Using-Shared-Code-with-
IronPython-for-ASP.NET.doc)  
3．Databinding with IronPython for ASP.NET.doc  
[ http://static.asp.net/asp.net/fi ... hon-for-ASP.NET.doc
](http://static.asp.net/asp.net/files/IronPython/Databinding-with-IronPython-
for-ASP.NET.doc)  
4．Debugging IronPython for ASP.NET.doc  
[ http://static.asp.net/asp.net/fi ... hon-for-ASP.NET.doc
](http://static.asp.net/asp.net/files/IronPython/Debugging-IronPython-for-
ASP.NET.doc)  
5．Creating a User Control with IronPython.doc  
[ http://static.asp.net/asp.net/fi ... with-IronPython.doc
](http://static.asp.net/asp.net/files/IronPython/Creating-a-User-Control-with-
IronPython.doc)  
**  
我想直接在vs中像建立c#项目一样建立ironpython项目,该怎么办? **  
  
很遗憾,现在还没有这样的vs补丁发布,但是,你可以下载一个Visual Studio 2005 SDK Version 4.0来暂时的使用这一特性  
[ http://www.microsoft.com/downloa ... &displaylang=en
](http://www.microsoft.com/downloads/details.aspx?FamilyID=51A5C65B-C020-4E08-8AC0-3EB9C06996F4&displaylang=en)  
  
这个下载并安装后,会给你提供一个vs项目,打开后,按ctrl+f5运行,就会给你开启一个新的vs实例,在这个vs中,可以像建立c#项目一样建立ironpython项目.  
关于这个sdk的更多信息,看这个文章  
[ http://blogs.msdn.com/aaronmar/archive/2006/02/16/533273.aspx
](http://blogs.msdn.com/aaronmar/archive/2006/02/16/533273.aspx)  
  
**想要关于ironpython的更多的信息**  
  
看博客园的ironpython小组:  
[ http://www.cnblogs.com/ipyteam/archive/2006/11/05/506995.html
](http://www.cnblogs.com/ipyteam/archive/2006/11/05/506995.html)  
  
  
以上给出的,是我昨天一天的研究成果,更多信息,请关注我的博客 ^_^ 给文章起这么个名,主要是方便广大用搜索找到这个文章的python初学眩晕者  
一起来学python吧,未来是我们的  

