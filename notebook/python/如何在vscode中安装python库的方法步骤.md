###  vscode安装python库

1.已经在vscode中装了python并配置好python运行环境。

![](https://img.jbzj.com/file_images/article/202101/2021010609493121.png)  

检查是否正确配置好运行环境，按Windows+R组合键在运行窗口输入cmd，打开命令提示符窗口输入python确定即可

![](https://img.jbzj.com/file_images/article/202101/2021010609493122.png)

2.找到vscode中python的路径

随便运行一个代码，例如 ` print（“hehe”） ` 下面的终端显示如下

![](https://img.jbzj.com/file_images/article/202101/2021010609493123.png)  

图中红色地方圈起的便是python的路径，到python3.8为止。  
如果你所显示的内容与我不同，可在setting.json中查找并将路径复制下来（在vscode中配置过python环境的应该都可以找到）

3.正式开始

在vscode中打开终端,点击View，在出现的选择栏中点击Terminal(集成终端)即可打开  

![](https://img.jbzj.com/file_images/article/202101/2021010609493224.png)  

打开终端后，我们在终端中进入python安装目录下的Scripts文件夹：输入cd+格式+刚才复制的路径+\Scripts\

![](https://img.jbzj.com/file_images/article/202101/2021010609493225.png)  

确定之后若终端直接出现了文件夹Scripts的路径，输入".\pip install
需要安装库名"确定等待安装成功即可（若失败可以多安装几次，也许会成功）。  

我以安装numpy为例：

![](https://img.jbzj.com/file_images/article/202101/2021010609493226.jpg)

当然若在输入“cd+格式+刚才复制的路径+\Scripts\”之后，并未跳出Scripts的路径，而是和我一样只有vscode的路径（如下图所示）

![](https://img.jbzj.com/file_images/article/202101/2021010609493227.png)  

直接点击打开链接地址，可以选择新建窗口，也可以不新建，此时终端会有Scripts的路径，在其后输入 ` .\pip install numpy ` 即可。

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010609493328.png)

###  VSCode使用Python缺少库怎么办

使用vscode进行Python编程时

import 库，提示ModuleNotFoundError: No module named ‘库名'

报错内容：  

> [Running] python -u
> “c:\Users\xp.vscode\python_project\tempCodeRunnerFile.py”  
>  Traceback (most recent call last):  
>  File “c:\Users\xp.vscode\python_project\tempCodeRunnerFile.py”, line 1, in  
>  import requests  
>  ModuleNotFoundError: No module named ‘requests'  
>

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010609535729.png)  

意思是你没有安装该库，那么怎么安装呢？  
这里使用的pip.exe这个文件，我的是安装了官方的python3.7就有了这个文件，路径是  
C:\Users\xp\AppData\Local\Programs\Python\Python37\Scripts  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010609535830.png)  

然后打开cmd，输入该文件所在路径  
cd C:\Users\xp\AppData\Local\Programs\Python\Python37\Scripts  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010609535831.png)

然后输入 .\pip install 库名  
比如我要安装名字为“requests”的库  
就输入.\pip install requests  
然后等待安装完成就行了。

到此这篇关于如何在vscode中安装python库的方法步骤的文章就介绍到这了,更多相关vscode安装python库内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

