###  背景

远程服务器是Ubuntu系统，操作中可以使用pycharm在windows或者Ubuntu系统上编辑代码并调试，但是首先需要professional版本的pycharm，community版本在Tool选项下找不到Deployment选项。  
区官网下载安装包，安装完成后激活。学生可在pycharm官网用域名为学校的邮箱注册账号，激活时登陆账号即可。

###  配置远程连接

打开 ` Tool ` -> ` Deployment- ` > ` Configuration ` ,  
点击 ` \+ ` -> ` SFTP `

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020122310160661.png)

自定义服务器名字，用来区别不同服务器。  
然后填写SSH 和人root path，root path可自动检测

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020122310160662.png)

填写映射，两个文件夹名字保持一致

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020122310160663.png)

完成后点击 ` OK `

###  添加python interpreter

这一步让pycharm告诉服务器用什么环境去执行你的代码  
打开 ` File ` -> ` Setting ` -> ` Project ` > ` python interpreter ` ,  
添加python interpreter，点击右上角螺母图标-> ` Add ` ,填写服务器地址和密码  
若不成功，尝试点击螺母图标-> ` Show All ` -> ` \+ ` 。总有一种能成功。  
使用conda虚拟环境下的python，在./conda的bin文件夹下，我的在/home/hl/.conda/envs/hlpy36/bin/python3.6  
Path mapping 一定要填写和上面提到的Development path一致的。

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020122310160664.png)

完成后点击 ` OK ` ，建议关闭自动上传，很烦。但是每次修改完代码后要点击 ` Tool ` -> ` Deployment- ` > ` upload
` 手动上传。

到此这篇关于pycharm远程连接服务器并配置python
interpreter的方法的文章就介绍到这了,更多相关pycharm远程连接服务器内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

