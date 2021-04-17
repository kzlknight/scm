###  前言

很多朋友在使用Jetbrains系列软件的时候，可能都会有一个问题，那就是鼠标右击出现的Open Folder as PyCharm
Project，有时候安装的时候没勾选，后期想加，或者是后期感觉没啥用，想删了，怎么操作呢？  
先说一下作者为啥喜欢用这一小右键菜单吧。因为我们打开pycharm软件，默认是打开近期最后一个使用的项目，那有时候我们临时起意要开其他的项目，那是不是得先打开我们的pycharm。  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020122910034521.png)  

然后先等我们的项目加载  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020122910034522.png)  

加载好了后，菜单 open 去选择我们要打开的项目  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020122910034523.png)  

要是最近的项目有点大 那可能加载时间就有些不够了，所以作者会比较喜欢这一功能Open Folder as PyCharm Project  
作者在安装的时候有勾选，前几天还有用着呢，也是很迷，刚才要打开项目的时候，它不在我的右击菜单中……

  * 计算机\HKEY_CLASSES_ROOT\Directory\Background\shell 
  * 作者先是在这添加，结果右击菜单后没有相应的菜单项 

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020122910034524.png)

心细的作者通过探索发现  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020122910034525.png)  

然后返回桌面，有了  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020122910034526.png)

###  具体操作步骤

打开我们的注册表管理器搜索  
计算机\HKEY_CLASSES_ROOT\Directory\Background\shell  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020122910034627.png)

选中shell，右击新建 项，命名都可以，作者是Pycharm  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020122910034628.png)

默认值 修改为我们右键菜单的文字内容  
![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020122910034629.png)

在右边区域右击新建字符串，这个是图标Icon 值为我们pycharm.exe的路径  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020122910034630.png)

选中pycharm项，新建项command  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020122910034631.png)

修改command的默认值，英文的"pycharm的路径" “%V”  
例： “C:\Program Files (x86)\PyCharm 2020.2\bin\pycharm64.exe” “%V”  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020122910034632.png)

###  注意

两个的shell都要设置好  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020122910034633.png)

###  怎么删除open foler as pycharm project  

首先你如果安装了xx管家那就比较方便

xx管家-->工具箱-->管理右键-->取消Open Folder as Pycharm Project-->确认

![](https://img.jbzj.com/file_images/article/202012/20201229101031560.png?20201129101051)

到此这篇关于详解Open Folder as PyCharm Project怎么添加的方法的文章就介绍到这了,更多相关PyCharm
Project添加内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

