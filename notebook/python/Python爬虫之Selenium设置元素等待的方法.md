**一、显式等待**  

WebDriverWait类是由WebDirver
提供的等待方法。在设置时间内，默认每隔一段时间检测一次当前页面元素是否存在，如果超过设置时间检测不到则抛出异常（TimeoutException）

```python

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time
    
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com/')
    
    element = WebDriverWait(driver, 5, 0.5).until(
          EC.presence_of_element_located((By.ID, "kw"))
          )
    element.send_keys('selenium')
    time.sleep(5)
    
    driver.quit()
    
```

语法：

  * WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None).until(method, message=‘')   

参数说明如下：

  * driver：浏览器驱动 
  * timeout：最长超时时间，默认以秒为单位 
  * poll_frequency：检测的间隔时间，默认为0.5s 
  * ignored_exceptions：超时后的异常信息，默认情况下抛NoSuchElementException异常 
  * until(method, message=‘')：调用该方法提供的驱动程序作为一个参数，直到返回值为True 
  * until_not(method, message=‘')：调用该方法提供的驱动程序作为一个参数，直到返回值为False 
  * presence_of_element_located()：判断元素是否存在。 

**二、隐式等待**  

```python

    from selenium import webdriver
    from selenium.common.exceptions import NoSuchElementException
    import time
    
    driver = webdriver.Chrome()
    
    # 设置隐式等待为5秒
    driver.implicitly_wait(5)
    driver.get("http://www.baidu.com")
    
    try:
     print(time.strftime('%Y-%m-%d %H:%M:%S'))
     driver.find_element_by_id("123456").send_keys('selenium') #不存在的id，看输出报错和时间
     # driver.find_element_by_id("kw").send_keys('selenium') # 存在的id
    except NoSuchElementException as e:
     print(e)
    finally:
     print(time.strftime('%Y-%m-%d %H:%M:%S'))
     driver.quit()
    
```

implicitly_wait()
默认0，参数的单位为秒，上边设置的等待时间为5秒，这个时间不像time.sleep(5)那样直接睡5秒；当执行流程到某个元素定位时，如果元素可以定位，则继续执行；如果元素定位不到，则它将以循环的方式不断地判断元素是否被定位到。比如说在1秒的时候定位到了，那么直接向下运行如果超出设置时长，则抛出异常。  

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
  
到此这篇关于Python爬虫之Selenium设置元素等待的方法的文章就介绍到这了,更多相关Selenium
元素等待内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

