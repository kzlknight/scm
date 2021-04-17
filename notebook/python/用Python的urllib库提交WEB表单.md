_复制代码_ 代码如下:

  
class EntryDemo( Frame ):  
"""Demonstrate Entrys and Event binding"""  
  
chosenrange = 2  
url_login="http://.../ipgw/ipgw.ipgw/"  
uid = '' ＃用户名  
password = '' # 密码  
operation = '' # 操作  
range = '2' ＃ 范围  
the_page = '' ＃ WEB服务器返回页面  
＃ 表单的INPUT 值一定要记得填齐全  
def login(self):  
values = {  
'uid' : self.uid,  
'password' : self.password,  
'operation' : self.operation,  
'range' : self.range, # 1:国际 2:国内  
'timeout':'0'  
}  
postdata = urllib.urlencode(values) ＃ 表单值编码  
req = urllib2.Request(self.url_login, postdata) ＃ 服务器请求  
response = urllib2.urlopen(req)  
self.the_page = response.read()  

  
#print self.the_page

