本文实例讲述了Python实现的网页截图功能。分享给大家供大家参考，具体如下：

**方法一、使用PyQt4的QtWebKit组件**

```python

    #!/usr/bin/env python
    # -*- coding: UTF-8 -*-
    import sys
    import os.path
    from PyQt4 import QtGui,QtCore,QtWebKit
    class PageShotter(QtGui.QWidget):
      def __init__(self,url,filename,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.url = url
        self.filename = filename
        self.webpage = None
      def shot(self):
        webview = QtWebKit.QWebView(self)
        webview.load(QtCore.QUrl(self.url))
        self.webpage = webview.page()
        self.connect(webview,QtCore.SIGNAL("loadFinished(bool)"),self.save_page)
      def save_page(self,finished):
        #print finished
        if finished:
          print u"开始截图！"
          size = self.webpage.mainFrame().contentsSize()
          print u"页面宽：%d，页面高：%d" % (size.width(),size.height())
          self.webpage.setViewportSize(QtCore.QSize(size.width()+16,size.height()))
          img = QtGui.QImage(size, QtGui.QImage.Format_ARGB32)
          painter = QtGui.QPainter(img)
          self.webpage.mainFrame().render(painter)
          painter.end()
          filename= self.filename;
          if img.save(filename):
            filepath = os.path.join(os.path.dirname(__file__), filename)
            print u"截图完毕：%s" % filepath
          else:
            print u"截图失败";
        else:
          print u"网页加载失败！"
        self.close()
    if __name__=="__main__":
      app = QtGui.QApplication(sys.argv)
      shotter = PageShotter("https://www.jb51.net/", 'shot.png')
      shotter.shot()
      sys.exit(app.exec_())
    
    
```

运行后输出：

> QFont::setPixelSize: Pixel size <= 0 (0)  
>  开始截图！  
>  页面宽：1058，页面高：9819  
>  截图完毕：C:\py\jb51PyDemo\src\Demo\shot.png

注：

Python2的32位操作系统安装包可至此下载： [ https://www.jb51.net/softs/548192.html
](https://www.jb51.net/softs/548192.html)  
64位操作系统下对应PyQt安装包可至此下载： [ https://www.jb51.net/softs/548197.html
](https://www.jb51.net/softs/548197.html) ）

Python3可直接使用pip命令安装PyQt5库，如：

```python

    pip3 install PyQt5-sip
    
    
```

**方法二、使用selenium**

```python

    #!/usr/bin/env python
    # -*- coding: UTF-8 -*-
    import time
    from selenium import webdriver
    browser = webdriver.Firefox()
    browser.set_window_size(1055, 800)
    browser.get("https://www.jb51.net/")
    browser.find_element_by_id("idClose").click()
    time.sleep(5)
    browser.save_screenshot("shot.png")
    browser.quit()
    
    
```

PS： ` selenium ` 库同样可以使用pip命令安装：

```python

    pip install selenium
    
    
```

另外，使用selenium时还需要下载geckodriver来驱动第三方浏览器，对于selenium3.x版本都会使用geckodriver来驱动firefox，所以需要下载geckodriver.exe,下载地址：https://github.com/mozilla/geckodriver/releases

下载后将geckodriver.exe放在C:\Python27即可（查看环境变量path中是否添加C:\Python27该路径）

更多关于Python相关内容感兴趣的读者可查看本站专题：《 [ Python图片操作技巧总结
](//www.jb51.net/Special/645.htm) 》、《 [ Python数据结构与算法教程
](//www.jb51.net/Special/663.htm) 》、《 [ Python函数使用技巧总结
](//www.jb51.net/Special/642.htm) 》、《 [ Python字符串操作技巧汇总
](//www.jb51.net/Special/636.htm) 》、《 [ Python入门与进阶经典教程
](//www.jb51.net/Special/520.htm) 》及《 [ Python文件与目录操作技巧汇总
](//www.jb51.net/Special/516.htm) 》

希望本文所述对大家Python程序设计有所帮助。

