**第1步：官网下载Python3.3**

这里面有windows和mac os x下的安装程序，下载那个64位的安装程序

**第2步：安装下载的img文件，安装完后的目录如下：  
**

_复制代码_ 代码如下:

  
/Library/Frameworks/Python.framework/Versions/3.3  

**第3步：移动python的安装目录**

原来的安装目录见第2步，不过所有的python都在  
/System/Library/Frameworks/Python.framework/Versions  
目录中，所以最好使用下面的命令移动一下，当然不移动也可以。但后面步骤中的某些路径需要修改下。  
sudo mv /Library/Frameworks/Python.framework/Versions/3.3
/System/Library/Frameworks/Python.framework/Versions  
第4步：改变Python安装目录的用户组为wheel  

_复制代码_ 代码如下:

  
sudo chown -R root:wheel
/System/Library/Frameworks/Python.framework/Versions/3.3  

  
python2.7的用户组就是wheel，3.3也照葫芦画瓢吧！

**第4步：修改Python当前安装目录的符号链接**

在 /System/Library/Frameworks/Python.framework/Versions/目录下有一个Current，这是一个目
录符号链接，指向当前的Python版本。原来指向2.7的，现在指向3.3。所以应先删除Current。然后重新建立Current符号链接，命令如 下：

_复制代码_ 代码如下:

  
sudo rm /System/Library/Frameworks/Python.framework/Versions/Current  
sudo ln -s /System/Library/Frameworks/Python.framework/Versions/3.3
/System/Library/Frameworks/Python.framework/Versions/Current  

**第5步：删除旧的命令符号链接**

在/usr/bin目录下有4个python命令的符号链接，使用下面的命令先删除  

_复制代码_ 代码如下:

  
sudo rm /usr/bin/pydoc  
sudo rm /usr/bin/python  
sudo rm /usr/bin/pythonw  
sudo rm /usr/bin/python-config  

**第6步：重新建立新的命令符号链接**

将第6步删除的符号链接重新使用下面命令建立，它们都指向Python3.3了。  

_复制代码_ 代码如下:

  
sudo ln -s
/System/Library/Frameworks/Python.framework/Versions/3.3/bin/pydoc3.3
/usr/bin/pydoc  
sudo ln -s
/System/Library/Frameworks/Python.framework/Versions/3.3/bin/python3.3
/usr/bin/python  
sudo ln -s
/System/Library/Frameworks/Python.framework/Versions/3.3/bin/pythonw3.3
/usr/bin/pythonw  
sudo ln -s
/System/Library/Frameworks/Python.framework/Versions/3.3/bin/python3.3m-config
/usr/bin/python-config  

**第7步：更新/root/.bash_profile文件中的路径  
**

_复制代码_ 代码如下:

  
cd ~  
vim .bash_profile  

在.bash_profile插入下面的内容即可

_复制代码_ 代码如下:

  
# Setting PATH for Python 3.3  
# The orginal version is saved in .bash_profile.pysave  
PATH="/System/Library/Frameworks/Python.framework/Versions/3.3/bin:${PATH}"  
export PATH  

ok，现在重新启动一下Console，然后执行python --version，得到的就是Python
3.3.3。如果在程序中，需要使用下面代码获取python版本

_复制代码_ 代码如下:

  
import platform  
print(platform.python_version())  

如果还是用了如PyDev等IDE，仍然需要更新一下相关的路径。

现在可以使用最新的Python3.3.3了。

