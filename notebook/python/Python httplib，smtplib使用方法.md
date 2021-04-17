例一：使用httplib访问某个url然后获取返回的内容：  
  

![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) import
httplib  
![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif)  
![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) conn  =
httplib.HTTPConnection(  "  www.cnblogs.com  "  )  
![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) conn.request(
"  GET  "  ,  "  /coderzh/archive/2008/05/13/1194445.html  "  )  
![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) r  =
conn.getresponse()  
![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) print
r.read()  #  获取所有内容

  
例二：使用smtplib发送邮件  
  

![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) import
smtplib  
![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) smtpServer  =
'  smtp.xxx.com  '  
![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) fromaddr  =  '
foo@xxx.com  '  
![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) toaddrs  =  '
your@xxx.com  '  
![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) msg  =  '
Subject: xxxxxxxxx  '  
![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) server  =
smtplib.SMTP(smtpServer)  
![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif)
server.sendmail(fromaddr, toaddrs, msg)  
![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) server.quit( )

