###  问题  

Jupyter Notebook可以说是非常好用的小工具，但是不经过配置只能够在本机访问  
笔者参阅了文档对jupyter notebook进行配置，实现了跨主机浏览器访问

###  安装jupyter notebook  

笔者使用conda包管理

```python

    conda install jupyter notebook
    
```

###  生成默认配置文件  

```python

    jupyter notebook --generate-config
    
```

将会在用户主目录下生成.jupyter文件夹，其中jupyter_notebook_config.py就是刚刚生成的配置文件

###  生成秘钥  

输入 ipython，进入ipyhon命令行  
输入

```python

    In [1]: from notebook.auth import passwd
    
    In [2]: passwd()
    
    
```

这里要求你输入以后登录使用的密码，然后生成一个秘钥，记得保存好秘钥，以免丢失。

```python

    Enter password: 
    Verify password: 
    Out[2]: 'sha1:1b4ea9662b35:3e3d6a823d264d466f125a0939623c05e7b66007'
    
```

###  修改配置文件  

修改用户主目录下~/.jupyter/jupyter_notebook_config.py文件  
取消c.NotebookApp.password = ''"注释，并将生成的秘钥复制进去

```python

    c.NotebookApp.password = 'sha1:1b4ea9662b35:3e3d6a823d264d466f125a0939623c05e7b66007'
    
```

取消下面几项注释，并注释修改ip、端口、不自动打开浏览器

```python

    c.NotebookApp.ip='*'#×允许任何ip访问
    c.NotebookApp.open_browser = False
    c.NotebookApp.port =8888 #可自行指定一个端口, 访问时使用该端口
    
```

如果是比较老的jupyter notebook版本还会有 allow_remote_access之类的一个设置，记得改成True并取消注释。  
大功告成

###  测试  

在服务器开启jupyter notebook

  * 浏览器不会自动开启 
  * 其他电脑在浏览器输入服务器ip：8888，能够访问jupyter notebook 

例，我服务器ip 192.168.199.219，笔记本ip 192.168.199.166  
服务器输入  

```python

    jupyter notebook
```

有如下提示

> (tf1.12) [ yep@yepdlpc:~$ ](mailto:yep@yepdlpc:~$) jupyter notebook  
>  [I 00:10:58.671 NotebookApp] Writing notebook server cookie secret to
> /run/user/1000/jupyter/notebook_cookie_secret  
>  [W 00:10:58.992 NotebookApp] WARNING: The notebook server is listening on
> all IP addresses and not using encryption. This is not recommended.  
>  [I 00:10:58.998 NotebookApp] Serving notebooks from local directory:
> /home/yep  
>  [I 00:10:58.998 NotebookApp] 0 active kernels  
>  [I 00:10:58.998 NotebookApp] The Jupyter Notebook is running at: [
> http://[all ](http://\[all) ip addresses on your system]:8888/  
>  [I 00:10:58.998 NotebookApp] Use Control-C to stop this server and shut
> down all kernels (twice to skip confirmation).  
>

在笔记本浏览器输入192.168.199.219:8888.  
成功远程访问服务器的jupyter notebook  

![](https://img.jbzj.com/file_images/article/202101/202111185523221.jpg?202101185538)

###  后记  

输入密码，接可以愉快的在笔记本写代码，在服务器跑代码啦  
可以在jupyter开terminal，连ssh登陆都省了～～  
不过如果服务器shell关闭后就无法访问了，可以在服务器后台运行jupyter notebook来避免这一问题

```python

    nohup jupyter notebook&
    
```

这样shell关闭也不会有问题啦

![](https://img.jbzj.com/file_images/article/202101/202111185556135.jpg?202101185614)

到此这篇关于Jupyter Notebook 远程访问配置详解的文章就介绍到这了,更多相关Jupyter Notebook
远程访问内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

