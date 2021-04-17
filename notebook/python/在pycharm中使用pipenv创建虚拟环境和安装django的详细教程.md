刚在网上查了一圈，好家伙，全都是那一篇文章，而且用的pycharm是老版本的，下边介绍的是pycharm2019专业版的，直接切入正题：

（1）打开 pycharm -> File文件 -> New Project 创建新项目

![](https://img.jbzj.com/file_images/article/202011/2020113014353279.png)

（2）选择Django项目

1、选择创建Django项目的本地路径（这里补充下，下边图应该没有后边的 \ , 必须要选择一个文件夹）。

2、选择Pipenv来创建虚拟环境。

3、Base interpreter 为本机系统的python解释器，也就是安装python时的路径。

4、Pipenv executable 表示pipenv命令的环境变量路径，就是是pipenv的安装目录。

5、输入项目中应用的名字，点击创建即可，pycharm会自动帮助你创建一个虚拟环境及Django的项目应用。

![](https://img.jbzj.com/file_images/article/202011/2020113014353280.png)

（3）以下是创建时pycharm创建项目截图

![](https://img.jbzj.com/file_images/article/202011/2020113014353281.png)

![](https://img.jbzj.com/file_images/article/202011/2020113014353282.png)

（4）下图是：创建完之后，在命令行中使用pipenv进入本项目的虚拟环境（使用cmd进入虚拟环境后，路径前边会有一个括号里边是虚拟环境文件的名字，说明你已经进入虚拟环境了；但使用powerShell没有前边的括号！），查看项目依赖及虚拟环境安装目录

![](https://img.jbzj.com/file_images/article/202011/2020113014353283.png)

（5）点击pycharm中的绿色小三角，运行项目：

![](https://img.jbzj.com/file_images/article/202011/2020113014353284.png)

成功：

![](https://img.jbzj.com/file_images/article/202011/2020113014353385.png)

到此这篇关于在pycharm中使用pipenv来创建虚拟环境和安装django的文章就介绍到这了,更多相关pycharm创建虚拟环境和安装django内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

