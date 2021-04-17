_复制代码_ 代码如下:

  
#coding: utf-8  
import socket  
import select  
import time  
import os  
import threading

def ser():  
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  
s.bind(("",43244))  
while 1:  
infds,outfds,errfds = select.select([s],[],[],5)  
if infds:  
sms = s.recv(1024)  
if sms=="alived":  
print "peer is alived"  
else:  
print "Can't hear peer!"  
os.system("./failover.sh")

def clt():  
while 1:  
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
sock.connect(('192.168.10.1', 43244))  
sock.send("alived")  
time.sleep(2)

if __name__=="__main__":  
ser=threading.Thread(target=ser)  
clt=threading.Thread(target=clt)  
ser.start()  
clt.start()  
ser.join()  
clt.join()  

failover.sh

_复制代码_ 代码如下:

  
#!/bin/bash

vip=8.8.8.8

vip_local=`ifconfig |grep -A 1 "eth0:0" |awk '/inet addr/{print $2}'|cut -d
":" -f2`

if [ ! $vip_local ];then ifconfig eth0:0 $vip netmask 255.255.255.0 up;fi  

