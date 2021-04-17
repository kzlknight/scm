##  需求

一般Django开发为了保障避免 csrf
的攻击，如果使用Django的模板渲染页面，那么则可以在请求中渲染设置一个csrftoken的cookie数据，但是如果需要前后端分离，不适用Django的模板渲染功能，怎么来动态获取
csrftoken 呢？

##  Django 通过 request 请求获取 csfttoken 的方法

```python

    from django.middleware.csrf import get_token
     
    def getToken(request):
      token=get_token(request)
      return HttpResponse(json.dumps({'token':token}), content_type="application/json,charset=utf-8")
```

使用这种方式的确可以获取csrftoken的数据，下面来写个示例来演示一下。

##  Django 后端获取 csrftoken 示例

###  在视图 views.py 设置 getToken 方法

```python

    from django.middleware.csrf import get_token
     
    # 获取cstftoken
    def getToken(request):
      token = get_token(request)
      return HttpResponse(json.dumps({'token': token}), content_type="application/json,charset=utf-8")
```

在 ` urls.py ` 配置URL

```python

    from django.urls import path, re_path
     
    from . import views
     
    urlpatterns = [
     
      # ex:/assetinfo/getToken
      path('getToken', views.getToken, name='getToken'),
      ...
    ]
```

使用 ` postman ` 测试接口，获取 csrftoken

![](https://img.jbzj.com/file_images/article/202012/2020122514050543.jpg)

现在是完成了基本功能了，能否动态获取 csrftoken，但是还有一个跨域问题，假如跨域后就无法获取 csrftoken 了。

我尝试过在Django中设置跨域返回的方式，但是这是不行的，因为不同的域名使用 csrftoken 就基本失去了原来的防止 csrf 攻击的意义。

最好的方式是使用 nginx 做本机的代理，分别反向代理前端、后端的服务，然后统一提供一个域名使用，即可使用 csrftoken 了。

###  在 postman 设置使用 csrftoken

当想要在 postman 中使用 csrftoken，那么只需要将获取的 csrftoken 值设置到 Headers 中即可，如下：

![](https://img.jbzj.com/file_images/article/202012/2020122514050544.jpg)

```python

    {"X-CSRFToken":"K6q7uqt9J8UocELWR04pw2DKd8T2LRNWjf2uQvsFBWm87Q1lJZQV1vj3pR8REzCR"}
```

如果不设置，那么则会出现 403拒绝报错 如下：

![](https://img.jbzj.com/file_images/article/202012/2020122514050545.jpg)

到此这篇关于Django前后端分离csrf token获取方式的文章就介绍到这了,更多相关Django csrf
token获取内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

