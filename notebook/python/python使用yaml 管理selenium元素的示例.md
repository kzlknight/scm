> 作者：做梦的人（小姐姐）  
>  出处： [ https://www.cnblogs.com/chongyou/
> ](https://www.cnblogs.com/chongyou/)

**1.所有元素都在PageElement下的.yaml,如图**

![](https://img.jbzj.com/file_images/article/202012/2020121162719558.png?2020111162730)

login_page.yaml文件：

```python

    username:
      dec: 登录页
      type: xpath
      value: //input[@class='custom-text']
    password:
      dec: 密码输入框
      type: xpath
      value: //input[@class='custom-text password']
     
    loginbtn:
      dec: 登录按钮
      type: xpath
      value: //button[@type='submit']
```

解析yaml文本

```python

    def  parseyaml():
        #当前脚本路径的父类
        basepath=os.path.dirname(os.path.dirname(__file__))
        #yaml_path=basepath+"\\PageElement"
        yaml_path = basepath + "\\PageElement"
        pageElements = {}
        # 遍历读取yaml文件
     
        for fpath, dirname, fnames in os.walk(yaml_path):
     
            for name in fnames:
                # yaml文件绝对路径
                yaml_file_path = os.path.join(fpath, name)
                print(yaml_file_path)
                # 排除一些非.yaml的文件
                if ".yaml" in str(yaml_file_path):
                    with open(yaml_file_path, 'r', encoding='utf-8') as f:
                        page = yaml.load(f)
                        pageElements.update(page)
        #返回字典内容
        #for i in pageElements[pagename]['locators']:
        #   print(i)
        return pageElements
     
     
    if __name__ == "__main__":
        a = parseyaml()
        print(a)
        print("*******************")
        print(a["username"]["type"])
        print(a["username"]["value"])
```

解析结果

![](https://img.jbzj.com/file_images/article/202012/2020121162825546.png?2020111162832)

以上就是python使用yaml 管理selenium元素的示例的详细内容，更多关于python yaml
管理selenium元素的资料请关注脚本之家其它相关文章！

