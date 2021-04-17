受控节点slave.py

_复制代码_ 代码如下:

  
import socket  
import re  
class Log(object):  
file_list=['access.log','C:\\access.log']  
master_ip='192.168.0.103'  
def __init__(self):  
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
s.bind(('',3333))  
s.listen(1)  
while True:  
conn,addr=s.accept()  
print addr[0]  
if addr[0]==self.master_ip:  
reg=conn.recv(1024)  
result=self.all_log(reg)  
conn.sendall(result)  
conn.close()

def all_log(self,reg):  
logs=''  
for f in self.file_list:  
logs+='\n'+self.log_match(f,reg)  
return logs

def log_match(self,f,reg):  
log_result='------------------------'+f+'------------------------'+'\n'  
fo=open(f,'r')  
line=fo.readline()  
rp=re.compile(reg)  
while line!='':  
log_match=rp.match(line)  
if log_match:  
log_result+='\n'+log_match.group()  
line=fo.readline()  
return log_result

if __name__=='__main__':  
ds=Log()  

主控节点master.py

_复制代码_ 代码如下:

  
import socket  
class SlvCluster(object):  
ip_list=['127.0.0.1']  
def __init__(self,reg):  
for ip in self.ip_list:  
self.single_slv(ip,reg)  
def single_slv(self,slv_ip,reg):  
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
s.connect((slv_ip,3333))  
s.sendall(reg)  
print '-----------------------'+slv_ip+'--------------------------'  
print s.recv(102400)  
s.close()  
if __name__=='__main__':  
reg=raw_input('Input the regular expression:')  
print '-----------Regular Expression: '+reg+'-----------------'  
sc=SlvCluster(reg)  

