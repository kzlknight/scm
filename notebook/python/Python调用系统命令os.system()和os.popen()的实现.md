作为一门脚本语言，写脚本时执行系统命令可以说很常见了，python提供了相关的模块和方法。

os模块提供了访问操作系统服务的功能，由于涉及到操作系统，它包含的内容比较多，这里只说system和popen方法。

```python

    >>> import os
    >>> dir(os)
    ['DirEntry', 'F_OK', 'MutableMapping', 'O_APPEND', 'O_BINARY', 'O_CREAT', 'O_EXCL', 'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 'O_RDWR', 'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT', 'O_TRUNC', 'O_WRONLY', 'P_DETACH', 'P_NOWAIT', 'P_NOWAITO', 'P_OVERLAY', 'P_WAIT', 'PathLike', 'R_OK', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'TMP_MAX', 'W_OK', 'X_OK', '_Environ', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_execvpe', '_exists', '_exit', '_fspath', '_get_exports_list', '_putenv', '_unsetenv', '_wrap_close', 'abc', 'abort', 'access', 'altsep', 'chdir', 'chmod', 'close', 'closerange', 'cpu_count', 'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2', 'environ', 'errno', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fdopen', 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fsync', 'ftruncate', 'get_exec_path', 'get_handle_inheritable', 'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getenv', 'getlogin', 'getpid', 'getppid', 'isatty', 'kill', 'linesep', 'link', 'listdir', 'lseek', 'lstat', 'makedirs', 'mkdir', 'name', 'open', 'pardir', 'path', 'pathsep', 'pipe', 'popen', 'putenv', 'read', 'readlink', 'remove', 'removedirs', 'rename', 'renames', 'replace', 'rmdir', 'scandir', 'sep', 'set_handle_inheritable', 'set_inheritable', 'spawnl', 'spawnle', 'spawnv', 'spawnve', 'st', 'startfile', 'stat', 'stat_float_times', 'stat_result', 'statvfs_result', 'strerror', 'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks', 'symlink', 'sys', 'system', 'terminal_size', 'times', 'times_result', 'truncate', 'umask', 'uname_result', 'unlink', 'urandom', 'utime', 'waitpid', 'walk', 'write']
```

###  os.system()  

```python

    >>> help(os.system)
    Help on built-in function system in module nt:
    
     
    system(command)
      Execute the command in a subshell.
    
    
```

从字面意思上看，os.system()是在当前进程中打开一个子shell（子进程）来执行系统命令。

官方说法：

> On Unix, the return value is the exit status of the process encoded in the
> format specified for wait().
>
> The subprocess module provides more powerful facilities for spawning new
> processes and retrieving their results; using that module is preferable to
> using this function.  
>

这个方法只返回状态码，执行结果会输出到stdout，也就是输出到终端。不过官方建议使用subprocess模块来生成新进程并获取结果是更好的选择。

```python

    >>> os.system('ls')
    access.log douban.py mail.py myapp.py polipo proxychains __pycache__  spider.py test.py users.txt
    0
    
```

###  os.popen()  

```python

    >>> help(os.popen)
    Help on function popen in module os:
    
    popen(cmd, mode='r', buffering=-1)
      # Supply os.popen()
    
    
```

cmd：要执行的命令。  
mode：打开文件的模式，默认为'r'，用法与open()相同。  
buffering：0意味着无缓冲；1意味着行缓冲；其它正值表示使用参数大小的缓冲。负的bufsize意味着使用系统的默认值，一般来说，对于tty设备，它是行缓冲；对于其它文件，它是全缓冲。

官方说法：

> Open a pipe to or from command cmd. The return value is an open file object
> connected to the pipe, which can be read or written depending on whether
> mode is 'r' (default) or 'w'.
>
> The close method returns None if the subprocess exited successfully, or the
> subprocess's return code if there was an error.
>
> This is implemented using subprocess.Popen;  
>

这个方法会打开一个管道，返回结果是一个连接管道的文件对象，该文件对象的操作方法同open()，可以从该文件对象中读取返回结果。如果执行成功，不会返回状态码，如果执行失败，则会将错误信息输出到stdout，并返回一个空字符串。这里官方也表示subprocess模块已经实现了更为强大的subprocess.Popen()方法。

```python

    >>> os.popen('ls')
    <os._wrap_close object at 0x7f93c5a2d780>
    >>> os.popen('la')
    <os._wrap_close object at 0x7f93c5a37588>
    >>> /bin/sh: la: command not found
    
    >>> f = os.popen('ls')
    >>> type(f)
    <class 'os._wrap_close'>
    
    
```

读取执行结果：

```python

    >>> f.readlines()
    ['access.log\n', 'douban.py\n', 'import_test.py\n', 'mail.py\n', 'myapp.py\n', 'polipo\n', 'proxychains\n', '__pycache__\n', 'spider.py\n', 'test.py\n', 'users.txt\n']
    
```

这里使用os.popen来获取设备号，使用os.system来启动macaca服务（有时间了将macaca的一些经历写写吧）。

两者的区别是：

（1）os.system(cmd)的返回值只会有0(成功),1,2

（2）os.popen(cmd)会把执行的cmd的输出作为值返回。

###  参考：  

[ https://docs.python.org/3/library/os.html#os.system
](https://docs.python.org/3/library/os.html#os.system)  
[ https://docs.python.org/3/library/os.html#os.popen
](https://docs.python.org/3/library/os.html#os.popen)

到此这篇关于Python调用系统命令os.system()和os.popen()的实现的文章就介绍到这了,更多相关Python
os.system()和os.popen()内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

