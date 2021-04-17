python sys模块包含了与python解释器和它的环境有关的函数,这个你可以通过dir(sys)来查看他里面的方法和成员属性

_复制代码_ 代码如下:

  
import sys  
print dir(sys)  

result:

_复制代码_ 代码如下:

  
['__displayhook__', '__doc__', '__excepthook__', '__name__', '__package__',
'__stderr__', '__stdin__', '__stdout__', '_clear_type_cache',
'_current_frames', '_getframe', '_mercurial', 'api_version', 'argv',
'builtin_module_names', 'byteorder', 'call_tracing', 'callstats', 'copyright',
'displayhook', 'dllhandle', 'dont_write_bytecode', 'exc_clear', 'exc_info',
'exc_type', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags',
'float_info', 'float_repr_style', 'getcheckinterval', 'getdefaultencoding',
'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount',
'getsizeof', 'gettrace', 'getwindowsversion', 'hexversion', 'long_info',
'maxint', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path',
'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'py3kwarning',
'setcheckinterval', 'setprofile', 'setrecursionlimit', 'settrace', 'stderr',
'stdin', 'stdout', 'subversion', 'version', 'version_info', 'warnoptions',
'winver']  

_复制代码_ 代码如下:

  
import sys  
print sys.path  
result:  
['C:\\Documents and Settings\\username\\My Documents\\Aptana Studio 3
Workspace\\Python_Test_Project\\src', 'C:\\Documents and
Settings\\username\\My Documents\\Aptana Studio 3
Workspace\\Python_Test_Project\\src', 'C:\\Python27', 'C:\\Python27\\DLLs',
'C:\\Python27\\lib', 'C:\\Python27\\lib\\lib-tk', 'C:\\Python27\\lib\\plat-
win', 'C:\\Python27\\lib\\site-packages', 'C:\\Python27\\lib\\site-
packages\\wx-2.8-msw-unicode', 'C:\\WINDOWS\\system32\\python27.zip']  

里面有个
sys.path属性。他是一个list.默然情况下python导入文件或者模块的话，他会先在sys.path里找模块的路径。如果没有的话，程序就会报错。  
所以我们一般自己写程序的话。最好把自己的模块路径给加到当前模块扫描的路径里,eg: sys.path.append('你的模块的名称'),这样程序就不会  
因为找不到模块而报错。。

