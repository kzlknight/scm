django-simple-
captcha是django的验证码包，非常简单实用，这次记录的是如何点击验证码后刷新验证码，因为这个功能官方文档并没有详细给出。

django-simple-captcha官方文档： [ http://django-simple-
captcha.readthedocs.io/en/latest/ ](http://django-simple-
captcha.readthedocs.io/en/latest/)

django-simple-captcha的github网址： [ https://github.com/mbi/django-simple-captcha
](https://github.com/mbi/django-simple-captcha)

开始  

1.安装 pip install django-simple-captcha， pip install Pillow

2.将captcha 加入 settings.py 的 INSTALLED_APPS

3.运行 python manage.py makemigrations 和 python manage.py migrate

4.url路由加入urls.py的urlpatterns

```python

    urlpatterns = [
      path('captcha/', include('captcha.urls')),    # 图片验证码 路由
      path('refresh_captcha/', views.refresh_captcha),  # 刷新验证码，ajax
      path('test/',IndexView.as_view()),         #get与post请求路径
    ]
```

5.在views.py中加入以下代码

```python

    from django.shortcuts import render
    from django.views.generic import View
    from captcha.models import CaptchaStore
    from captcha.helpers import captcha_image_url
    from django.http import HttpResponse
    import json
    
    
    # 创建验证码
    def captcha():
      hashkey = CaptchaStore.generate_key() # 验证码答案
      image_url = captcha_image_url(hashkey) # 验证码地址
      captcha = {'hashkey': hashkey, 'image_url': image_url}
      return captcha
    
    #刷新验证码
    def refresh_captcha(request):
      return HttpResponse(json.dumps(captcha()), content_type='application/json')
    
    # 验证验证码
    def jarge_captcha(captchaStr, captchaHashkey):
      if captchaStr and captchaHashkey:
        try:
          # 获取根据hashkey获取数据库中的response值
          get_captcha = CaptchaStore.objects.get(hashkey=captchaHashkey)
          if get_captcha.response == captchaStr.lower(): # 如果验证码匹配
            return True
        except:
          return False
      else:
        return False
    
    
    class IndexView(View):
      def get(self, request):
        hashkey = CaptchaStore.generate_key() # 验证码答案
        image_url = captcha_image_url(hashkey) # 验证码地址
        print(hashkey,image_url)
        captcha = {'hashkey': hashkey, 'image_url': image_url}
        return render(request, "login.html", locals())
    
      def post(self, request):
        capt = request.POST.get("captcha", None) # 用户提交的验证码
        key = request.POST.get("hashkey", None) # 验证码答案
        if jarge_captcha(capt, key):
          return HttpResponse("验证码正确")
        else:
          return HttpResponse("验证码错误")
```

6.templates文件夹下login.html的内容

```python

    {% load static %}
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Title</title>
      <script src="https://cdn.bootcdn.net/ajax/libs/jquery/3.5.1/jquery.js"></script>
      <script src="https://cdn.bootcdn.net/ajax/libs/twitter-bootstrap/4.0.0/js/bootstrap.js"></script>
    </head>
    <body>
      <form action="/test/" method="post">
        {% csrf_token %}
        <a href="#" rel="external nofollow" class="captcha">
          <img src="{{ captcha.image_url }}" alt="点击切换" id="id_captcha" >
        </a> <br>
        <input type="text" name="captcha" placeholder="验证码"> <br>
        <input value="{{ captcha.hashkey }}" name="hashkey" type="hidden" id="id_captcha_0">
        <button type="submit" class="btn btn-primary btn-block ">提交</button>
      </form>
    <script>
        <!-- 动态刷新验证码js -->
        $(document).ready(function(){
          $('.captcha').click(function () {
            $.getJSON("/refresh_captcha/", function (result) {
              $('#id_captcha').attr('src', result['image_url']);
              $('#id_captcha_0').val(result['hashkey'])
            });
          });
        });
    </script>
    </body>
    </html>
```

django-simple-captcha并没有使用session对验证码进行存储，而是使用了数据库，当你在做数据库迁移的时候会生成一个表
captcha_captchastore ，包含以下字段

> challenge = models.CharField(blank=False, max_length=32) # 验证码大写或者数学计算比如 1+1  
>  response = models.CharField(blank=False, max_length=32) # 需要输入的验证码
> 验证码小写或数学计算的结果 比如 2  
>  hashkey = models.CharField(blank=False, max_length=40, unique=True) # hash值  
>  expiration = models.DateTimeField(blank=False) # 到期时间  
>

以上就是本文的全部内容，希望对大家的学习有所帮助，也希望大家多多支持脚本之家。

