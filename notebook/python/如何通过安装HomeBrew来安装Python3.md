首先说什么是HomeBrew？

Homebrew是一款Mac
OS平台下的软件包管理工具，拥有安装、卸载、更新、查看、搜索等很多实用的功能。简单的一条指令，就可以实现包管理，而不用你关心各种依赖和文件路径的情况，十分方便快捷。

###  为什么要使用Homebrew

Mac OS X是基于Unix的，它可以使用非常多Linux平台上开源的优秀工具，比如wget，比如dos2unix脚本工具等。  
但是OS X系统本身却缺少Linux下得包管理器。比如Fedora的yum与dnf，比如Ubuntu的apt-
get，比如ArchLinux的Pacman等。  
于是这些优秀的开源软件在Mac上的安装只能通过下载源码，编译，安装，配置环境变量的步骤来完成安装。对于大部分的软件，在安装过程中是需要很多的依赖库的，手动去解决这些依赖库是十分痛苦的事情。包管理器干的就是这样的事情：解决软件安装过程中的依赖关系。  
有一个开源的项目叫Homebrew，完美解决了Mac OS X上没有包管理器的尴尬。

百度HomeBrew可以发现以下两条链接：

[ _Homebrew_ ― The missing package manager for macOS
](http://www.baidu.com/link?url=cGS7CBAWpmb_MzAh_UBFpJGAuDCNBVeZVnEh2LSBTdK&wd=&eqid=a348a5ee0002f425000000065872f63c)

[ _Homebrew_ ― macOS 不可或缺的套件管理器
](http://www.baidu.com/link?url=2pq_dOZecD7w1ZPGXBSthZO_4wFX9Au0i1mWsGGaB8pLY0c8Ioxp6rE3sC8Mea_u&wd=&eqid=a348a5ee0002f425000000065872f63c)

点击链接会跳转到HomeBrew的官网，

打开终端窗口，输入以下命令

```python

    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

即可成功安装HomeBrew。

可能到现在你还不知道到底HomeBrew有什么用，那我们用它安装一下Python，因为我的Mac
OS系统是10.12的，所以我要安装3.X的python版本。

在终端输入以下命令：

```python

    brew install python3
```

就可以轻松easy安装python了，安装完成后提示

![](https://img.jbzj.com/file_images/article/202012/2020122309532541.png)

大意就是：python安装完成，具体路径是：/usr/local/Cellar/python3/3.6.0，可以在finder中前往，

并通过以下命令把软件链接到LaunchPad中，也就是应用程序里。

试一下：

```python

    brew linkapps python3
```

完成后提示：

![](https://img.jbzj.com/file_images/article/202012/2020122309532542.png)

再一看launchPad果然多了两个APP，

![](https://img.jbzj.com/file_images/article/202012/2020122309532543.png)

到此这篇关于如何通过安装HomeBrew来安装Python3的文章就介绍到这了,更多相关HomeBrew安装Python3内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

