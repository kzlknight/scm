在原txt文件中，我们需要匹配出的字符串为:休闲服务（中间参杂着换行）

![](https://img.jbzj.com/file_images/article/202012/202012091005051.png)

直接复制到notebook里进行处理

![](https://img.jbzj.com/file_images/article/202012/202012091005052.png)  

**①发现需要拿出的字符串都在证卷研究报告前，第一步就把证券报告前面的所有内容全部提出来（包括换行）**

![](https://img.jbzj.com/file_images/article/202012/202012091005053.png)

**②发现需要的字符串在两个换行符（\n）的中间，再对其进行处理**

![](https://img.jbzj.com/file_images/article/202012/202012091005054.png)

**完整代码**

```python

    import re
    txt = """ 行业报告 | 行业点评 
     
       休闲服务
       证券研究报告"""
    result = re.findall(r"([\s\S]*)证券研究报告",txt)[0]
    sstr = re.findall("\n([\s\S]*)\n",result)[0].strip()
    print(" 匹配结果:",sstr)
    
```

到此这篇关于python使用正则表达式匹配txt特定字符串的文章就介绍到这了,更多相关python正则匹配txt特定字符串内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

