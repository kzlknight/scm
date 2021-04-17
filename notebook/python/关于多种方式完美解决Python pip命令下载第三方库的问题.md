###  写在前面

众所周知python拥有众多的第三方库，据不完全统计python有1w多个第三方库(为什么是不完全统计，因为我也记不清了☺)，那既然有这么多的库，那么不可避免的就是我们要去下载他。但对我们这些国内用户的话，有时候用pip命令安装库的话速度实属龟速，下面介绍几个提速的方法，对你有用的话别忘了点赞关注+收藏哦~

> 另外最近发现总有人搬运我的文章，并且不加原文链接，这里我郑重声明一下，本人目前仅在CSDN这一个平台发布文章，其他小伙伴如果想转载
> 或者引用请注明引用来源，未经许可不得直接搬运，请尊重创作人的劳动成果，谢谢！(唉，我这么一个小菜鸡居然还有人搬运，还望搬运大佬手下留情~)**

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020122110072322.gif)

###  一、临时提速

国内的主要镜像地址如下：

清华：https://pypi.tuna.tsinghua.edu.cn/simple

阿里云：http://mirrors.aliyun.com/pypi/simple/

中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/

华中理工大学：http://pypi.hustunique.com/

山东理工大学：http://pypi.sdutlinux.org/

豆瓣：http://pypi.douban.com/simple/

**使用方法如下：**

pip install -i 国内镜像地址 包名

例如： pip install -i https://mirrors.aliyun.com/pypi/simple/ requests

注：新版ubuntu要求使用https源

###  二、永久提速

每次临时复制镜像地址放在后面也挺麻烦的，所以接下来介绍永久提速的方法。做一下简单的配置即可完成。

(一) Windows系统配置 在 C:\Users\Administrator\pip 建一个文件 pip.ini，如果Administrator
中没有pip文件夹则自己新建一个，然后新建一个 pip.ini 文件。在 pip.ini 文件输入：

```python

    [global]
    index-url = https://pypi.douban.com/simple
    
    [install]
    trusted-host = pypi.douban.com
```

使用记事本默认的ANSI编码格式复制上面的文本粘贴即可，最后将.txt的后缀去掉，效果如图：

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020122110072423.png)

在command中测试：win+r输入cmd进入控制台输入命令 ` pqi ls ` ，没有安装pqi模块的可以用 ` pip install pqi `
命令安装一下，安装后输入命令，效果如下：

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020122110072424.png)

显示出了可用的镜像源，然后输入 ` pqi show ` 命令可以查看我们当前使用的镜像源

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020122110072425.png)

可以看到我们已经将镜像源更改为豆瓣了，所有步骤到结束，大家可以动手试试哦，如果遇到任何问题欢迎评论区留言或者私信我呦~

(二) Mac 和 Linux 配置

  * 打开terminal 
  * 输入命令： 

```python

    mkdir .pip
    vim .pip/pip.conf
```

（这两步是在home目录下新建文件: .pip/pip.conf）

3.按 i 键进入输入模式，在这个文件中复制粘贴写入如下内容：

```python

     [global］
    index-url = https://pypi.doubanio.com/simple/
    timeout = 1000
    【install】
    use-mirrors = true
    mirrors = https://pypi.doubanio.com//
```

按ESC退出插入模式后，直接输入 :wq 回车，这样就会保存并退出刚才创建的文件和输入的内容了。

以上就是所有的配置方式啦，小伙伴们还在等什么赶紧去下载一个库试试吧，以前十几分钟才能下载完的，现在只需三秒喔~

到此这篇关于多种方式完美解决pip命令下载第三方库的问题的文章就介绍到这了,更多相关pip命令下载第三方库内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

