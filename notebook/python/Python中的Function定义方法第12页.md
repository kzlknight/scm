下面就先定义一个函数：  

_复制代码_ 代码如下:

  
def foo():  
print('function')  
foo()  

  
在上述代码中，定义了一个名为foo的函数，这个函数没有参数。最后一行代码的功能是调用这个函数。这是一个函数的最简单形式。下面来介绍一下有参数的函数：  

_复制代码_ 代码如下:

  
def foo():  
print('function')  
def foo1(a,b):  
print(a+b)  
foo()  
foo1(1,2)  

  
foo1就是一个有参数的函数，使用foo1(1,2)就可以调用这个有参的函数了。  
  
在程序中，有变量存在，就会涉及到变量的作用域的问题。在Python中，变量的作用域分三个等级：global、local和nonlocal。  
  
global：顾名思义，表示全局变量。即这个变量在python中处于最高层次上，也就是这个变量的定义层次最高，而不是在函数或类中。  
local：局部变量，被定义在函数之中。  
nonlocal：这是一个相对的概念。在python中，函数内部可以嵌套定义内部函数，这样函数内部的变量相对于函数内部的内嵌函数来讲就是nonlocal的。  
下面，给出相关的程序来说明，首先看一下全局和局部变量：  

_复制代码_ 代码如下:

  
x = 1  
y = 2  
def foo(x):  
print(x)  
print(y)  
print('***********')  
x = 3  
global y  
y = 3  
print(x)  
print(y)  
print('***********')  
foo(x)  
print(x)  
print(y)  
  
#************************  
#运行结果  
1  
2  
***********  
3  
3  
***********  
1  
3  

  
在上述程序中，定义了两个全局变量x和y，
在函数foo内部，也定义了一个局部变量x。根据运行结果可知，在foo内部，变量x是真正的局部变量。因为对其所做的修改并没有对全局变量x产生影响。另外，如果在foo内部需要使用全局变量，则需要使用global关键字。global
y的意图就是声明变量y为外部声明过的全局变量y。所以，在foo内部对y进行修改后，在foo外部仍然有影响。因为foo修改的是全局变量。  
再来看一下nonlocal：  

_复制代码_ 代码如下:

  
def out():  
z = 3  
def inner():  
nonlocal z  
z = 4  
print('inner function and z = {0}'.format(z))  
inner()  
print('out function and z = {0}'.format(z))  
out()  
#**********  
#运行结果  
inner function and z = 4  
out function and z = 4  

  

**1** [ 2 ](20142_2.htm) [ 下一页 ](20142_2.htm) [ 阅读全文 ](20142_all.htm)

