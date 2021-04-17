**1 拷贝下面的代码到一个文件，并命名为forkcore.py**

_复制代码_ 代码如下:

  
import os  
import threading  
import select  
import socket

class ds_forkcore(object):  
  
#async IO(epoll)  
def ds_epoll(self):  
epoll=select.epoll()  
epoll.register(self.s.fileno(),select.EPOLLIN|select.EPOLLET)  
while 1:  
epoll_list=epoll.poll()  
for fd,_events in epoll_list:  
if fd==self.s.fileno():  
conn,addr=self.s.accept()  
print "Current process's pid is "+str(os.getpid())  
self.worker(conn,addr)  
  
#multi_thread  
def ds_thread(self,thread_num=100):  
for _ in range(0,thread_num):  
t=threading.Thread(target=self.ds_epoll)  
t.setDaemon(1)  
t.start()  
t.join()  
  
#multi_process  
def ds_process(self,child_process_num=8):  
pid=os.getpid()  
print "Main process start, pid is "+str(pid)  
for _ in range(0,child_process_num):  
if pid==os.getpid():  
if os.fork():  
pass  
else:  
print "Worker process start, pid is "+str(os.getpid())  
self.ds_thread()  
  
#init function  
def __init__(self,worker,port=3333):  
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)  
s.bind(("",port))  
s.listen(50000)  
self.s=s  
self.worker=worker  
self.ds_process()  

2 编写自己的代码

1> 导入forkcore库。

2> 定义worker函数，worker函数需要两个参数，conn代表客户端连接的socket，addr是(ip,port)的元组。

3> 直接使用forkcore.ds_forecore(worker,port=5555)即可，port用于指定监听端口。

_复制代码_ 代码如下:

  
import forkcore

if __name__=="__main__":  
def worker(conn,addr):  
print "Message from ("+str(addr[0])+":"+str(addr[1])+"):
"+conn.recv(1024)[0:-1]  
  
forkcore.ds_forkcore(worker,port=5555)  

注：需要linux 2.6以上的内核

