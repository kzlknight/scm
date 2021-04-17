python爬虫写起来非常快，虽然也可以用java，但是没有python来的简洁迅速

selenium在前面总结过，是一个自动化测试库。headless
chrome是无界面的浏览器模式，和PHANTOMJS类似。但是PHANTOMJS往往会出现莫名的错误，而且速度没有headless chrome快

```python

    from selenium.webdriver.chrome.options import Options
     
    global DRIVER
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
      
    DRIVER = webdriver.Chrome(chrome_options=chrome_options)
    
```

爬虫的代码有一点需要注意，需要操作事件的时候最好不要直接用相应的方法，比如click。最好嵌入js脚本的方式进行调用。因为爬虫的代码执行速度很快，前端元素结构往往反应不过来，从而找出元素不可见或者不存在的错误。

```python

    province_items = DRIVER.find_element_by_class_name("city-province").find_elements_by_tag_name("a")
     
    #province_item.click()
    DRIVER.execute_script('arguments[0].click();',province_item)
```

下面来个例子，由于做电商平台，省、市、区的数据很好找，但是没有镇、街道的信息。这里通过爬虫从淘宝网将镇，街道的信息抓取下来

```python

    #! /usr/local/bin/python
    # encoding: utf-8
     
    '''
    Created on 2018年1月5日
     
    @author: wulinfeng
    @date: 2018-1-5
    '''
     
    import time
    #import request
    from selenium import webdriver
    #from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    from selenium.webdriver.chrome.options import Options
    import pymysql
     
    def init_db():
      global CONNECTION 
      CONNECTION = pymysql.connect("地址","用户名","密码","数据库" ,use_unicode=True, charset="utf8")
     
    def init_web_driver():
      global DRIVER
      #DRIVER = webdriver.PhantomJS(executable_path='C:\phantomjs-1.9.2-windows\phantomjs.exe')
      #DRIVER.set_window_size(1920, 1080)
      '''  
      dcap = dict(DesiredCapabilities.PHANTOMJS)
     
      dcap["phantomjs.page.settings.userAgent"] = (
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36"
      )
      
      dcap["phantomjs.page.settings.viewportSize"] = (
        "width: 1920, "
        "height: 1080"
      )
      
      DRIVER = webdriver.PhantomJS(executable_path='C:\phantomjs-1.9.2-windows\phantomjs.exe',desired_capabilities=dcap)
      DRIVER.set_window_size(1920, 1080)
      '''
      
      chrome_options = Options()
      chrome_options.add_argument('--headless')
      chrome_options.add_argument('--disable-gpu')
      
      DRIVER = webdriver.Chrome(chrome_options=chrome_options)
      
      #DRIVER=webdriver.Ie()
      #DRIVER=webdriver.Chrome()
     
    def close_db():
      CONNECTION.close()    
      
    def close_web_driver():
      DRIVER.quit() 
      
    def login_taobao(username, password):
      DRIVER.get("https://member1.taobao.com/member/fresh/deliver_address.htm?spm=a1z08.2.0.0.7dad47611Wnj46")
      #DRIVER.get("https://login.taobao.com/member/login.jhtml?spm=a21bo.2017.201864-2.d1.7d2082a4FxukGr&f=top&redirectURL=http%3A%2F%2Fwww.taobao.com%2F")
      #选择登陆方式
      DRIVER.find_element_by_xpath("//*[@id=\"J_Quick2Static\"]").click()
     
      #登陆
      input_user = DRIVER.find_element_by_xpath("//*[@id=\"TPL_username_1\"]")
      input_user.clear()
      input_user.send_keys(username)
      
      DRIVER.find_element_by_xpath("//*[@id=\"TPL_password_1\"]").send_keys(password)
      DRIVER.find_element_by_xpath("//*[@id=\"J_SubmitStatic\"]").click();
      
      time.sleep(0.5)
      
    def get_data():
      #点击地址选择
      #DRIVER.find_element_by_xpath("//*[@id=\"city-title\"]").click()
      city_title = DRIVER.find_element_by_id("city-title")
      DRIVER.execute_script('arguments[0].click();',city_title)
      
      get_province_and_sub()
      
    def get_province_and_sub():
      #获得省列表
      province_items = DRIVER.find_element_by_class_name("city-province").find_elements_by_tag_name("a")
      
      for province_item in province_items:
        pid = province_item.get_attribute("attr-id");
        pname = province_item.get_attribute("title");
        if pid == "-1":
          print("continue province")
          continue
        
        sql = "insert into region_province_t (province_id,province) values('"+pid+"','"+pname+"')"
        print(sql) 
        cursor = CONNECTION.cursor()
        cursor.execute(sql)
        CONNECTION.commit()
        
        #province_item.click()
        DRIVER.execute_script('arguments[0].click();',province_item)
        time.sleep(0.5)
        
        get_city_and_sub(pid)
        back_tab(0) 
      
    def get_city_and_sub(pid):
      #获得市列表
      city_items = DRIVER.find_element_by_class_name("city-city").find_elements_by_tag_name("a")
      for city_item in city_items:
        cid = city_item.get_attribute("attr-id");
        cname = city_item.get_attribute("title");
        if cid == "-1":
          print("continue city")
          continue
      
        sql = "insert into region_city_t (city_id,city,province_id) values('"+cid+"','"+cname+"','"+pid+"')"
        print(sql) 
        cursor = CONNECTION.cursor()
        cursor.execute(sql)
        CONNECTION.commit()
        
        #city_item.click()
        DRIVER.execute_script('arguments[0].click();',city_item)
        time.sleep(1)
        
        get_area_and_sub(cid)
        back_tab(1)
        
    def get_area_and_sub(cid):
      #获得县区列表
      area_items = DRIVER.find_element_by_class_name("city-district").find_elements_by_tag_name("a")
      for area_item in area_items:
        aid = area_item.get_attribute("attr-id");
        aname = area_item.get_attribute("title");
        if aid == "-1":
          print("continue area")
          continue
        
        sql = "insert into region_area_t (area_id,area,city_id) values('"+aid+"','"+aname+"','"+cid+"')"
        print(sql) 
        cursor = CONNECTION.cursor()
        cursor.execute(sql)
        CONNECTION.commit()
        
        #area_item.click()
        DRIVER.execute_script('arguments[0].click();',area_item)
        time.sleep(0.5)
        
        get_town_and_sub(aid)
        back_tab(2)
        
      
    def get_town_and_sub(aid):
      #获得镇列表
      town_items = DRIVER.find_element_by_class_name("city-street").find_elements_by_tag_name("a")
      for town_item in town_items:
        tid = town_item.get_attribute("attr-id");
        tname = town_item.get_attribute("title");
        if tid == "-1":
          print("continue town")
          continue
        
        sql = "insert into region_town_t (town_id,town,area_id) values('"+tid+"','"+tname+"','"+aid+"')"
        print(sql) 
        cursor = CONNECTION.cursor()
        cursor.execute(sql)
        CONNECTION.commit()
        
    def back_tab(index):
      districtEle = DRIVER.find_element_by_class_name("city-select-tab").find_elements_by_tag_name("a")[index]
      DRIVER.execute_script('arguments[0].click();',districtEle)
      time.sleep(0.5)
      
    init_db()
    init_web_driver()
    login_taobao("用户名", "密码")
    get_data()
    close_db()
    close_web_driver()
    
```

到此这篇关于selenium+headless chrome爬虫的实现示例的文章就介绍到这了,更多相关selenium+headless
chrome爬虫内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

