前言：在页面操作过程中有时候点击某个链接会弹出新的窗口，但由于Selenium的所有操作都是在第一个打开的页面进行的，这时就需要主机切换到新打开的窗口上进行操作。WebDriver提供了switch_to.window()方法，可以实现在不同的窗口之间切换。
以百度首页和百度注册页为例，在两个窗口之间的切换。

本章中用到的关键方法如下：

  * current_window_handle：获得当前窗口句柄 
  * window_handles：返回所有窗口的句柄到当前会话 
  * switch_to.window()：用于切换到相应的窗口 

跳转至注册页面，然后获取所有页面的句柄，并打印各个页面的title

```python

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import time
    
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    
    time.sleep(2) #睡两秒，看一下效果
    
    driver.find_element_by_link_text('登录').click()
    
    time.sleep(2) #睡两秒，看一下效果
    
    driver.find_element_by_link_text("立即注册").click()
    
    time.sleep(2) #睡两秒，看一下效果
    
    # 获得当前窗口句柄
    sreach_windows = driver.current_window_handle
    
    # 获得当前所有打开的窗口的句柄
    all_handles = driver.window_handles
    for handle in all_handles:
     if handle != sreach_windows:
      driver.switch_to.window(handle)
      print(driver.title)
     else:
      print('当前页面title：%s'%driver.title)
    
    driver.quit()
    
    
```

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
  
到此这篇关于Python爬虫之Selenium多窗口切换的实现的文章就介绍到这了,更多相关Selenium多窗口切换内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

