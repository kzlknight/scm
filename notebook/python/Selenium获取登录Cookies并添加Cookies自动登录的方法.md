本章中用到的关键方法如下：

  * get_cookies()： 获得所有cookie信息。 
  * get_cookie(name)： 返回字典的key为“name”的cookie信息。 
  * add_cookie(cookie_dict)： 添加cookie。“cookie_dict”指字典对象，必须有name 和value 值。 
  * delete_cookie(name,optionsString)：删除cookie信息。“name”是要删除的cookie的名称，“optionsString”是该cookie的选项，目前支持的选项包括“路径”，“域”。 
  * delete_all_cookies()： 删除所有cookie信息。 

**1、模拟登陆并获取Cookies**  

```python

    from selenium import webdriver
    import time
    
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com/')
    
    # 模拟登陆
    driver.find_element_by_link_text('登录').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__footerULoginBtn"]').click()
    time.sleep(2)
    driver.find_element_by_name("userName").send_keys("账号")
    driver.find_element_by_name("password").send_keys("密码")
    driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__submit"]').click()
    time.sleep(20) #可能会出现验证码，手动点一下
    
    # 获取cookies
    cookies = driver.get_cookies()
    print(cookies)
    driver.quit()
    
    
```

**2、添加Cookies自动登录**  

注：

获取Cookies的时候每个字典的字段不统一，全部添加会报错，所以本人只添加了比较重要的几个字段。  
把代码中cookies字段的list换成上一步获取的内容，或者自己构建。  

```python

    from selenium import webdriver
    import time
    
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com/')
    time.sleep(2)
    cookies = [] #换成上一步获取的Cookies
    for cookie in cookies:
     driver.add_cookie(
     {
      'domain':cookie['domain'],
      'name': cookie['name'],
      'value':cookie['value'],
      'path': cookie['path']
     }
     )
    # # 刷新页面
    driver.refresh()
    
    # driver.quit() #为方便查看，页面就不关了
```

**selenium 使用 cookies**  

selenium 需要先打开一个网址，才能加载进去cookies(知道cookies是哪个网站的)。添加完cookies再打开网址，使用cookies

前面读取的cookies 是一个包含着每一个cookies的name,value
的字典，即name1:value1,name2:value2字典。遍历添加网站使用的每一个cookies的name,value.

```python

    tbCookies = readTaobaoCookies()
    
    brower.get("https://www.taobao.com")
    for cookie in tbCookies:
     brower.add_cookie({
     "domain":".taobao.com",
     "name":cookie,
     "value":tbCookies[cookie],
     "path":'/',
     "expires":None
     })
    brower.get("https://www.taobao.com")
    
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
  
到此这篇关于Selenium获取登录Cookies并添加Cookies自动登录的方法的文章就介绍到这了,更多相关Selenium获取登录Cookies内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

