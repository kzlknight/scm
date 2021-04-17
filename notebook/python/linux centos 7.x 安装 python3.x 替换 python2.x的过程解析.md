![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020121416315439.png)

##  前言

一般而言，新的 centos 7.x 中自带的 python 都是 2.x 的版本。对于我们运行 python 软件支持并不友好，所以需要进行升级操作

下载 python3 的包之前，要先安装相关的依赖包，用于下载编译 python3：

```python

    yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make
```

##  安装 pip

默认的 centos7 是没有安装 pip，先添加 epel 扩展源

```python

    yum -y install epel-release
```

安装 pip

```python

    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

一般 centos7 系统都有自带的 python 2.x 的版本，所以直接使用 python 运行即可

```python

    python get-pip.py
```

pip 测试安装

```python

    pip -V
    
    # pip 版本展示如下
    pip 20.3.1 from /usr/local/python3/lib/python3.6/site-packages/pip (python 3.6)
```

##  安装 wget

安装 wget 命令如下

```python

    pip install wget
```

用 wget 下载 python3 的源码包，或者自己先下载好，上传到服务器再安装，如果网络快可以直接安装

```python

    wget https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tar.xz
```

##  编译 python 源码包

编译 python3 源码包，解压

```python

    xz -d Python-3.6.8.tar.xz
    tar -xf Python-3.6.8.tar
```

进入解压后的目录，依次执行下面命令进行手动编译

```python

    cd Python-3.6.8
    ./configure prefix=/usr/local/python3
```

如果执行报如下错误，是因为由于本机缺少 gcc 编译环境，如果不报错，直接执行下一步骤

```python

    configure: error: in `/root/Python-3.6.8':
    configure: error: no acceptable C compiler found in $PATH
    See `config.log' for more details
    
    
    # 执行命令
    yum install -y gcc
```

执行成功后，开始手动编译，时间稍等几分钟

```python

    make && make install
```

安装依赖 zlib、zlib-deve

```python

    yum install zlib zlib
    yum install zlib zlib-devel
```

最后没提示出错，就代表正确安装了，在/usr/local/目录下就会有 python3 目录

##  替换 python 软链接

添加软链接，将原来的链接备份，如果没有 python 软连接可以不执行

```python

    mv /usr/bin/python /usr/bin/python.bak
```

添加 python3 的软链接

```python

    ln -s /usr/local/python3/bin/python3.6 /usr/bin/python
```

测试是否安装成功了

```python

    python -V
    
    # python 版本展示
    Python 3.6.8
```

##  更新 yum 文件

而因为 yum 使用的是 python2，所以替换成为 python3 后可能会无法工作，因此还需要修改 yum 的配置文件

在此之前需要确认下，python 是否有 2.7 的版本

![](https://img.jbzj.com/file_images/article/202012/2020121416315440.png)

确认后就可以修改了

```python

    # 把文件头部的 #! /usr/bin/python 改成 #! /usr/bin/python2.7
    vi /usr/bin/yum
    # 把文件头部的 #! /usr/bin/python 改成 #! /usr/bin/python2.7
    vi /usr/libexec/urlgrabber-ext-down
    # 把文件头部的 #! /usr/bin/python 改成 #! /usr/bin/python2.7
    # 如果没有此文件，就不必修改
    vi /usr/bin/yum-config-manager
```

修改完成后可以下载个平时比较常用的 tree 组件

```python

    yum install tree -y
```

到此这篇关于linux centos 7.x 安装 python3.x 替换 python2.x的文章就介绍到这了,更多相关 python3.x 替换
python2.x内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

