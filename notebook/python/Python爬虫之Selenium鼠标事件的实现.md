**一、常用方法**

函数名  |  说明  
---|---  
click(on_element=None)  |  点击鼠标右键  
click_and_hold(on_element=None)  |  点击鼠标左键，不松开  
release(on_element=None)  |  在某个元素位置松开鼠标左键  
context_click(on_element=None)  |  点击鼠标右键  
double_click(on_element=None)  |  双击鼠标左键  
drag_and_drop(source, target)  |  拖拽到某个元素然后松开  
drag_and_drop_by_offset(source, xoffset, yoffset)  |  拽到某个坐标然后松开  
move_by_offset(xoffset, yoffset)  |  鼠标从当前位置移动到某个坐标  
move_to_element(to_element)  |  鼠标移动到某个元素  
move_to_element_with_offset(to_element, xoffset, yoffset)  |
移动到距某个元素（左上角坐标）多少距离的位置  
perform()  |  执行所有 ActionChains 中存储的行为,相当于提交  
  
**二、代码示例**  

选几个经常使用的测试一下，其他事件语法相同

```python

    from selenium import webdriver
    import time
    from selenium.webdriver import ActionChains
    
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.cn")
    
    #定位到需要右击的元素，然后执行鼠标右击操作（例：对新闻标签进行右击）
    context_click_location = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[3]/a[1]')
    ActionChains(driver).context_click(context_click_location).perform()
    
    time.sleep(2) #睡两秒，看一下效果
    
    # 定位到需要悬停的元素,然后执行鼠标悬停操作（例：对设置标签进行悬停）
    move_to_element_location = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[3]/a[8]")
    ActionChains(driver).move_to_element(move_to_element_location).perform()
    
    time.sleep(2) #睡两秒，看一下效果
    
    # 鼠标悬浮后点击高级搜索
    driver.find_element_by_xpath("/html/body/div[1]/div[6]/a[2]").click()
    
    time.sleep(2) #睡两秒，看一下效果
    
    driver.quit() #关闭所有标签页
```

由于百度没有可拖动的元素，所以在菜鸟上找了一个网址进行测试，由于菜鸟上的网页是使用frame内嵌的，所以添加了个处理frame的过程，关于frame的处理请参考我的另一篇文章：
[ Python爬虫 - Selenium（8）frame/iframe表单嵌套页面
](https://www.jb51.net/article/201392.htm)

```python

    from selenium import webdriver
    from selenium.webdriver import ActionChains
    import time
    
    driver = webdriver.Chrome()
    driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-example-draggable-scroll")
    # 切换到目标元素所在的frame
    driver.switch_to.frame("iframeResult")
    
    # 确定拖拽目标的起点和终点，完成拖拽
    start_location = driver.find_element_by_id("draggable")
    end_location = driver.find_element_by_id("draggable3")
    ActionChains(driver).drag_and_drop(start_location,end_location).perform()
    
    time.sleep(2) #睡两秒，看一下效果
    
    driver.quit() #关闭所有标签页
    
    
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
  
到此这篇关于Python爬虫之Selenium鼠标事件的实现的文章就介绍到这了,更多相关Selenium
鼠标事件内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

