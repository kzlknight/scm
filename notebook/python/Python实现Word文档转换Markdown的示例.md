随着SaaS服务的流行，越来越多的人选择在各个平台上编写文档，制作表格并进行分享。

同时，随着Markdown语法的破圈，很多平台开始集成支持这种简洁的书写标记语言，这样可以保证平台上用户文档样式的统一性。

但是在一些场景下，我们还是会在本地的Office软件上写有很多文档，或者历史遗留了很多本地文档。

如果我们需要将其上传到各大平台，直接复制粘贴，大概率是会造成文档内容结构和样式的丢失。于此我们需要将其转换为 Markdown 语法。

很多桌面软件（比如Typora）都提供了导入 Word 文件的功能，这类功能一般是通过 Pandoc 这个软件来扩展实现的。

Pandoc 是一个全能型的文档格式转换工具，其能够将多种文档格式转换为各类常见的文档格式。具体的文档格式之间的转换如下图所示（来源于官网）：

![](https://img.jbzj.com/file_images/article/202012/2020122293310415.png?2020112293318)

Pandoc 是瑞士军刀一般的存在，能够较好的处理各类的文档格式转换，但是如果我们需要自己写程序，调用 Pandoc 则需要额外的安装 Pandoc
才行，并且也不方便自定义。

幸而，在 Python 中有很多第三方模块提供了此类文档格式的转换功能。今天，我们来实现一下比较频繁使用到的 Word 文档转 Markdown 文档。

##  转换逻辑  

Word 文档到 Markdown 文档的转换总体而言分两步来实现：

  * 第一步，将 Word 文档转换为 HTML 文档； 
  * 第二步，将 HTML 文档转换为 Markdown 文档；   

##  依赖模块  

要实现这个功能我们需要借助 Python 的两个第三方模块：

  * mammoth 
  * markdownify   

mammoth 是一个用于将 Word 文档转换为 HTML 的模块，它支持在 Python、JavaScript、Java、.Net等平台使用。而
markdownify 则是将 HTML 转换为 Markdown 文档的模块。

##  处理 Word 图片  

因为 Word 文档中不可避免地会存在很多图片，为了在转换后的文档中能够正确地显示图片，我们需要自定义一下Word
文档内图片的处理方式。默认情况下，mammoth 会将图片转换为 base64
编码的字符串，这样不用生成额外的本地图片文件，但是会使文档体积变得很大。所以我们选择将图片另存为本地图片：

```python

    # 转存Word文档内的图片
    def convert_img(image):
      with image.open() as image_bytes:
        file_suffix = image.content_type.split("/")[1]
        path_file = "./img/{}.{}".format(str(time.time()),file_suffix)
        with open(path_file, 'wb') as f:
          f.write(image_bytes.read())
    
      return {"src":path_file}
```

##  正式转换  

在这里，我们以州的先生很久以前写的《Python爬虫实战与机器学习应用》（需要这本书的小伙伴可以微信私聊我）这本书的 Word 文档来演示。

![](https://img.jbzj.com/file_images/article/202012/2020122293707906.png?2020112293715)

代码如下所示：

```python

    # 读取Word文件
    with open(r"F:\自媒体\Python爬虫实战与机器学习应用.docx" ,"rb") as docx_file:
      # 转化Word文档为HTML
      result = mammoth.convert_to_html(docx_file,convert_image=mammoth.images.img_element(convert_img))
      # 获取HTML内容
      html = result.value
      # 转化HTML为Markdown
      md = markdownify(html,heading_style="ATX")
      print(md)
      with open("./docx_to_html.html",'w',encoding='utf-8') as html_file,open("./docx_to_md.md","w",encoding='utf-8') as md_file:
        html_file.write(html)
        md_file.write(md)
      messages = result.messages
```

运行程序，最终生成2个文件：

  * docx_to_html.html 
  * docx_to_md.md 

其中，docx_to_html.html 是 Word 文档转换为 HTML 后的文档：

![](https://img.jbzj.com/file_images/article/202012/2020122293751696.png?202011229380)

docx_to_md.md 是 HTML 转换为 Markdown 后的文档：

![](https://img.jbzj.com/file_images/article/202012/2020122293824754.png?2020112293832)

最后是另存为的图片：

![](https://img.jbzj.com/file_images/article/202012/2020122293850314.png?2020112293858)

怎么样，简单的二三十行代码就完成了 Word 到 Markdown 文档的转换，是不是很简单？

此功能将集成到觅道文档作为文档导入的功能实现，欢迎持续进行关注！

> 文章版权所有： [ 州的先生博客 ](https://zmister.com/)
>
> 原文地址： [ https://zmister.com/archives/1601.html
> ](https://zmister.com/archives/1601.html)

以上就是Python实现Word文档转换Markdown的示例的详细内容，更多关于python
Word文档转换Markdown的资料请关注脚本之家其它相关文章！

