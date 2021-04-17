selenium操作chrome浏览器需要有ChromeDriver驱动来协助。webdriver中关浏览器关闭有两个方法，一个叫quit，一个叫close。  

```python

    /**
      * Close the current window, quitting the browser if it's the last window currently open.
      */
     void close();
    
     /**
      * Quits this driver, closing every associated window.
      */
     void quit();
    
    
```

通过查看以上官方声明文档，可以看出close方法是关闭当前窗口，这个当前如何理解？就是driver实例操作的页面，叫当前。如果当前窗口只有一个tab，那么这个close方法就相当于关闭了浏览器。quit方法就是直接退出并关闭所有关联的tab窗口。所以，close方法一般关闭一个tab，quit方法才是我们认为的完全关闭浏览器方法。为了证明这个，我们用一个例子去演示：  

```python

    package lessons;
    
    import org.openqa.selenium.By;
    import org.openqa.selenium.WebDriver;
    import org.openqa.selenium.chrome.ChromeDriver;
    
    public class FindElement_LinkText {
    
      public static void main(String[] args) throws Exception {
    
        System.setProperty("webdriver.chrome.driver", ".\\Tools\\chromedriver.exe");
    
        WebDriver driver = new ChromeDriver();
        driver.manage().window().maximize();
    
        driver.get("https://www.baidu.com");
    
        driver.close();
        //driver.quit();
      }
    
    }
    
    
```

通过切换注销最后两行代码，分别运行，观察这两种方法的实际效果。当使用close方法的时候，因为只有百度首页这个tab，所以会关闭浏览器，但是通过查看任务管理器发现，ChromeDriver进程仍存在内存中。如果使用quit方法，整个浏览器都直接关闭，ChromeDriver进程也会被结束。

ChromeDriver是轻量级的服务，在单任务或不需要频繁启动浏览器的情况下，使用driver.quit()关闭浏览器，可以正常结束ChromeDriver进程。若在一个比较大的
测试套件中频繁的启动关闭，会增加一个比较明显的延时导致浏览器进程不被关闭的情况发生，为了避免这一状况我们可以通过ChromeDriverService来控制ChromeDriver进程的生死，达到用完就关闭的效果避免进程占用情况出现（Running
the server in a child process）。具体实现如下：

```python

    ChromeDriverService service = new ChromeDriverService.Builder() .usingChromeDriverExecutable(new File("E:\\Selenium WebDriver\\chromedriver_win_23.0.1240.0\\chromedriver.exe")).usingAnyFreePort().build();
    service.start();
    driver = new ChromeDriver();
    driver.get("http://www.baidu.com");
    driver.quit();
    // 关闭 ChromeDriver 接口
    service.stop();
    
```

以上讨论的均是java版的实现，对于python来说是使用service库来实现控制chromedriver的开启和关闭。

```python

    from selenium.webdriver.chrome.service import Service
    
```

创建的时候需要把chromedriver.exe的位置写在Service的XXX部分，需要调用他的命令行方法，不然报错，然后启动就可以了。

```python

    c_service = Service('xxx')
    c_service.command_line_args()
    c_service.start()
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    
```

关闭的时候用quit而不是采用close，close只会关闭当前页面，quit会退出驱动并且关闭所关联的所有窗口，最后执行完以后就关闭。

```python

    driver.quit()
    c_service.stop()
    
```

嫌麻烦也可以直接使用python的os模块执行下面两句话结束进程

```python

    os.system('taskkill /im chromedriver.exe /F')
    os.system('taskkill /im chrome.exe /F')
    
```

到此这篇关于Selenium执行完毕未关闭chromedriver/geckodriver进程的解决办法(java版+python版)的文章就介绍到这了,更多相关Selenium关闭chromedriver/geckodriver进程内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

