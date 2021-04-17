之前小编介绍过python中将字符串小写字符转为大写的upper函数的使用方法（upper函数）。有将小写转为大写的需要，那也有将大写转为小写的情况。本文主要介绍在python中可以将字符串大写自摸转换为小写字母的lower函数。

###  1、lower()

转换字符串中所有大写字符为小写

###  2、语法

```python

    str.lower() -> str
```

###  3、返回值

返回将字符串中的所有大写字母转换为小写字母的字符串

###  4、使用实例

```python

    #!/usr/bin/python3
    str = "ABCDEFG"
    print( str.lower() )
```

输出

> abcdefg

以上就是python中lower函数的介绍，如果需要将字符串中个的大写转为小写，可以使用lower函数哦

lower函数实例

```python

    #实现lower
    def my_lower(string):
      if not string:
        return None
      
      lst = list(string)
      for index,item in enumerate(lst):#同时列出数字和下标
        ascii_index = ord(item)
        if 65 <= ascii_index <= 90:
          s = chr(ascii_index+32)
          lst[index] = s
      return ''.join(lst)
    
    if __name__ == '__main__':
      print(my_lower("2345ZRdV"))
    
```

到此这篇关于python中lower函数实现方法及用法讲解的文章就介绍到这了,更多相关如何实现python中lower函数内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

