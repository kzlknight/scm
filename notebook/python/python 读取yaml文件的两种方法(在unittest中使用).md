> 作者：做梦的人（小姐姐）  
>  出处： [ https://www.cnblogs.com/chongyou/
> ](https://www.cnblogs.com/chongyou/)

python读取yaml文件使用，有两种方式：

1.使用ddt读取

2,使用方法读取ddt的内容，在使用方法中进行调用

**1.使用ddt读取**

```python

    @ddt.ddt
    class loginTestPage(unittest.TestCase):
        @ddt.file_data(path)
        @ddt.unpack
        def testlogin(self,**kwargs):
            u'''
           "输入邮件账号、用户名、密码符合要求
           勾选同意协议"  1、注册成功，跳转到注册成功页面    "
            1、验证URL，https://www.XX.com/site/register-success.html
            2、邮箱收到注册成功邮件
            3、数据库中user表中有成功添加注册账号数据"
     
            :return:
            '''
     
            self.loginPage = CBLogin(self.driver)
            log.info(kwargs)
            self.page = Page(self.driver,kwargs.get('login_url'))
     
            self.page.send_text(self.loginPage.login_sendkes_username(),kwargs.get('username'))
            self.page.send_text(self.loginPage.login_sendkes_password(),kwargs.get('password'))
            self.page.click(self.loginPage.login_click_btn())
            # 断言登录是否成功
            self.assertIsNotNone(self.loginPage.is_success(),"元素没有查找到，登录失败")
```

**2.使用已有的方法进行调用**

```python

    class HandleYmal:
        """
        获取测试环境的配置
        """
        def __init__(self,file_path=None):
            if file_path:
                self.file_path=file_path
            else:
                #获取path
                root_dir=os.path.dirname(os.path.abspath('.'))
                print(root_dir)
                self.file_path=root_dir+"/config/base.yaml"
        def get_data(self):
            fp=open(self.file_path,encoding="utf-8")
            data=yaml.load(fp)
            return  data
     
     
     
    @ddt.ddt
    class loginTestPage(unittest.TestCase):
     
        @classmethod
        def setUpClass(cls):
            """前置应该是读取所有内容"""
     
            yaml=HandleYmal()
            cls.kwargs=yaml.get_data()['testenvironment']
            cls.driver = webdriver.Chrome()
     
        def testlogin(self):
            u'''
           "输入邮件账号、用户名、密码符合要求
           勾选同意协议"  1、注册成功，跳转到注册成功页面    "
            1、验证URL，https://www.chinabrands.com/site/register-success.html
            2、邮箱收到注册成功邮件
            3、数据库中user表中有成功添加注册账号数据"
     
            :return:
            '''
     
            self.loginPage = CBLogin(self.driver)
            log.info(self.kwargs)
            self.page = Page(self.driver,self.kwargs.get('login_url'))
            self.page.send_text(self.loginPage.login_sendkes_username(),self.kwargs.get('username'))
            self.page.send_text(self.loginPage.login_sendkes_password(),self.kwargs.get('password'))
            self.page.click(self.loginPage.login_click_btn())
            # 断言登录是否成功
            self.assertIsNotNone(self.loginPage.is_success(),"元素没有查找到，登录失败")
```

以上就是python 读取yaml文件的两种方法(在unittest中使用)的详细内容，更多关于python
读取yaml文件的资料请关注脚本之家其它相关文章！

