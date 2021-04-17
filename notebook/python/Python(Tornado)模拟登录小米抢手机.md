今天看到同事参与小米的抢购，几经数个星期的尝试，终于抢到了一台小米电视……看了一下小米的抢购流程，似乎可以用程序可破。于是想写点东西玩玩（你懂的……），第一步肯定是先得模拟登录小米帐号，当练手吧。  
用 Python 来实现吧，由于是写一个Web应用，那么框架就选 Tornado。  
首先是定义应用的 URL：  

_复制代码_ 代码如下:

  
def main():  
tornado.options.parse_command_line()  
application = tornado.web.Application([  
(r"/", MainHandler),  
(r"/mibuy/", MiBuyHandler),  
],**settings)  
http_server = tornado.httpserver.HTTPServer(application)  
http_server.listen(options.port)  
tornado.ioloop.IOLoop.instance().start()  

  
接下来就是寻找需要 post 过去的数据，用 Fiddler 来嗅探一下：  
![](https://img.jbzj.com/file_images/article/201311/20131112090852.jpg?2013101291640)  
也就是说，POST 的地址是 [ https://account.xiaomi.com/pass/serviceLoginAuth2
](https://account.xiaomi.com/pass/serviceLoginAuth2)  
![](https://img.jbzj.com/file_images/article/201311/20131112090940.jpg?201310129177)  
需要构造的表单参数也很简单（已进行 URL
编码）：passToken=&user=www.nowamagic.net&pwd=password&callback=https%3A%2F%2Faccount.xiaomi.com&sid=passport&qs=%253Fsid%253Dpassport&hidden=&_sign=KKkRvCpZoDC%2BgLdeyOsdMhwV0Xg%3D。即：  

_复制代码_ 代码如下:

  
post_data = urllib.urlencode({'passToken':'', 'user': 'www.nowamagic.net',
'pwd': 'password', 'callback':'https://account.xiaomi.com', 'sid':'passport',
'qs':'%3Fsid%3Dpassport', 'hidden':'',
'_sign':'KKkRvCpZoDC+gLdeyOsdMhwV0Xg='})  
path = 'https://account.xiaomi.com/pass/serviceLoginAuth2'  

  
接下来函数也可以写出来了：  

_复制代码_ 代码如下:

  
class MiBuyHandler(tornado.web.RequestHandler):  
def get(self):  
cj = cookielib.CookieJar()  
post_data = urllib.urlencode({'passToken':'', 'user': 'www.nowamagic.net',
'pwd': 'password', 'callback':'https://account.xiaomi.com', 'sid':'passport',
'qs':'%3Fsid%3Dpassport', 'hidden':'',
'_sign':'KKkRvCpZoDC+gLdeyOsdMhwV0Xg='})  
path = 'https://account.xiaomi.com/pass/serviceLoginAuth2'  
cookieHandle = urllib2.HTTPCookieProcessor(cj)  
opener = urllib2.build_opener(cookieHandle)  
#opener.addheaders = [('User-agent', 'Opera/9.23')]  
urllib2.install_opener(opener)  
req = urllib2.Request(path, post_data)  
response = urllib2.urlopen(req)  
html = response.read()  
self.render("mibuy.html",message=html)  

  
如何需要把 cookie 打印出来，直接 print cj 就可以看到 cookie 的内容。  
接下来的事情貌似也很简单，就是解析 hdcontrol
（URL：http://tc.hd.xiaomi.com/hdget?callback=hdcontrol） 这个 json。  

_复制代码_ 代码如下:

  
hdcontrol(  
{  
stime: 1383645496,  
status: {  
allow: true,  
miphone: {  
hdurl: "",  
duration: null,  
hdstop: true,  
reg: true,  
pmstart: false,  
hdstart: false  
},  
mibox: {  
hdurl: "",  
duration: null,  
hdstop: true,  
reg: true,  
pmstart: false,  
hdstart: false  
},  
mitv: {  
hdurl: "",  
duration: null,  
hdstop: true,  
reg: false,  
pmstart: false,  
hdstart: false  
}  
}  
})  

  
当 allow 为 true 的时候，hdurl 会有值，比如
?_a=20131105_phone_a212a2b30e5&_op=choose&_s=72b686828&_m=1
之类的，这个就是真实的抢购地址，直接访问这个地址应该就不用再点排队的按钮。仅当抛砖引玉，懂程序的各位都该知道怎么办了吧……  
仅仅适用于目前（2013年11月），后续小米那边可能会改变一些规则。

