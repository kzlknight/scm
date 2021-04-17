本文实例讲述了python 协程 gevent原理与用法。分享给大家供大家参考，具体如下：

**gevent**

greenlet已经实现了协程，但是这个还的人工切换，是不是觉得太麻烦了，不要捉急，python还有一个比greenlet更强大的并且能够自动切换任务的模块gevent

其原理是当一个greenlet遇到IO(指的是input output
输入输出，比如网络、文件操作等)操作时，比如访问网络，就自动切换到其他的greenlet，等到IO操作完成，再在适当的时候切换回来继续执行。

由于IO操作非常耗时，经常使程序处于等待状态，有了gevent为我们自动切换协程，就保证总有greenlet在运行，而不是等待IO

**安装**

```python

    pip3 install gevent
```

**1. gevent的使用**

```python

    import gevent
    def f(n):
      for i in range(n):
        print(gevent.getcurrent(), i)
    g1 = gevent.spawn(f, 5)
    g2 = gevent.spawn(f, 5)
    g3 = gevent.spawn(f, 5)
    g1.join()
    g2.join()
    g3.join()
    
    
```

运行结果

> <Greenlet at 0x10e49f550: f(5)> 0  
>  <Greenlet at 0x10e49f550: f(5)> 1  
>  <Greenlet at 0x10e49f550: f(5)> 2  
>  <Greenlet at 0x10e49f550: f(5)> 3  
>  <Greenlet at 0x10e49f550: f(5)> 4  
>  <Greenlet at 0x10e49f910: f(5)> 0  
>  <Greenlet at 0x10e49f910: f(5)> 1  
>  <Greenlet at 0x10e49f910: f(5)> 2  
>  <Greenlet at 0x10e49f910: f(5)> 3  
>  <Greenlet at 0x10e49f910: f(5)> 4  
>  <Greenlet at 0x10e49f4b0: f(5)> 0  
>  <Greenlet at 0x10e49f4b0: f(5)> 1  
>  <Greenlet at 0x10e49f4b0: f(5)> 2  
>  <Greenlet at 0x10e49f4b0: f(5)> 3  
>  <Greenlet at 0x10e49f4b0: f(5)> 4

可以看到，3个greenlet是依次运行而不是交替运行

**2. gevent切换执行**

```python

    import gevent
    def f(n):
      for i in range(n):
        print(gevent.getcurrent(), i)
        #用来模拟一个耗时操作，注意不是time模块中的sleep
        gevent.sleep(1)
    g1 = gevent.spawn(f, 5)
    g2 = gevent.spawn(f, 5)
    g3 = gevent.spawn(f, 5)
    g1.join()
    g2.join()
    g3.join()
    
    
```

运行结果

> <Greenlet at 0x7fa70ffa1c30: f(5)> 0  
>  <Greenlet at 0x7fa70ffa1870: f(5)> 0  
>  <Greenlet at 0x7fa70ffa1eb0: f(5)> 0  
>  <Greenlet at 0x7fa70ffa1c30: f(5)> 1  
>  <Greenlet at 0x7fa70ffa1870: f(5)> 1  
>  <Greenlet at 0x7fa70ffa1eb0: f(5)> 1  
>  <Greenlet at 0x7fa70ffa1c30: f(5)> 2  
>  <Greenlet at 0x7fa70ffa1870: f(5)> 2  
>  <Greenlet at 0x7fa70ffa1eb0: f(5)> 2  
>  <Greenlet at 0x7fa70ffa1c30: f(5)> 3  
>  <Greenlet at 0x7fa70ffa1870: f(5)> 3  
>  <Greenlet at 0x7fa70ffa1eb0: f(5)> 3  
>  <Greenlet at 0x7fa70ffa1c30: f(5)> 4  
>  <Greenlet at 0x7fa70ffa1870: f(5)> 4  
>  <Greenlet at 0x7fa70ffa1eb0: f(5)> 4

**3. 给程序打补丁**

```python

    from gevent import monkey
    import gevent
    import random
    import time
    def coroutine_work(coroutine_name):
      for i in range(10):
        print(coroutine_name, i)
        time.sleep(random.random())
    gevent.joinall([
        gevent.spawn(coroutine_work, "work1"),
        gevent.spawn(coroutine_work, "work2")
    ])
    
    
```

运行结果

> work1 0  
>  work1 1  
>  work1 2  
>  work1 3  
>  work1 4  
>  work1 5  
>  work1 6  
>  work1 7  
>  work1 8  
>  work1 9  
>  work2 0  
>  work2 1  
>  work2 2  
>  work2 3  
>  work2 4  
>  work2 5  
>  work2 6  
>  work2 7  
>  work2 8  
>  work2 9

更多关于Python相关内容感兴趣的读者可查看本站专题：《 [ Python进程与线程操作技巧总结
](//www.jb51.net/Special/878.htm) 》、《 [ Python数据结构与算法教程
](//www.jb51.net/Special/663.htm) 》、《 [ Python函数使用技巧总结
](//www.jb51.net/Special/642.htm) 》、《 [ Python字符串操作技巧汇总
](//www.jb51.net/Special/636.htm) 》、《 [ Python入门与进阶经典教程
](//www.jb51.net/Special/520.htm) 》、《 [ Python+MySQL数据库程序设计入门教程
](//www.jb51.net/Special/864.htm) 》及《 [ Python常见数据库操作技巧汇总
](//www.jb51.net/Special/681.htm) 》

希望本文所述对大家Python程序设计有所帮助。

