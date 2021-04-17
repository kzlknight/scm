前言：由程序去执行的操作不允许有任何误差，有些时候在测试的时候未出现问题，但是放到服务器上就会报错，而且打印的错误信息并不十分明确。这时，我在想如果在脚本执行出错的时候能对当前窗口截图保存，那么通过图片就可以非常直观地看出出错的原因。WebDriver提供了截图函数get_screenshot_as_file()来截取当前窗口。

本章中用到的关键方法如下：

get_screenshot_as_file()：截图  

```python

    from selenium import webdriver
    
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com/')
    
    # 截图，图片后缀最好为.png，如果是其他的执行的时候会有警告，但不会报错
    driver.get_screenshot_as_file("D:\\baidu_index.png")
    
    driver.quit()
    
    
```

实例：

```python

    #窗口截图操作
    #coding utf-8
    
    from selenium import webdriver
    from time import sleep
    
    driver = webdriver.Firefox()
    
    url = "http://www.baidu.com"
    
    driver.get(url)
    
    driver.find_element_by_id('kw').send_keys('selenium python')
    driver.find_element_by_id('su').click()
    
    sleep(2)
    
    driver.get_screenshot_as_file("D:\\baidu_error.jpg")
    
    driver.quit()
    
    
```

运行结果：

有个warning，什么意思呢，就是说截图最好是使用 .png格式的图片，而我的代码中使用的是.jpg格式，但是，不影响最终结果

> file type. It should end with a `.png` extension  
>  "type. It should end with a `.png` extension", UserWarning)

网页截图： - 不出意外，渣度第一时间给你推送广告！！呵呵呵！-

![](https://img.jbzj.com/file_images/article/202012/2020124115745381.jpg?202011411589)

Selenium文集传送门：

标题  |  简介  
---|---  
[ Python爬虫 - Selenium（1）安装和简单使用 ](https://www.jb51.net/article/201370.htm) |
详细介绍Selenium的依赖环境在Windows和Centos7上的安装及简单使用  
[ Python爬虫 - Selenium（2）元素定位和WebDriver常用方法
](https://www.jb51.net/article/201375.htm) |
详细介绍定位元素的8种方式并配合点击和输入、提交、获取断言信息等方法的使用  
[ Python爬虫 - Selenium（3）控制浏览器的常用方法 ](https://www.jb51.net/article/201377.htm)
|  详细介绍自定义浏览器窗口大小或全屏、控制浏览器后退、前进、刷新浏览器等方法的使用  
[ Python爬虫 - Selenium（4）配置启动项参数 ](https://www.jb51.net/article/201379.htm) |
详细介绍Selenium启动项参数的配置，其中包括无界面模式、浏览器窗口大小设置、浏览器User-Agent (请求头)等等  
[ Python爬虫 - Selenium（5）鼠标事件 ](https://www.jb51.net/article/201383.htm) |
详细介绍鼠标右击、双击、拖动、鼠标悬停等方法的使用  
[ Python爬虫 - Selenium（6）键盘事件 ](https://www.jb51.net/article/201387.htm) |
详细介绍键盘的操作，几乎包含所有常用按键以及组合键  
[ Python爬虫 - Selenium（7）多窗口切换 ](https://www.jb51.net/article/201389.htm) |
详细介绍Selenium是如何实现在不同的窗口之间自由切换  
[ Python爬虫 - Selenium（8）frame/iframe表单嵌套页面
](https://www.jb51.net/article/201392.htm) |
详细介绍如何从当前定位的主体切换为frame/iframe表单的内嵌页面中  
[ Python爬虫 - Selenium（9）警告框(弹窗)处理 ](https://www.jb51.net/article/201394.htm) |
详细介绍如何定位并处理多类警告弹窗  
[ Python爬虫 - Selenium（10）下拉框处理 ](https://www.jb51.net/article/201397.htm) |
详细介绍如何灵活的定位并处理下拉框  
[ Python爬虫 - Selenium（11）文件上传 ](https://www.jb51.net/article/201410.htm) |
详细介绍如何优雅的通过send_keys()指定文件进行上传  
[ Python爬虫 - Selenium（12）获取登录Cookies，并添加Cookies自动登录
](https://www.jb51.net/article/201411.htm) |  详细介绍如何获取Cookies和使用Cookies进行自动登录  
[ Python爬虫 - Selenium（13）设置元素等待 ](https://www.jb51.net/article/201412.htm) |
详细介绍如何优雅的设置元素等待时间，防止程序运行过快而导致元素定位失败  
[ Python爬虫 - Selenium（14）窗口截图 ](https://www.jb51.net/article/201417.htm) |
详细介绍如何使用窗口截图  
[ Python爬虫 - Selenium（15）关闭浏览器 ](https://www.jb51.net/article/201419.htm) |
详细介绍两种关闭窗口的区别  
  
到此这篇关于Python爬虫之Selenium实现窗口截图的文章就介绍到这了,更多相关Selenium
窗口截图内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

