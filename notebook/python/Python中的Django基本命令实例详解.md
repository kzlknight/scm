**一、新建项目**

` $django-admin.py startproject project_name `

# 特别是在 windows 上，如果报错，尝试用 django-admin 代替 django-admin.py 试试

注意 project_name 是自己的项目名称，需要为合法的 Python 包名，如不能为 1a 或 a-b。

**二、新建APP**

要先进入项目目录下，cd project_name 然后执行下面的命令；  
$ python manage.py startapp app_name  
或 django-admin.py startapp app_name

一般一个项目有多个app，当然通用的app也可以在多个项目中使用。  
与项目名类似app name也需要为合法的Python 包名，如blog,news,aboutus等都是合法的app名称；

**三、创建数据库表或更改数据表或字段**

Django 1.7.1及以上 用以下命令  

```python

    # 1. 创建更改的文件
    $python manage.py makemigrations
    # 2. 将生成的py文件应用到数据库
    $python manage.py migrate
```

  

旧版本的Django 1.6及以下用

` $python manage.py syncdb `

这种方法可以在SQL等数据库中创建与models.py代码对应的表，不需要自己手动执行SQL

**四、使用开发服务器**

开发服务器，即开发时使用，一般修改代码后会自动重启，方便调试和开发，但是由于性能问题，建议只用来测试，不要用在生产环境。  

```python

    $python manage.py runserver
     # 当提示端口被占用的时候，可以用其它端口：
    $python manage.py runserver 8001
    $python manage.py runserver 9999
    （当然也可以kill掉占用端口的进程，具体后面有讲，此处想知道的同学可查下 lsof 命令用法）
    # 监听机器所有可用 ip （电脑可能有多个内网ip或多个外网ip）
    $python manage.py runserver 0.0.0.0:8000
    # 如果是外网或者局域网电脑上可以用其它电脑查看开发服务器
    # 访问对应的 ip加端口，比如 http://172.16.20.2:8000
```

**五、清空数据库**

` $python manage.py flush `

此命令会询问是yes or no，选择yes会把数据全部清空掉，只留下空表

**六、创建超级管理员**

```python

    $python manage.py createsuperuser
    # 按照提示输入用户名和对应的密码就好了邮箱可以留空，用户名密码必填
    # 修改 用户密码可以用：
    $python manage.py changepassword username
```

**七、导出数据，导入数据**

```python

    $python manage.py dumpdata appname > appname.json
    $python manage.py loaddata appname.json
```

**八、Django 项目环境终端**

` $python manage.py shell `

如果你安装了 bpython 或 ipython 会自动用它们的界面，推荐安装 bpython。

这个命令和 直接运行 python 或 bpython 进入 shell 的区别是：你可以在这个 shell 里面调用当前项目的 models.py 中的
API，对于操作数据，还有一些小测试非常方便。

**九、数据库命令行**

` $python manage.py dbshell `

Django 会自动进入在settings.py中设置的数据库，如果是 MySQL 或 postgreSQL,会要求输入数据库用户密码。

在这个终端可以执行数据库的SQL语句。如果您对SQL比较熟悉，可能喜欢这种方式。

**十、更多命令**

```python

     mysite python3.6 manage.py
    Type 'manage.py help <subcommand>' for help on a specific subcommand.
    Available subcommands:
    [auth]
      changepassword
      createsuperuser
    [contenttypes]
      remove_stale_contenttypes
    [django]
      check
      compilemessages
      createcachetable
      dbshell
      diffsettings
      dumpdata
      flush
      inspectdb
      loaddata
      makemessages
      makemigrations
      migrate
      sendtestemail
      shell
      showmigrations
      sqlflush
      sqlmigrate
      sqlsequencereset
      squashmigrations
      startapp
      startproject
      test
      testserver
    [sessions]
      clearsessions
    [staticfiles]
      collectstatic
      findstatic
      runserver
```

**总结**

以上所述是小编给大家介绍的Python中的Django基本命令实例详解，希望对大家有所帮助，如果大家有任何疑问欢迎给我留言，小编会及时回复大家的！

