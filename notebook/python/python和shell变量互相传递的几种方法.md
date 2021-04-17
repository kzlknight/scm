python -> shell：

**1.环境变量**

_复制代码_ 代码如下:

  
import os  
var=123或var='123'  
os.environ['var']=str(var) #environ的键值必须是字符串  
os.system('echo $var')  

_复制代码_ 代码如下:

  
import os  
var=123或var='123'  
os.environ['var']=str(var) #environ的键值必须是字符串  
os.system('echo $var')  

**2.字符串连接**

_复制代码_ 代码如下:

  
import os  
path='/root/a.txt'  
var=[1]  
var='bash'  
os.system('echo ' + path) #注意echo后有空格  
os.system('echo ' + str(var[0]))  
os.system('echo ' + var + ' /root/c.sh') #注意echo后和/root前有空格  

_复制代码_ 代码如下:

  
import os  
path='/root/a.txt'  
var=[1]  
var='bash'  
os.system('echo ' + path) #注意echo后有空格  
os.system('echo ' + str(var[0]))  
os.system('echo ' + var + ' /root/c.sh') #注意echo后和/root前有空格  

**3.通过管道**

_复制代码_ 代码如下:

  
import os  
var='123'  
os.popen('wc -c', 'w').write(var)  

_复制代码_ 代码如下:

  
import os  
var='123'  
os.popen('wc -c', 'w').write(var)  

**4.通过文件**

_复制代码_ 代码如下:

  
output = open('/tmp/mytxt', 'w')  
output.write(S) #把字符串S写入文件  
output.writelines(L) #将列表L中所有的行字符串写到文件中  
output.close()  

_复制代码_ 代码如下:

  
output = open('/tmp/mytxt', 'w')  
output.write(S) #把字符串S写入文件  
output.writelines(L) #将列表L中所有的行字符串写到文件中  
output.close()  

**5.通过重定向标准备输出**

_复制代码_ 代码如下:

  
buf = open('/root/a.txt', 'w')  
print >> buf, '123\n', 'abc'  

_复制代码_ 代码如下:

  
buf = open('/root/a.txt', 'w')  
print >> buf, '123\n', 'abc'  

或

_复制代码_ 代码如下:

  
print >> open('/root/a.txt', 'w'), '123\n', 'abc' #写入或生成文件  
print >> open('/root/a.txt', 'a'), '123\n', 'abc' #追加  

_复制代码_ 代码如下:

  
print >> open('/root/a.txt', 'w'), '123\n', 'abc' #写入或生成文件  
print >> open('/root/a.txt', 'a'), '123\n', 'abc' #追加  

**shell - > python： **

**1.管道**

_复制代码_ 代码如下:

  
import os  
var=os.popen('echo -n 123').read( )  
print var  

_复制代码_ 代码如下:

  
import os  
var=os.popen('echo -n 123').read( )  
print var  

2.   

_复制代码_ 代码如下:

  
import commands  
var=commands.getoutput('echo abc') #输出结果  
var=commands.getstatusoutput('echo abc') #退出状态和输出结果  

_复制代码_ 代码如下:

  
import commands  
var=commands.getoutput('echo abc') #输出结果  
var=commands.getstatusoutput('echo abc') #退出状态和输出结果  

**3.文件  
**

_复制代码_ 代码如下:

  
input = open('/tmp/mytxt', 'r')  
S = input.read( ) #把整个文件读到一个字符串中  
S = input.readline( ) #读下一行（越过行结束标志）  
L = input.readlines( ) #读取整个文件到一个行字符串的列表中  

_复制代码_ 代码如下:

  
input = open('/tmp/mytxt', 'r')  
S = input.read( ) #把整个文件读到一个字符串中  
S = input.readline( ) #读下一行（越过行结束标志）  
L = input.readlines( ) #读取整个文件到一个行字符串的列表中  

  

