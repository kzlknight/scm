最近在使用Python处理MySQL数据库相关问题时，需要用到Python2.7.5及以上版本，而centos6.5等版本操作系统默认自带的版本为2.6.6，因此需要对python进行升级。

Python升级的步骤大致分为如下步骤：

  * 安装依赖包 
  * 下载安装包并上传至操作系统，下载路径 
  * 解压、编译、安装 
  * 配置相关路径下的python命令 
  * 修改yum启动路径 

**1. 安装依赖包**

# 编译时需要使用gcc，故需先检查并安装gcc

```python

    yum install gcc -y
```

**2. 下载安装包并上传至操作系统**

# 本次采用wget直接在linux系统下载。下载路径为python官网 [ https://www.python.org/ftp/python
](https://www.python.org/ftp/python) ，选择对应的版本，并下载

```python

    wget https://www.python.org/ftp/python/2.7.15/Python-2.7.15.tgz
```

**3. 解压、编译、安装**

# 解压

```python

    tar -zxvf Python-2.7.15.tgz
```

# 编译、安装

```python

    cd Python-2.7.15
    ./configure --prefix=/usr/local/python2.7
```

检查是否有错误，如无错误则继续

![](https://img.jbzj.com/file_images/article/202012/202012141411317.png)

```python

    make
    make install
```

# 查看安装结果

```python

    cd /usr/local/python2.7/bin
    ll
    ./python2　　　　　　　　　　 #运行本路径下的python2,或写全路径测试，否则为原版本的命令
    ./python2.7　　　　　　　　 #运行本路径下的python2,或写全路径测试，否则为原版本的命令  
```

![](https://img.jbzj.com/file_images/article/202012/202012141411318.png)

**4. 配置相关路径下的python命令**

# 查看python命令

```python

    whereis python
```

![](https://img.jbzj.com/file_images/article/202012/202012141411329.png)

# 拷贝命令，修改配置软链接，注意不能将python2.6版本的命令删除，因为yum不支持python2.7,后续修改yum命令时需要用到python2.6

```python

    cd /usr/bin
    ll *python*
    unlink python
    unlink python2
    ll *python*
    cp /usr/local/python2.7/bin/python2.7 /usr/bin/python2.7 #注意路径
    ln -s /usr/bin/python2.7 python　　　　　　
    ln -s python python2
    ll *python* python    #可以看到提示的Python2.7.15,证明安装成功，但是还没有彻底结束
```

**![](https://img.jbzj.com/file_images/article/202012/2020121414113210.png) **

**5.修改yum启动路径**

yum不兼容 Python 2.7，当把Python2.6.6升级成了Python2.7以后, yum将不能正常工作，因此需要指定 yum
的Python版本

# 升级后运行yum命令报错信息

> There was a problem importing one of the Python modules  
>  required to run yum. The error leading to this problem was:  
>  
>  No module named yum  
>  
>  Please install a package which provides this module, or  
>  verify that the module is installed correctly.  
>  
>  It's possible that the above module doesn't match the  
>  current version of Python, which is:  
>  2.7.15 (default, Jun 25 2018, 09:22:50)  
>  [GCC 4.4.7 20120313 (Red Hat 4.4.7-18)]  
>  
>  If you cannot solve this problem yourself, please go to  
>  the yum faq at:  
>  http://yum.baseurl.org/wiki/Faq

![](https://img.jbzj.com/file_images/article/202012/2020121414113211.png)

# 修改yum启动命令

```python

     vim /usr/bin/yum　　　　　　#将头部#!/usr/bin/python 修改为 #!/usr/bin/python2.6
```

![](https://img.jbzj.com/file_images/article/202012/2020121414113212.png)

# 修改后测试，如下表明已修改好，yum可以正常工作了

![](https://img.jbzj.com/file_images/article/202012/2020121414113213.png)

至此，python2.6.6升级为python2.7.15工作就完成了，运行python命令就相当于运行python2.7.15版本的Python，运行python2.6即使用python2.6.6版的python,如下所示：

![](https://img.jbzj.com/file_images/article/202012/2020121414113214.png)

到此这篇关于Python 2.6.6升级到Python2.7.15的过程详解的文章就介绍到这了,更多相关Python
2.6.6升级到Python2.7.15内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

