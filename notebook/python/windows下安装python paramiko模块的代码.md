1.安装python windows版本好：python-2.5.1.msi  
  
2.安装pycrypto windows版本号：pycrypto-2.0.1.win32-py2.5.exe  
地址： [
http://tmrc.mit.edu/mirror/twisted/Dependencies/Win/pycrypto-2.0.1.win32-py2.5.exe
](http://tmrc.mit.edu/mirror/twisted/Dependencies/Win/pycrypto-2.0.1.win32-py2.5.exe)

3. 安装MySQL DB Module for Python 2.5   
地址： [ http://sourceforge.net/projects/mysql-python/files/mysql-
python/1.2.2/MySQL-python-1.2.2.win32-py2.5.exe/download
](http://sourceforge.net/projects/mysql-python/files/mysql-python/1.2.2/MySQL-
python-1.2.2.win32-py2.5.exe/download)

4.安装开源版的zip压缩软件  
7-Zip：7z920.exe；可用于解压缩 以 lzma为后缀名的压缩文件。  
地址： [ http://www.7-zip.org/ ](http://www.7-zip.org/)

5.安装支持ssl，pyOpenSSL-0.8.winxp32-py2.5.msi  
地址： [ http://sourceforge.net/projects/pyopenssl/
](http://sourceforge.net/projects/pyopenssl/)

6.安装 easy_install  
请参考这篇文章： [ linux下安装easy_install的方法 ](https://www.jb51.net/article/34004.htm)  
  
7、因为此软件需要编译，因此windows上需要安装gcc编译器。  
[ http://www.mingw.org/wiki/Getting_Started
](http://www.mingw.org/wiki/Getting_Started)

包括几个大步骤：  
1）按照网站的说明：下载所需的软件包,exe的可以直接安装不需要7zip  
2）将所有的软件包解压缩到一个文件夹下，例如： E:\MinGW。以lzma为后缀名的文件，用7zip解压缩。  
3）将 E:\MinGW\bin 加入系统环境变量

至此，windows上的gcc安装完成  
这时就可以在cmd命令下执行输入gcc执行命令了。

8.修改python的安装文件：  
假设python的安装目录为 C:\Python25\Lib\distutils  
在目录 C:\Python25\Lib\distutils 下新建一个distutils.cfg文件  
内容：  
  

_复制代码_ 代码如下:

  
[build]  
compiler=mingw32  

9.至此，可以正常编译安装paramiko模块。

_复制代码_ 代码如下:

  
cd python25/scripts  
easy_install paramiko  

10.搞定

_复制代码_ 代码如下:

  
import paramiko  

