一、Eclipse 的安装

Eclipse的安装是很容易的。Eclipse是基于java的一个应用程序，因此需要一个java的运行环境（JRE）才行。（我这里主要介绍windows下的安装）

JRE的下载地址：http://www.oracle.com/technetwork/java/javase/downloads/index.html

进入JRE的下载页面你会发现有很多的安装版本，在这里我选择安装 jre-7u3-windows-i586.exe，双击安装即可。

Eclipse的下载地址：http://www.eclipse.org/downloads/

  
2012年6月发布的Eclipse 4.2（朱诺）。建议适用于Eclipse 4.2的​​Java 6 JRE / JDK。

下载后，直接将压缩包解压缩到你想要安放的目录即可，比如放在：F：\Eclipse，这样即可使用Eclipse。

二、安装Python

python的下载地址：http://www.python.org/getit/

最新版本是：python 3.3.0

进入下载地址后，根据你的需求进行下载。在这里我下载的是：python-3.3.0.msi，下载完后直接点击安装即可。我的安装目录为：F:\files\python

然后配置系统环境：我的电脑 ―>属性―>高级―>环境变量―>系统变量

设置Path，将你的python的安装路径写入Path变量中即可。

三、安装PyDev插件

官方地址：http://pydev.org/index.html  
下载地址：http://sourceforge.net/projects/pydev/files/

Pydev是预先安装的Aptana Studio 3。

对于使用Django模板编辑器，Aptana Studio 3是必需的。

Aptana Studio 3如果PyDev中使用，它可以不被安装单独的或更新的（Aptana Studio 3必须始终被更新作为一个整体）

Eclipse插件（更新管理器URL）：http://download.aptana.com/studio3/plugin/install

直接在Eclipse中选择菜单：Help―Install New
Updates―And，输入http://download.aptana.com/studio3/plugin/install，下载并安装。

安装PyDev插件的两种安装方法：

1、将下载的PyDev解压（目前最新版本 PyDev 2.4.0.zip
压缩包），PyDev解压后一般包含Plugins和Feature文件夹，将PyDev解压后的文件夹拷贝到Eclipse解压后的目录下即可，完成后再启动Eclipse，可以在Eclipse菜单Help->About
Eclipse SDK->Installation Detail看到PyDev组件的安装。

2、直接在Eclipse中选择菜单：Help―Install New
Updates―And，输入http://pydev.org/updates，下载并安装。

四、Eclipse中的PyDev的配置

在Eclipse菜单Windows->Preferences->PyDev->Interpreter python配置你要只用的python解析器。

点击New按钮，从Python的安装路径下选择Python.exe。

