先上脚本吧，等下来讲下知识点:  

_复制代码_ 代码如下:

  
#!/usr/bin/env python  
#encoding=utf-8  
import sys  
import re  
import urllib2  
import urllib  
import cookielib  
  
class Renren(object):  
  
def __init__(self):  
self.name = self.pwd = self.content = self.domain = self.origURL = ''  
self.operate = ''#登录进去的操作对象  
self.cj = cookielib.LWPCookieJar()  
try:  
self.cj.revert('renren.coockie')  
except Exception,e:  
print e  
  
self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))  
urllib2.install_opener(self.opener)  
  
  
def setinfo(self,username,password,domain,origURL):  
'''设置用户登录信息'''  
self.name = username  
self.pwd = password  
self.domain = domain  
self.origURL = origURL  
  
def login(self):  
'''登录人人网'''  
params = {'domain':self.domain,'origURL':self.origURL,'email':self.name,
'password':self.pwd}  
print 'login.......'  
req = urllib2.Request(  
'http://www.renren.com/PLogin.do',  
urllib.urlencode(params)  
)  
  
self.operate = self.opener.open(req)  
  
if self.operate.geturl() == 'http://www.renren.com/Home.do':  
print 'Logged on successfully!'  
self.cj.save('renren.coockie')  
self.__viewnewinfo()  
else:  
print 'Logged on error'  
  
def __viewnewinfo(self):  
'''查看好友的更新状态'''  
self.__caiinfo()  
  
  
def __caiinfo(self):  
'''采集信息'''  
  
h3patten = re.compile('<h3>(.*?)</h3>')#匹配范围  
apatten = re.compile('<a.+>(.+)</a>:')#匹配作者  
cpatten = re.compile('</a>(.+)\s')#匹配内容  
infocontent = self.operate.readlines()  
# print infocontent  
print 'friend newinfo:'  
for i in infocontent:  
content = h3patten.findall(i)  
if len(content) != 0:  
for m in content:  
username = apatten.findall(m)  
info = cpatten.findall(m)  
if len(username) !=0:  
print username[0],'说:',info[0]  
print '----------------------------------------------'  
else:  
continue  
  
ren = Renren()  
username = ''#你的人人网的帐号  
password = ''#你的人人网的密码  
domain = 'renren.com'#人人网的地址  
origURL = 'http://www.renren.com/Home.do'#人人网登录以后的地址  
ren.setinfo(username,password,domain,origURL)  
ren.login()  

  
主要用到了python cookielib,urllib2,urllib这3个模块，这3个模块是python做http这方面比较好的模块.  
  
  
self.cj = cookielib.LWPCookieJar()  
  
try:  
self.cj.revert('renren.coockie')  
except Exception,e:  
print e  
self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))  
  
urllib2.install_opener(self.opener)  
这几行是在本地建立人人网的cookies，因为人人网要验证cookies才能登录，你运行这个脚本的话，会发现在当前目录
有个程序会自动建立一个renren.cookie这个文件。  
  
我这里renren.cookie的信息是: #LWP-Cookies-2.0 Set-Cookie3:
WebOnLineNotice_244225225=1; path="/"; domain=".renren.com"; path_spec;
domain_dot; expires="2010-04-11 06:59:33Z"; version=0
总结一下如果网站登录要用cookie的话，就要用到cookielib这个模块，不然你用程序登录不了网站,过断时间在写个urlib的例子，大家可以先用上面这个脚本玩玩!体会下python
人人网代码的乐趣!

