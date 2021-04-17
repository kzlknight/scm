在selenium中没有对应的方法,需要自己去写。

  * 元素存在，但不唯一，操作元素会报错 
  * 元素不存在，操作元素也会报错 

**第一种：捕获异常**  

弊端：只要页面上有元素，不几个，都返回True

```python

    from selenium import webdriver
    import unittest
    class Test1（unittest.TestCase）:
    # 一、准备浏览器驱动、网站地址
    # setUp在每个测试函数运行前运行，注意大小写；self不能省略
     def setUp(self):
     self.driver=webdriver.Chrome()
     self.baseurl="https://www.baidu.com"
     
    # 二、打开浏览器，发送请求
     函数名必须以test开头
     def test_01(self):
     browser=self.driver
     browser.get(self.baseurl)
    # 四、调用方法，判断元素是否存在
     flag=Test1.isElementExist（self，“input”）
     if flag：
      print（“该元素存在”）
     else：
      print（“该元素不存在”）
    # 三、判断元素是否存在的方法
     def isElementExist（self）：
     flag=True
     browser=self.driver
     try:
      browser.find_element_by_css_selector(element)
      return flag
     except:
      flag=False
      return flag
    # 五、运行所有以test开头的测试方法
    if __name__=="__main__":
     unittest.main()
```

**第二种：find_elements方法  
**

```python

    #除第三步，其他步骤同上
    def isElementExist(self):
     flag=True
     browser=self.driver
     ele=browser.find_elements_by_css_selector(element)
     if len(ele)==0:
     flag=False
     return flag
     if len(ele)==1:
     return flag
     else:
     flag=False
     return flag 
```

到此这篇关于selenium判断元素是否存在的两种方法小结的文章就介绍到这了,更多相关selenium判断元存在
内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

