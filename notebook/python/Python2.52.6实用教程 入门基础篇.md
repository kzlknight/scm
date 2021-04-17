起步走  

_复制代码_ 代码如下:

  
#! /usr/bin/python  
  
a=2  
b=3  
c="test"  
c=a+b  
print "execution result: %i"%c  

  
知识点  
  
Python是动态语言,变量不须预先声明.  
打印语句采用C风格  
字符串和数字  
但有趣的是,在javascript里我们会理想当然的将字符串和数字连接,因为是动态语言嘛.但在Python里有点诡异,如下:  

_复制代码_ 代码如下:

  
#! /usr/bin/python  
  
a=2  
b="test"  
c=a+b  

  
  
运行这行程序会出错,提示你字符串和数字不能连接,于是只好用内置函数进行转换  

_复制代码_ 代码如下:

  
#! /usr/bin/python  
  
a=2  
b="test"  
c=str(a)+b  
d="1111"  
e=a+int(d)  
#How to print multiply values  
print "c is %s,e is %i" % (c,e)  

  
知识点:  
  
用int和str函数将字符串和数字进行转换  
打印以#开头,而不是习惯的//  
打印多个参数的方式  
国际化  
写腻了英文注释,我们要用中文!  
  
  
#! /usr/bin/python  
# -*- coding: utf8 -*-  
  
print "上帝重返人间:马拉多纳出任阿根廷国家足球队主帅."  
知识点:  
  
加上字符集即可使用中文  
列表  
列表类似Javascript的数组,方便易用  

_复制代码_ 代码如下:

  
  
#! /usr/bin/python  
# -*- coding: utf8 -*-  
  
#定义元组  
word=['a','b','c','d','e','f','g']  
  
#如何通过索引访问元组里的元素  
a=word[2]  
print "a is: "+a  
b=word[1:3]  
print "b is: "  
print b # index 1 and 2 elements of word.  
c=word[:2]  
print "c is: "  
print c # index 0 and 1 elements of word.  
d=word[0:]  
print "d is: "  
print d # All elements of word.  
  
#元组可以合并  
e=word[:2]+word[2:]  
print "e is: "  
print e # All elements of word.  
f=word[-1]  
print "f is: "  
print f # The last elements of word.  
g=word[-4:-2]  
print "g is: "  
print g # index 3 and 4 elements of word.  
h=word[-2:]  
print "h is: "  
print h # The last two elements.  
i=word[:-2]  
print "i is: "  
print i # Everything except the last two characters  
l=len(word)  
print "Length of word is: "+ str(l)  
print "Adds new element"  
word.append('h')  
print word  
  
#删除元素  
del word[0]  
print word  
del word[1:3]  
print word  

  
知识点:  
  
列表长度是动态的,可任意添加删除元素.  
用索引可以很方便访问元素,甚至返回一个子列表  
更多方法请参考Python的文档  
字典  

_复制代码_ 代码如下:

  
#! /usr/bin/python  
  
x={'a':'aaa','b':'bbb','c':12}  
print x['a']  
print x['b']  
print x['c']  
  
for key in x:  
print "Key is %s and value is %s",(key,x[key])  
  
keys=x.items();  
print keys[0]  
keys[0]='ddd'  
print keys[0]  

  
知识点:  
  
将他当Java的Map来用即可.  
字符串  
比起C/C++,Python处理字符串的方式实在太让人感动了.把字符串当列表来用吧.  
  

_复制代码_ 代码如下:

  
word="abcdefg"  
a=word[2]  
print "a is: "+a  
b=word[1:3]  
print "b is: "+b # index 1 and 2 elements of word.  
c=word[:2]  
print "c is: "+c # index 0 and 1 elements of word.  
d=word[0:]  
print "d is: "+d # All elements of word.  
e=word[:2]+word[2:]  
print "e is: "+e # All elements of word.  
f=word[-1]  
print "f is: "+f # The last elements of word.  
g=word[-4:-2]  
print "g is: "+g # index 3 and 4 elements of word.  
h=word[-2:]  
print "h is: "+h # The last two elements.  
i=word[:-2]  
print "i is: "+i # Everything except the last two characters  
l=len(word)  
print "Length of word is: "+ str(l)  

  
不过要注意Asc和Unicode字符串的区别:  

_复制代码_ 代码如下:

  
#! /usr/bin/python  
# -*- coding: utf8 -*-  
  
s=raw_input("输入你的中文名,按回车继续");  
print "你的名字是 : " +s;  
  
l=len(s)  
print "你中文名字的长度是:"+str(l);  
a=unicode(s,"utf8")  
l=len(a)  
print "对不起,刚才计算错误.我们应该用utf8来计算中文字符串的长度, \  
你名字的长度应该是:"+str(l);  

  
知识点:  
  
用unicode函数进行转码  
条件和循环语句  

_复制代码_ 代码如下:

  
#! /usr/bin/python  
x=int(raw_input("Please enter an integer:"))  
if x<0:  
x=0  
print "Negative changed to zero"  
  
elif x==0:  
print "Zero"  
  
else:  
print "More"  
  
  
# Loops List  
a = ['cat', 'window', 'defenestrate']  
for x in a:  
print x, len(x)  

  
知识点:  
  
条件和循环语句  
如何得到控制台输入  
函数  

_复制代码_ 代码如下:

  
#! /usr/bin/python  
# -*- coding: utf8 -*-  
  
def sum(a,b):  
return a+b  
  
  
func = sum  
r = func(5,6)  
print r  
  
# 提供默认值  
def add(a,b=2):  
return a+b  
r=add(1)  
print r  
r=add(1,5)  
print r  

  
一个好用的函数  

_复制代码_ 代码如下:

  
#! /usr/bin/python  
# -*- coding: utf8 -*-  
  
# The range() function  
a =range(5,10)  
print a  
a = range(-2,-7)  
print a  
a = range(-7,-2)  
print a  
a = range(-2,-11,-3) # The 3rd parameter stands for step  
print a  

  
知识点:  
  
Python 不用{}来控制程序结构,他强迫你用缩进来写程序,使代码清晰.  
定义函数方便简单  
方便好用的range函数  
异常处理  

_复制代码_ 代码如下:

  
#! /usr/bin/python  
s=raw_input("Input your age:")  
if s =="":  
raise Exception("Input must no be empty.")  
  
try:  
i=int(s)  
except ValueError:  
print "Could not convert data to an integer."  
except:  
print "Unknown exception!"  
else: # It is useful for code that must be executed if the try clause does not
raise an exception  
print "You are %d" % i," years old"  
finally: # Clean up action  
print "Goodbye!"  

