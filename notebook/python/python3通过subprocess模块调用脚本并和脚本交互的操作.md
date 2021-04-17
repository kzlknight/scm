因工作需要，需实现如题所示功能。查阅网上博客，资料，大多都是针对python2的，而且很多地方不明所以，所以自己整理了一下查阅的结果，重新写一篇博客。

**预备知识**

**1、python3的默认字符串类型**

Python 2.x 同时支持ASCII和 Unicode字符串，默认情况下是ASCII编码。而 Python
3中这种支持刚好调换：Unicode现在变成了默认类型，而 ASCII 字符串现在称为 bytes。 bytes 数据结构包含字节值，并且它

不应该再被视为一个字符串，因为它是一个包含数据的不可变字节数组

上面这句话出自《python核心编程》（第三版）。这造成了python2和python3的很大的不兼容性。就是很多方法在python2中可用，但是在python3中不可用。幸运的是python提供了解决这种问题的方法。

如果想把默认字符串转换成bytes类型，既把Unicode变成ASCII

```python

    # 方法一
    bytes("str",encoding="utf8") # encoding="utf8"参数不可省略
    egg:
     bytes("中国",encoding="gbk")
     b'\xd6\xd0\xb9\xfa'
     bytes("中国",encoding="utf-8")
     b'\xe4\xb8\xad\xe5\x9b\xbd'
    #方法二
    "str".encode(encoding="utf8") # encoding="utf8"可省略，因为已经是默认参数
    egg:
     "中国".encode(encoding="gbk")
     b'\xd6\xd0\xb9\xfa'
     "中国".encode(encoding="utf8")
     b'\xe4\xb8\xad\xe5\x9b\xbd'
     
    #上面两种方法的意思是一样的，就是按某种编码的方式，将Unicode转变成ASCII。其中utf8是Unicode码的一种存储类型或者实现类型（这个不是很清楚），常见的还有utf16等
```

如果想把bytes字符串转换成Unicode类型

```python

    bytes.decode( bytes码,encoding="编码方式" ) # bytes码的一般格式是 ： b+字符串，如 b'abc'
    egg:
     bytes.decode(b'\xe4\xb8\xad\xe5\x9b\xbd',encoding="utf-8")
     '中国'
     bytes.decode(b'\xd6\xd0\xb9\xfa',encoding="gbk")
     '中国'
```

**2、sys模块的stdout,stdin,stderr***

```python

    sys.stdout.write(str) #将字符串str写入pipe,因为pipe的默认出口是终端，所以这句等价于 ：print(str)
    sys.stdin.readline() #从pipe读入一行数据，因为pipe的默认入口是终端，所以这里可以从终端输入数据
    
    # 此外,需要注意的是这里的str使用unicode类型的字符串即可，不需要bytes类型的字符串
    
```

**正式内容**

建立文件src/main.py

```python

     import subprocess as sub
     import sys
    
     popen = sub.Popen("python ./test.py", stdin=sub.PIPE, stdout=sub.PIPE, stderr=sub.PIPE) #将输入，输出，错误都定向到新的pipe
    
     for line in sys.stdin: # 读取终端输入
      popen.stdin.write(line.encode(encoding="utf8")) # 写入pip,write的参数要是bytes类型
      popen.stdin.flush() #必须
      output = popen.stdout.readline() #从子进程读取数据，读到的结果是bytes类型
      sys.stdout.write(bytes.decode(output)) # sys模块stdout的参数要求是字符串，所以要解码，相当于print(out)
    
```

建立文件src/test.py，

```python

    import sys
    
    while True:
     line = sys.stdin.readline() #读取父进程写入的内容
     sys.stdout.write(line) #将读到的内容返回给父进程，可哟用print代替
     # 注意：子进程的内容是无法打印的，其输出的任何信息都会发送给父进程，所以我们通过输出判断line变量是bytes类型还是unicode类型，但是根据上一个文件的sys.stdout.write(bytes.decode(output)语句可知应该是str类型。
    
```

**补充知识：** **python中多进程子进程使用input（）为什么运行会报EOFError**

关于python3多进程中，子进程中从键盘录入值，运行报错问题。

![](https://img.jbzj.com/file_images/article/202012/20201205143306.jpg)

在python中，主进程允许从键盘录入值。而子进程是不允许的。

以上这篇python3通过subprocess模块调用脚本并和脚本交互的操作就是小编分享给大家的全部内容了，希望能给大家一个参考，也希望大家多多支持脚本之家。

