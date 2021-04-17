python2.4版本以后，如果int的值超出范围不会溢出，而是内部转换为long，在网上没有找到从long型强制转换成int的代码，这里所说的int取值范围是和java里一致，即用四个字节表示。  
自己写了一个函数，勉强可以用，供大家参考。

_复制代码_ 代码如下:

  
import sys  
def LongToInt(value):  
assert isinstance(value, (int, long))  
return int(value & sys.maxint)  

经过测试，在32位和64位上运算结果一致。

