##  （一）Selenium基础  

入门教程： [ Selenium官网教程 ](http://www.selenium.org.cn/1598.html)

###  1.Selenium简介  

Selenium是一个用于测试网站的自动化测试工具，支持各种浏览器包括Chrome、Firefox、Safari等主流界面浏览器，同时也支持phantomJS无界面浏览器。

###  2.支持多种操作系统  

如Windows、Linux、IOS、Android等。

###  3.安装Selenium  

```python

    pip install Selenium
    
```

###  4.安装浏览器驱动  

Selenium3.x调用浏览器必须有一个webdriver驱动文件

Chrome驱动文件下载： [ 点击下载chromedrive
](https://chromedriver.storage.googleapis.com/index.html?path=2.35/)

Firefox驱动文件下载: [ 点击下载geckodriver
](https://github.com/mozilla/geckodriver/releases)

###  5.配置环境变量  

设置浏览器的地址非常简单。 我们可以手动创建一个存放浏览器驱动的目录，如： F:\GeckoDriver ,
将下载的浏览器驱动文件（例如：chromedriver、geckodriver）丢到该目录下。

