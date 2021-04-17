**一、定位元素的8种方式**  

1、方法介绍

定位一个元素  |  定位多个元素  |  含义  
---|---|---  
find_element_by_id()  |  find_elements_by_id()  |  通过元素id定位  
find_element_by_name()  |  find_elements_by_name()  |  通过元素name定位  
find_element_by_xpath()  |  find_elements_by_xpath()  |  通过xpath表达式定位  
find_element_by_link_text()  |  find_elements_by_link_text()  |  通过完整超链接定位  
find_element_by_partial_link_text()  |  find_elements_by_partial_link_text()
|  通过部分链接定位  
find_element_by_tag_name()  |  find_elements_by_tag_name()  |  通过标签定位  
find_element_by_class_name()  |  find_elements_by_class_name()  |  通过类名进行定位  
find_elements_by_css_selector()  |  find_elements_by_css_selector()  
  
2、实例演示  

```python

    from selenium import webdriver
    
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com/')
    
    #通过元素id定位（）
    driver.find_element_by_id('kw')
    
    #通过元素name定位
    driver.find_element_by_name('wd')
    
    #通过类名进行定位
    driver.find_element_by_class_name('s_ipt')
    
    #通过标签定位
    driver.find_element_by_tag_name('input')
    
    #通过xpath表达式定位
    driver.find_element_by_xpath('//*[@id="kw"]')
    
    #通过css选择器进行定位
    driver.find_element_by_css_selector('#kw')
    
    #通过完整超链接定位
    driver.find_element_by_link_text('新闻')
    
    #通过部分链接定位
    driver.find_element_by_partial_link_text('hao')
    
    driver.quit()#关闭所有标签页
    
    
```

关于xpaht和css的定位比较复杂，请参考：

[ XPath获取方法 ](https://www.jb51.net/article/138386.htm)  
[ XPath语法 ](https://www.runoob.com/xpath/xpath-syntax.html)  
[ CSS选择器语法 ](https://www.runoob.com/cssref/css-selectors.html)  

  1. 此处定位可能无法直接查看效果（打印结果为获取的元素对象） 
  2. 定位一般都配合一些常用方法使用 
  3. 上述实例中都是单个元素定位，多个元素定位关键字请参考上边的方法介绍   

**二、WebDriver常用方法（配合定位方法使用）**  

1.点击和输入

  1. clear()： 清除文本，大多数用于输入框 
  2. send_keys ()： 模拟按键输入，大多数用于输入框 
  3. click()： 单击元素，用处比较广泛 

更多鼠标键盘事件请参考：  
[ Python爬虫 - Selenium（5）鼠标事件 ](https://www.jb51.net/article/201383.htm)  
[ Python爬虫 - Selenium（6）键盘事件 ](https://www.jb51.net/article/201387.htm)

```python

    from selenium import webdriver
    import time
    
    driver = webdriver.Chrome()
    
    driver.get('https://www.baidu.com/')
    
    driver.find_element_by_id("kw").clear()
    driver.find_element_by_id("kw").send_keys("程序猿杂记")
    driver.find_element_by_id("su").click()
    time.sleep(5)
    
    driver.quit() # 关闭所有标签页
    
```

3.提交  

submit()：用于提交表单，相当于回车，应用范围远不及 click()广泛  

```python

    from selenium import webdriver
    import time
    
    driver = webdriver.Chrome()
    
    driver.get('https://www.baidu.com/')
    
    driver_id = driver.find_element_by_id("kw")
    driver_id.send_keys("程序猿杂记")
    driver_id.submit()
    time.sleep(5)
    
    driver.quit() # 关闭所有标签页
    
    
```

4.获取一些内容

  * title：获得当前页面的标题 
  * current_url：用户获得当前页面的URL 
  * size： 获取元素的尺寸 
  * text： 获取元素的文本 
  * get_attribute()： 获得属性值 
  * is_displayed()： 该元素是否用户可见 

```python

    from selenium import webdriver
    
    driver = webdriver.Chrome()
    
    driver.get('https://www.baidu.com/')
    
    # 获取当前页面的title
    title = driver.title
    print(title)
    
    #获取当前页的url
    url = driver.current_url
    print(url)
    
    # 获得输入框的尺寸
    input_size = driver.find_element_by_id('kw').size
    print(input_size)
    
    # 返回百度页面底部备案信息
    text = driver.find_element_by_id("cp").text
    print(text)
    
    # 返回元素的属性值， 可以是 id、 name、 type 或其他任意属性
    attribute = driver.find_element_by_id("kw").get_attribute('type')
    print(attribute)
    
    # 返回元素的结果是否可见， 返回结果为 True 或 False
    result = driver.find_element_by_id("kw").is_displayed()
    print(result)
    
    driver.quit() # 关闭所有标签页
    
    
    
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
  
到此这篇关于详解Selenium 元素定位和WebDriver常用方法的文章就介绍到这了,更多相关Selenium
元素定位内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

