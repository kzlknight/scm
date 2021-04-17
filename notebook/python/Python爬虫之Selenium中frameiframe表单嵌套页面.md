在Web应用中经常会遇到frame/iframe表单嵌套页面的应用，WebDriver只能在一个页面上对元素识别与定位，对于frame/iframe表单内嵌页面上的元素无法直接定位。这时就需要通过
` switch_to.frame() ` 方法将当前定位的主体切换为frame/iframe表单的内嵌页面中。

本章中用到的关键方法如下：

  * switch_to.frame()：切换为frame/iframe表单的内嵌页面中 
  * switch_to.parent_frame()：退出内嵌页面 

**以ip138网站为例**  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/202012041055467.jpg)

```python

    from selenium import webdriver
    
    driver = webdriver.Chrome()
    
    # 打开ip138网站
    driver.get("http://www.ip138.com/")
    
    # 定位到内嵌网页(iframe),并进入表单
    xf = driver.find_element_by_xpath('/html/body/div/div[3]/iframe')
    driver.switch_to.frame(xf)
    #driver.switch_to.frame(name or id) #默认直接取表单的id 或name属性,如果都没有则通过上边的定位方式
    print(driver.find_element_by_xpath('/html/body/p[1]').text)
    
    # 退出内嵌网页(iframe)，如果想操作外层的页面，不退出是会报错的
    driver.switch_to.default_content()
    print(driver.find_element_by_xpath('/html/body/div/div[3]/h3').text)
    
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
  
到此这篇关于Python爬虫之Selenium中frame/iframe表单嵌套页面的文章就介绍到这了,更多相关Selenium
frame/iframe表单嵌套内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

