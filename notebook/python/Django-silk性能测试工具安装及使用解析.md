**介绍**  

Silk是Django框架的实时分析和检查工具。  

源代码名称:django-silk  

源代码网址: [ http://www.github.com/jazzband/django-silk
](http://www.github.com/jazzband/django-silk)  

**快速开始  
**

1、安装pip install django-silk

2、配置 setting.py

> INSTALLED_APPS = (  
>  ...  
>  'silk'  
>  )  
>

> MIDDLEWARE = [  
>  ...  
>  'silk.middleware.SilkyMiddleware',  
>  ...  
>  ]  
>

3、urls.py

urlpatterns += [url(r'^silk/', include('silk.urls', namespace='silk'))]  

4、迁移：生成silk用的相关数据库表

> python manage.py makemigrations  
>  python manage.py migrate  
>  python manage.py collectstatic  
>

PS: 如果settings.py中没有配置过STATIC_ROOT，在执行“python manage.py
collectstatic”的时候，有可能会报错，提示缺少STATIC_ROOT配置。加上即可。如：STATIC_ROOT = BASE_DI

5、启动项目

python manage.py runserver

6、查看性能报告

http://127.0.0.1/silk

7、补充：需要程序详细的跟踪记录和执行情况，需要添加装饰器，以联系上下文来参考：

settings设置：

> # 使用Python的内置cProfile分析器  
>  SILKY_PYTHON_PROFILER = True
>
> # 生成.prof文件，silk产生的程序跟踪记录，详细记录来执行来哪个文件，哪一行，用了多少时间等信息  
>  SILKY_PYTHON_PROFILER_BINARY = True
>
> # .prof文件保存路径  
>  SILKY_PYTHON_PROFILER_RESULT_PATH = '/data/profiles/'  
>

函数加上装饰器

```python

    from silk.profiling.profiler import silk_profile
    @silk_profile(name='user login') # name在Profiling页面区分不同请求名称
    def test(request):
      pass
```

以上就是本文的全部内容，希望对大家的学习有所帮助，也希望大家多多支持脚本之家。

