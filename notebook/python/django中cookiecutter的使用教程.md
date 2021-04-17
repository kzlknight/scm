##  一、安装  

导入： ` pipenv install cookiecutter `

问题：在导入的过程中可能会报错：  

> pkg_resources.VersionConflict: (importlib-metadata 3.1.0
> (/Users/apple/.local/share/virtualenvs/testProject-h0hp04R9/lib/python3.6/site-
> packages), Requirement.parse('importlib-metadata<2,>=0.12; python_version <
> "3.8"'))。  
>

原因及解决：这个问题的出现主要是pipenv版本不支持，需要更新pipenv，使用命令：pip3 install -U pipenv，然后重新导入即可。

##  二、创建项目  

运行cookiecutter

问题：直接报错 ` zsh: command not found: cookiecutter `

解决办法：使用pipenv --py获取python环境的安装目录，在该目录下运行cookiecutter

运行之后会继续报错：缺少Template

```python

    Usage: cookiecutter [OPTIONS] TEMPLATE [EXTRA_CONTEXT]...
    Try 'cookiecutter -h' for help.
    Error: Missing argument 'TEMPLATE'.
    
```

在github中找到pydanny/cookiecutter-django，赋值github地址，把地址写在python运行环境的后边，再次运行

```python

    /Users/apple/.local/sha~~~~re/virtualenvs/testProject-h0hp04R9/bin/cookiecutter https://github.com/pydanny/cookiecutter-django.git
    
```

成功进入配置选项，进行具体的配置

##  三、具体配置  

  * project_name：项目名字 
  * project_slug：默认和项目的名字保持一直，不必填写 
  * description：项目的简单描述 
  * author_name：作者的名称，格式 名字 
  * domain_name：网站域名 
  * eamil：邮箱 
  * version [0.1.0] Select open_source_license: 选择是否开源类型 
  * timezone：时区设置，Asia/Shanghai 
  * windows：是否使用的是windows系统开发 
  * use_pycharm：是否使用pycharm 
  * use_docker：是否使用docker 
  * Select postgresql_version：选择postgresql的版本，默认为最新版，并且默认没有继承Mysql~~~~ 
  * Select js_task_runner：js的运行器，使用默认的 
  * Select cloud_provider：默认 
  * Select mail_service：选择email的服务 
  * use_async：是否使用异步编程 
  * use_drf：是否使用django rest_framework，前后端分离的话选择y 
  * custom_bootstrap_compilation：是否自定义bootstrap压缩 
  * use_compressor：用于压缩js、css的技术，需要选择y 
  * use_celery：是否使用celery，使用选择y 
  * use_mailhog：第三方的邮件发送服务 
  * use_sentry：是否使用错误日志监控 
  * use_whitenoise：用于部署静态文件的，带有文件压缩功能 
  * use_heroku：国外有名的pass平台，如果要部署到上边的话选择y会自动生成对应的配置 
  * Select ci_tool：选择工具(None/Travis/Gitlab/Github） 
  * keep_local_envs_in_vcs：是否在本地环境变量中使用版本配置，选择y 
  * debug：是否使用debug，选择y   

##  四、问题：  

项目在进行数据迁移的时候可能会报错：

```python

     File "/Users/apple/.local/share/virtualenvs/django-pro-7n8-wfJY/lib/python3.6/site-packages/django_celery_beat/models.py", line 60, in crontab_schedule_celery_timezone
     choice[0].zone for choice in timezone_field.TimeZoneField.CHOICES
    AttributeError: type object 'TimeZoneField' has no attribute 'CHOICES'
    
```

原因：django-celery-beat setup.py有一个https://github.com/celery/django-celery-
beat/blob/master/requirements/default.txt依赖要求，强制django-timezone-
field只能使用>=4.0和<5.0版本的，开发者推送了一个4.1.1版本的django-timezone-field，中断了数据迁移过程。

解决办法：pipenv install django-timezone-field==4.0，重新执行数据迁移就可以了

##  总结

到此这篇关于django中cookiecutter使用教程的文章就介绍到这了,更多相关django中cookiecutter使用内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

