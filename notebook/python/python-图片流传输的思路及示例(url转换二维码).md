##  1.场景  

  * 将URL动态生成二维码前端展示(微信支付等，)--》   

1.静态文件路径访问  
返回URL_name,（a标签，src 静态路由访问）

2.流传输，前端渲染  
二进制流返回前端，前端根据二进制流编码类型显示

3.前端js生成  
后台获取到微信支付的code_url,前端js将code_url生成二维码，并渲染

  * 实际代码   

使用python_web 框架--》tornado  
manager.py

```python

    import os
    import asyncio
    
    import tornado.ioloop
    import tornado.httpserver
    import tornado.web
    import tornado.options
    
    from tornado.options import define, options, parse_command_line
    from apps import UrlHandler, Url2Handler, Url3Handler
    
    
    define("port", default=8000, type=int)
    
    
    def create_app():
      settings = {
        "template_path": os.path.join(os.path.dirname(__file__), "templates"),
        "static_path": os.path.join(os.path.dirname(__file__), "static"),
      }
      application = tornado.web.Application(
        handlers=[
          (r"/url", UrlHandler),
          (r"/url2", Url2Handler),
          (r"/url3", Url3Handler),
        ],
        debug=True,
        **settings,
      )
      return application
    
    
    if __name__ == '__main__':
      parse_command_line()
      app = create_app()
      server = tornado.httpserver.HTTPServer(app)
      server.listen(options.port)
      asyncio.get_event_loop().run_forever()
```

apps.py

```python

    import tornado.web
    from manager_handler import gen_qrcode, gen_qrcode_obj,gen_qrcode_buf
    
    
    class BaseHandler(tornado.web.RequestHandler):
      pass
    
    
    class UrlHandler(BaseHandler):
      def get(self):
        # 获取链接
        self.render('qrcode.html', title='url', data='URL-提交', img_stream='')
    
      async def post(self):
        # 生成二维码
        url = self.get_argument('url_str')
    
        # URL转换二维码
        img_stream = gen_qrcode(url)
        await self.render('qrcode.html', title='qrcode', data='扫码支付', img_stream=img_stream)
    
    
    class Url2Handler(BaseHandler):
      def get(self):
        # 获取链接
        self.render('qrcode.html', title='url', data='URL-提交', img_stream='')
    
      async def post(self):
        # 生成二维码
        url = self.get_argument('url_str')
    
        # URL转换二维码
        img_stream = gen_qrcode_obj(url=url)
        # await self.render('qrcode.html', title='qrcode', data='扫码支付', img_stream=img_stream)
        self.set_header('Content_Type', 'image/jpg')
        self.set_header('Content_length', len(img_stream))
        self.write(img_stream)
    
    
    class Url3Handler(BaseHandelr):
      def get(self):
        self.render('qrcode.html', title='url', data='URL-提交', img_stream='')
    
      def post(self):
        url = self.get_argument('url')
        img_stream = gen_qrcode_buf(url)
        self.set_header('Content-Type', 'image/png')
        self.write(img_stream)
```

manager_handler.py

```python

    import qrcode
    import io
    import base64
    import time
    
    
    def gen_qrcode(url):
      """
      方式1： URL转换二维码
      :param url: 转换二维码的URL
      :return: base64编码后的 二进制流 二维码数据
      """
      qr = qrcode.make(url)
      buf = io.BytesIO()
      qr.save(buf)
      img_buf = buf.getvalue()
      img_stream = base64.b64encode(img_buf)
      return img_stream
    
    
    def gen_qrcode_obj(version=1, box_size=10, border=4, url=None):
      """
      方式2： URL转换二维码（图片流传输， template需要指明 data:base64编码）
      :param version:
      :param box_size:
      :param border:
      :return:
      """
      qr = qrcode.QRCode(
        version=version,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
      )
    
      url = "https://www.12dms.com" if url is None else url
      save_name = "./" + "qrcode" + str(time.time()) + ".png"
    
      qr.add_data(url)
      qr.make()
      img = qr.make_image()
      img.save(save_name.encode())
      with open(save_name, 'rb') as img_f:
        img_stream = img_f.read()
        img_stream = base64.b64encode(img_stream)
        print(img_stream)
      return img_stream
    
    def gen_qrcode_buf(words):
      qr = qrcode.make(words)
      buf = io.BytesIO()
      qr.save(buf, 'png')
      qr_buf = buf.getvalue()
      # img_stream = base64.b64encode(qr_buf)
      return qr_buf
```

base.html

```python

    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>{% block title %}{% end %}</title>
      {% block head %}{% end %}
    </head>
    
    <body>
      <h1 style="text-align: center">
        {% block h1 %}{{ data }}{% end %}
      </h1>
      {% block content %}{% end %}
    </body>
    </html>
```

qrcode.html

```python

    {% extends "base.html" %}
    
    {% block title %}
      {{ title }}
    {% end %}
    
    {% block h1 %}
      {{ data }}
    {% end %}
    
    
    {% block content %}
      <form method="post" action="" >
        <p>
          输入待转换的URL：<input name="url_str"/>
          <br>
    {#      {{ img_stream }}#}
          {% if img_stream %}
            <img style="width:180px" src="data:;base64,{{ img_stream }}" alt="">
          {% end %}
        </p>
        <br>
        <input id="submit" type="submit" value="生成二维码">
      </form>
    {% end %}
```

以上就是python-图片流传输的思路及示例(url转换二维码)的详细内容，更多关于python 图片流传输的资料请关注脚本之家其它相关文章！

