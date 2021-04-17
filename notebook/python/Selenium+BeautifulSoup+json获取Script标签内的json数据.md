Selenium爬虫遇到 数据是以 JSON 字符串的形式包裹在 Script 标签中，  

假设Script标签下代码如下：

```python

    <script id="DATA_INFO" type="application/json" >
    {
      "user": {
        "isLogin": true,
        "userInfo": {
          "id": 123456,
          "nickname": "LiMing",
          "intro": "人生苦短，我用python"
        }
      }
    }
    </script>
    
```

此时drive.find_elements_by_xpath('//*[@id="DATA_INFO"]
只能定位到元素，但是无法通过.text方法，获取Script标签下的json数据

```python

    from bs4 import BeautifulSoup as bs
    import json as js
    #selenium获取当前页面源码
    html = drive.page_source
    #BeautifulSoup转换页面源码
    bs=BeautifulSoup(html,'lxml')
    #获取Script标签下的完整json数据，并通过json加载成字典格式
    js_test=js.loads(bs.find("script",{"id":"DATA_INFO"}).get_text())
    #获取Script标签下的nickname 值
    js_tes
```

到此这篇关于Selenium+BeautifulSoup+json获取Script标签内的json数据的文章就介绍到这了,更多相关Selenium+BeautifulSoup获取json内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

