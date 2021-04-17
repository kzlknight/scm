在开发软件的过程中，我们经常会碰到需要在指定目录下生成文件和删除文件的操作，下面就演示一下怎样用python进行之类操作。

###  生成文件  

```python

    import os
    
    #在指定目录里面创建空文件
    def mkdir():
      path = 'C:\wan\wan'//这里是生成文件的地址
      for i in range(5):
        file_name = path + str(oct(i))
        os.mkdir(file_name)
    
    mkdir()
    
    
```

###  删除文件  

```python

    import os
    
    #去除文件里面的空文件
    def clean_dir():
      for i in range(5):
        path = "C:\wan"//这里是所需删除文件的地址
        filename = path + str(oct(i))
        try:
          os.removedirs(filename)
        except FileNotFoundError:
          pass
    
    clean_dir()
    
```

生成文件时一定要注意生成的数量，一不小心就是成千上万的文件夹了哟！

到此这篇关于Pycharm在指定目录下生成文件和删除文件的实现的文章就介绍到这了,更多相关Pycharm指定目录生成和删除文件内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

