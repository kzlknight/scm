JavaScript 有三种弹窗 Alert (只有确定按钮), Confirmation (确定,取消等按钮), Prompt
(有输入对话框)，而且弹出的窗口是不能通过前端工具对其进行定位的，这个时候就可以通过switch_to.alert方法来定位这个弹窗，并进行一系列的操作。

本章中用到的关键方法如下：

  * switch_to.alert：定位到警告框 
  * text：获取警告框中的文字信息 
  * accept()：接受现有警告框(相当于确认) 
  * dismiss()：解散现有警告框(相当于取消) 
  * send_keys('文本内容')：发送文本至警告框(适用于有输入对话框的弹窗) 
  * click()：鼠标点击事件(其他鼠标事件请参考 [ Python爬虫 - Selenium（5）鼠标事件 ](https://www.jb51.net/article/201383.htm) ) 
  * move_to_element()：鼠标悬停(详情请参考 [ Python爬虫 - Selenium（5）鼠标事件 ](https://www.jb51.net/article/201383.htm) ) 

```python

    from selenium import webdriver
    from selenium.webdriver import ActionChains
    import time
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    
    # 鼠标悬停至“设置”链接
    link = driver.find_element_by_link_text('设置')
    ActionChains(driver).move_to_element(link).perform()
    time.sleep(2) #睡两秒，看一下效果
    
    # 打开搜索设置
    driver.find_element_by_link_text("搜索设置").click()
    time.sleep(2) #睡两秒，看一下效果
    
    # 保存设置
    driver.find_element_by_class_name("prefpanelgo").click()
    time.sleep(2) #睡两秒，看一下效果
    
    # 定位警告框
    alert = driver.switch_to.alert
    print(alert.text) # 打印警告框内容
    #alert.send_keys('输入内容') #此测试网站不是可输入类型的弹窗，先注释掉
    alert.accept() #接受现有警告框，相当于确认
    #alert.dismiss() #解散现有警告框，相当于取消
    time.sleep(2) #睡两秒，看一下效果
    
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
  
到此这篇关于Python爬虫之Selenium警告框(弹窗)处理的文章就介绍到这了,更多相关Selenium警告框内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

