###  环境

Django 2.0 + Win 10 + Pycharm + 360浏览器

###  报错

![](https://img.jbzj.com/file_images/article/202012/2020121811383217.png)

###  项目结构（报异常）

![](https://img.jbzj.com/file_images/article/202012/2020121811383218.png)

###  解决方法

看了好多大佬的解决方法，基本上都是配置settings.py文件，配来配去搞了好几个小时，依然没有解决问题。

后来发现，提示说的是templates路径下找不到文件，那么我们就在项目里面自己建个文件夹，命名为templates。

运行发现，还是有问题，还是找不到html，修改路由啥的搞了一通，还是没用。

经过多次实验，发现了正解：在templates下新建个文件夹，与应用名称相同（我的是indexpage），再把html放到路径下，终于可以访问了！

###  项目结构（已解决）

![](https://img.jbzj.com/file_images/article/202012/2020121811383319.png)

###  代码（已解决）

indexpage/views.py

```python

     ... ...
    def get_login_page(request):
      return render(request, "indexpage/login.html")
     ... ...
```

indexpage/urls.py

```python

    from django.urls import path, include
     
    import indexpage.views
     
    urlpatterns = [
     
      path('hello',indexpage.views.helloworld),
      path('login', indexpage.views.get_login_page),
      
    ]
```

settings.py（保持默认）

```python

     ... ...
     
    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
     
    # print(BASE_DIR)
    TEMPLATES = [
      {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
          'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
          ],
        },
      },
    ]
        ... ...
```

到此这篇关于Django模板报TemplateDoesNotExist异常(亲测可行)的文章就介绍到这了,更多相关Django
TemplateDoesNotExist异常内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

