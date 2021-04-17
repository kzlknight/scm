##  1. 监测端口

我们要引用的socket模块来校验端口是否被占用。

###  1.1 socket是什么？

简单一句话：网络上的两个程序通过一个双向的通信连接实现数据的交换，这个连接的一端称为一个socket。建立网络通信连接至少要一对端口号(socket)。

###  1.2 socket本质是什么？

socket本质是编程接口(API)，对TCP/IP的封装，TCP/IP也要提供可供程序员做网络开发所用的接口，这就是Socket编程接口。

关于socket的通讯原理，我们可以参考 [ socket通讯原理
](https://www.cnblogs.com/wangcq/p/3520400.html)  
关于socket模块内容，我们可以参考 [ python 的socket模块文档
](https://docs.python.org/3.7/library/socket.html)

我们上代码，看看如何检测端口是否被使用

```python

    # -*- coding: utf-8 -*-
    """
    @ auth : carl_DJ
    @ time : 2020-7-7
    """
    
    
    import socket
    
    def check_port(host,port):
     "检查端口是否被占用"
    
     #创建socket对象
     s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     try:
      s.connect((host,port))
      s.shutdown(2) #表示将来禁止读和写
     except OSError as msg:
      print("port %s is available !" %port)
      print(msg)
      return True
     else:
      print("port %s already in use! " %port)
      return False
    
    if __name__ == '__main__':
     host = '127.0.0.1'
     prot = 4723
     check_port(host,prot)
    
```

这里注意一点：  
shutdown(self,flag)：禁止在一个Socket上进行数据的接收和发送。  
利用shutdown()函数，使双向数据传输变为单向数据传输。  

参数：  
>0表示禁止将来读；  
>1表示禁止将来写  
>2表示禁止将来读和写。

**我们来看看代码执行结果：**  

如下图状态，说明服务器没有开启这个端口服务，所以这个端口是可以使用！  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020123111310428.png)

##  2. 释放端口

如果端口被占用，我们就需要释放它。  
那如何释放端口呢，？  
有两种方法：  
1.cmd窗口 释放 端口；  
2.python代码释放端口。

###  2.1 cmd 释放端口

1、先查找我们要需要的端口号

```python

    netstat -aon | findstr "5037"
```

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020123111310529.png)  

2、通过端口号，查找pid，然后杀死进程

```python

    taskkill -f -pid 18028
```

###  2.2 Python代码释放端口

那如果在python里面，如何实现呢？  
我们看代码：

```python

    # -*- coding: utf-8 -*-
    """
    @ auth : carl_DJ
    @ time : 2020-7-7
    """
    import os
    
    def release_port(port):
     "释放指定端口"
    
     #查找端口对应的pid
     cmd_find = 'netstat -ano | findstr %s' %port
     print(cmd_find)
    
     #返回命令执行结果
     result = os.popen(cmd_find).read()
     print(result)
    
     if str(port) and 'LISTENING' in result:
      #获取端口对应的pid进程
      i = result.index('LISTENING')
      # 'LISTENING'与端口号之间相隔7个空格
      start = i + len('LISTENING') +7
      end = result.index('\n')
      pid = result[start:end]
    
      #关闭被占用端口的pid
      cmd_kill = 'taskkill -f -pid %s' %pid
      print(cmd_kill)
      os.popen(cmd_kill)
     else:
      print('port %s is available !' %port)
    
    if __name__ == '__main__':
     host = '127.0.0.1'
     port = 4723
     release_port(port)
```

我们来瞅瞅，运行结果是啥：  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020123111310530.png)  

说明4723这个端口，是可用的。  
这里再说一句：  
os.popen() ：就是要打开一个管道，获取输入到cmd控制台的信息。  
更详细的内容，可以参考 [ pyhton的os.popen()官方文档
](https://docs.python.org/3/library/os.html#os.popen)  
当然，如果想飞速了解os.popen()与os.system()  
可以参照这篇《 [ 调用系统命令 os.system()和os.popen()
](https://www.jb51.net/article/203291.htm) 》文章。

到此这篇关于Python实现Appium端口检测与释放的实现的文章就介绍到这了,更多相关Python
Appium端口检测内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

