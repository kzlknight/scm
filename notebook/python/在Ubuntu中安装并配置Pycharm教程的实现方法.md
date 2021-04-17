###  软件介绍

PyCharm
是一款功能强大的Python编辑器，可以跨平台在Windows、Mac、Ubuntu上运行。本文介绍了在Ubuntu上安装PyCharm的方法，Ubuntu版本是20.04，以2020.2.3版本的PyCharm为例。

首先我们进入 [ PyCharm官网 ](https://www.jetbrains.com/pycharm/) 。  
点击Download下载自己所需的版本即可。  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010611302381.png)  

JetBrains公司分别针对不同的用户需求提供了专业版和社区版Pycharm。他们各自拥有的功能如下：

![](https://img.jbzj.com/file_images/article/202101/2021010611302382.png)  

相比较的话，Pycharm专业版增加了Web开发、Python Web框架、Python分析器、远程开发、支持数据库与SQL等更多高级功能。  
一般建议选择Community社区版，用作学习是没有问题的。  
而如果想要安装使用其他版本的Pycharm，只需在下载页面点击“Other versions”即可选择适合自己的版本。  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010611302383.png)

###  下载、启动和配置

下载时候点击Download，保存到本地磁盘即可（这里以pycharm-community-2020.2.3为例）。

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010611302484.png)

保存完毕进行解压缩，解压缩完成之后就可以启动使用。

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010611302485.png)  

但出于统一管理安装软件的考虑，可以将软件移动到opt目录下(opt文件夹可以用来存放下载的文件)，在终端输入

```python

    sudo mv pycharm-community-2020.2.3/ /opt/
```

当然“pycharm-community-2020.2.3”部分可以根据自己安装的版本不同进行更改，之后输入密码进行确认即可。

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010611302486.png)  

文件夹移动之后就可以启动软件进行使用了，首先在终端进入pycharm的bin文件夹

```python

    cd /opt/pycharm-community-2020.2.3/bin
```

然后启动pycharm等待即可。

```python

    ./pycharm.sh
```

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010611302487.png)  

紧接着就可以看到Pycharm的启动界面。  
**注意：目前发现Ubuntu中搜狗输入法和Pycharm存在冲突，当Ubuntu所用输入法为搜狗时，启动Pycharm之后一直卡在加载页面无法出现下图的启动成功页面。**

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010611302488.png)  

软件安装完成之后，就可以配置Python
Interpreter也就是Python的解释器了。在启动页面点击Configure，选中Settings进入设置。  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010611302589.png)  

在设置页面选中“Python Interpreter”选项，然后点击右侧齿轮形状按钮。

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010611302590.png)  

选择Add添加Python解释器。

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010611302591.png)  

然后再弹出的Add Python Interpreter对话框中选择Conda
Environment(当然前提是已经利用Anaconda安装了Python)，选择Existing
environment，在自己的虚拟环境文件目录下的bin文件夹中找到python即可，然后点击OK选定默认解释器。

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010611302692.png)  

进行应用即可。

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010611302693.png)  

到这里，Pycharm的安装就已经基本完成了。

###  创建快捷方式

但是由于Pycharm配置完成之后并没有出现类似windows的快捷方式，启动程序都需要在终端中键入命令相对比较麻烦，所以可以在配置好Python解释器之后，在启动页面点击Configure，选中Create
Desktop Entry，并在弹出的对话框中勾选for all users即可生成快捷方式。

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010611302794.png)

###  PyCharm的卸载

上文已经提到所有的程序相关文件都保存在了 /opt/pycharm-community-2020.2.3/ 目录下。  
而配置信息文件是在home下的.config/JetBrains/PyCharm×目录中，缓存文件是在home下的.cache/JetBrains/PyCharm×目录中。（例：PyCharmCE2020.2）

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010611302795.png)  

安装完成之后生成的快捷方式通常是保存在 /usr/share/applications 目录下。

所以卸载PyCharm时，分别在终端执行以下命令

```python

    # 删除程序相关文件
    sudo rm -r /opt/pycharm-community-2020.2.3/
    # 删除配置信息相关文件
    rm -r ~/.config/JetBrains/PyCharmCE2020.2
    # 删除缓存文件
    rm -r ~/.cache/JetBrains/PyCharmCE2020.2
    # 删除快捷方式
    sudo rm /usr/share/applications/jetbrains-pycharm-ce.desktop
```

删除配置信息和缓存文件之后如图

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010611302796.png)  

至此软件在Ubuntu中的安装、配置和卸载已经介绍完毕。欢迎在评论区讨论，如果对你有帮助，记得点赞哟！  
**注：文中包括文件夹名等命令操作都可根据自己的实际情况进行调整。**

到此这篇关于在Ubuntu中安装并配置Pycharm教程的实现方法的文章就介绍到这了,更多相关Ubuntu安装配置Pycharm内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

