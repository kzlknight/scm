之所以把selenium爬虫称之为可视化爬虫

主要是相较于前面所提到的几种网页解析的爬虫方式

selenium爬虫主要是模拟人的点击操作

selenium驱动浏览器并进行操作的过程是可以观察到的

就类似于你在看着别人在帮你操纵你的电脑，类似于别人远程使用你的电脑

当然了，selenium也有无界面模式

**快速入门**

**selenium基本介绍:**

selenium 是一套完整的web应用程序测试系统，

包含了测试的录制（selenium IDE）,编写及运行（Selenium Remote Control）  
和测试的并行处理（Selenium Grid）。

Selenium的核心Selenium Core基于JsUnit，  
完全由JavaScript编写，因此可以用于任何支持JavaScript的浏览器上。  
selenium可以模拟真实浏览器，自动化测试工具，支持多种浏览器，

爬虫中主要用来解决JavaScript渲染问题。

用python写爬虫的时候，主要用的是selenium的Webdriver，

```python

    #安装selenium库
    pip install selenium
    #安装对应浏览器驱动
    # 我们可以通过下面的方式先看看Selenium.Webdriver支持哪些浏览器
    from selenium import webdriver
    print(help(webdriver))
```

```python

    适用浏览器：
    PACKAGE CONTENTS
      android (package)  blackberry (package)  chrome (package)
      common (package)   edge (package)     firefox (package)
      ie (package)     opera (package)     phantomjs (package)
      remote (package)   safari (package)    support (package)  webkitgtk (package)
    #这里要说一下比较重要的PhantomJS,
    #PhantomJS是一个而基于WebKit的服务端JavaScript API,
    #支持Web而不需要浏览器支持，
    #其快速、原生支持各种Web标准：Dom处理，CSS选择器，JSON等等。
    #PhantomJS可以用用于页面自动化、网络监测、网页截屏，以及无界面测试
```

[ 谷歌浏览器驱动下载地址 ](http://npm.taobao.org/mirrors/chromedriver/)  
注意对应版本号，chrome地址栏输入chrome://version/ 查看自己的Chrome版本  
我使用的是anaconda 下载好后丢入anaconda3\Scripts文件夹下就可以了  
如果是其他ide如：pycharm、VScode但加载的还是anaconda的集成python，依然可以这么操作

简单测试

```python

    from selenium import webdriver
    # #声明浏览器对象
    browser1 = webdriver.Chrome()
    browser2 = webdriver.Firefox()
    # #访问页面
    browser1.get("http://www.baidu.com")
    print(browser1.page_source)
    #关闭当前窗口
    browser1.close()
```

**元素定位**

要想对页面进行操作，首先要做的是选中页面元素，  
比较常见的八种元素定位方式，如下表

定位一个元素  |  定位多个元素  |  定位方式描述  
---|---|---  
find_element_by_id  |  find_elements_by_id  |  通过元素 id进行定位  
find_element_by_name  |  find_elements_by_name  |  通过元素 名称进行定位  
find_element_by_xpath  |  find_elements_by_xpath  |  通过xpath路径进行定位  
find_element_by_link_text  |  find_elements_by_link_text  |  通过完整超链接文本进行定位  
find_element_by_partial_link_text  |  find_elements_by_partial_link_text  |
通过部分超链接文本进行定位  
find_element_by_tag_name  |  find_elements_by_tag_name  |  通过标记名称进行定位  
find_element_by_class_name  |  find_elements_by_class_name  |  通过类名称进行定位  
find_element_by_css_selector  |  find_elements_by_css_selector  |
通过css选择器进行定位  
  
更详细定位方式可以参考：《 [ 史上最全！Selenium元素定位的30种方式
](https://www.jb51.net/article/186318.htm) 》

**页面操作**

1.表单填充

```python

    # 找到用户名输入用户名
    user = drive.find_element_by_name("LoginForm[username]")
    user.send_keys(username)
    # 找到密码输入密码
    pwd=drive.find_element_by_id("LoginForm_password")
    pwd.send_keys(password)
    # 点击登录按钮实现登录
    drive.find_element_by_class_name("login_btn").click()
```

2.窗口句柄

简单讲，句柄就是浏览器上方每一个窗口栏的唯一标识  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/202012040943011.png)

```python

    #获取当前窗口所有句柄
    handles = drive.window_handles
    #通过句柄 切换到第2个标签页
    drive.switch_to.window(handles[2])
    """操作完成"""
    #关闭当前窗口
    driver.close() 
    #通过句柄 切换到第1个标签页
    drive.switch_to.window(handles[0])
    time.sleep(random.uniform(2,3))
```

3.url加载和获取

```python

    #url加载
    drive.get(url)
    # 获取当前页面url并断言
    currentPageUrl = driver.current_url
```

4.cookie处理

  * get_cookies:获取cookie信息 
  * add_cookie:添加cookie信息 

```python

    drive.get("http://www.baidu.com")
    cookie = {'name':'foo','value':'bar'}
    drive.add_cookie(cookie)
    drive.get_cookies()
```

**等待方式**

现在很多网站采用 Ajax技术  
无法确定网页元素什么时候能被完全加载  
所以网页元素的选取比较困难  
此时就需要设置等待（等待网页加载完成）

selenium有两种等待方式:

  * 显式等待 
  * 隐式等待 

**1.显式等待**  
显式等待是一种条件触发式等待  
直到设置的某一条件达成时才会继续执行  
可以设置超时时间，如果超过超时时间元素依然没被加载，就会抛出异常

```python

    from selenium import webdriver
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    drive = webdriver.Chrome()
    url = 'http://www.baidu.com/'
    drive.get(url)
    
    try:
    	WebDriverWait(self.driver,10).until(EC.presence_of_element_located(By.ID,"LoginForm[username]")) #显示等待
    except:
     print('%s页面未找到元素'% loc)
```

以上代码加载 'http://www.baidu.com/'页面  
并定位id为"LoginForm[username]"的元素  
设置超时时间10秒，webDriverWait默认会500ms检测一下元素是否存在

selenium提供了一些内置的用于显示等待的方法，  
位于expected_conditions类中，详细见下表

内置方法  |  功能  
---|---  
title_is  |  判断当前页面的title是否等于预期内容  
title_contains  |  判断当前页面的title是否包含预期字符串  
presence_of_element_located  |  判断某个元素是否被加到了dom树里,  
并不代表该元素一定可见  
presence_of_all_element_located  |  判断是否至少有1个元素存在于dom树里  
visibility_of_element_located  |  判断某个元素是否可见  
visibility_of  |  判断某个元素是否可见  
invisibility_of_element_located  |  判断某个元素是否不存在于dom树里或不可见  
text_to_be_present_in_element  |  判断元素中的text是否包含了预期的字符串  
text_to_be_present_in_element_value  |  判断元素中的value属性是否包含了预期字符  
frame_to_be_available_and_switch_to_it  |  判断该frame是否可以切换进去，如果可以，  
返回True并切换进去，否则返回False  
element_to_be_clickable  |  判断某个元素是否可见并且是enable的  
staleness_of  |  等待某个元素从dom树中移除  
element_to_be_selected  |  判断某个元素是否被选中了，一般用于下拉列表  
element_located_to_be_selected  |  判断某个元素是否被选中了，一般用于下拉列表  
element_selection_state_to_be  |  判断某个元素的选中状态是否符合预期  
element_located_selection_state_to_be  |  判断某个元素的选中状态是否符合预期  
alert_is_present  |  判断页面上是否存在alert框  
  
**2.隐式等待**

隐式等待是在尝试定位某个元素时，如果没能立刻发现，就等待固定时长  
类似于socket超时，默认设置是0秒，即相当于最长等待时长

在浏览器界面直观感受是：  
等待直到网页加载完成（地址栏这个地方不是× 变成如下）时继续执行，  
网页加载超过设置等待时长才报错  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/202012040943012.png)  

使用方法

```python

    from selenium import webdriver
    drive = webdriver.Chrome()
    url = 'http://www.baidu.com/'
    #设置最大等待时长 10秒
    drive.implicitly_wait(10)
    drive.get(url)
    user = drive.find_element_by_name("LoginForm[username]")
```

**3.线程休眠**  
time.sleep(time)是比较常用的线程休眠方式  
为了避免风险，我个人比较喜欢随机休眠  
time.sleep(random.uniform(4,5))

扩展程序加载

```python

    # 设置好应用扩展
    chrome_options.add_extension(extension_path)
    #添加下载路径
    #download.default_directory：设置下载路径  profile.default_content_settings.popups：设置为 0 禁止弹出窗口
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory':tmp_path}
    chrome_options.add_experimental_option('prefs', prefs)
```

到此这篇关于python
爬虫之selenium可视化爬虫的实现的文章就介绍到这了,更多相关selenium可视化爬虫内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

