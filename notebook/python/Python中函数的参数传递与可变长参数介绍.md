**1.Python中也有像C++一样的默认缺省函数**

_复制代码_ 代码如下:

  
def foo(text,num=0):  
print text,num

foo("asd") #asd 0  
foo("def",100) #def 100  

定义有默认参数的函数时，这些默认值参数 位置必须都在非默认值参数后面。

调用时提供默认值参数值时，使用提供的值，否则使用默认值。

**2.Python可以根据参数名传参数**  

_复制代码_ 代码如下:

  
def foo(ip,port):  
print "%s:%d" % (ip,port)

foo("192.168.1.0",3306) #192.168.1.0:3306  
foo(port=8080,ip="127.0.0.1") #127.0.0.1:8080  

  
**第4行，没有指定参数名，按照顺序传参数。**

**第5行，指定参数名，可以按照参数名称传参数。**

3.可变长度参数  

_复制代码_ 代码如下:

  
#coding:utf-8 #设置python文件的编码为utf-8，这样就可以写入中文注释  
def foo(arg1,*tupleArg,**dictArg):  
print "arg1=",arg1 #formal_args  
print "tupleArg=",tupleArg #()  
print "dictArg=",dictArg #[]  
foo("formal_args")  

  
上面函数中的参数，tupleArg前面“*”表示这个参数是一个元组参数，从程序的输出可以看出，默认值为()；dicrtArg前面有“**”表示这个字典参数(键值对参数)。可以把tupleArg、dictArg看成两个默认参数。多余的非关键字参数，函数调用时被放在元组参数tupleArg中；多余的关键字参数，函数调用时被放字典参数dictArg中。

下面是可变长参数的一些用法：  

_复制代码_ 代码如下:

  
#coding:utf-8 #设置python文件的编码为utf-8，这样就可以写入中文注释  
def foo(arg1,arg2="OK",*tupleArg,**dictArg):  
print "arg1=",arg1  
print "arg2=",arg2  
for i,element in enumerate(tupleArg):  
print "tupleArg %d-->%s" % (i,str(element))  
for key in dictArg:  
print "dictArg %s-->%s" %(key,dictArg[key])

myList=["my1","my2"]  
myDict={"name":"Tom","age":22}  
foo("formal_args",arg2="argSecond",a=1)  
print "*"*40  
foo(123,myList,myDict)  
print "*"*40  
foo(123,rt=123,*myList,**myDict)  

输出为：

![](https://img.jbzj.com/file_images/article/201506/2015630110802328.png?201553011814)

从上面的程序可以看出：

(1)如代码第16行。

参数中如果使用“*”元组参数或者“**”字典参数，这两种参数应该放在参数列表最后。并且“*”元组参数位于“**”字典参数之前。

关键字参数rt=123,因为函数foo(arg1,arg2="OK",*tupleArg,**dictArg)中没有rt参数，所以最后也归到字典参数中。

(2)如代码第14行。

元组对象前面如果不带“*”、字典对象如果前面不带“**”，则作为普通的对象传递参数。

多余的普通参数，在foo(123,myList,myDict)中，123赋给参数arg1，myList赋给参数arg2，多余的参数myDict默认为元组赋给myList。

