本文示例环境：CentOS 7，远程服务器  
可能的依赖：python; pip； python-devel; gcc; gcc-c++;

###  一、安装（命令行操作） 如果没有pip，要安装pip：

安装 setuptools

```python

    cd /tmp
    wget https://pypi.python.org/packages/69/56/f0f52281b5175e3d9ca8623dadbc3b684e66350ea9e0006736194b265e99/setuptools-38.2.4.zip#md5=e8e05d4f8162c9341e1089c80f742f64  # 具体下载地址可能变更，请参见官网：https://pypi.python.org/pypi/setuptools#downloads
    unzip setuptools-38.2.4.zip # 我下载的是 .zip 源码，所以用 unzip 解压
    cd setuptools-38.2.4/
    python setup.py install
```

再安装 pip

```python

    cd /tmp
    wget https://pypi.python.org/packages/11/b6/abcb525026a4be042b486df43905d6893fb04f05aac21c32c638e939e447/pip-9.0.1.tar.gz#md5=35f01da33009719497f01a4ba69d63c9  # 同样，具体下载地址参考：https://pypi.python.org/pypi/pip#downloads
    tar zxvf pip-9.0.1.tar.gz # 解压
    cd pip-9.0.1/
    python setup.py install
```

###  安装 jupyter notebook

如果想用 python2：

```python

    python -m pip install --upgrade pip
    python -m pip install jupyter
```

如果报错：

> ………………………………  
>  error: command 'gcc' failed with exit status 1

试试:

```python

    sudo yum install gcc gcc-c++ python-devel
```

再运行

如果想用 python3：

```python

    python3 -m pip install --upgrade pip
    python3 -m pip install jupyter
```

###  安装完测试一下好不好用：

**若jupyter 部署在远程服务器上，服务器防火墙开启时，端口可能不能访问，所以加一步端口开放**

```python

    firewall-cmd --zone=public --add-port=8888/tcp --permanent
    success  
    systemctl restart firewalld.service 
```

**注意：如果是腾讯云等云服务器，可能需要上官网管理平台，手动配置安全组开放端口才行**  
然后启动 jupyter

```python

    jupyter notebook --ip=*  # root下换成：jupyter notebook --ip=* --allow-root
```

命令行显示：  

![jupyter notebook
正常启动的示意图](https://img.jbzj.com/file_images/article/202101/2021010611374497.png)

打开浏览器，输入url: localhost:8888，回车，浏览器显示：  
**注意：在远程服务器上部署jupyter的要把 localhost 改成对应的 ip 地址**

![token登录界面](https://img.jbzj.com/file_images/article/202101/2021010611374498.png)

让你用token登录，把上面命令行反馈的 token （倒数第二行）复制过来输入，登录成功：

![token登录成功](https://img.jbzj.com/file_images/article/202101/2021010611374499.png)

###  二、配置

上述步骤创建的 jupyter notebook 是临时性的，没有配置密码、SSL、工作目录等等，不方便也不安全。下面为需要的用户建立专属的配置。

**注意** ：下文中的例子在 root 账户下进行，建议实际不要用 root 用户。

###  配置文件生成

如果服务器上你的账户下已有默认 jupyter 用户（的配置文件），可以直接拷贝一份，改个名字，比如：

```python

    cd /root/.jupyter
    cp jupyter_notebook_config.py jupyter_my_config.py
```

或者，直接自己找个任意目录，比如 /root/my_configs，直接创建一个新文件作为配置文件（反正就是个文本文件，放哪里都行）：

```python

    mkdir /root/my_configs
    cd /root/my_configs
    touch jupyter_notebook_config.py
```

再或者，账户下未建立默认 jupyter 配置文件的情况下，可以自动生成：

```python

    jupyter notebook --generate-config
```

![生成了配置文件](https://img.jbzj.com/file_images/article/202101/20210106113744100.png)  

现在假设我们的配置文件是用最后一种方式创建的，我们进入目录看看

```python

    [root@VM_157_11_centos ~]# cd /root/.jupyter/
    [root@VM_157_11_centos .jupyter]# ls
    jupyter_notebook_config.py
    [root@VM_157_11_centos .jupyter]# 
```

###  配置文件编辑

打开 jupyter_notebook_config.py 文件：

```python

    vim jupyter_notebook_config.py
```

可以看到全是注释的配置说明，比较复杂，也不是都用得上，这里我们自己写一些重要的配置即可，在文件开头写入：

```python

    c = get_config()
    c.IPKernelApp.pylab = "inline"
    c.NotebookApp.ip = "*"
    c.NotebookAPp.open_browser = False
    c.NotebookApp.password = 'sha1:b39d2445079f:9b9ab99f65150e113265cb99a841a6403aa52647'
    c.NotebookApp.certfile = u'/root/.jupyter/mycert.pem'
    c.NotebookApp.port= 8888
    c.NotebookApp.notebook_dir = "/root/ipython"
```

**注意1** ：第五行 password 填入的是<登录密码的 sha1 加密版>，通过以下方式生成：

```python

    [root@VM_157_11_centos .jupyter]# python
    Python 2.7.5 (default, Aug 4 2017, 00:39:18) 
    [GCC 4.8.5 20150623 (Red Hat 4.8.5-16)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from IPython.lib import passwd
    >>> passwd()
    Enter password: 
    Verify password: 
    'sha1:175e8efe8974:eacef02a2e3f959d6efdf6c93d142c7f4712f5cc'
    >>> exit()
    [root@VM_157_11_centos .jupyter]# 
```

**注意2** ：第六行的 certfile 证书文件可以通过下面这行命令生成（中间的交互信息可以随便填），注意路径要对应上：

```python

    openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout mycert.pem -out mycert.pem
```

**注意3** ：第七行的 port 应该是一个未被占用的、被防火墙允许的端口（在上面的步骤我们已经打开了 8888
端口），这里再强调一遍（同样的，腾讯云等服务器需要在官网修改安全策略）：

```python

    firewall-cmd --zone=public --add-port=8888/tcp --permanent
    success  # 系统反馈信息
    systemctl restart firewalld.service 
```

**注意4** ：第八行的 notebook_dir 是你的文档目录，需要自行选择并创建（否则运行时会报错）：

```python

    mkdir /root/ipython
```

运行

```python

    [root@VM_157_11_centos .jupyter]# jupyter notebook --config jupyter_notebook_config.py --allow-root
    [I 19:58:54.278 NotebookApp] Serving notebooks from local directory: /root/ipython
    [I 19:58:54.279 NotebookApp] 0 active kernels
    [I 19:58:54.279 NotebookApp] The Jupyter Notebook is running at:
    [I 19:58:54.279 NotebookApp] https://[all ip addresses on your system]:8888/
    [I 19:58:54.279 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
    [W 19:58:54.279 NotebookApp] No web browser found: could not locate runnable browser.
```

**关于参数**

