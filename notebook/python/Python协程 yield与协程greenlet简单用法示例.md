本文实例讲述了Python协程 yield与协程greenlet简单用法。分享给大家供大家参考，具体如下：

**协程**

协程，又称微线程，纤程。英文名Coroutine。

**协程是啥**

协程是python个中另外一种实现多任务的方式，只不过比线程更小占用更小执行单元（理解为需要的资源）。
为啥说它是一个执行单元，因为它自带CPU上下文。这样只要在合适的时机， 我们可以把一个协程 切换到另一个协程。 只要这个过程中保存或恢复
CPU上下文那么程序还是可以运行的。

通俗的理解：在一个线程中的某个函数，可以在任何地方保存当前函数的一些临时变量等信息，然后切换到另外一个函数中执行，注意不是通过调用函数的方式做到的，并且切换的次数以及什么时候再切换到原来的函数都由开发者自己确定

**协程和线程差异**

在实现多任务时, 线程切换从系统层面远不止保存和恢复 CPU上下文这么简单。
操作系统为了程序运行的高效性每个线程都有自己缓存Cache等等数据，操作系统还会帮你做这些数据的恢复操作。
所以线程的切换非常耗性能。但是协程的切换只是单纯的操作CPU的上下文，所以一秒钟切换个上百万次系统都抗的住。

**简单实现协程**

```python

    import time
    def work1():
      while True:
        print("----work1---")
        yield
        time.sleep(0.5)
    def work2():
      while True:
        print("----work2---")
        yield
        time.sleep(0.5)
    def main():
      w1 = work1()
      w2 = work2()
      while True:
        next(w1)
        next(w2)
    if __name__ == "__main__":
      main()
    
    
```

运行结果：

> ----work1---  
>  ----work2---  
>  ----work1---  
>  ----work2---  
>  ----work1---  
>  ----work2---  
>  ----work1---  
>  ----work2---  
>  ----work1---  
>  ----work2---  
>  ----work1---  
>  ----work2---  
>  ...省略...

**greenlet**

为了更好使用协程来完成多任务，python中的greenlet模块对其封装，从而使得切换任务变的更加简单

**安装方式**

使用如下命令安装greenlet模块:

```python

    sudo pip3 install greenlet
    
    
```

```python

    #coding=utf-8
    from greenlet import greenlet
    import time
    def test1():
      while True:
        print "---A--"
        gr2.switch()
        time.sleep(0.5)
    def test2():
      while True:
        print "---B--"
        gr1.switch()
        time.sleep(0.5)
    gr1 = greenlet(test1)
    gr2 = greenlet(test2)
    #切换到gr1中运行
    gr1.switch()
    
    
```

运行效果

> ---A--  
>  ---B--  
>  ---A--  
>  ---B--  
>  ---A--  
>  ---B--  
>  ---A--  
>  ---B--  
>  ...省略...

更多关于Python相关内容感兴趣的读者可查看本站专题：《 [ Python进程与线程操作技巧总结
](//www.jb51.net/Special/878.htm) 》、《 [ Python数据结构与算法教程
](//www.jb51.net/Special/663.htm) 》、《 [ Python函数使用技巧总结
](//www.jb51.net/Special/642.htm) 》、《 [ Python字符串操作技巧汇总
](//www.jb51.net/Special/636.htm) 》、《 [ Python入门与进阶经典教程
](//www.jb51.net/Special/520.htm) 》、《 [ Python+MySQL数据库程序设计入门教程
](//www.jb51.net/Special/864.htm) 》及《 [ Python常见数据库操作技巧汇总
](//www.jb51.net/Special/681.htm) 》

希望本文所述对大家Python程序设计有所帮助。

