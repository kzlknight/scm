之前总是想要买aj，但是淘宝店铺每次发售手动抢的时候一般都会被黄牛抢走。。。最近毕业设计学习了一下python的东西，所以写了这么一个抢购的东西算是解决自己一个小小的愿望，这可是aj啊。  
我会把内容写的尽量面向初学者，从头至尾的过程都会有所提及。代码也放在了后面

###  一、所需环境

Selenium

Selenium是一个开源的自动化测试工具。原理是通过模拟浏览器操作，还支持java，python，c#，php等主流的编程语言。

一般爬虫也支持Selenium，一些经过js渲染的内容和数据和ajax异步请求出来的数据通过Selenium就能很简单直观的爬取下来。但是Selenium的缺点也是显而易见的，相比于正则的匹配Selenium要加载浏览器以及更多的东西，他的执行速度比其他模块慢很多，所以若要保证速度，能不用Selenium就不要用Selenium吧。

web测试自动化：不同于单元测试和接口测试，web测试的自动化更加贴近于人的行为，通过对用户点击行为和文本输入行为等进行模拟，当web自动化登录成功后，就去获取这个数据进行断言。断言如果相等，测试通过；如果不相等，测试失败。用户可以看到某一项操作是否真的产生了，但是程序只能通过判断某些“证据”去判断之前的行为是否真的生效。

###  二、安装

下载 [ Selenium ](https://www.selenium.dev/) 并安装

安装对应浏览器的驱动程序 [ WebDriver ](https://selenium-
python.readthedocs.io/installation.html)  

驱动程序要和自己电脑上的浏览器版本相对应，比如我使用的chrome浏览器是72版本的，就要下载ChromeDriver2.46这个版本。

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/202101070950207.png)

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/202101070950208.png)  

下载解压之后配置环境变量Path即可。 Mac对应的环境变量配置可以参考这位老哥的文章进行配置

###  三、代码

```python

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    
    from selenium import webdriver
    import datetime
    import time
    
    
    def login():
      # 打开淘宝登录页，并进行扫码登录
      browser.get("https://www.taobao.com")
      time.sleep(3)
      if browser.find_element_by_link_text("亲，请登录"):
        browser.find_element_by_link_text("亲，请登录").click()
        print("请在15秒内完成扫码")
        time.sleep(15)
        browser.get("https://cart.taobao.com/cart.htm")
      time.sleep(3)
    
      now = datetime.datetime.now()
      print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))
    
    
    def buy(times, choose):
      is_buyed = False
      # 点击购物车里全选按钮
      if choose == 2:
        print("请手动勾选需要购买的商品")
      while True:
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        print('现在时间：', now)
        # 对比时间，时间到的话就点击结算
        if now > times:
          if choose == 1:
            while True:
              try:
                if browser.find_element_by_id("J_SelectAllcbx1"):
                  browser.find_element_by_id("J_SelectAllcbx1").click()
                  print('尝试全选')
                  break
              except:
                print("找不到全选按钮")
          # 点击结算按钮
          try:
            if browser.find_element_by_id("J_Go"):
              browser.find_element_by_id("J_Go").click()
              print("结算成功")
          except:
            pass
          while True:
            try:
              if browser.find_element_by_link_text('提交订单') and is_buyed == False:
                browser.find_element_by_link_text('提交订单').click()
                now1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
                print("抢购成功时间：%s" % now1)
            except:
              print("再次尝试提交订单")
          time.sleep(0.005)
    
    
    if __name__ == "__main__":
      times = input("请输入抢购时间，格式如(2018-09-06 11:20:00.000000):")
      # 时间格式："2018-09-06 11:20:00.000000"
      browser = webdriver.Chrome()
      browser.maximize_window()
      login()
      choose = input("到时间自动勾选购物车请输入“1”，否则输入“2”：")
      buy(times, choose)
```

最后run()一把就ok了！！

到此这篇关于python+selenium+chrome实现淘宝购物车秒杀自动结算的文章就介绍到这了,更多相关python+selenium+chrome
秒杀自动结算内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

