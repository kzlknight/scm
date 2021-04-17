测试配置文件test.conf内容如下：

_复制代码_ 代码如下:

  
[first]  
w = 2  
v: 3  
c =11-3

[second]

sw=4  
test: hello  

测试配置文件中有两个区域，first和second，另外故意添加一些空格、换行。

下面解析：

_复制代码_ 代码如下:

  
>>> import ConfigParser  
>>> conf=ConfigParser.ConfigParser()  
>>> conf.read('test.conf')  
['test.conf']  
>>> conf.sections() #获得所有区域  
['first', 'second']  
>>> for sn in conf.sections():  
... print conf.options(sn) #打印出每个区域的所有属性  
...  
['w', 'v', 'c']  
['sw', 'test']  

获得每个区域的属性值：

_复制代码_ 代码如下:

  
for sn in conf.sections():  
print sn,'-->'  
for attr in conf.options(sn):  
print attr,'=',conf.get(sn,attr)  

输出：

_复制代码_ 代码如下:

  
first -->  
w = 2  
v = 3  
c = 11-3  
second -->  
sw = 4  
test = hello  

好了，以上就是基本的使用过程，下面是动态的写入配置,

_复制代码_ 代码如下:

  
cfd=open('test2.ini','w')  
conf=ConfigParser.ConfigParser()  
conf.add_section('test') #add a section  
conf.set('test','run','false')  
conf.set('test','set',1)  
conf.write(cfd)  
cfd.close()  

上面是向test2.ini写入配置信息。

