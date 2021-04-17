###  1 StreamingHttpResponse下载  

StreamingHttpResponse(streaming_content)：流式相应，内容的迭代器形式，以内容流的方式响应。

注：StreamingHttpResponse一般多现实在页面上，不提供下载。

以下为示例代码

```python

    def streamDownload(resquest):
     def file_iterator(filepath, chunk_size = 512):
     with open(filepath, 'rb') as f:
      while True:
      con = f.read(512)
      if con:
       yield con
      else:
       break
     filename = os.path.abspath(__file__) + 'test.txt'
     response = StreamingHttpResponse(file_iterator(filename)
     return response 
    # 最后程序会将结果打印在显示器上
    
```

###  2 FileResponse下载  

FileResponse(stream)：以流形式打开后的文件

注：FileResponse是StreamingHttpResponse的子类

以下为示例代码：

```python

    def homeproc2(request):
     cwd = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
     response = FileResponse(open(cwd + "/msgapp/templates/youfile", "rb"))
     response['Content-Type] = 'application/octet-stream'
     response['Content-Disposition'] = 'attachment;filename="filename"'
     return response
    
```

需要解释说明的是：

```python

     response['Content-Type] = 'application/octet-stream'
     response['COntent-Disposition'] = 'attachment;filename="filename"'
    
```

  * Content-Type：用于指定文件类型。 
  * COntent-Disposition：用于指定下载文件的默认名称，对，没错！ “CO”两个字符都要大写。 

两者都是MIME协议里面的标准类型。

到此这篇关于详解Django关于StreamingHttpResponse与FileResponse文件下载的最优方法的文章就介绍到这了,更多相关Django
StreamingHttpResponse与FileResponse内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

