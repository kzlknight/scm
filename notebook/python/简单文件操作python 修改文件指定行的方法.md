例一：  

_复制代码_ 代码如下:

  
#!/usr/bin/python  
import sys  
import re  
if __name__=="__main__":  
f=file("hi.txt","w+")  
li=["hello\n","hi\n"]  
f.writelines(li)  
f.close()  

  
"W+"模式：如果没有hi.txt则创建文件写入；如果存在，则清空hi.txt内容，从新写入。

例二：修改文件指定行

用的方法比拟笨，将文件内容按行读入到一个列表中，修改指定行即给列表中元素赋值；修改完后，用writelines将列表从新写入文件。

  

_复制代码_ 代码如下:

  
#!/usr/bin/python

import sys,os

f=open('hi.txt','r+')  
flist=f.readlines()  
flist[4]='hi\n'  
f=open('hi.txt','w+')  
f.writelines(flist)  

  
将hi.txt第五行内容修改成hi

