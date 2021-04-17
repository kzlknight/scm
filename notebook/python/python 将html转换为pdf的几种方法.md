将 HTML 网页转换为 PDF 是很多人常见的一个需求，在浏览器上，我们可以通过浏览器的“打印”功能直接将网页打印输出为 PDF。

但是如果有多个网页就不好办了。

##  二进制软件  

网络上存在很多将 HTML 转换为 PDF 的软件和工具。比较著名的有 Carelib、wkhtmltopdf。

###  whtmltopdf  

wkhtmltopdf 真是一个优秀的 HTML 转换 PDF 工具。其借助 Qt 的 WebKit 渲染引擎，将 HTML 文档渲染导出为 PDF
文档或图像。

![](https://img.jbzj.com/file_images/article/202012/2020122985950461.png?2020112985958)

功能十分完善，但是由于使用的渲染引擎是 Qt 的 WebKit，其没法对 ES6 的 JavaScript 代码提供支持，导致一些采用 ES6 编写的
HTML 页面渲染不出实际的效果来，导致州的先生最终放弃了它。

###  Carelib  

Carelib 是一个电子书管理软件，其中提供了各类文档的转换工具，所以可以借助其电子书转换工具来实现 HTMl 到 PDF 的转换。

这些都是用于桌面环境的二进制软件，如果要在 Python 中使用，要么使用 Popen()
方法调用这些二进制软件的命令，要么使用一些第三方的封装模块，比如：pdfkit、pypandoc
等，这些第三方模块通过集成调用上述二进制软件，封装了一些方便 Python 调用的接口。

##  纯 Python 库实现  

上面介绍的那些 Python 第三方模块虽然可以很好的进行 HTML 到 PDF
的转换工作，但是都需要额外在计算机上安装其他的二进制软件，很多小伙伴并不喜欢这种调用方式。

不依赖于二进制软件的实现，有如下的方案：

###  xhtml2pdf  

这是一个基于 ReportLab、html5lib、PyPDF2 等 Python 模块构建的 HTML 到 PDF 转换模块。能够很好的支持 HTML5
、CSS2.1 和部分 CSS3 语法。

因为是基于 Report Lab
模块进行的开发，其对中文的支持在某些环境下会有问题。而且由于开发人员的变更，模块的功能出现了一些断层。但是仍然是一个非常棒的 HTML 转 PDF 模块。

###  weasyprint  

这是一个用于 HTML 和 CSS 的可视化渲染引擎，可以将 HTML 文档导出为打印标准的 PDF 文件。

xhtml2pdf 模块也曾推荐使用这个模块来进行 HTML 转换 PDF 的工作。

这个模块功能很强大、效果很出色，但是，模块的依赖项太多了：

![](https://img.jbzj.com/file_images/article/202012/2020122990058295.png?20201129917)

州的先生至今没有在 Windows 电脑上安装成功过！

##  浏览器方案  

在上述两种方案中，二进制程序的可控制性稍有不足，而纯 Python 实现的渲染解析则在功能上和依赖上不是有友好。

处理上述两种方案，我们还能采用第三种方式进行 HTMl 到 PDF 的转换。那就是借助 Web 自动化测试的浏览器内核和 Qt for Python 的
Web 引擎 来实现。

###  Web 自动化的浏览器内核  

使用 Python 的小伙伴经常会使用 Selenium、pyppeteer 这两个 Web 自动化测试的模块来进行数据采集和 Web 自动化测试工作。

这两个模块都是用来驱动一个真实的浏览器来进行网页的操作。正是基于此，我们可以调用浏览器中打印相关的 API 接口，来实现 HTML 转 PDF 的功能。

例如，在 pyppeteer 中可以按照下面示例的方式，打开一个 HTML 文档，然后将其转换为 PDF 文档：

![](https://img.jbzj.com/file_images/article/202012/2020122990305095.png?202011299313)

###  Qt 的 Web 引擎  

在 Qt5 中，Qt 使用新的 Chromium 内核代替了老旧的 WebKit 作为 Web 的渲染引擎。使得在 Qt 中进行可以现代化的浏览器开发。

借助于 Qt 的 Python 实现（PyQt5 系列 和 PySide2 系列），我们可以直接调用 Qt 中的 Web 引擎相关的接口。

其中 QtWebEngineWidgets 子模块中的 QWebEngineView() 类提供了 printToPdf 方法供我们将网页打印为 PDF
文档，所以基于此，我们也可以使用 PyQt5 或 PySide2 进行 HTML 转换 PDF，示例如下所示：

![](https://img.jbzj.com/file_images/article/202012/2020122990335094.png?202011299345)

##  最后  

在上面，州的先生介绍了 3 种在 Python 中转换 HTML 文档为 PDF
文档的方案，每种方案都有各自的优势和不足，正确地评估自己的需求然后选择合适的方案，也能弥补其不足。

以上就是python 将html转换为pdf的几种方法的详细内容，更多关于python 将html转换为pdf的资料请关注脚本之家其它相关文章！

