**一、变量和表达式**

_复制代码_ 代码如下:

  
>>> 1 + 1  
2  
>>> print 'hello world'  
hello world  
>>> x = 1  
>>> y = 2  
>>> x + y  
3  

Python是强类型语言，无法根据上下文自动解析转换成合适的类型。
Python是一种动态语言，在程序运行过程中，同一个变量名在运行的不同阶段可以代表不同形式的值（整型，浮点，列表，元组），变量名只是各种数据及对象的引用。C语言中的变量名是用来存放结果的内存片段。

1、在Python中是通过对象的引用而不是值来赋值给变量的。

2、赋值操作符主要是"="，同时也可使用增量赋值，如 x+=1。但是没有自增、自减操作符。

3、在C语言中，赋值语句可以当作表达式（可以返回值），但是在Python中赋值语句不会返回值，如下面的就是非法的：  

_复制代码_ 代码如下:

  
>>> x=1  
>>> y=(x=x+1)  

SyntaxError: invalid syntax  
以 #! 开头的称为组织行，这行告诉你的Linux/Unix系统当你执行你的程序的时候，它应该运行哪个解释器。例如：#!/usr/bin/python

以 # 开头的称为注释行。

**二、条件语句**

控制流语句：通过使用or，and，not关键字可以建立任意的条件表达式

if-elif-else：(Python 没有 switch-case 语句，可以通过 if 语句配合字典完成同样的工作)

_复制代码_ 代码如下:

  
if something == 1:  
doSomething1()  
elif something == 2:  
doSomething2()  
else:  
pass # 表示一个空的块或者是空的主体，使用pass语句  
while-else:  
while something:  
doSomething1()  
else:  
doSomething2()  
for-else:  
for i in range(1, 10, 2): # i 值从 1 到 10，步长为2  
print i  
else:  
print 'The for loop is over'  

break 和 continue：用于中断和继续循环。

**三、文件的输入/输出**

_复制代码_ 代码如下:

  
f=open("foo.txt")  
line=f.readline()  
while line:  
print line,  
line=f.readline() #读取一行，包括换行符'\n'，读到文件末尾，返回空字符串  
f.close()

f=open("out.txt","w")  
year=1  
money=1000  
while year<=5:  
money=money*(1+0.05)  
f.write("%3d %0.2f\n" % (year,money)) # print>>f,"%3d %0.2f" % (year,money)  
year+=1  
f.close()

for line in f.xreadlines():  
# Do something with line  

**四、内建类型**

4.1 None类型

None表示空对象。如果一个函数没有显示的返回一个值，None就被返回。None的bool值为false

4.2 数值类型

Python有4种数值类型：整数、长整数、浮点数和复数。所有数值类型都是不可变类型。

python不支持自增自减操作符++，--，++i，其实是+(+i)的意思

运算符与表达式：基本上与其它语言相类似，只是有以下几点不同：

x*y：乘法。2 * 3得到6。'la' * 3得到'lalala'。  
x**y：幂运算，返回 x 的 y 次幂。  
x/y：x 除以 y，4/3得到1（整数的除法得到整数结果）。4.0/3或4/3.0得到1.3333333333333333。  
x//y：取整除。返回商的整数部分。4 // 3.0得到1.0。  
除法//：地板除在任何时候都会将小数部分舍为0  
-x 改变x的符号位 

4.3 字符串  
字符串：单引号（‘）和双引号（"）的作用相同，只能创建单行字符串。转义符是（\）。

三引号（如：'''或者"""）之间的一切都是字符串的内容。

自然字符串：在字符串前加R（或r）指示某些不需要如转义符那样的特别处理的字符串，如：print R“Hello\n World”，将直接输出“Hello\n
World”而不会出现换行的情况。

_复制代码_ 代码如下:

  
a="hello world"  
b=a[0,5] # b="hello"  
c=a+" I love you" # c="hello world I love you"  
s="The value of x is "+ str(x)  

  
获得子串： s[i:j]，返回 s 从i到j（不包括j）之间的子串。若i省略则i=0，若j省略则j=len(s)-1

str() repr() 函数或者向后的引号(`)可以将其他类型的数据转换为字符串。

Unicode字符串：在字符串前加U（或u）。如 a=u'hello'，每个字符用16位来表示 "hello"
'world'会被自动连接为一个字符串"helloworld" ，"s1" u"s2"就会产生u"s1s2"

字符串、Unicode字符串及tuple是不可变的序列。

4.4 列表和元组(list & tuple)

列表和元组是任意对象的序列，支持的常用操作：  

_复制代码_ 代码如下:

  
len()  
append()  
insert(index,aMember)  
list[index]=aNewMember  

一个元素的元组：a=(12,) #注意一定要个额外的逗号！  
对于tuple中的元素，不可以修改，也不可以添加  
列表是可变的序列，允许插入，删除，替换元素等操作

可变序列支持的操作：  

_复制代码_ 代码如下:

  
s[i]=v  
s[i:j]=t # t要是个序列  
del s[i]  
del s[i:j]  

**4.5 字典**

字典就是一个关联数组（或称为哈希表），是一个通过关键字索引的对象集合。

使用{}来创建一个字典

_复制代码_ 代码如下:

  
a={  
"username":"loo"  
"home":"/home/loo"  
"uid":500  
}  
u=a["username"] #访问  
a["username"]="lu" #修改  
a["shell"]="/usr/bin/tcsh" #添加  
del a["shell"] #删除  
len(a) #元素个数  
a[("loo",123)]="abc"  

字典的key是不能修改的对象（比如数字和tuple）。

**五、循环  
  
**

_复制代码_ 代码如下:

  
for i in range(1,5):  
print "2 to the %d power is %d" % (i,2**i)  

  
内建函数range([i,]j[,stride])建立一个列表，参数i和参数stride是可选的，默认分别为0和1。

_复制代码_ 代码如下:

  
a=range(5,1,-1) # a=[5,4,3,2]  
s="hello world"  
for c in s: # 打印每个字符  
print c  

  
range()函数在内存中建立一个列表，当需要一个很大的列表时候，这个占内存且耗时间，为了克服这个缺点，python提供了xrange()。xrange()函数只在需要的时候才临时计算提供值，大大节省了内存。

**六、函数**

def say(message, times = 1): # time 的默认参数值是 1  
print message * times  
return time # 无返回值的函数可省掉 return，等同于return None  
只有在形参表末尾的那些参数可以有默认参数值，即你不能在声明函数形参的时候，先声明有默认值的形参而后声明没有默认值的形参。这是因为赋给形参的值是根据位置而赋值的。例如，def
func(a, b=5)是有效的，

但是def func(a=5, b)是无效的。

global a # 获得全局变量a

用户自定义函数：

_复制代码_ 代码如下:

  
def foo(x,y):  
print '%s+%s is %s' % (str(x),str(y),str(x+y))  
bar=foo  
bar(3,4)  
d={}  
d['callback']=foo  
d['callback'](3,4) # 调用foo  

用户自定义函数有如下属性：

f.__module__ #函数所在的模块名  
f.__doc__ 或者 f.func_doc #文档字符串  
f.__name__ 或者 f.func_name #函数名  
f.__dict__ 或者 f.func_dict #支持任意函数属性的函数名字空间  
f.func_code #编译后产生的字节码  
f.func_defaults #包含所有默认参数的元组  
f.func_globals #函数所在的模块的全局名称空间的字典  
f.func_closure #None or a tuple of cells that contain bindings for the
function's free variables.

**七、类**

_复制代码_ 代码如下:

  
class Stack(object):  
def __init__(self):  
self.stack=[]  
def push(self,object):  
self.stack.append(object)  
def pop(self):  
return self.stack.pop()  
def length(self):  
return len(self.stack)  
s=Stack()  
s.push("Dave")  
s.push(42)  
s.push([3,4,5])  
print s.length()  
print s.pop()  
y=s.pop()  
print y  
del s  

类方法的定义：

_复制代码_ 代码如下:

  
# 静态方法：  
class AClass(object):  
@staticmethod  
def astatic():  
print 'a static method'  
# 类方法：  
class ABase(object):  
@classmethod  
def aclassmethod(cls):  

  
isinstance(s,C) 用于测试s是否是C或是C的子类的实例  
issubclass(A,B) 用于测试A是否是B的子类

**八、异常**

用try和except语句来捕获异常：

_复制代码_ 代码如下:

  
try:  
f=open("file.txt","r")  
except IOError,e:  
print e  
except TypeError,e:  
print e  
...  
try:  
do something  
except:  
print 'An error occurred'  

如果有IOError异常，就将错误原因放置在对象e中，然后运行except代码块，如果发生其他类型的异常就将控制权转到处理该异常的except的代码块，如果没找到该代码块，程序将终止运行，若没有发生异常，except代  
码会被忽略掉。

**九、模块**

import 模块名  
import 模块名 as 别名  
from 模块 import 对象(函数)  
from 模块 import *  
内建函数dir()可以列出一个模块中的所有可访问的内容  
可以被import导入的模块：  
1.使用python写的程序（.py程序）  
2.C或C++扩展（已编译的共享库或DLL）  
3.包（包含多个模块）  
4.内建模块（使用C写的并已链接到python解释器内）

**十、引用与副本（引用计数）**

python中的一切数据都是对象。  
对于可变对象，改变一个引用就等于改变了该对象的所有的引用：  

_复制代码_ 代码如下:

  
a=[1,2,3,4]  
b=a  
b[2]=100  
print a # a=[1,2,100,4]  

  
为了避免这种情况，你需要创建一个可变对象的副本，然后对该副本进行操作。

两种创建可变对象的副本：

(1)浅拷贝(shallow copy)：创建一个新对象，但它包含的子元素仍然是原来对象子元素的引用：

_复制代码_ 代码如下:

  
b=[1,2,[3,4]]  
a=b[:]  
a.append(100)  
print b # b=[1,2,[3,4]] b没有变  
a[0]=100  
print b # b=[1,2,[3,4]] b没有变  
a[2][0]=100  
print b # b=[1,2,[100,4]] b被改变了  

(2)深拷贝(deep copy)

_复制代码_ 代码如下:

  
import copy  
b=[1,2,[3,4]]  
a=copy.deepcopy(b)  

  
__del__()在对象销毁时调用。 del x 只是减少对象x的引用计数，并不调用这个函数。

**十一、类型转换**

_复制代码_ 代码如下:

  
int(x[,base]) #转换为int  
long(x[,base])  
float(x)  
tuple(x)  
list(x)  
chr(x) #转换为字符  
unichr(x) #转换为Unicode字符  
ord(x) #字符转换为整数值  
str(x)  
a=[1,2,3,4]  
s=repr(a) # s='[1,2,3,4]' 也可以使用 s='a'  
b=eval(s) # b=[1,2,3,4] 再转换成一个列表  
eval('3+4')  
f=open("foo")  
a=repr(f) # a="<open file 'foo',mode 'r' at dc030>"  

十二、其他

文档字符串DocStrings： 如果一个模块、类、函数体的第一个语句是未命名的字符串，改字符串就自动成为该对象的文档字符串
说白了就是类似于JavaDoc的东西。

文档字符串的惯例是一个多行字符串，它的首行以大写字母开始，句号结尾。第二行是空行，从第三行开始是详细的描述。可以使用__doc__（注意双下划线）调用函数的文档字符串属性（属于函数的名称）。Python把每一样东西都作为对象，包括这个函数。

Python中的help()，它所做的只是抓取函数的__doc__属性，然后整洁地展示给你。

自动化工具也可以以同样的方式从你的程序中提取文档。随Python发行版附带的pydoc命令，与help()类似地使用DocStrings。

_复制代码_ 代码如下:

  
def printMax(x, y):  
'''Prints the maximum of two numbers.''' # 这里是文档字符串  
print "DocStrings" # 这里是函数体命令行参数  
>>>print printMax.__doc__  
Prints the maximum of two numbers.  

  
id(a)可以查看该对象的标识（当前的实现是该对象在内存中的位置）

_复制代码_ 代码如下:

  
if type(a) is type(b):  
print 'a and b have the same type'  
if type(a) is types.ListType  
print 'Is a list'  

  
isinstance(s,C) 用于测试s是否是C或是C的子类的实例

_复制代码_ 代码如下:

  
import types  
isinstance(3,types.IntType) #返回True  

  
x==y 比较x和y的值是否相等  
x is y 和x is not y 比较x和y在内存中是否指向同一个对象

