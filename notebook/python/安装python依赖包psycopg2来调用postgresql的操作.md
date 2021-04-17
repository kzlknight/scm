###  1、先安装psycopg2的依赖组件

本案例的操作系统为linux red hat

在安装python依赖包psycopg之前，你必须需要先安装postgresql数据库的相关组件：

postgresql-devel,postgresql,postgresql-libs这三个组件比较重要。另外，可选组件：postgresql-server

安装上述组件之前，可以用命令来查看你的系统现在是否已经安装了相关组件：

```python

    [root@dthost27 ~]# rpm -qa | grep PostgreSQL
```

如果都没有安装，则可执行命令如下：

```python

    [root@dthost27 ~]# yum install postgresql-devel
```

(安装过程中会顺带安装上postgresql和postgresql-libs组件)

###  2、安装psycopg2依赖包

保证依赖组件存在后，就可以使用pip命令安装了：

```python

    [root@dthost27 ~]# pip install psycopg2-binary
```

注：这里安装的是binary格式的psycopg2依赖包，其实安装psycopg2也可以，但是有时候执行pip install
psycopg2会报错，而安装psycopg2-binary（编译后）则不会

启动python测试

```python

    import psycopg2
```

**补充：安装psycopg2报错_解决方案**

报错信息

```python

    (python3-virtualenv) [root@vl-bg-anaylsis02 extract_log]# pip3 install psycopg2
    Collecting psycopg2
     Using cached psycopg2-2.8.4.tar.gz (377 kB)
      ERROR: Command errored out with exit status 1:
       command: /disk2/extract_log/python3-virtualenv/bin/python3 -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/tmp/pip-install-2d9wyu3k/psycopg2/setup.py'"'"'; __file__='"'"'/tmp/pip-install-2d9wyu3k/psycopg2/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /tmp/pip-install-2d9wyu3k/psycopg2/pip-egg-info
         cwd: /tmp/pip-install-2d9wyu3k/psycopg2/
      Complete output (23 lines):
      running egg_info
      creating /tmp/pip-install-2d9wyu3k/psycopg2/pip-egg-info/psycopg2.egg-info
      writing /tmp/pip-install-2d9wyu3k/psycopg2/pip-egg-info/psycopg2.egg-info/PKG-INFO
      writing dependency_links to /tmp/pip-install-2d9wyu3k/psycopg2/pip-egg-info/psycopg2.egg-info/dependency_links.txt
      writing top-level names to /tmp/pip-install-2d9wyu3k/psycopg2/pip-egg-info/psycopg2.egg-info/top_level.txt
      writing manifest file '/tmp/pip-install-2d9wyu3k/psycopg2/pip-egg-info/psycopg2.egg-info/SOURCES.txt'
    
      Error: pg_config executable not found.
    
      pg_config is required to build psycopg2 from source. Please add the directory
      containing pg_config to the $PATH or specify the full executable path with the
      option:
    
        python setup.py build_ext --pg-config /path/to/pg_config build ...
    
      or with the pg_config option in 'setup.cfg'.
    
      If you prefer to avoid building psycopg2 from source, please install the PyPI
      'psycopg2-binary' package instead.
    
      For further information please check the 'doc/src/install.rst' file (also at
      <http://initd.org/psycopg/docs/install.html>).
    
      ----------------------------------------
    ERROR: Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
    
```

###  解决方案 For ubuntu

```python

    sudo apt-get install libpq-dev python3-dev
```

###  解决方案 For Fedora/Centos

```python

    yum install -y postgresql10
    yum install postgresql-libs python3-devel postgresql-devel
    yum install gcc
```

以上为个人经验，希望能给大家一个参考，也希望大家多多支持脚本之家。如有错误或未考虑完全的地方，望不吝赐教。

