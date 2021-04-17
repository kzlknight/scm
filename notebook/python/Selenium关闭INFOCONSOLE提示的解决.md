参考： [ https://stackoverflow.com/questions/33983860/hide-chromedriver-console-
in-python?rq=1 ](https://stackoverflow.com/questions/33983860/hide-
chromedriver-console-in-python?rq=1)

**1. 问题起因：**

Selenium设置了headless，导致cmd控制台不断输出CONSOLE信息

```python

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu') # 上面三行代码就是为了将Chrome不弹出界面
```

**让人头疼的INFO:CONSOLE，不断输出ing**  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020120711540739.jpg)

**2. 解决：**

2.1 修改源码：External Libraries \ site-packages \ selenium \ webdriver \ common \
services.py

![](https://img.jbzj.com/file_images/article/202012/2020120711540740.jpg)

![](https://img.jbzj.com/file_images/article/202012/2020120711540741.jpg)

2.2 编辑service.py，默认是可读文件，会提示是否修改，选择运行就可以

**添加：**

```python

    from win32process import CREATE_NO_WINDOW
```

![](https://img.jbzj.com/file_images/article/202012/2020120711540842.jpg)

**找到start() Popen添加，如下图：**

```python

    creationflags=CREATE_NO_WINDOW
```

![](https://img.jbzj.com/file_images/article/202012/2020120711540843.jpg)

**3. 再次运行**

**干净清爽，舒服极了！**  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020120711540844.jpg)

到此这篇关于Selenium关闭INFO:CONSOLE提示的解决的文章就介绍到这了,更多相关Selenium关闭INFO:CONSOLE提示内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

