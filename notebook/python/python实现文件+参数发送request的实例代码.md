需求：

该接口，含两个参数，一个是file，一个是paperName。其中file为上传的文件。content-type为form-data。

![](https://img.jbzj.com/file_images/article/202101/2021010510283810.png)

根据python中的request源代码，可知，发送一个request，可以传递的参数有很多。而我们这次主要用到的就是files，当然method、url、headers、及data/json也是每次发送request必备的。

![](https://img.jbzj.com/file_images/article/202101/2021010510283811.png)

主要的实现方式：

```python

    # 用二进制的方式打开需上传的文件。
    
    f = open(filename, "rb")
    file = [
     ("file", (filename, f, "file/xlsx")) # 此处"file"为上传的参数名；filename可以为当前目录下的文件(仅文件名即可)，也可以是其他目录下的文件(用相对路径)
    ]
```

实现代码：

```python

    f = open(filename, "rb")
    file = [
     ("file", (filename, f, "file/xlsx")) 
    ]
    filename = '../data/required_upload.xlsx' # 此处写的是放在data目录下的文件。如果是当前目录下的，直接'required_upload.xlsx'即可
    response = request(method=method, url=url, headers=headers, files=file, data=data)
    f.close()
```

总结tips：

1. 以二进制的方式打开文件，文件可以是file / img   
2. 文件名如果非当前目录，则应使用相对路径   
3. 发送请求结束后，应立刻关闭文件   
6. content-type为form-data，request语句中应注意是data=data，若content-type为application/json等，则是json=data   
_4. 试着去读一读看看源码  
_ __5. 如果多次需要上传文件，不妨把#主要实现方式#里的代码封装起来，方便以后调用_ _

到此这篇关于python实现文件+参数发送request的文章就介绍到这了,更多相关python发送request内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

