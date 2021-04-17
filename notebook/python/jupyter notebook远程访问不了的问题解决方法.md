jupyter notebook非常方便，想在服务器上面搭建一个，但是访问不了。

###  （一）首先是安装jupyter notebook，

```python

    pip install jupyter
```

如果pip安装报错，缺少sqlite的库，那么请安装

```python

    sudo apt-get install libsqlite3-dev
```

然后需要 **“重新编译python”，** 再通过pip安装（python3.x则不需要安装pysqlite）

```python

    pip install pysqlite
```

###  （二）启动jupyter

```python

    jupyter notebook
```

其实这时候，local如果有browser的话，就可以输入访问了，但是没有，所以需要远程访问： http://ip:8888，发现访问不了

###  （三）配置远程访问jupyter

1）首先输入ipython生成秘钥

```python

    $ ipython
    from notebook.auth import passwd
    passwd()
```

设定一个密码，会生成一个sha1的秘钥，如下图：

![](https://img.jbzj.com/file_images/article/202101/202101110840111.png)

2）生成jupyter的config文件

```python

    $ jupyter notebook --generate-config
```

这时候会生成配置文件，在 ~/.jupyter/jupyter_notebook_config.py

3）修改配置文件：~/.jupyter/jupyter_notebook_config.py

```python

    $vim ~/.jupyter/jupyter_notebook_config.py
```

加入如下内容，其中sha1那一串秘钥是上面生成的那一串

```python

    c.NotebookApp.ip='*'
    c.NotebookApp.password = u'sha1:f9030dd55bce:75fd7bbaba41be6ff5ac2e811b62354ab55b1f63'
    c.NotebookApp.open_browser = False
    c.NotebookApp.port =8888
```

如图：

![](https://img.jbzj.com/file_images/article/202101/202101110840122.png)

保存退出。

4）启动jupyter

```python

    $jupyter notebook
```

![](https://img.jbzj.com/file_images/article/202101/202101110840123.png)

在远程电脑上，打开浏览器，输入： ` http://your-server-ip:8888 `  

![](https://img.jbzj.com/file_images/article/202101/202101110840124.png)

需要输入密码，就是上面设置的那个密码，输入即可

![](https://img.jbzj.com/file_images/article/202101/202101110840125.png)

到此这篇关于jupyter notebook远程访问不了的问题解决方法的文章就介绍到这了,更多相关jupyter
notebook远程访问内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

