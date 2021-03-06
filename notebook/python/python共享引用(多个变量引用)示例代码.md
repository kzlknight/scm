_复制代码_ 代码如下:

  
a = 3  
b = a  

先上图（图1）吧，大家一看就一目了然了：  
  
![](https://img.jbzj.com/file_images/article/201312/20131204112421.jpg?2013114112911)

  
变量名和对象，在运行赋值语句b = a之后，变量a,b都指向了对象3的内存空间.  
假设这时执行 a = 'python', a将指向刚创建的字符串对象。  
我们再来试试这种情况:

_复制代码_ 代码如下:

  
>>>list_1 = [1,2,3,4]  
>>>list_2 = list_1  
>>>list_2  
>>>list_1[0] = 'python'  
>>>list_2  

result:  

_复制代码_ 代码如下:

  
[1,2,3,4]  
['python',2,3,4]  

  
  
![](https://img.jbzj.com/file_images/article/201312/20131204112522.jpg?2013114113031)

从我的理解上来解释的话: list是一个类型对象，而对象里的每一个元素可以看成是变量，去引用了不同内存空间的对象list_1 =
[1,2,3,4]是让list_1指向list的内存空间，list_2 =
list_1时，他们将指向同一个内存空间。当List_1[0]改变指向时，list_2依然指向list对象的，所以看是改变list_1[0]的值，实际上是python通过list_1直接到内存空间去做了修改，list_2的指向没有任何变量。  
或许这种结果并不是我们想要的。如果你不想要这样的现象发生，需要python对象拷贝，而不是创建引用。  
如：  
  
![](https://img.jbzj.com/file_images/article/201312/20131204112556.jpg?2013114112646)  

