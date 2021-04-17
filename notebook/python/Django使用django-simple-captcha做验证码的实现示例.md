安装django-simple-captcha

```python

    pip install django-simple-captcha
```

将captcha 安装在installed_apps里面

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010714221831.png)

将captcha配置url

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010714221932.png)

迁移同步，生成captcha所依赖的表

```python

    python manage.py makemigrations
    python manage.py migrate
```

将captcha字段在form类当中进行设置, 但是要导入from captcha.fields import CaptchaField

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010714221933.png)

在后台逻辑当中，get请求里面实例化我们的form,将form对象返回到页面  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010714221934.png)

在页面上通过{  { form.captcha}} 获取验证码  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010714221935.png)

效果图  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010714222036.png)  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010714222037.png)  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010714222038.png)  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010714222039.png)  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010714222040.png)  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010714222141.png)

注册成功

到此这篇关于Django使用django-simple-captcha做验证码的文章就介绍到这了,更多相关Django
验证码内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

