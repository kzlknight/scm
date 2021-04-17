本文实例讲述了python获得文件创建时间和修改时间的方法。分享给大家供大家参考。具体如下：

这里需要用户从控制台输入文件路径

```python

    import os.path, time
    import exceptions
    class TypeError (Exception):
      pass
    if __name__ == '__main__':
     if (len(os.sys.argv) < 1):
       raise TypeError()
     else:
       print "os.sys.argv[0]: %s" % os.sys.argv[0]
       # os.sys.argv[0] is the current file, in this case, file_ctime.py
     f = os.sys.argv[0]
     mtime = time.ctime(os.path.getmtime(f))
     ctime = time.ctime(os.path.getctime(f))
     print "Last modified : %s, last created time: %s" % (mtime, ctime)
    
    
```

希望本文所述对大家的Python程序设计有所帮助。

