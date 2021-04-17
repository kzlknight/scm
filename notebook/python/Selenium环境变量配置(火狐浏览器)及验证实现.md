**前言**

配置火狐浏览器对应的selenium驱动

**一、火狐浏览器驱动下载**

[ 下载地址 ](https://github.com/mozilla/geckodriver/releases)  
根据对应的系统环境下载相应的压缩包（这里下载的是Windows系统64位安装包）

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020120711471125.png)  

安装包下载成功后将压缩包解压  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020120711471126.png)

**二、配置环境变量**

将geckodriver.exe放置到环境变量中（个人推荐放置到python环境变量中）

选中此电脑图标点击鼠标右键打开属性进入，选择高级系统设置  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020120711471127.png)

系统属性界面选择环境变量  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020120711471128.png)

环境变量选择Path，点击编辑  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020120711471129.png)

复制Python环境变量地址（注意不要进行改动）  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020120711471130.png)

我的电脑中粘贴地址前往（注意：scripts需要删除）  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020120711471131.png)

将解压好的geckodriver.exe文件复制粘贴到文件夹  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020120711471232.png)  

环境配置成功（谷歌、IE驱动也都可下载放入其中）

**三、验证安装**

打开Python的IDLE  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020120711471233.png)

从selenium导入webdriver方法（from selenium import webdriver）  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020120711471234.png)

打开火狐浏览器 browser = webdriver.Firefox()  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020120711471235.png)  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020120711471236.png)

打开百度 browser.get(“https://baidu.com”)  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020120711471237.png)  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020120711471238.png)

**至此完成环境配置及验证**

到此这篇关于Selenium环境变量配置(火狐浏览器)及验证实现的文章就介绍到这了,更多相关Selenium环境变量配置内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

