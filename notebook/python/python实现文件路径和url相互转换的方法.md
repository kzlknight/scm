本文实例讲述了python实现文件路径和url相互转换的方法。分享给大家供大家参考。具体实现方法如下：

```python

    import urllib 
    pathname = 'path/to/file/or/folder/' 
    url = urllib.pathname2url(pathname) 
    pathname = urllib.url2pathname(url)
    print pathname
    
    
```

运行结果如下：  
path\to\file\or\folder\

希望本文所述对大家的Python程序设计有所帮助。

