使用Python内置函数：bin()、oct()、int()、hex()可实现进制转换。  
先看Python官方文档中对这几个内置函数的描述：  
**bin(x)**  
Convert an integer number to a binary string. The result is a valid Python
expression. If x is not a Python int object, it has to define an __index__()
method that returns an integer.  
**oct(x)  
** Convert an integer number to an octal string. The result is a valid Python
expression. If x is not a Python int object, it has to define an __index__()
method that returns an integer.  
int([number | string[, base]])  
Convert a number or string to an integer. If no arguments are given, return 0.
If a number is given, return number.__int__(). Conversion of floating point
numbers to integers truncates towards zero. A string must be a base-radix
integer literal optionally preceded by ‘+' or ‘-‘ (with no space in between)
and optionally surrounded by whitespace. A base-n literal consists of the
digits 0 to n-1, with ‘a' to ‘z' (or ‘A' to ‘Z') having values 10 to 35. The
default base is 10. The allowed values are 0 and 2-36. Base-2, -8, and -16
literals can be optionally prefixed with 0b/0B, 0o/0O, or 0x/0X, as with
integer literals in code. Base 0 means to interpret exactly as a code literal,
so that the actual base is 2, 8, 10, or 16, and so that int('010', 0) is not
legal, while int('010') is, as well as int('010', 8).  
**hex(x)  
** Convert an integer number to a hexadecimal string. The result is a valid
Python expression. If x is not a Python int object, it has to define an
__index__() method that returns an integer.  
↓  |  2进制  |  8进制  |  10进制  |  16进制  
---|---|---|---|---  
2进制  |  -  |  bin(int(x, 8))  |  bin(int(x, 10))  |  bin(int(x, 16))  
8进制  |  oct(int(x, 2))  |  -  |  oct(int(x, 10))  |  oct(int(x, 16))  
10进制  |  int(x, 2)  |  int(x, 8)  |  -  |  int(x, 16)  
16进制  |  hex(int(x, 2))  |  hex(int(x, 8))  |  hex(int(x, 10))  |  -  
  
bin()、oct()、hex()的返回值均为字符串，且分别带有0b、0o、0x前缀。

