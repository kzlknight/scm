**前言**

本文主要给大家介绍了利用django-
suit模板在管理后台添加自定义的菜单和自定义的页面、设置访问权限的相关内容，分享出来供大家参考学习，下面话不多说了，来随着小编一起看看详细的介绍吧

**方法如下：**

1、先在settings.py里面的SUIT_CONFIG中添加配置，我们平时添加的配置都是app类型的，我们需要自定义页面的话，就不能用app了，需要用url，这里面我们使用如下：

```python

    # django-suit config
    SUIT_CONFIG = {
     'ADMIN_NAME': 'X・X',
     'HEADER_DATE_FORMAT': '',
     'HEADER_TIME_FORMAT': 'H:i',
     'SHOW_REQUIRED_ASTERISK': True,
     'CONFIRM_UNSAVED_CHANGES': True,
     'LIST_PER_PAGE': 20,
     'MENU_OPEN_FIRST_CHILD': True,
     'MENU': (
      # sites是默认原先的app和models
      # 'sites',
      '-',
      {'app': 'auth', 'label': u'权限管理', 'icon': 'icon-lock'},
      '-',
      {'app': 'duser', 'label': u'平台用户', 'icon': 'icon-user'},
      '-',
      {'app': 'dtheme', 'label': u'主题管理', 'icon': 'icon-tags'},
      '-',
      {'app': 'dpost', 'label': u'文章管理', 'icon': 'icon-edit'},
      '-',
      # 如果使用http这种绝对路径的话，菜单不会展开，且不会标记为active状态
      {'url': '/admin/theme/mysql', 'label': u'第三数据', 'icon': 'icon-lock'},
      '-',
      {'label': u'统计数据', 'icon': 'icon-tags', 'models': (
       {'url': '/admin/theme/data', 'label': u'第一数据'},
       {'url': '/admin/theme/show', 'label': u'第二数据'}
      )}
     )
    }
```

2、然后就是在urls.py里面添加路由，这个路由一定要添加在admin.site.urls的前面，因为不然的话，它会先去admin.site.urls里面去匹配，造成混乱或报错。

```python

    from dtheme import views
    
    urlpatterns = [
     # 第一个就是我们自己新增的url路径
     url(r'^admin/theme/data', views.data),
     url(r'^admin/', admin.site.urls),
     url(r'^api/user/', include('duser.urls')),
     url(r'^api/post/', include('dpost.urls')),
     url(r'^api/theme/', include('dtheme.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

3、然后，就是写views了，我们假如dtheme模块的views里面写：

```python

    def data(request):
     return render(request, "data.html")
```

4、请注意，之所以我们上面可以直接用data.html，是因为我们在dtheme模块下面创建了一个templates文件夹，然后把data.html放在里面了，它会扫描这个文件夹找模板。那么这个模板写成什么样呢？我们就随意写了一个东西。这里面需要注意的是，我们需要继承base_site.html，不然那些header和footer，还有左边的菜单什么的都没有了，相当于谁也不继承。内容就写在content里面即可。

```python

    {% extends "admin/base_site.html" %}
    
    {% block content %}
    hello, new page.
    {% endblock %}
```

5、OVER。

6、回来，还没完。这个时候如果我们从后台注销，然后直接在浏览器中输入http://127.0.0.1:8000/admin/theme/data的话，发现还是可以直接访问到这个页面，输入管理后台的其他页面它就会要求你验证。所以说我们自定义的这个页面还是十分危险的，其他人知道网址后就可以直接访问它了，我们的想法其实也很简单啊，我们也不想搞特殊，在安全这方面，只要求和其他后台的页面一样就行了：即用户在访问这些后台页面的时候要做一个用户验证，如果用户已经登录了，就可以访问，没登录没通过验证的话，就不能访问，直接跳转到登录页面。这个需要我们再view里面做设置。

```python

    from django.contrib.admin.views.decorators import staff_member_required
    
    def data(request):
     return render(request, "data.html")
    
    data = staff_member_required(data)
```

看到上面的变化了没有？就是我们引入了一个staff_member_required模块，这个模块就是用来验证是否是内部人员（也就是是否登录）用的。当然我们要把我们的view函数放在它里面。这样就OK了。

7、这里面还有一个如何把自定义页面加入到auth里面的坑，待研究完再回来补充。

**总结**

以上就是这篇文章的全部内容了，希望本文的内容对大家的学习或者工作具有一定的参考学习价值，如果有疑问大家可以留言交流，谢谢大家对脚本之家的支持。  

