首先你要确保你机器上面安装了python，其次，你还要确保你上面 [ 安装了Django
](https://www.jb51.net/article/42702.htm) 。  
接下来，才能进入到搭建第一个Django应用程序  
很简单的操作，即在windows终端输入代码：  

_复制代码_ 代码如下:

  
1 django-admin.py startproject mysite  

  
即可，如：我是在我电脑的 E:\Python33\python_workspace 目录下面创建项目的  
目录是你自己定的  
运行命令：  

_复制代码_ 代码如下:

  
django-admin.py startproject mysite

#意思是创建一个以mysite命名的应用程序  

  
  
![](https://img.jbzj.com/file_images/article/201311/20131119095146.jpg?2013101995638)

接下来就要进入到： E:\Python33\python_workspace\mysite 目录  
注意：这里一定要先进到 mysite 目录，否则，会失败滴！！！！  
运行代码：

_复制代码_ 代码如下:

  
python manage.py runserver 8080

#意思是启动服务，端口为：8080,如果不设置端口，默认为：80000  

如下图：  
![](https://img.jbzj.com/file_images/article/201311/20131119095157.jpg?2013101995726)

启动好了服务，那么我们现在就可以通过浏览器进行访问了  
在浏览器地址栏中输入： [ http://localhost:8080 ](http://localhost:8080)  
  
![](https://img.jbzj.com/file_images/article/201311/20131119095209.jpg?2013101995825)

到现在，你的第一个django应用程序就算是成功了！！！  
  
遇到的问题及解决方案：  
**1.importError：No module named django.core  
** 分析和解决方案：这是在运行命令：django-admin.py startproject mysite的时候遇到的问题，可以确定的是，在  
自己机器上面django是已经成功安装了的，可以通过：

_复制代码_ 代码如下:

  
python -c "import django;print(django.get_version())"  

来验证；其次，已经把django-admin.py加入到了环境变量中：

_复制代码_ 代码如下:

  
#加入到path环境变量中 #django的安装目录  
E:\Python33\Lib\site-packages\django\bin  

我上面两步操作都做了，但是还是出现了错误，后来发现了问题的原因：我电脑上面安装的python版本过多：python2.7.5,python32,python33  
最后把python2.7.5，python32卸载了，只留下python33,然后再运行，成功！！！  
**2.python:can't open file 'manage.py'  
** 这个和上面的原因差不多，解决的方法，也是版本冲突，把其他卸载掉，只留下python33，成功！！！

