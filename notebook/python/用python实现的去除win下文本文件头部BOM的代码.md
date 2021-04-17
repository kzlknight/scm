问题：  
windows环境下新建或编辑文本文件，保存时会在头部加上BOM。  
使用ftp上传到linux下，在执行时第一行即报错。  
以下方法可以去除BOM头，有需要的朋友可以参考下。

_复制代码_ 代码如下:

  
import codecs  
data = open("Test.txt").read()  
if data[:3] == codecs.BOM_UTF8:  
data = data[3:]  
print data.decode("utf-8")  

说明: 文件开始部为 0xEF 0xBB 0xBF 为BOM

