在我们浏览网页的时候经常会碰到下拉框，WebDriver提供了Select类来处理下拉框，详情请往下看：

本章中用到的关键方法如下：

  * select_by_value()：设置下拉框的值 
  * switch_to.alert.accept()：定位并接受现有警告框(详情请参考 [ Python爬虫 - Selenium（9）警告框(弹窗)处理 ](https://www.jb51.net/article/201394.htm) ) 
  * click()：鼠标点击事件(其他鼠标事件请参考 [ Python爬虫 - Selenium（5）鼠标事件 ](https://www.jb51.net/article/201383.htm) ) 
  * move_to_element()：鼠标悬停(详情请参考 [ Python爬虫 - Selenium（5）鼠标事件 ](https://www.jb51.net/article/201383.htm) ) 

```python

    from selenium import webdriver
    from selenium.webdriver import ActionChains
    from selenium.webdriver.support.select import Select
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
    
    # 搜索结果显示条数
    sel = driver.find_element_by_xpath("//select[@id='nr']")
    Select(sel).select_by_value('50') # 显示50条
    time.sleep(2) #睡两秒，看一下效果
    
    # 保存设置
    driver.find_element_by_class_name("prefpanelgo").click()
    time.sleep(2) #睡两秒，看一下效果
    
    # 定位并接受现有警告框
    alert = driver.switch_to.alert.accept()
    time.sleep(2) #睡两秒，看一下效果
    
    driver.quit()
```

select类中的函数列表

函数  |  解析  
---|---  
options  |  返回select元素所有的options  
all_selected_options  |  返回select元素中所有已选中的选项  
first_selected_option  |  返回select元素中选中的第一个选项  
select_by_index(index)  |  通过索引定位，index索引是从“0”开始  
select_by_value(value)  |  通过value属性值定位  
select_by_visible_text(text)t  |
通过文本值定位，visible_text是在option标签中间的值，即显示在下拉框的值；  
deselect_all()  |  取消全部的已选择项  
deselect_by_index(index)  |  取消已选中的索引项  
deselect_by_value(value)  |  取消已选中的value值  
deselect_by_visible_text(text)  |  取消已选中的文本值  
  
举例

html如下：  

```python

    <!DOCTYPE html>
    <html lang="en">
    <head>
     <meta charset="UTF-8">
     <title>我是标题</title>
    </head>
    <body>
    <!--select标签-->
    <select name="city" size="5" multiple="multiple">
     <option value="1" tabindex="1">北京</option>
     <option value="2" tabindex="2" selected="selected">河南</option>
     <option value="3" tabindex="3">河北</option>
     <option value="4" tabindex="4">山东</option>
     <option value="5" tabindex="5">上海</option>
    </select>
    
    </body>
    </html>
```

![](https://img.jbzj.com/file_images/article/202012/2020124110619299.png?202011411632)

```python

    from selenium import webdriver
    from selenium.webdriver.support.select import Select
    import time
    
    driver = webdriver.Chrome(r"D:\browser\chromedriver\chromedriver.exe")
    driver.get("http://localhost:63342/ui_test/select%E6%A0%87%E7%AD%BE.html")
    
    driver.maximize_window()
    
    ele = driver.find_element_by_name("city")
    select = Select(ele)
    select.select_by_value("3") # 选中"河北"
    time.sleep(3)
    select.select_by_index(0) # 选中"北京"
    time.sleep(3)
    select.deselect_by_value("3") # 取消选中"河北"
    time.sleep(3)
    select.deselect_by_index(0) # 取消选中"北京"
    time.sleep(3)
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
  
到此这篇关于Python爬虫之Selenium下拉框处理的实现的文章就介绍到这了,更多相关Selenium
下拉框内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

