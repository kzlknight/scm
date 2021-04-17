本文实例讲述了python列出目录下指定文件与子目录的方法。分享给大家供大家参考。具体实现方法如下：

```python

    # if you know the exact name: 
    import os 
    files = os.listdir('/path/to/dir/') 
    # if you want shell-style globbing: 
    import glob 
    files = glob.glob('/path/to/dir/*.html') 
    
    
```

希望本文所述对大家的Python程序设计有所帮助。

