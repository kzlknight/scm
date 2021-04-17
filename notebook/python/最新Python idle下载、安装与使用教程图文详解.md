简介：IDLE是Python软件包自带的一个集成开发环境，可以方便地创建、运行、调试Python程序。本文包括IDEL安装、使用配置、和运行调试教程。

由于Google、YouTube等大型公司的推广， **python** 编程语言越来越受欢迎，很多编程爱好者，也将Python做为了首先的编程语言。  
今天我们就来讲一下，学习的第一步，安装 **Python idle编辑器** ，也它的调试和使用。

第一步，我们先去下载一个Python idle程序安装包。

本节讲的是windows下的idle，Linux idle是没有的，可以直接使用相应的python 解释器，我们先来打开， _www.python.org_
Python的官网网站，找到Downloads区，点击进去，找到适合的版本安装包。

![](https://img.jbzj.com/file_images/article/202011/2020112810365851.png)

由于本博主的系统是Window10 64位，选择 (WindowsX86-64web-based installer)idle python版本下载。

![](https://img.jbzj.com/file_images/article/202011/2020112810365852.png)

第二步，找到刚下载的Python程序安装包，双击打开，运行安装程序。

一般无需要过多设置，直接点击下一步，直至安装成功，点击完成就可以了。如果想切换安装目录的朋友，可以在那一步换一下安装的路径。

![](https://img.jbzj.com/file_images/article/202011/2020112810365853.png)

![](https://img.jbzj.com/file_images/article/202011/2020112810365954.png)

第三步，安装完成之后，在我们的开始菜单，找到 Python
idle，双击运行，就可以在我们的idle中，调试我们的python代码了。开始菜单中，选择idle (Python 3.7
64-bit)，这也是一个Python编写的GUI程序，其它几个选项是Python的模块文档和帮助。

![](https://img.jbzj.com/file_images/article/202011/2020112810365955.png)

下面我们输出一条python字符串语句，还有计算2个变量相加的值，输出在屏幕上面。

![](https://img.jbzj.com/file_images/article/202011/2020112810365956.png)

上面讲的都是Windows平台下的Python
idle安装和调试的过程，通常Linux系统，如：Ubuntu、CentOS都已经默认随系统安装好python程序了，在linux类系统中，这个idle叫做Python解释器，它是从终端模拟器中，输入“python”这个命令启动的。Python编程的一切都从这个IDLE编辑器中开始，在之后入门后，可以选择更多自己喜欢的Python编辑器，如：Wing
IDE专业级Python编辑器。

##  二、IDLE运行与配置使用

依次点击Options->Configure IDLE，在Settings页面可以设置字体、语法高亮、和快捷键等。  
我这里为了代码显示美观选了等宽字体Consolas。  
建议选择等宽字体，很容易辨识数字0和大写字母O，数字1和字母l（L的小写字母）、I（i的大写字母）。视觉效果好，不知道哪个是等宽字体请自行度娘，眼神儿不好的可以把size字号改大。点击OK或Apply会立即生效。

![](https://img.jbzj.com/file_images/article/202011/2020112810365957.png)

##  三、IDLE调试

在“Python Shell”窗口中单击“Debug”菜单中的“Debugger”菜单项，就可以启动IDLE的交互式调试器。这时，IDLE会打开“Debug
Control”窗口，并在“Python Shell”窗口中输出“[DEBUG
ON]”并后跟一个“>>>”提示符。这样，我们就能像平时那样使用这个“Python
Shell”窗口了，只不过现在输入的任何命令都是允许在调试器下。我们可以在“Debug
Control”窗口查看局部变量和全局变量等有关内容。如果要退出调试器的话，可以再次单击“Debug”菜单中的“Debugger”菜单项，IDLE会关闭“Debug
Control”窗口，并在“Python Shell”窗口中输出“[DEBUG OFF]”。

  
![](https://img.jbzj.com/file_images/article/202011/2020112810365958.png)

![](https://img.jbzj.com/file_images/article/202011/2020112810365959.png)

到此这篇关于最新Python idle下载、安装与使用教程图文详解的文章就介绍到这了,更多相关Python
idle下载、安装与使用内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

