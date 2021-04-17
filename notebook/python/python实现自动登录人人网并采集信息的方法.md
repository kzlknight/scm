本文实例讲述了python实现自动登录人人网并采集信息的方法。分享给大家供大家参考。具体实现方法如下：

```python

    #!/usr/bin/python
    # -*- coding: utf-8 -*-
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
          self.cj.revert('./renren.coockie') 
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
        params = {
          'domain':self.domain,
          'origURL':self.origURL,
          'email':self.name, 
          'password':self.pwd}
        print 'login.......'
        req = urllib2.Request( 
          'http://www.renren.com/PLogin.do',
          urllib.urlencode(params)
        )
        self.file=urllib2.urlopen(req).read()    
        newsfeed = open('news.html','w')
        try:
          newsfeed.write(self.file)
        except Exception, e:
          newsfeed.close()
        self.operate = self.opener.open(req) 
        print type(self.operate)
        print self.operate.geturl()
        if self.operate.geturl(): 
          print 'Logged on successfully!'
          self.cj.save('./renren.coockie')
          self.__viewnewinfo()
        else:
          print 'Logged on error'
      def __viewnewinfo(self):
        '''查看好友的更新状态'''
        self.__caiinfo()
      def __caiinfo(self):
        '''采集信息'''    
        h3patten = re.compile('<article>(.*?)</article>')#匹配范围
        apatten = re.compile('<h3.+>(.+)</h3>:')#匹配作者
        cpatten = re.compile('</a>(.+)\s')#匹配内容 
        content = h3patten.findall(self.file)
        print len(content)  
        infocontent = self.operate.readlines()
        print type(infocontent)
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
    username = 'username'#你的人人网的帐号
    password = 'password'#你的人人网的密码
    domain = 'www.renren.com'#人人网的地址
    origURL = 'http://www.renren.com/home'#人人网登录以后的地址
    ren.setinfo(username,password,domain,origURL)
    ren.login()
    
    
```

希望本文所述对大家的Python序设计有所帮助。

