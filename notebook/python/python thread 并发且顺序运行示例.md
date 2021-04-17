_复制代码_ 代码如下:

  
#-*- coding:utf-8 -*-  
import threading  
import time  
def fun(name, ls_name, front_thread = None):  
'''''  
线程启动函数  
通过front_thread来使用线程有序的运行  
'''  
time.clock()  
time.sleep(2)  
# 如果front_thread存在，则在front_thread运行完成后，才运行当前线程  
if front_thread != None:  
front_thread.join()  
ls_name.append(name)  
print "thread %s : %s"% (name, time.clock())  
  
if __name__ == '__main__':  
ls_result_name = []  
ls_thread = []  
time.clock()  
# 逐一启动1000个线程  
for i in range(0,10):  
if len(ls_thread) == 0:  
t = threading.Thread(target=fun, args=(i,ls_result_name,None))  
else:  
t = threading.Thread(target=fun, args=(i,ls_result_name,ls_thread[-1]))  
t.start()  
ls_thread.append(t)  
  
# 等待所有线程结束  
for t in ls_thread:  
t.join()  
  
print 'ls_result_name:', ls_result_name  
print "main thread:%s" % time.clock()  

  
运行结果为：  
thread 0 : 1.99962006344  
thread 1 : 2.00000866032  
thread 2 : 2.00059113658  
thread 3 : 2.00080345407  
thread 4 : 2.00100068584  
thread 5 : 2.00119456523  
thread 6 : 2.00138593033  
thread 7 : 2.00166753037  
thread 8 : 2.00211758757  
thread 9 : 2.0024776892  
ls_result_name: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  
main thread:2.003211302  
线程更明细的使用可参考：  
http://docs.python.org/library/threading.html  
time.clock模块的更详细介绍可参考：  
http://blog.csdn.net/kiki113/archive/2009/03/28/4033017.aspx

