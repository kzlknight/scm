今天有同学问，用os模块的access()能否判断一个文件是否被占用？直觉上，这是行不通的，因为access()返回的是文件的读写属性。为了确认这一点，我简单测试了一下。

```python

    >>> import os
    >>> fn = r'D:\temp\csdn\t.py' # 测试用的文件
    >>> os.access(fn, os.F_OK) # 文件是否存在
    True
    >>> os.access(fn, os.R_OK) # 文件是否可读
    True
    >>> os.access(fn, os.W_OK) # 文件是否可写
    True
    >>> os.access(fn, os.X_OK) # 文件是否可执行
    True
    >>> fp = open(fn, 'a+') # 以追加写的方式打开文件
    >>> os.access(fn, os.F_OK) # 文件当然还在
    True
    >>> os.access(fn, os.R_OK) # 文件依然可读
    True
    >>> os.access(fn, os.W_OK) # 文件依然可写
    True
    >>> os.access(fn, os.X_OK) # 文件依然执行
    True
    >>> fp.close()
    
```

可见，os.access()返回的是文件读写属性，与文件是否被占用没有半毛钱关系。

后来，群里有同学建议说，不妨用try尝试着open文件，如果成功，表示文件没有被占用，如果抛出异常，则表示文件被占用。果真如此吗？还是用代码验证一下吧。

```python

    >>> fp1 = open(fn, 'a+')
    >>> fp2 = open(fn, 'a+')
    >>> fp1.close()
    >>> fp2.close()
    
```

结果表明，对同一个文件以写的方式打开多次，系统并没有抛出异常。为什么会这样呢？究其原因，是因为文件被打开和文件被占用是完全两个不同的问题。顺便提醒一下，做上面的测试时，不要使用'w'的方式，否则文件内容会被清空。

那么，究竟应该如何用Python判断一个文件是否被占用呢？这个问题还是要回归到操作系统层面来解决，也就是依赖win32api模块。

```python

    >>> import win32file
    >>> def is_used(file_name):
    	try:
    		vHandle = win32file.CreateFile(file_name, win32file.GENERIC_READ, 0, None, win32file.OPEN_EXISTING, win32file.FILE_ATTRIBUTE_NORMAL, None)
    		return int(vHandle) == win32file.INVALID_HANDLE_VALUE
    	except:
    		return True
    	finally:
    		try:
    			win32file.CloseHandle(vHandle)
    		except:
    			pass
    		
    >>> fn = r'D:\temp\csdn\t.py'
    >>> is_used(fn)
    False
    >>> fp = open(fn, 'a+')
    >>> is_used(fn)
    True
    >>> fp.close()
    >>> is_used(fn)
    False
    
```

简单验证了一下，函数is_used()基本可用。

到此这篇关于使用Python判断一个文件是否被占用的文章就介绍到这了,更多相关Python判断文件被占用内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

