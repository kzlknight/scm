##  1. Key Promoter X

如果让我给新手推荐一个 PyCharm 必装插件，那一定是 ` Key Promoter X ` 。

它就相当于一个快捷键管理大师，它时刻地在：

督促你，当下你的这个操作，应该使用哪个快捷操作来提高效率？

提醒你，当下你的这个操作，还没有设置快捷键，赶紧设置一个？

有了 ` Key Promoter X ` ，你很快就能熟练地掌握快捷键，替代鼠标指日可待。

比如我使用鼠标点开 ` Find in Path ` ，它就会在右下角弹窗提示你该用哪个快捷键。

![](https://img.jbzj.com/file_images/article/202101/202101110928584.png)

##  2. Vim in PyCharm

在大多数场景之下，使用鼠标的效率和精准度，是远不如键盘快捷键的（前提是你已经相当熟练的掌握了快捷键），这个你得承认吧。

Vi 可以满足你对文本操作的所有需求，比可视化界面更加效率，更加 geek。如果你和我一样，是忠实的 vim 粉。在安装完 Pycharm
完后，肯定会第一时间将 ` ideaVim ` 这个插件也装上，它可以让我们在 Pycharm 中 使用 vim 来编辑代码。

安装方法如下，安装完后需要重启 Pycharm 生效。

![](https://img.jbzj.com/file_images/article/202101/202101110928585.png)

##  3. Markdown

富文本排版文档是一件非常痛苦的事情 ，对于程序员写文档，最佳的推荐是使用 Markdown ，我所有的博客日记都是使用 Markdown 写出来的。

从 Github下载的代码一般也都会带有README.md文件，该文件是一个Markdown格式的文件。

PyCharm是默认没有安装Markdown插件的，所以不能按照Markdown格式显示文本，显示的是原始文本。

因此，如果要在 PyCharm 中阅读 Markdown 文档，可以装一下 Markdown support 这个插件。

安装的方法有两种：

1、第一种，最方便的，就是你打开一个 MD 的文档，PyCharm 就会提示你安装它。

2、从插件商店中搜索安装。

![](https://img.jbzj.com/file_images/article/202101/202101110928586.png)

效果如下

[外链图片转存失败,源站可能有防盗链机制,建议将图片保存下来直接上传(img-
NOEVbklj-1609131420961)(http://image.iswbm.com/20200827130420.png)]

##  4. Jupyter Notebook

使用 Jupyter 之前 ，先要安装它

```python

    $ pip install jupyter
```

然后按照下图指示新建一个 Notebook ，就可以开始运作了。

![](https://img.jbzj.com/file_images/article/202101/202101110928587.png)

这个界面感觉和 Jupyter 的风格不太符

![](https://img.jbzj.com/file_images/article/202101/202101110928588.png)

但是使用上是没有什么区别的，记住三个快捷键就好(下面指的是 Mac 上的，Windows 上的有所不同)

  * Ctrl+Enter：运行该 cell 
  * Option + shift + Enter：调试该 cell 
  * Shift + Enter：插入一个新的 cell 

![](https://img.jbzj.com/file_images/article/202101/202101110928599.png)

只要你安装了 Jupyter 后，你使用 Python Console 也会自动变成 Jupyter 的模式

![](https://img.jbzj.com/file_images/article/202101/2021011109285910.png)

##  5. Regex Tester

Regex Tester是PyCharm的第三方插件，可以测试正则表达式。

按照下图入口，安装 Regex Tester 插件：

![](https://img.jbzj.com/file_images/article/202101/2021011109285911.png)

安装完成后，无需重启 PyCharm ，点击 PyCharm 界面左下方的小矩形按钮，就能找到 Regex Tester 选项。

![](https://img.jbzj.com/file_images/article/202101/2021011109285912.png)

点击进入后，就出现了如下界面。我随手写了个匹配手机号码的正则（不一定准确），匹配到的字符串背景会被高亮。右上方还有一些选项如大小写敏感，多行模式等，可根据需要进行选择。Regex
Tester 还提供了Split，Replace功能等。

使用效果如下：

![](https://img.jbzj.com/file_images/article/202101/2021011109285913.png)

##  6. Use Bash in Windows

（注：这个是自带工具，不是插件）  
在 Windows 上的 cmd 命令和 Linux 命令有不少的差异，比如要列出当前目录下的所有文件，Windows 上是用 ` dir ` ，而
Linux 上则是用 ` ls -l ` 。

对于像我这样熟悉 Linux 的开发者来说，Windows 的 那些 CMD 命令带来的糟糕体验是无法忍受的。

![](https://img.jbzj.com/file_images/article/202101/2021011109285914.png)

在弹出的 Bash 窗口，你可以敲入你想使用的 Linux 命令，是不是舒服多了。

![](https://img.jbzj.com/file_images/article/202101/2021011109285915.png)

##  7. Auto PEP8

` pep8 ` 是Python
语言的一个代码编写规范。如若你是新手，目前只想快速掌握基础，而不想过多去注重代码的的编写风格（虽然这很重要），那你可以尝试一下这个工具 - `
autopep8 `

首先在全局环境中（不要在虚拟环境中安装），安装一下这个工具。

```python

    $ sudo pip install autopep8
```

然后在 PyCharm 导入这个工具，具体设置如下图

```python

    Name: AutoPep8
    Description: autopep8 your code
    Program: autopep8
    Arguments: --in-place --aggressive --aggressive $FilePath$
    Working directory: $ProjectFileDir$
    Output filters: $FILE_PATH$\:$LINE$\:$COLUMN$\:.*
```

![](https://img.jbzj.com/file_images/article/202101/2021011109290016.png)

我随意写了一段不符合 pep8 规范的代码。

![](https://img.jbzj.com/file_images/article/202101/2021011109290017.png)

点击右键，选择 ` External Tools ` -> ` AutoPep8 `

![](https://img.jbzj.com/file_images/article/202101/2021011109290018.png)

看一下效果，还是挺明显的。

![](https://img.jbzj.com/file_images/article/202101/2021011109290019.png)

你可能会说，Pycharm 本身就自带这个功能了呀，快捷键 ` Command ` + ` Option ` + ` L `
，就可以实现一键pep8了。你可以对比一下，Pycharm 自带的代码 pep8 化功能 并没有像这个 ` autopep8 ` 来得彻底。
我相信你最终的选择肯定是后者。

##  8. Test RESTful Web Service

PyCharm 的 Test RESTful Web
Service工具提供了RESTful接口测试界面，如下图所示，提供了get、post，put等http方法，其中的Request子界面headers，Parameters，Body等功能，Response子界面用于显示返回值，Response
Headers用于显示返回的消息头。

为了演示，我先使用 Flask 写一个 HTTP 接口

```python

    from flask import Flask, request
    
    app = Flask(__name__)
    
    
    @app.route('/hello')
    def index():
     name = request.args.get('name')
     return '你好，' + name
    
    if __name__ == '__main__':
     app.run()
```

并运行它开启服务，访问地址是： [ http://127.0.0.1:5000/ ](http://127.0.0.1:5000/)

![](https://img.jbzj.com/file_images/article/202101/2021011109290020.png)

通过下图方式打开 ` Test RESTful Web Service `

![](https://img.jbzj.com/file_images/article/202101/2021011109290021.png)

会出现如下界面，在红框处填写如下信息

![](https://img.jbzj.com/file_images/article/202101/2021011109290022.png)

然后点击最左边的运行按钮，即可向服务器发送 http 请求。

![](https://img.jbzj.com/file_images/article/202101/2021011109290123.png)

##  9. Execute Selection in Console

（注：这个是自带工具，不是插件）

当你想写一段简单的测试代码时，或许你会这样子

使用 Python Shell 直接写。缺点是没有自动补全。在 PyCharm 中新开一个文件。缺点是要新创建一个文件，完了后还要删除。

今天再给大家介绍一种新的方法，可以完全避开上面两种方式的缺点。

那就是 ` Execute Selection in Console ` ，可以说是 ` Run in Anywhere ` .

只要在当前文件中，写好代码，然后光标选择后，右键点击 ` Execute Selection in Python Console ` 或者 使用快捷键
option + shift + E (windows 上是 alt + shift + E)。

![](https://img.jbzj.com/file_images/article/202101/2021011109290124.png)

接着 PyCharm 就会弹出一个 Python Console 窗口，然后运行你所选择的代码。

![](https://img.jbzj.com/file_images/article/202101/2021011109290125.png)

可以发现其中的一个亮点，就是使用这种方法，PyCharm 会自动帮我们处理好缩进（我们选择时，前面有缩进，可是在执行时，会自动去掉前面多余的缩进）

##  10. CodeGlance

如果你曾使用过 Sublime Text，切换到其他代码编辑器，或多或少会有些不习惯，因为很少有编辑器会像 Sublime 那样自带一个预览功能的滚动条。

在 PyCharm 中，就没有解决不了的问题，如果有，那么就装个插件。

要想在 PyCharm 中使用这个预览滚动条，只要装上 ` CodeGlance ` 这个插件。使用效果如下

![](https://img.jbzj.com/file_images/article/202101/2021011109290126.png)

##  11. Chinese Plugin

经常听到很多初学者抱怨说，PyCharm 怎么是全英文的？学起来好难啊。

在以前，我会跟他们说，学习编程语言，英文是一项非常重要的能力，千万不能惧怕它，逃避它，而要是去学习它，适应它，如果连个 IDE 都适应不了，那就别学编程了。

而现在，JetBrains 官方自己出了汉化插件，名字就叫： chinese，在插件市场里一搜，排名第一便是它，下载量已经 40
万，对比排名第二的民间汉化插件，简直不是量级的。

![](https://img.jbzj.com/file_images/article/202101/2021011109290127.png)

点击 ` INSTALL ` 安装后，会提示你进行重启，才能生效。

![](https://img.jbzj.com/file_images/article/202101/2021011109290128.png)

重启完成后，展现在我们面前的是一个既熟悉又陌生的界面，所有的菜单栏全部变成了中文。

![](https://img.jbzj.com/file_images/article/202101/2021011109290129.png)

点进设置一看，可以说基本实现了汉化，只剩下一小撮的英文（难道是因为这些词保留英文会比翻译后更容易理解吗？就像 socket
和套接字一样。），不过个人感觉完全不影响使用了。

![](https://img.jbzj.com/file_images/article/202101/2021011109290230.png)

##  12. Profile

（注：这个是自带工具，不是插件）

在 Python 中有许多模块可以帮助你分析并找出你的项目中哪里出现了性能问题。

比如，常用的模块有 cProfile，在某些框架中，也内置了中间件帮助你进行性能分析，比如 Django ，WSGI。

做为Python 的第一 IDE， PyCharm 本身就支持了这项功能。而且使用非常方便，小白。

假设现在要分析如下这段代码的性能损耗情况，找出到底哪个函数耗时最多

```python

    import time
    
    def fun1():
     time.sleep(1)
    
    def fun2():
     time.sleep(1)
    
    def fun3():
     time.sleep(2)
    
    def fun4():
     time.sleep(1)
    
    def fun5():
     time.sleep(1)
     fun4()
    
    fun1()
    fun2()
    fun3()
    fun5()
```

点击 Run -> Profile ‘程序' ，即可进行性能分析。

![](https://img.jbzj.com/file_images/article/202101/2021011109290231.png)

运行完毕后，会自动跳出一个性能统计界面。

![](https://img.jbzj.com/file_images/article/202101/2021011109290232.png)

性能统计界面由Name、Call Count、Time(ms)、Own Time(ms) ，4列组成一个表格，见下图。

  * 表头Name显示被调用的模块或者函数；Call Count显示被调用的次数；Time(ms)显示运行时间和时间百分比，时间单位为毫秒（ms）。 
  * 点击表头上的小三角可以升序或降序排列表格。 
  * 在Name这一个列中双击某一行可以跳转到对应的代码。 
  * 以fun4这一行举例：fun4被调用了一次，运行时间为1000ms，占整个运行时间的16.7% 

点击 Call Graph（调用关系图）界面直观展示了各函数直接的调用关系、运行时间和时间百分比，见下图。

![](https://img.jbzj.com/file_images/article/202101/2021011109290233.png)

右上角的4个按钮表示放大、缩小、真实大小、合适大小；

  * 箭头表示调用关系，由调用者指向被调用者； 
  * 矩形的左上角显示模块或者函数的名称，右上角显示被调用的次数； 
  * 矩形中间显示运行时间和时间百分比； 
  * 矩形的颜色表示运行时间或者时间百分比大小的趋势：红色 > 黄绿色 > 绿色，由图可以看出fun3的矩形为黄绿色，fun1为绿色，所有fun3运行时间比fun1长。 
  * 从图中可以看出Test.py直接调用了fun3、fun1、fun2和fun5函数；fun5函数直接调用了fun4函数；fun1、fun2、fun3、fun4和fun5都直接调用了print以及sleep函数；整个测试代码运行的总时间为6006ms，其中fun3的运行时间为1999ms，所占的时间百分比为33.3%，也就是 1999ms / 6006ms = 33.3%。 

##  13. Json Parser

在开发过程中，经常会把校验一串 JSON 字符串是否合法，在以前我的做法都是打开 https://tool.lu/json/
这个在线网站，直接美化来校验，只有 JSON 格式都正确无误合法的，才能够美化。

![img](https://img.jbzj.com/file_images/article/202101/2021011109290234.png)

直到后来发现在 PyCharm 有一个插件专门来做这个事，那就是 ` JSON Parser ` ，在插件市场安装后，重启 PyCharm
，就能在右侧边栏中看到它。

![img](https://img.jbzj.com/file_images/article/202101/2021011109290235.png)

##  14. Inspect Code in PyCharm

对于编译型的语言，如
Java，需要将代码编译成机器可识别的语言才可运行，在编译过程中，就可以通过分析或检查源程序的语法、结构、过程、接口等来检查程序的正确性，找出代码隐藏的错误和缺陷。这个过程叫做静态代码分析检查。

那对于 Python
这种解释型的语言来说，代码是边运行边翻译的，不需要经过编译这个过程。很多肉眼无法一下子看出的错误，通常都是跑一下（反正跑一下这么方便）才能发现。

由于Python 运行是如此的方便，以至于我们都不太需要关注静态分析工具。

但也不是说，静态分析工具完全没有用武之地，我认为还是有。

如果你的编码能力还没有很成熟，代码中可以有许许多多的隐藏bug，由于 Python
是运行到的时候才解释，导致一次运行只能发现一个错误，要发现100个bug，要运行100次，数字有点夸大，其实就是想说，如果这么多的错误都能通过一次静态检查发现就立马修改，开发调试的效率就可以有所提升。当然啦，并不是说所有的错误静态分析都能提前发现，这点希望你不要误解。

做为 Python 最强 IDE，PyCharm本身内置了这个功能，不需要你安装任何插件。

你只需要像下面这样点击项目文件夹，然后右键，选择 ` Inspect Code ` ，就可以开启静态检查。

![](https://img.jbzj.com/file_images/article/202101/2021011109290236.png)

我对开源组件 nova 的静态检查发现，其有不规范的地方有数千处。

![](https://img.jbzj.com/file_images/article/202101/2021011109290237.png)

另外，我还整理了 100 个 PyCharm 的使用技巧，为了让新手能够直接上手，我花了很多的时间录制了上百张 GIF 动图。

有兴趣的前往在线文档阅读： [ PyCharm 中文指南 ](http://python.iswbm.com/en/latest/)

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021011109290338.jpg)

到此这篇关于装上这 14 个插件后，PyCharm 真的是无敌的存在的文章就介绍到这了,更多相关PyCharm
插件内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

