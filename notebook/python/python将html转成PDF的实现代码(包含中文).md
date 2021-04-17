前提：

安装xhtml2pdf [ https://pypi.python.org/pypi/xhtml2pdf/
](https://pypi.python.org/pypi/xhtml2pdf/)  
下载字体：微软雅黑；给个地址： [ https://www.jb51.net/fonts/8481.html
](https://www.jb51.net/fonts/8481.html)

待转换的文件：1.htm  

_复制代码_ 代码如下:

  
<meta charset="utf8"/>  
<style type='text/css'>  
@font-face {  
font-family: "code2000";  
src: url("code2000.ttf")  
}

html {  
font-family: code2000;  
}  
</style>  
<html>  
<body><table>  
<tr>  
<td>文字</td>  
<td>123</td>  
</tr>  
<tr>  
<td>图片</td>  
<td><img src="1.jpg"></td>  
</tr>  
</table></body></html>  

**html_to_pdf.py程序**

_复制代码_ 代码如下:

  
# -*- coding: utf-8 -*-  
import sx.pisa3 as pisa  
data= open('1.htm').read()  
result = file('test.pdf', 'wb')  
pdf = pisa.CreatePDF(data, result)  
result.close()  
pisa.startViewer('test.pdf')  

说明：xhtml2pdf不能识别汉字，需要在html文件中通过CSS的方式嵌入code2000字体，貌似只能用code2000，原因不明。

