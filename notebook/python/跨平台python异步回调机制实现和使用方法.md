1 将下面代码拷贝到一个文件，命名为asyncore.py

_复制代码_ 代码如下:

  
import socket  
import select  
import sys

def ds_asyncore(addr,callback,timeout=5):  
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
s.connect(addr)  
r,w,e = select.select([s],[],[],timeout)  
if r:  
respose_data=s.recv(1024)  
callback(respose_data)  
s.close()  
return 0  
else:  
s.close()  
return 1  

2 编写自己的代码

1> 导入asyncore

2> 定义回调函数callback,callback需要一个参数，代表请求返回数据

3> 直接调用asyncore.ds_asyncore(('127.0.0.1',
33333),callback,timeout=5)，其中第一个参数是一个(ip,port)元组，第二个是回调函数，第三个是超时时间。

_复制代码_ 代码如下:

  
import asyncore

if __name__=="__main__":  
def callback(respose_data):  
print respose_data  
asyncore.ds_asyncore(('127.0.0.1', 33333),callback,timeout=5)  

注：此代码可在windows,linux上运行

