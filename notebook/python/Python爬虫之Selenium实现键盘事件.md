**一、常用按键**

按键  |  说明  
---|---  
Keys.BACK_SPACE  |  回退键（BackSpace）  
Keys.TAB  |  制表键（Tab）  
Keys.ENTER  |  回车键（Enter）  
Keys.SHIFT  |  大小写转换键（Shift）  
Keys.CONTROL  |  Control键（Ctrl）  
Keys.ALT  |  ALT键（Alt）  
Keys.ESCAPE  |  返回键（Esc）  
Keys.SPACE  |  空格键（Space）  
Keys.PAGE_UP  |  翻页键上（Page Up）  
Keys.PAGE_DOWN  |  翻页键下（Page Down）  
Keys.END  |  行尾键（End）  
Keys.HOME  |  行首键（Home）  
Keys.LEFT  |  方向键左（Left）  
Keys.UP  |  方向键上（Up）  
Keys.RIGHT  |  方向键右（Right）  
Keys.DOWN  |  方向键下（Down）  
Keys.INSERT  |  插入键（Insert）  
Keys.DELETE  |  删除键（Delete）  
Keys.NUMPAD0 ~ NUMPAD9  |  数字键1-9  
Keys.F1 ~ F12  |  F1 - F12键  
(Keys.CONTROL, 'a')  |  组合键Ctrf+a，全选  
(Keys.CONTROL, 'c')  |  组合键Ctrf+c，复制  
(Keys.CONTROL, 'x')  |  组合键Ctrf+x，剪切  
(Keys.CONTROL, 'v')  |  组合键Ctrf+v，粘贴  
  
**二、代码示例**  

```python

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import time
    
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    
    # 输入框输入内容
    driver.find_element_by_id("kw").send_keys("程序猿杂记6")
    
    time.sleep(2) #睡两秒，看一下效果
    
    # 删除多输入的一个 6
    driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
    
    time.sleep(2) #睡两秒，看一下效果
    
    # 输入空格键+“CSDN”
    driver.find_element_by_id("kw").send_keys(Keys.SPACE)
    driver.find_element_by_id("kw").send_keys("CSDN")
    
    time.sleep(2) #睡两秒，看一下效果
    
    # ctrl+a 全选输入框内容
    driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')
    
    time.sleep(2) #睡两秒，看一下效果
    
    # ctrl+x 剪切输入框内容
    driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')
    
    time.sleep(2) #睡两秒，看一下效果
    
    # ctrl+v 粘贴内容到输入框
    driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'v')
    
    time.sleep(2) #睡两秒，看一下效果
    
    #通过回车键来代替单击操作
    driver.find_element_by_id("su").send_keys(Keys.ENTER)
    
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
  
到此这篇关于Python爬虫之Selenium实现键盘事件的文章就介绍到这了,更多相关Selenium
键盘事件内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

