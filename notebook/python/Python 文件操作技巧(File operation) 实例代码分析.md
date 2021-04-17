常用的module是 os ,os.path 和shutil,所以要先引入他们.  
  
**python遍历文件夹和文件**  
这个也许是最常用的功能,如下:  

_复制代码_ 代码如下:

  
import os  
import os.path  
  
rootdir = "D:\\programmer\\training"  
for parent, dirnames, filenames in os.walk(rootdir):  
#case 1:  
for dirname in dirnames:  
print "parent is:" + parent  
print "dirname is:" + dirname  
#case 2  
for filename in filenames:  
print "parent is:" + parent  
print "filename with full path :" + os.path.join(parent, filename)  

  
解释说明:  
  
1.os.walk返回一个三元组.其中dirnames是所有文件夹名字(不包含路径),filenames是所有文件的名字(不包含路径).parent表示父目录.  
2.case1 演示了如何遍历所有目录.  
3.case2 演示了如何遍历所有文件.  
4.os.path.join(dirname,filename) : 将形如"/a/b/c"和"d.java"变成/a/b/c/d.java".  
  
  
**perl分割路径和文件名**  
常用函数有三种:分隔路径,找出文件名.找出盘符(windows系统),找出文件的扩展名.  

_复制代码_ 代码如下:

  
import os.path  
  
spath="D:/download/flight/flighthtml.txt"  
  
# case 1:  
p,f=os.path.split(spath);  
print "dir is:"+p  
print "file is:"+f  
  
# case 2:  
drv,left=os.path.splitdrive(spath);  
print "driver is:"+drv  
print "left is:"+left  
# case 3:  
f,ext=os.path.splitext(spath);  
print "f is:"+f  
print "ext is:"+ext  

  
这三个函数都返回二元组.  
1.case1 分隔目录和文件名  
2.case2 分隔盘符和文件名  
3.case3 分隔文件和扩展名  

