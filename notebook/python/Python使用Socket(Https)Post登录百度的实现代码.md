登录百度，首先当然是先抓百度的登录包
，由于是网页登录，最方便的自然是httpwatch了，我使用的测试账号是itiandatest1，密码是itianda，抓包结果：  
  

_复制代码_ 代码如下:

  
POST /?login HTTP/1.1  
Accept: image/jpeg, application/x-ms-application, image/gif,
application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/vnd.ms-
excel, application/vnd.ms-powerpoint, application/msword, */*  
Referer: https://passport.baidu.com/?login&amp;tpl=mn  
Accept-Language: zh-CN  
User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/5.0;
SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media
Center PC 6.0; .NET4.0C; .NET4.0E; Alexa Toolbar; BOIE9;ZHCN)  
Content-Type: application/x-www-form-urlencoded  
Accept-Encoding: gzip, deflate  
Host: passport.baidu.com  
Content-Length: 243  
Connection: Keep-Alive  
Cache-Control: no-cache  

  
登录包抓到了，下面开始写代码：  
  

_复制代码_ 代码如下:

  
import socket  
import ssl  
sock = ssl.wrap_socket(socket.socket())  

  
ssl是专门用来处理https的模块，我们使用该模块的wrap_socket函数生成一个SSLSocket对象。  
  
然后建立连接：  

_复制代码_ 代码如下:

  
sock.connect(('passport.baidu.com', 443))  

  
这里需要注意的是https使用443端口，不是80。  
  
之后发送数据：  
  

_复制代码_ 代码如下:

  
data = '''\  
POST /?login HTTP/1.1  
Accept: image/jpeg, application/x-ms-application, image/gif,
application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/vnd.ms-
excel, application/vnd.ms-powerpoint, application/msword, */*  
Referer: https://passport.baidu.com/?login&amp;tpl=mn  
Accept-Language: zh-CN  
User-Agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/5.0;
SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media
Center PC 6.0; .NET4.0C; .NET4.0E; Alexa Toolbar; BOIE9;ZHCN)  
Content-Type: application/x-www-form-urlencoded  
Host: passport.baidu.com  
Content-Length: 243  
Connection: Keep-Alive  
Cache-Control: no-cache  
tpl_ok=&amp;next_target=&amp;tpl=mn&amp;skip_ok=&amp;aid=&amp;need_pay=&amp;need_coin=&amp;pay_method=&amp;u=http%3A%2F%2Fwww.baidu.com%2F&amp;return_method=get&amp;more_param=&amp;return_type=&amp;psp_tt=0&amp;password=itianda&amp;safeflg=0&amp;isphone=tpl&amp;username=itiandatest1&amp;verifycode=&amp;mem_pass=on\  
'''  
sock.sendall(data)  

  
需要注意的是sendall之后不能调用shutdown方法。  
  
其余部分就和普通的socket处理方式没什么差别了 ：  

_复制代码_ 代码如下:

  
recv_data = sock.recv(8192)  
sock.close()  
print recv_data  

  
由于我们只需要cookie信息，所以只接收少量数据就可以了。  
  
登录成功的标志是服务器返回含有BDUSS的set-cookie：  
  

_复制代码_ 代码如下:

  
HTTP/1.1 200 OK  
Set-Cookie: BAIDUID=DB464E1EBA6571FB82D70460D6AAB666:FG=1; max-age=946080000;
expires=Wed, 11-Dec-41 17:18:17 GMT; domain=.baidu.com; path=/; version=1  
P3P: CP=" OTI DSP COR IVA OUR IND COM "  
Date: Mon, 19 Dec 2011 17:18:17 GMT  
Server: Apache  
P3P: CP=" OTI DSP COR IVA OUR IND COM "  
P3P: CP=" OTI DSP COR IVA OUR IND COM "  
P3P: CP=" OTI DSP COR IVA OUR IND COM "  
Set-Cookie: BAIDUID=26FD0CB5389BF4699C447982D8080239:FG=1; expires=Wed,
11-Dec-41 17:18:17 GMT; max-age=946080000; path=/; domain=.baidu.com;
version=1  
Set-Cookie: BAIDUID=26FD0CB5389BF4698191E4134CACEA29:FG=1; expires=Wed,
11-Dec-41 17:18:17 GMT; max-age=946080000; path=/; domain=.baidu.com;
version=1  
Set-Cookie: BDUSS=dTajkzWTFWR3hXT3Jsc09LdkNsZ011YlZka340VWtqNkZzbW0tUTdOUFp-
aFpQQVFBQUFBJCQAAAAAAAAAAAouTSCLkioVaXRpYW5kYXRlc3QxAAAAAAAAAAAAAAAAAAAAAAAAAADgmoV5AAAAAOCahXkAAAAAuWZCAAAAAAAxMC42NS40NNlx707Zce9OWT;
expires=Tue, 01 Jan 2030 00:00:00 GMT; path=/; domain=.baidu.com  
Set-Cookie: PTOKEN=16ba4a120f070f3cc759a817981c2516; expires=Tue, 01 Jan 2030
00:00:00 GMT; path=/; domain=passport.baidu.com; HttpOnly  
Set-Cookie: STOKEN=fda94395cd4ae4661cefd3a4017a8454; expires=Tue, 01 Jan 2030
00:00:00 GMT; path=/; domain=passport.baidu.com  
Set-Cookie: USERID=626167789a799e630e60fb27466fa80e; expires=Tue, 01 Jan 2030
00:00:00 GMT; path=/; domain=.baidu.com  
Content-Type: text/html;charset=gbk  
Cache-Control: no-cache  
Pragma: no-cache  
Content-Encoding: none  
Content-Length: 850  
Connection: close  

  
OK，登陆成功。  
本文来自: itianda's blog

