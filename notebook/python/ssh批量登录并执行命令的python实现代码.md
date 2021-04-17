局域网内有一百多台电脑，全部都是linux操作系统，所有电脑配置相同，系统完全相同（包括用户名和密码），ip地址是自动分配的。现在有个任务是在这些电脑上执行某些命令，者说进行某些操作，比如安装某些软件，拷贝某些文件，批量关机等。如果一台一台得手工去操作，费时又费力，如果要进行多个操作就更麻烦啦。  
或许你会想到网络同传，
网络同传是什么？就是在一台电脑上把电脑装好，配置好，然后利用某些软件，如“联想网络同传”把系统原样拷贝过去，在装系统时很有用，只要在一台电脑上装好，同传以后所有的电脑都装好操作系统了，很方便。同传要求所有电脑硬件完全相同，在联想的电脑上装的系统传到方正电脑上肯定会出问题的。传系统也是很费时间的，根据硬盘大小，如果30G硬盘，100多台电脑大约要传2个多小时，反正比一台一台地安装快！但是如果系统都传完了，发现忘了装一个软件，或者还需要做些小修改，再同传一次可以，但是太慢，传两次半天时间就没了。这时候我们可以利用ssh去控制每台电脑去执行某些命令。  
先让我们回忆一下ssh远程登录的过程：首先执行命令 ssh username@192.168.1.x
，第一次登录的时候系统会提示我们是否要继续连接，我们要输入“yes”，然后等一段时间后系统提示我们输入密码，正确地输入密码之后我们就能登录到远程计算机，然后我们就能执行命令了。我们注意到这里面有两次人机交互，一次是输入‘yes'，另一次是输入密码。就是因为有两次交互我们不能简单的用某些命令去完成我们的任务。我们可以考虑把人机交互变成自动交互，python的pexpect模块可以帮我们实现自动交互。下面这段代码是用pexpect实现自动交互登录并执行命令的函数：  

_复制代码_ 代码如下:

  
#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
import pexpect  
def ssh_cmd(ip, passwd, cmd):  
ret = -1  
ssh = pexpect.spawn('ssh root@%s "%s"' % (ip, cmd))  
try:  
i = ssh.expect(['password:', 'continue connecting (yes/no)?'], timeout=5)  
if i == 0 :  
ssh.sendline(passwd)  
elif i == 1:  
ssh.sendline('yes\n')  
ssh.expect('password: ')  
ssh.sendline(passwd)  
ssh.sendline(cmd)  
r = ssh.read()  
print r  
ret = 0  
except pexpect.EOF:  
print "EOF"  
ssh.close()  
ret = -1  
except pexpect.TIMEOUT:  
print "TIMEOUT"  
ssh.close()  
ret = -2  
return ret  

  
利用pexpect模块我们可以做很多事情，由于他提供了自动交互功能，因此我们可以实现ftp，telnet，ssh，scp等的自动登录，还是比较实用的。根据上面的代码相信读者已经知道怎么实现了（python就是那么简单！）。  
用上面的代码去完成任务还是比较费时间的，因为程序要等待自动交互出现，另外ubuntu用ssh连接就是比较慢，要进行一系列的验证，这样才体现出ssh的安全。我们要提高效率，在最短的时间内完成。后来我发现了python里面的paramiko模块，用这个实现ssh登录更加简单。看下面的代码：  

_复制代码_ 代码如下:

  
#-*- coding: utf-8 -*-  
#!/usr/bin/python  
import paramiko  
import threading  
def ssh2(ip,username,passwd,cmd):  
try:  
ssh = paramiko.SSHClient()  
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
ssh.connect(ip,22,username,passwd,timeout=5)  
for m in cmd:  
stdin, stdout, stderr = ssh.exec_command(m)  
# stdin.write("Y") #简单交互，输入 ‘Y'  
out = stdout.readlines()  
#屏幕输出  
for o in out:  
print o,  
print '%s\tOK\n'%(ip)  
ssh.close()  
except :  
print '%s\tError\n'%(ip)  
if __name__=='__main__':  
cmd = ['cal','echo hello!']#你要执行的命令列表  
username = "" #用户名  
passwd = "" #密码  
threads = [] #多线程  
print "Begin......"  
for i in range(1,254):  
ip = '192.168.1.'+str(i)  
a=threading.Thread(target=ssh2,args=(ip,username,passwd,cmd))  
a.start()  

  
上面的程序还是有些技巧的：  
1.利用多线程，同时发出登录请求，同时去连接电脑，这样速度快很多，我试了一下，如果不用多线程，直接一个一个挨着执行的话，大约5～10秒钟才能对一台电脑操作完，具体时间要根据命令的来决定，如果是软件安装或者卸载时间要更长一些。这样下来怎么也要一二十分钟，用多线程后就快多了，所有的命令执行完用了不到2分钟！  
2.最好用root用户登录，因为安装或者卸载软件的时候如果用普通用户又会提示输入密码，这样又多了一次交互，处理起来就比较麻烦！安装软件时apt-get
install xxx 最好加上“-y”参数，因为有时安装或删除软件时提示是否继续安装或卸载，这又是一次自动交互！加上那个参数后就没有人机交互了。  
3. 循环时循环所有ip，因为计算机的ip是路由器自动分配的，保险起见，最好全部都执行，保证没有遗漏的主机   
4.远端执行命令时如果有交互，可以这样用 stdin.write("Y")来完成交互，“Y”就是输入“Y”。  
5.把所有的命令放到一个列表里面，遍历列表可以依次执行列表里面的命令  
6.为了更好的进行控制，最好在电脑上提前把root用户打开，装好ssh服务器并让其开机自动执行。  
  
作者：cnblogs ma6174

