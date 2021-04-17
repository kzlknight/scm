新版本的selenium已经明确警告将不支持PhantomJS，建议使用headless的Chrome或FireFox。

两者使用方式非常类似，基本步骤为：

  * 下载驱动 
  * 创建选项，设定headless 
  * 创建WebDriver，指定驱动位置和选项 
  * 对URL发起请求，获得结果，进行解析 

###  Chrome

驱动的下载路径为： [ https://chromedriver.storage.googleapis.com/index.html
](https://chromedriver.storage.googleapis.com/index.html)

接下来创建选项并设定headless：

```python

    options = webdriver.ChromeOptions()
    options.set_headless()
    
```

创建WebDriver，指定驱动位置和选项：

```python

    driver = webdriver.Chrome(
      'D://chromedriver_win32//chromedriver', chrome_options=options)
    
```

发起请求，获得结果并进行解析：

```python

    driver.get('http://www.sohu.com/')
    time.sleep(3)
    print(driver.page_source)
    driver.close()
```

###  Firefox

驱动的下载路径为： [ https://github.com/mozilla/geckodriver
](https://github.com/mozilla/geckodriver)

启动的步骤与Chrome一致，只不过使用的选项对象和创建的WebDriver对象略有不同。直接上源代码：

```python

    options = webdriver.FirefoxOptions()
    options.set_headless()
    driver = webdriver.Firefox(
      firefox_options=options,
      executable_path='D:/geckodriver-win64/geckodriver')
    driver.get('http://www.sohu.com/')
    time.sleep(3)
    print(driver.page_source)
    driver.close()
    
```

###  SELENIUM使用HEADLESS无头模式实现无界面运行

先导包：

```python

    from selenium.webdriver.chrome.options import Options
```

加入如下配置：

```python

    chrome_options = Options()
    
    chrome_options.add_argument('--window-size=1920,1080')   # 设置窗口界面大小
    
    chrome_options.add_argument('--headless')
    
    driver = webdriver.Chrome(chrome_options=chrome_options)
    
    
```

参考代码：

```python

    from selenium import webdriver
    import time
    import multiprocessing
    from selenium.webdriver.chrome.options import Options
    
    
    
    class Zutuan():
      def __init__(self):
        """打开浏览器"""
        self.chrome_options = Options()
        self.chrome_options.add_argument('--window-size=1920,1080')
        self.chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options)
    
      def open_zutuan(self, url):
        """传入组团url"""
        self.driver.get(url)
        #self.driver.maximize_window()
        self.driver.refresh()
        #time.sleep(0.01)
        self.driver.implicitly_wait(30)    # todo implicitly隐式等待，等待元素可见
    
      def option_element(self, user, password):
        """xpath定位元素"""
        self.driver.find_element_by_xpath('//div[@class="login a"]/i').click()
        time.sleep(0.01)
        self.driver.find_element_by_xpath('//div[@class="a-title"]').click()
        self.driver.find_element_by_xpath('//input[@type="text" or @class="userName"]').send_keys(user)
        self.driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
        self.driver.find_element_by_xpath('//div[@class="button"]').click()
        time.sleep(1)
        self.driver.refresh()
    
    
      def select_commodity(self, content):
        """搜索组团商品"""
        # TODO self.content实例属性传给下面的方法使用,如果想把值给下面的方法用，添加实例属性解决
        self.content = content
        self.driver.find_element_by_xpath('//input[@type="text"]').send_keys(content)
        self.driver.find_element_by_xpath('//div[@class="search"]').click()
        self.driver.refresh()
        #return content
    
      def result(self):
        """判断搜索商品成功后的提示信息，断言页面是否成功"""
        if self.content in self.driver.page_source:
          #print(self.content)
          print('商品搜索成功，测试通过')
        else:
          print('商品搜索错误，测试失败')
    
      def closed(self):
        """关闭浏览器"""
        time.sleep(1)
        self.driver.quit()
    
    
    def run1():
      # TODO 根据操作顺序，调用方法执行
      zt = Zutuan()
      zt.open_zutuan('http://www.zutuan.cn/index.html#/')
      zt.option_element('1489088761@qq.com', 'mg123456')
      zt.select_commodity('香蕉')
      zt.result()
      zt.closed()
    
    
    class View_details(Zutuan):
      """把商品添加为明星单品，"""
      def check_commodity(self, number):
        """进入商品详情页，点击添加明星单品"""
        self.driver.find_element_by_xpath('//a[@target="_blank"]/img').click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element_by_xpath('//div[@class="child start"]').click()
        self.driver.find_element_by_xpath('//div[@class="el-dialog__body"]//input[@type="text"]').send_keys(number)
        self.driver.find_element_by_xpath('//button[@type="button" and @class="el-button el-button--danger"]').click()
        time.sleep(1)
    
      def result(self):
        """重写父类方法，判断商品添加成功后的提示信息，断言页面是否成功"""
        if '添加成功' in self.driver.page_source:
          print('商品添加成功，测试通过')
        else:
          print('商品添加失败，测试失败')
        # 调用父类方法关闭
        super().closed()
    
    
    def run2():
      vd = View_details()
      vd.open_zutuan('http://www.zutuan.cn/index.html#/')
      vd.option_element('1489088761@qq.com', 'mg123456')
      vd.select_commodity('苹果')
      vd.check_commodity(91628)
      vd.result()
    
    
    def main():
      p1 = multiprocessing.Process(target=run1)
      p2 = multiprocessing.Process(target=run2)
    
      p1.start()
      p2.start()
    
    
    if __name__ == '__main__':
      main()
    
```

到此这篇关于selenium设置浏览器为headless无头模式(Chrome和Firefox)的文章就介绍到这了,更多相关selenium
浏览器为headless无头模式内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

