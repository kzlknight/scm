首先，来看每次处理一个字符的情况，可以有如下方法去实现：  
方法一：  

_复制代码_ 代码如下:

  
>>> a='1234567'  
>>> list(a)  
['1', '2', '3', '4', '5', '6', '7']  
>>>  

  
方法二：  

_复制代码_ 代码如下:

  
>>> a='1234567'  
>>> for i in a:  
... print i  
...  
1  
2  
3  
4  
5  
6  
7  
>>>  

  
方法三：列表解析(map)  

_复制代码_ 代码如下:

  
>>> a  
'1234567'  
>>> [int(i)+1 for i in a]  
[2, 3, 4, 5, 6, 7, 8]  
>>>  

  
但是如果每次处理两个字符或者更多的字符，上面的方法就不好用了，下面我总结了如下两种：

方法一：使用分片操作，每次处理两个字符：  

_复制代码_ 代码如下:

  
>>> a='abcdefghijk'  
>>> num=0  
>>> while True:  
... str = a[num:num+2]  
... if str:  
... print str  
... else:  
... break  
... num += 2  
...  
ab  
cd  
ef  
gh  
ij  
k  
>>>  

  
方法二：使用正则表达式，分割字符串，每次处理3个字符  

_复制代码_ 代码如下:

  
>>> import re  
>>> a="1234567890"  
>>> for i in re.findall(".{1,3}",a):  
... print i  
...  
123  
456  
789  
0  
>>>  

  
可以根据需求更改每次处理n个字符。

