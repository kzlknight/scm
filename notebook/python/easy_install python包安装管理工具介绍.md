easy_install更准确的说是一个和setuptools绑定的模块，一切下载、构建、安装和管理的工作都可以由它来担当。  
  
一般的执行方式：  
easy_install + URL  
  
但是，如果某些应用或脚本在Python CheeseShop里，可以直接执行：  
  
easy_install +安装包名  
这样比我们打开一个网站，再去慢慢的下载、安装来得快得多。  
  
使用easy_install需要先 [ 安装setuptools工具 ](http://pypi.python.org/pypi/setuptools)
，然后将easy_install所在目录加到PATH环境变量里:  
Windows: C:\Python25\Scripts  
  
如果想删除通过easy_install安装的软件包，比如说：XXX，可以执行命令：  
easy_install -m XXX

