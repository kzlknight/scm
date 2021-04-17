apk换源

```python

    sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories
```

安装Python的构建环境

```python

    apk add --no-cache --virtual build-dependencies \
    python3-dev \
    libffi-dev \
    openssl-dev \
    gcc \
    libc-dev \
    make
```

安装Python依赖包 ` ImportError: cannot import name 'Feature' from 'setuptools' `

```python

    pip install --upgrade pip setuptools==45.2.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
```

` ModuleNotFoundError: No module named 'Cython' `

```python

    pip install cython -i https://pypi.tuna.tsinghua.edu.cn/simple
```

**pymssql安装不上**

` command 'gcc' failed with exit status 1 `

后面发现是漏装了一个环境 ` freetds-dev `  
重新安装之后，就能成功安装依赖了

` apk add freetds-dev `

注意的是，依赖成功安装之后，如果为了docker镜像大小，卸载了 ` freetds-dev ` 这个环境包，会导致访问数据库的时候报错 `
libsybdb.so.5: cannot open shared object file: No such file or directory `

**grpcio安装不上**

和上面一样，漏了环境 ` build-base linux-headers `

执行 ` apk add build-base linux-headers ` 之后，就能成功安装

**Pillow安装不上**

和上面一样，漏了环境 ` jpeg-dev zlib-dev `

执行 ` apk add jpeg-dev zlib-dev ` 之后，就能成功安装

最后卸载依赖

```python

    apk del build-dependencies
```

到此这篇关于Alpine安装Python3依赖出现的问题及解决方法的文章就介绍到这了,更多相关Alpine安装Python3依赖内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

