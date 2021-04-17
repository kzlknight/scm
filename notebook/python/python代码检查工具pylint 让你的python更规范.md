**1、pylint是什么？  
  
** Pylint 是一个 Python 代码分析工具，它分析 Python 代码中的错误，查找不符合代码风格标准（Pylint 默认使用的代码风格是
PEP 8，具体信息，请参阅参考资料）和有潜在问题的代码。目前 Pylint 的最新版本是 pylint-0.18.1。  
  
Pylint 是一个 Python
工具，除了平常代码分析工具的作用之外，它提供了更多的功能：如检查一行代码的长度，变量名是否符合命名标准，一个声明过的接口是否被真正实现等等。  
Pylint 的一个很大的好处是它的高可配置性，高可定制性，并且可以很容易写小插件来添加功能。  
  
如果运行两次 Pylint，它会同时显示出当前和上次的运行结果，从而可以看出代码质量是否得到了改进。  
  
目前在 eclipse 的 pydev 插件中也集成了 Pylint。  
  
pylint是一个Python代码风格的检查工具, 它依据的标准是Guido van Rossum的PEP8。  
  
pylint类似于PyChecker, 但提供了更多的功能, 如检查代码行的长度, 检查变量命名是否符合编码规范, 或检查声明的接口是否被真正的实现,
完整的检查功能请参见http://www.logilab.org/card/pylintfeatures。  
  
pylint的最大优势在于其高度的可配置化和可定制化，你可以很容易地写一个小插件添加个人功能。  
  
安装方法：pip install pylint  
  
参考链接：  
  
http://www.ibm.com/developerworks/cn/aix/library/au-cleancode/index.html  
  
http://www.douban.com/note/46830857/  
  
http://zh.wikipedia.org/wiki/Pylint  
  
**2、为什么使用pylint？  
  
** ​为了写出好代码。什么是好代码？符合团队编码习惯的代码：统一的命名，结构。  
  
它的类似产品是什么？PyChecker  
  
你还有啥补充？  
  
**3、 怎么使用pylint？  
**  
基础使用：  
  
通过三种代码来进行测时，得分从1,不断的根据pylint的提示进行重构，最终得到10分。  
v1_fetch.py:  

_复制代码_ 代码如下:

  
#coding:utf-8  
import urllib  
import time  
  
def a(url):  
content = urllib.urlopen(url).read()  
f = open('tmp%s.html' % str(time.time()), 'w')  
f.write(content)  
f.close()  
  
def main(urls):  
for url in urls:  
a(url)  
  
if __name__ == '__main__':  
urls = ['http://www.baidu.com','http://www.sohu.com']  
main(urls)  

  
修改命名：  
v2_fetch.py:  

_复制代码_ 代码如下:

  
#coding:utf-8  
import urllib  
import time  
  
def fetch(url):  
content = urllib.urlopen(url).read()  
f_html = open('tmp%s.html' % str(time.time()), 'w')  
f_html.write(content)  
f_html.close()  
  
def main(urls):  
for url in urls:  
fetch(url)  
  
if __name__ == '__main__':  
from_urls = ['http://www.baidu.com','http://www.sohu.com']  
main(from_urls)  

  
再次修改：  
v3_fetch.py:  

_复制代码_ 代码如下:

  
#coding:utf-8  
'''  
a test function module  
'''  
import urllib  
import time  
  
def fetch(url):  
'''  
fetch url  
'''  
content = urllib.urlopen(url).read()  
f_html = open('tmp%s.html' % str(time.time()), 'w')  
f_html.write(content)  
f_html.close()  
  
def main(urls):  
'''  
main func to be called  
'''  
for url in urls:  
fetch(url)  
  
if __name__ == '__main__':  
FROM_URLS = ['http://www.baidu.com','http://www.sohu.com']  
main(FROM_URLS)  

  
基本上有以下几种判断标准：  
  
1、命名方式  
  
2、docstring  
  
当然直接用pylint进行包检测也是可以的：pylint package  
  
参看下面了解更多的使用方法，一定要动手练习才行：  
  
参看内容：  
  
Pylint 的调用  
  
清单 1. Pylint 的调用命令  
pylint [options] module_or_package  
  
使用 Pylint 对一个模块 module.py 进行代码检查：  
1. 进入这个模块所在的文件夹，运行 pylint [options] module.py   
这种调用方式是一直可以工作的，因为当前的工作目录会被自动加入 Python 的路径中。  
  
2. 不进入模块所在的文件夹，运行 pylint [options] directory/module.py   
这种调用方式当如下条件满足的时候是可以工作的：directory 是个 Python 包 ( 比如包含一个 __init__.py 文件 )，或者
directory 被加入了 Python 的路径中。  
  
使用 Pylint 对一个包 pakage 进行代码检查：  
1. 进入这个包所在文件夹，运行 pylint [options] pakage。   
这种调用方式是一直可以工作的，因为当前的工作目录会被自动加入 Python 的路径中。  
  
2. 不进入包所在的文件夹，运行 pylint [options] directory/ pakage。   
这种情况下当如下条件满足的时候是可以工作的：directory 被加入了 Python 的路径中。比如在 Linux 上，export
PYTHONPATH=$PYTHONPATH: directory。  
  
此外，对于安装了 tkinter 包的机器，可以使用命令 pylint-gui打开一个简单的 GUI 界面，在这里输入模块或者包的名字 ( 规则同命令行
), 点击 Run，Pylint 的输出会在 GUI 中显示。  
Pylint 的常用命令行参数  

