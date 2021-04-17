**1、下载安装MySQLdb类库  
** http://www.djangoproject.com/r/python-mysql/  
**2、修改settings.py 配置数据属性  
**

_复制代码_ 代码如下:

  
DATABASES = {  
'default': {  
'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql',
'sqlite3' or 'oracle'.  
'NAME': 'djangodb', # Or path to database file if using sqlite3.  
# The following settings are not used with sqlite3:  
'USER': 'root',  
'PASSWORD': 'root',  
'HOST': '127.0.0.1', # Empty for localhost through domain sockets or
'127.0.0.1' for localhost through TCP.  
'PORT': '3306', # Set to empty string for default.  
}  
}  

  
修改完后进入DOS进入项目目录下执行python manage.py shell命令启动交互界面输入一下代码验证数据库配置是否成功。没报错则成功！  

_复制代码_ 代码如下:

  
>>> from django.db import connection  
>>> cursor = connection.cursor()  

  
**3、创建一个Django app  
**
一个项目中包含一个或多个这样的app。app可以理解为一块功能集合。比如产品管理模块就包含增删该查等功能，可以把产品管理叫做一个app。每个Django
app都有独立的models，views等，易移植和被复用。  
DOS进入项目目录 执行 python manage.py startapp products生成目录文件如下：  

_复制代码_ 代码如下:

  
products/  
__init__.py  
models.py  
tests.py  
views.py  

  
**4、编写models  
**

_复制代码_ 代码如下:

  
from django.db import models  
# Create your models here.  
class Company(models.Model):  
full_name = models.CharField(max_length=30)  
address = models.CharField(max_length=50)  
tel = models.CharField(max_length=15,blank=True)  
class Product(models.Model):  
product_name = models.CharField(max_length=30)  
price = models.FloatField()  
stock = models.IntegerField(max_length=5)  
company = models.ForeignKey(Company)  

  
**5、模型安装（修改settings.py）  
**

_复制代码_ 代码如下:

  
INSTALLED_APPS = (  
'django.contrib.auth',  
'django.contrib.contenttypes',  
'django.contrib.sessions',  
'django.contrib.sites',  
'django.contrib.messages',  
'django.contrib.staticfiles',  
# Uncomment the next line to enable the admin:  
'django.contrib.admin',  
# Uncomment the next line to enable admin documentation:  
'django.contrib.admindocs',  
'DjangoMysqlSite.products',  
)  

  
  
采用 python manage.py validate 检查模型的语法和逻辑是否正确。  
没有错误则执行 python manage.py syncdb创建数据表。  
现在你可以看到你的数据库除了生成了products_company，products_product外还创建了其它好几个表，这些是django管理后台所需表暂不管。  
  
**6、简单的增删改查  
** 进入python manage.py shell  

_复制代码_ 代码如下:

  
from DjangoMysqlSite.products.models import Company  
>>> c = Company(full_name='集团',address='杭州西湖',tel=8889989)  
>>> c.save()  
  
>>> company_list = Company.objects.all()  
>>> company_list  
  
>>> c = Company.objects.get(full_name="集团")  
>>> c.tel = 123456  
>>> c.save()  

>>> c = Company.objects.get(full_name="集团")  
>>> c.delete()  
#删除所有  
>>> Company.objects.all().delete()  

