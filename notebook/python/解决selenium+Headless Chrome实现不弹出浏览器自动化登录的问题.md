目前由于phantomjs已经不维护了，而新版的Chrome（59+）推出了Headless模式，对爬虫来说尤其是定时任务的爬虫截屏之类的是一大好事。

不过按照网络上的一些方法来写的话，会报下面的错误：

![](https://img.jbzj.com/file_images/article/202101/202101090943343.png)

后来经过分析，他们运行python是在mac或者linux下进行的，win下由于高版本的chromedriver只能通过路径进行指定，所以会出现这类找不到驱动程序的错误。

经过比对常识网络上的各种代码，后来得出了win下可顺畅执行的driver的写法如下：

```python

    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from PIL import Image,ImageEnhance
    
    path = 'E:/Cyou/chromedriver.exe'
     
    #打开浏览器
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    # 驱动路径
    path = 'E:/Cyou/chromedriver.exe'
    # 创建浏览器对象
    driver = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
```

> 注意：别忘了导入：from selenium.webdriver.chrome.options import Options

否则会报错。

然后后面就可以进行之前的逻辑不进行改动了，只要这里书写正确就可以了。

问题解决。

到此这篇关于解决selenium+Headless
Chrome实现不弹出浏览器自动化登录的问题的文章就介绍到这了,更多相关Chrome实现不弹出浏览器自动化登录内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

