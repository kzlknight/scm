python可以使用os模块中的system函数来启动外部程序。

Windows平台下使用start命令就可以不阻塞当前进程的执行程序，测试代码如下：

> import os
>
> os.system('start calc')

**补充知识：** **Python：启动大量子进程**

我就废话不多说了，大家还是直接看代码吧~

```python

    #!/usr/bin/env python
    # coding:UTF-8 
     
    """
    @version: python3.x
    @author:曹新健
    @contact: 617349013@qq.com
    @software: PyCharm
    @file: 5.启动大量子进程.py
    @time: 2018/9/18 22:28
    """ 
    from multiprocessing import Process,Pool
    import time,os,random
     
    def run(num):
     print("子进程%d启动---%s" % (num,os.getpid()))
     start = time.time()
     time.sleep(random.choice([1,2,3]))
     end = time.time()
     #print(end)
     print("子进程%d结束---%s---耗时%.2f" % (num, os.getpid(),end-start))
     
    if __name__ == "__main__":
     print("父进程启动")
     #创建进程池,Pool默认为CPU核心数
     pp = Pool()
     for i in range(8):
      #创建进程，放入进程池统一管理
      result = pp.apply_async(run,args=(i,))
     
     #进程池在调动join之前必须先调动close，调用close之后就不能再继续添加新的进程了
     pp.close()
     pp.join()
     
     print("父进程结束")
     
```

以上这篇python实现启动一个外部程序,并且不阻塞当前进程就是小编分享给大家的全部内容了，希望能给大家一个参考，也希望大家多多支持脚本之家。

