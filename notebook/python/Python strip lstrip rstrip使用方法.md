注意的是，传入的是一个字符数组，编译器去除两端所有相应的字符，直到没有匹配的字符，比如：  
  

_复制代码_ 代码如下:

  
theString = 'saaaay yes no yaaaass'  
print theString.strip('say')  

  
theString依次被去除首尾在['s'，'a'，'y']数组内的字符，直到字符在不数组内。所以，输出的结果为：  
yes no  
比较简单吧，lstrip和rstrip原理是一样的。注意：当没有传入参数时，是默认去除首尾空格的。  
  

_复制代码_ 代码如下:

  
theString = 'saaaay yes no yaaaass'  
print theString.strip('say')  
print theString.strip('say ') #say后面有空格  
print theString.lstrip('say')  
print theString.rstrip('say')  

  
运行结果：  
yes no  
es no  
yes no yaaaass  
saaaay yes no

