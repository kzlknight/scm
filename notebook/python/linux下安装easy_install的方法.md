如果想使用easy_install工具，可能需要先安装setuptools，不过更酷的方法是使用ez_setup.py脚本：  

_复制代码_ 代码如下:

  
wget -q http://peak.telecommunity.com/dist/ez_setup.py  
python ez_setup.py  

安装完后，最好确保easy_install所在目录已经被加到PATH环境变量里:  

_复制代码_ 代码如下:

  
Windows: C:\Python25\Scripts  
Linux: /usr/local/bin  

比如说要安装Python的MySQL支持，可以执行如下命令，系统会自动在pypi网站列表里查找相关软件包：

_复制代码_ 代码如下:

  
easy_install MySQL-python  

如果你在Windows+python2.5上执行如上命令的话，可能会出现如下错误：

_复制代码_ 代码如下:

  
Processing MySQL-python-1.2.3c1.tar.gz  
Running MySQL-python-1.2.3c1\setup.py -q bdist_egg --dist-dir c:\docume~1\...  
\locals~1\temp\easy_install-fvvfve\MySQL-python-1.2.3c1\egg-dist-tmp-q9moxf  
error: The system cannot find the file specified  

出现这类错误的原因是选错了版本，针对这个案列，我们可以显式指定软件包的版本号：

_复制代码_ 代码如下:

  
easy_install "MySQL-python==1.2.2"  

通过easy_install安装软件，相关安装信息会保存到easy-install.pth文件里，路径类似如下形式：

_复制代码_ 代码如下:

  
Windows：C:\Python25\Lib\site-packages\easy-install.pth  
Linux：/usr/local/lib/python25/site-packages/easy-install.pth  

如果想删除通过easy_install安装的软件包，比如说：MySQL-python，可以执行命令：

_复制代码_ 代码如下:

  
easy_install -m MySQL-python  

此操作会从easy-install.pth文件里把MySQL-python的相关信息抹去，剩下的egg文件，手动删除即可。

