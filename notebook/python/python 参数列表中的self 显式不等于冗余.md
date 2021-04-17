self在区分全局变量/函数和对象中的成员变量/函数十分有用。例如，它提供了一种作用域机制，我个人认为比Ruby的@和@@清晰多了，这可能是习惯使然吧，但它确实和C++、Java中的this很相似。  
然而，self总是有令我困扰的地方，我以前在这里说过―我曾幻想能在Python3中这些能得以改进，然后通常会引发一轮热议并最终以人们所说的“显胜于隐”告终。  
我在巴西的时候曾和Luciano
Ramalho（巴西Python组织的主席）有过一次交谈。他让我明白并非无处不在的self让我困扰不已，而是参数列表中的self，我想也称为非pythonic（un-
pythonic）。  
它是如何使用的  
下面是一些简单的Python代码，说明了如何使用类。  

_复制代码_ 代码如下:

  
def f(): pass  
a = 1  
class C1(object):  
a = 2  
def m1(self):  
print a # Prints '1'  
print self.a # Prints '2'  
f() # The global version  
self.m2() # Must scope other members  
def m2(self): pass  
obj = C1()  
obj.m1()  

  
首先看f()和a，它们都可在全局作用域中调用。类C1被定义成继承自object，这是定义一个新类的标准过程（我想在Python3中这些会变得更加不明显）。  
注意，m1()和m2()的第一个参数都是self。在Python中，self不是关键字。但按照惯例“self”代表当前对象的地址，也就是对象的地址通常是第一个参数。  
在类范围上定义a是创建对象作用域的方式之一。你也可以在a的method里赋值给self.a，并且第一次运行该语句时就分配了这个域的内存空间。但有必要区分两种版本的a。若在method内部使用a，那么这个a就是全局版本的，而self.a体现的是对象域（你也可以在类内部对全局变量进行赋值，这里我暂不考虑这种情况）。  
同样地，一个对f()的非限定调用（unqualified
call）造就了全局函数，通过对其限定self.m2()调用的是成员函数（同时将当前对象地址作为传递给m2()的self变量）。  
现在来看一个含有带参数的method的类：  

_复制代码_ 代码如下:

  
class C2(object):  
def m2(self, a, b): pass  

  
为了调用该method，我们创建了一个对象实例，然后使用点表达式调用对象obj上的m2()：  

_复制代码_ 代码如下:

  
obj = C2()  
obj.m2(1,2)  

  
在调用过程中，obj的地址作为self变量在m2()中隐含传递，这里遇到了一个严重的矛盾：为何当定义method时隐式好于显式，而调用method时隐式也毫无问题？  
当然我想这可能是method调用语法所要求的，但这就意味着method的定义和调用有很大不同，这里既没有“显式”也不pythonic。在调用参数个数错误的method时就能看出来：  
obj.m2(1)  
结果错误提示为：  
Traceback (most recent call last):  
File "classes.py", line 9, in <module>  
obj.m2(1)  
TypeError: m2() takes exactly 3 arguments (2 given)  
由于method调用期间self的隐式参数传递，上述错误信息实际是说应该这样调用method：  
C2.m2(obj,1,2)  
即使上面这行语句运行成功，它当然也不是实际的调用方式。你应该使用常规的method调用语法，即传递两个参数：  
obj.m2(1,2)  
错误信息“m2() takes exactly 3 arguments (2
given)”不仅让初学者十分糊涂，我每次看到它后也常常懵住。我想这既表明了它是非Pythonic、也直指method定义和调用的矛盾。  
绝望的建议  
尽管漫长历史中尽是绝望，我又有哪些建议呢？  
在Python3.1中增加self为关键字（有一点更加向后不兼容）（或直接使用this来使C++和Java程序员时更容易过渡）。而所有与self有关的已有规则都不变。  
唯一的改变是：你不必将self放入method参数列表中。这是唯一隐式的地方，其它都是显式的―除了依旧不变的method调用。  
它实现了method定义和调用的一致性。你可以定义一个与调用时具有相同参数个数的method。当调用method所传递参数个数出错时，错误信息会通知method应含有的实际参数个数，而不是多出一个。  
显式 vs.冗余  
在我再一次听到“显胜于隐”之前，让某件事变得清晰和变得冗余还是有区别的。我们已有这样一种语言：它让你历经了无数考验，原因就是起初看起来似乎很好但之后问题却越来越多。它叫做Java。  
如果想让每一件东西都变为显式，我们可以使用C或汇编以及其它能够精确说明和展现机器内部运行细节的语言。  
强制程序员将self放入method参数列表与显式根本不沾边，它只是强制造成冗余的做法，也不会增加编程的表达方式（已经知道是一个method了，何必还要在参数列表中加入self来提醒我们呢）。我认为，它是死板的，也是非pythonic。

