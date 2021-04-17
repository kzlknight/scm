_复制代码_ 代码如下:

  
if (typeof(objA) == typeof(String))  
{  
//TODO  
}  

  
在Python中只需要使用内置的函数isinstance，使用起来非常简单，比如下面的例子：  
  

_复制代码_ 代码如下:

  
class objA:  
pass  
  
A = objA()  
B = 'a','v'  
C = 'a string'  
  
print isinstance(A, objA)  
print isinstance(B, tuple)  
print isinstance(C, basestring)  

输出结果：  
True  
True  
True  

