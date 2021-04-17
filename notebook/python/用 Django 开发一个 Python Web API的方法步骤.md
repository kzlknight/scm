Django 是 Python 编程语言驱动的一个开源模型-视图-控制器（MVC）风格的 Web 应用程序框架。它是Python
API开发中最受欢迎的名称之一，自2005年成立以来，其知名度迅速提升。

Django由Django软件基金会（Django Software
Foundation）维护，并获得了社区的大力支持，在全球拥有11,600多个成员。在Stack
Overflow上，Django大约有191,000个带标签的问题。Spotify，YouTube和Instagram等网站都依赖Django进行应用程序和数据管理。

本文演示了使用HTTP协议的GET方法从服务器获取数据的简单API。

**建立一个项目**

首先，为您的Django应用程序创建一个结构；您可以在系统上的任何位置执行此操作：

```python

    $ mkdir myproject
    $ cd myproject
    
```

然后创建一个虚拟环境，它能够使我们根据需要安装一些特定的包来跑通我们的程序，并且不影响当前环境，用完退出虚拟环境即可。

```python

    $ python3 -m venv env
    $ source env/bin/activate
    
```

在Windows上，使用命令env \ Scripts \ activate激活Python虚拟环境。

**安装Django和Django REST框架**

接下来，安装Django和Django REST框架模块：

```python

    $ pip3 install django
    $ pip3 install djangorestframework
```

**实例化一个新的Django项目**

既然您已经为应用程序创建了工作环境，那么您必须实例化一个新的Django项目。与像Flask这样的小框架不同，Django在此过程中包含专用命令（请注意第一个命令中的结尾.字符）：

```python

    $ django-admin startproject tutorial .
    $ cd tutorial
    $ django-admin startapp quickstart
    
```

Django使用数据库作为其后端，因此您应该在开始开发之前同步数据库。可以使用运行django-
admin命令时创建的manage.py脚本来管理数据库。由于您当前位于tutorial路径中，因此请使用../命令来运行脚本，该脚本位于同一个路径中：

```python

    $ python3 ../manage.py makemigrations
    No changes detected
    $ python4 ../manage.py migrate
    Operations to perform:
     Apply all migrations: admin, auth, contenttypes, sessions
    Running migrations:
     Applying contenttypes.0001_initial... OK
     Applying auth.0001_initial... OK
     Applying admin.0001_initial... OK
     Applying admin.0002_logentry_remove_auto_add... OK
     Applying admin.0003_logentry_add_action_flag_choices... OK
     Applying contenttypes.0002_remove_content_type_name... OK
     Applying auth.0002_alter_permission_name_max_length... OK
     Applying auth.0003_alter_user_email_max_length... OK
     Applying auth.0004_alter_user_username_opts... OK
     Applying auth.0005_alter_user_last_login_null... OK
     Applying auth.0006_require_contenttypes_0002... OK
     Applying auth.0007_alter_validators_add_error_messages... OK
     Applying auth.0008_alter_user_username_max_length... OK
     Applying auth.0009_alter_user_last_name_max_length... OK
     Applying auth.0010_alter_group_name_max_length... OK
     Applying auth.0011_update_proxy_permissions... OK
     Applying sessions.0001_initial... OK
    
```

**在Django中创建用户**

使用示例密码password123创建一个名为admin的初始用户：

```python

    $ python3 ../manage.py createsuperuser \
     --email admin@example.com \
     --username admin
    
```

根据提示创建密码。

**在Django中实现序列化组件和视图层**

为了使Django能够将信息传递给HTTP GET请求，必须将传递对象转换为有效的响应数据。Django为此实现了序列化组件。

在您的项目中，通过创建一个名为quickstart / serializers.py的新模块来定义一些序列化器，该模块将用于数据传输：

```python

    from django.contrib.auth.models import User, Group
    from rest_framework import serializers
     
    class UserSerializer(serializers.HyperlinkedModelSerializer):
      class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
     
    class GroupSerializer(serializers.HyperlinkedModelSerializer):
      class Meta:
        model = Group
        fields = ['url', 'name']
    
```

Django中的视图是一个接受Web请求并返回Web响应的函数。响应可以是HTML，或者是HTTP重定向，或者是HTTP错误，JSON或XML文档，图像或TAR文件，或者可以从Internet获得的任何其他内容。要创建视图函数，请打开quickstart
/ views.py并输入以下代码。该文件模板已经存在，并且其中包含一些样板文本，因此请保留该文本并将其添加到文件中：

```python

    from django.contrib.auth.models import User, Group
    from rest_framework import viewsets
    from tutorial.quickstart.serializers import UserSerializer, GroupSerializer
     
    class UserViewSet(viewsets.ModelViewSet):
      """
      API endpoint allows users to be viewed or edited.
      """
      queryset = User.objects.all().order_by('-date_joined')
      serializer_class = UserSerializer
     
    class GroupViewSet(viewsets.ModelViewSet):
      """
      API endpoint allows groups to be viewed or edited.
      """
      queryset = Group.objects.all()
      serializer_class = GroupSerializer
```

**使用Django生成URL**

现在，您可以生成URL，以便人们可以访问您的API。在文本编辑器中打开urls.py，并将默认示例代码替换为以下代码：

```python

    from django.urls import include, path
    from rest_framework import routers
    from tutorial.quickstart import views
     
    router = routers.DefaultRouter()
    router.register(r'users', views.UserViewSet)
    router.register(r'groups', views.GroupViewSet)
     
    # Use automatic URL routing
    # Can also include login URLs for the browsable API
    urlpatterns = [
      path('', include(router.urls)),
      path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    ]
    
```

**调整您的Django项目设置**

此示例项目的设置模块存储在tutorial /
settings.py中，因此请在文本编辑器中将其打开，然后将rest_framework添加到INSTALLED_APPS列表的末尾：

```python

    INSTALLED_APPS = [
      ...
      'rest_framework',
    ]
    
```

**测试您的Django API**

现在，您可以测试已构建的API。首先，从命令行启动内置服务器：

```python

    $ python3 manage.py runserver
    
```

您可以使用curl获取URL http：// localhost：8000 / users来访问您的API：

```python

    $ curl --get http://localhost:8000/users/?format=json
    [{"url":"http://localhost:8000/users/1/?format=json","username":"admin","email":"admin@example.com","groups":[]}]
    
```

或使用Firefox浏览器等：

有关使用Django和Python的RESTful API的更深入的知识，请参阅Django文档（ [
https://docs.djangoproject.com/en/2.2/
](https://docs.djangoproject.com/en/2.2/) ）。

到此这篇关于用 Django 开发一个 Python Web API的方法步骤的文章就介绍到这了,更多相关Django 开发Python
Web内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

