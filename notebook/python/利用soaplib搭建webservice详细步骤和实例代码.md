最近在搞基于python的webservice项目，今天为把环境给配好，折腾了不少时间，还是把配的过程记录下来，以后备用：  
首先你系统上要有python，这个不必说啦，我系统上用的是2.7+  
其次，要用python进行webservice开发，还需要一些库：  
lxml ：  
命令行下 sudo easy_install lxml 就能安装

pytz ：  
命令行下 sudo easy_install pytz 就能安装

soaplib：  
进行webservice开发必须要用的库，可以在https://github.com/volador/soaplib拿到，注意要先安装上面两个插件再安装这个，因为这个依赖于上面两个插件，把zip拿下来后解压，sudo
python setup.py install 就能安装了。

_复制代码_ 代码如下:

  
Soaplib is an easy to use python library for publishing soap web services
using WSDL 1.1 standard, and answering SOAP 1.1 requests. With a very small
amount of code, soaplib allows you to write a useful web service and deploy it
as a WSGI application.  

soaplib是python的soap框架，可以用来建立webservice.soaplib这样在这里下载：https://github.com/volador/soaplib

装好soaplib后新建一个test.py，建立一个webservice，实现返回两个整数相加的和。代码如下：

_复制代码_ 代码如下:

  
# -*- coding: cp936 -*-  
import soaplib  
from soaplib.core.util.wsgi_wrapper import run_twisted #发布服务  
from soaplib.core.server import wsgi  
from soaplib.core.service import DefinitionBase #所有服务类必须继承该类  
from soaplib.core.service import soap #声明注解  
from soaplib.core.model.clazz import Array #声明要使用的类型  
from soaplib.core.model.clazz import ClassModel #若服务返回类，该返回类必须是该类的子类  
from soaplib.core.model.primitive import Integer,String  
class C_ProbeCdrModel(ClassModel):  
__namespace__ = "C_ProbeCdrModel"  
Name=String  
Id=Integer  
class AdditionService(DefinitionBase): #this is a web service  
@soap(Integer,Integer,_returns=String)  
def addition(self,a,b):  
return str(a)+'+'+str(b)+'='+str(a+b)  
@soap(_returns=Array(String))  
def GetCdrArray(self):  
L_Result=["1","2","3"]  
return L_Result  
@soap(_returns=C_ProbeCdrModel)  
def GetCdr(self): #返回的是一个类，该类必须是ClassModel的子类，该类已经在上面定义  
L_Model=C_ProbeCdrModel()  
L_Model.Name=L_Model.Name  
L_Model.Id=L_Model.Id  
return L_Model  
  
  
if __name__=='__main__': #发布服务  
try:  
print '服务已经开启'  
from wsgiref.simple_server import make_server  
soap_application = soaplib.core.Application([AdditionService], 'tns')  
wsgi_application = wsgi.Application(soap_application)  
server = make_server('localhost', 7789, wsgi_application)  
server.serve_forever()  
  
except ImportError:  
print 'error'  

在浏览器中访问http://127.0.0.1:7789/SOAP/?wsdl出现一大版的xml而不是访问错误，就说明服务添加成功啦  
在命令行下既可以测试

_复制代码_ 代码如下:

  
>>>from suds.client import Client  
>>> test=Client('http://localhost:7789/SOAP/?wsdl')  
>>> print test.service.addition(1,2)  
1+2=3  

问题注意：代码运行过程中，会出现各种模块没找到，那是因为你没有安装，根据提示，google搜索下载安装就好，如果是windows，找不到exe,zip格式的安装文件，下载tar.gz也行的，解压后在cmd切换到解压目录，执行：python
setup.py install便安装成功了。  
第一次建立连接很慢很慢，慢到无法忍受，>>>
test=Client('http://localhost:7789/SOAP/?wsdl')，不知道是怎么回事。

