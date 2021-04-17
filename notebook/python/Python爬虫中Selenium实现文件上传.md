前言：大部分的文件上传功能都是用input标签实现，这样就完全可以把它看作一个输入框，可以通过send_keys()指定文件进行上传了。

本章中用到的关键方法如下：

```python

    send_keys()：上传文件或者输入文本
    from selenium import webdriver
    import time
    
    driver = webdriver.Chrome()
    driver.get('http://file.yiyuen.com/file/')
    
    # 定位上传按钮，添加本地文件
    driver.find_element_by_name("files").send_keys('D:\\test.txt')
    time.sleep(10)
    
    driver.quit()
    
    
```

Web上本地上传图片，弹出的框Selenium是无法识别的，也就是说，selenium本身没有直接的方法去实现上传本地文件，这里总结了两种上传文件的方式。

**一、利用Robot类处理文件上传。**

其大致流程可以为：

1、 利用selenium点击web上本地文件的上传按钮；

2、 在弹出的弹框中，文件路径输入框默认的是光标的聚焦，将文件在磁盘上的路径通过拷贝和黏贴的方法写上去。

3、 通过按下回车，默认触发弹框的确定按钮，完成文件上传的功能。

这里以百度首页的利用图片搜索为例：

打开百度首页，搜索按钮左侧有一个照相机的图标，点击可以选择图片搜索，我们通过本地上传图片的过程来模拟文件自动化上传操作。准备条件，在百度图片搜索一个图片，保存到桌面，例如找到一个关于selenium的图片，然后保存在桌面，名称为selenium.jpg。

相关实现代码如下：

```python

    package first;
    
    import java.awt.Robot;
    
    import java.awt.Toolkit;
    
    import java.awt.datatransfer.StringSelection;
    
    import java.awt.event.KeyEvent;
    
    import java.util.concurrent.TimeUnit;
    
    import org.openqa.selenium.By;
    
    import org.openqa.selenium.WebDriver;
    
    import org.openqa.selenium.firefox.FirefoxDriver;
    
    public class shangchuang {
    
    public static void main(String[] args)throws Exception {
    
    WebDriver driver=new FirefoxDriver();
    
    driver.manage().window().maximize();
    
    driver.manage().timeouts().implicitlyWait(4, TimeUnit.SECONDS);
    
    
    driver.get("https://www.baidu.com");
    
    //指定图片路径
    
    StringSelection selection=new StringSelection("C:\\Users\\你的用户名\\Desktop\\selenium.jpg");
    
    //把图片路径复制到剪切板
    
    Toolkit.getDefaultToolkit().getSystemClipboard().setContents(selection, null);
    
    System.out.println("selection"+selection);
    
    //点击照相机这个工具
    
    driver.findElement(By.xpath("//*/span[@class='soutu-btn']")).click();
    
    //点击本地上传图片
    
    driver.findElement(By.xpath("//*/div[@class='upload-wrap']")).click();
    
    
    //新建一个Robot类的对象
    
    Robot robot=new Robot();
    
    Thread.sleep(1000);
    
    //按下Ctrl+V
    
    robot.keyPress(KeyEvent.VK_CONTROL);
    
    robot.keyPress(KeyEvent.VK_V);
    
    //释放Ctrl+V
    
    robot.keyRelease(KeyEvent.VK_CONTROL);
    
    robot.keyRelease(KeyEvent.VK_V);
    
    Thread.sleep(2000);
    
    //点击回车
    
    robot.keyPress(KeyEvent.VK_ENTER);
    
    robot.keyRelease(KeyEvent.VK_ENTER);
    }
    }
```

**二、利用AutoIt上传文件**

以上是第一种方的实现，第二种方式是利用AutoIt这个工具。这是一个能支持桌面GUI自动化的工具，它支持脚本语言编写。在Selenium脚本中如果需要AutoIt来协助这个文件上传功能，大概步骤是这样的：

1. Selenium点击web产品上的文件上传按钮，弹窗上传框。 

2.执行AutoIt实现准备好的脚本文件，这个脚本文件写了关于上传什么文件的一个.exe文件。

在一切测试工作之前，我们先下载和安装AutoIt。

1）打开AutoIt的官网下载地址

[ https://www.autoitscript.com/site/autoit/downloads/
](https://www.autoitscript.com/site/autoit/downloads/)

2）点击下载zip，当然也可以下载Editor。

![](https://img.jbzj.com/file_images/article/202012/202012041144498.png)

解压得到的效果如图：

![](https://img.jbzj.com/file_images/article/202012/202012041144509.png)

3）点击SciTe文件夹，我们打开脚本编辑器。双击SciTE.exe

![](https://img.jbzj.com/file_images/article/202012/2020120411445010.png)

4）打开百度图片上传窗口，同时打开AutoIt 脚本编辑器和元素定位器。拖动元素定位器上那个靶点形状按钮到文件上传弹窗，能够捕获到一些元素信息。

![](https://img.jbzj.com/file_images/article/202012/2020120411445011.png)

5）在AutoIt脚本编辑器里输入如下脚本，绿色部分为解释的，不需要写。

![](https://img.jbzj.com/file_images/article/202012/2020120411445012.png)

6）编译成一个.exe文件

先保存到本地，例如默认路径保存，名称为UploadFile.au3,然后在AutoIt脚本编辑器中点击Tools菜单，选择compile,会在同路径下生成一个UploadFile.exe的文件，待会在Selenium脚本要使用。

![](https://img.jbzj.com/file_images/article/202012/2020120411445013.png)

7）Selenium脚本执行UploadFile.exe文件，观察文件是否上传。

```python

    package first;
    
    import java.util.concurrent.TimeUnit;
    
    import org.openqa.selenium.By;
    
    import org.openqa.selenium.WebDriver;
    
    import org.openqa.selenium.firefox.FirefoxDriver;
    
    public class AutoIt {
    
    public static void main(String[] args) throws Exception{
    
    WebDriver driver=new FirefoxDriver();
    
    driver.manage().window().maximize();
    
    driver.manage().timeouts().implicitlyWait(4, TimeUnit.SECONDS);
    
    
    driver.get("http://www.baidu.com");
    
    //点击照相机这个工具
    
    driver.findElement(By.xpath("//*/span[@class='soutu-btn']")).click();
    
    //点击本地上传图片
    
    driver.findElement(By.xpath("//*/div[@class='upload-wrap']")).click();
    
    // 执行桌面的AutoIt封装的脚本
    
    Runtime.getRuntime().exec("C:\\Users\\你的用户名\\Desktop\\UploadFile.exe");
    
    }
    
    }
    
    
```

我用的是火狐62，最终的效果如图所示：

![](https://img.jbzj.com/file_images/article/202012/2020120411445014.png)

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
  
到此这篇关于Python爬虫中Selenium实现文件上传的文章就介绍到这了,更多相关Selenium
文件上传内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

