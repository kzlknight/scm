1、开发环境运行项目

```python

    python mange.py runserver 0.0.0.0:8000
```

2、使用gunicorn在生产环境部署

Gunicorn“绿色独角兽”是一个被广泛使用的高性能的Python WSGI UNIX HTTP服务器

```python

    pip install gunicorn
    gunicorn -w 2 -b 0.0.0.0:8000 project_django.wsgi
```

常用参数：

> -c 指定一个配置文件(py文件)  
>  -b 与指定的socket进行绑定  
>  -D 以守护进程形式来运行Gunicorn进程，其实就是将这个服务放到后台去运行  
>  -w 工作的进程数量;  
>  -k 工作进程类型，sync（默认）, eventlet, gevent, or tornado, gthread, gaiohttp.  
>  http://docs.gunicorn.org/en/latest/settings.html

3、其它：使用gunicorn部署django项目时，发现静态文件加载失败问题

在项目project_django/urls.py中更改如下即可搞定：

```python

    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
     
    urlpatterns = [
      url('^admin/', admin.site.urls),
    ]
    urlpatterns += staticfiles_urlpatterns()
```

到此这篇关于使用gunicorn部署django项目的文章就介绍到这了,更多相关gunicorn部署django项目内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

