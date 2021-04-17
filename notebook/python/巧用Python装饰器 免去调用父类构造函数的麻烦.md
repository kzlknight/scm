先看一段代码：  
  

_复制代码_ 代码如下:

  
class T1(threading.Thread):  
def __init__(self, a, b, c):  
super(T1, self).__init__()  
self.a = a  
self.b = b  
self.c = c  
  
def run(self):  
print self.a, self.b, self.c  

  
代码定义了一个继承自threading.Thread的class，看这句  
  
super(T1, self).__init__()  
  
也有些人喜欢这么写  
  
threading.Thread.__init__(self)  
  
当然作用都是调用父类的构造函数。  
  
写了这么久的python代码，每次写到这都有重复造轮子的感觉。刚才突然想到装饰器这个好东西，试着写了个autoInitClass来帮助pythoner脱离苦海，免去手动调用父类构造函数的麻烦。  
代码如下：  

_复制代码_ 代码如下:

  
def autoInitClass(OldClass):  
superClass = OldClass.mro()[1]  
class NewClass(OldClass):  
def __init__(*args):  
self = args[0]  
superClass.__init__(self)  
apply(OldClass.__init__, args)  
return NewClass  

  
使用autoInitClass装饰器构造新类：  
  

_复制代码_ 代码如下:

  
@autoInitClass  
class T2(threading.Thread):  
def __init__(self, a, b, c):  
#不用再写super(T2, self).__init__()  
self.a = a  
self.b = b  
self.c = c  
  
def run(self):  
print self.a, self.b, self.c  

  
本文来自: itianda's blog ，转载请注明原文出处

