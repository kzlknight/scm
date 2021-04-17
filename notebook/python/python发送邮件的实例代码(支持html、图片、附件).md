第一段代码：  
  

_复制代码_ 代码如下:

  
#!/usr/bin/python  
# -*- coding: utf-8 -*-

import email  
import mimetypes  
from email.MIMEMultipart import MIMEMultipart  
from email.MIMEText import MIMEText  
from email.MIMEImage import MIMEImage  
import smtplib

def sendEmail(authInfo, fromAdd, toAdd, subject, plainText, htmlText):

strFrom = fromAdd  
strTo = ', '.join(toAdd)

server = authInfo.get('server')  
user = authInfo.get('user')  
passwd = authInfo.get('password')

if not (server and user and passwd) :  
print 'incomplete login info, exit now'  
return

# 设定root信息  
msgRoot = MIMEMultipart('related')  
msgRoot['Subject'] = subject  
msgRoot['From'] = strFrom  
msgRoot['To'] = strTo  
msgRoot.preamble = 'This is a multi-part message in MIME format.'

# Encapsulate the plain and HTML versions of the message body in an  
# 'alternative' part, so message agents can decide which they want to display.  
msgAlternative = MIMEMultipart('alternative')  
msgRoot.attach(msgAlternative)

#设定纯文本信息  
msgText = MIMEText(plainText, 'plain', 'utf-8')  
msgAlternative.attach(msgText)

#设定HTML信息  
msgText = MIMEText(htmlText, 'html', 'utf-8')  
msgAlternative.attach(msgText)

#设定内置图片信息  
fp = open('test.jpg', 'rb')  
msgImage = MIMEImage(fp.read())  
fp.close()  
msgImage.add_header('Content-ID', '<image1>')  
msgRoot.attach(msgImage)

#发送邮件  
smtp = smtplib.SMTP()  
#设定调试级别，依情况而定  
smtp.set_debuglevel(1)  
smtp.connect(server)  
smtp.login(user, passwd)  
smtp.sendmail(strFrom, strTo, msgRoot.as_string())  
smtp.quit()  
return

if __name__ == '__main__' :  
authInfo = {}  
authInfo['server'] = 'smtp.somehost.com'  
authInfo['user'] = 'username'  
authInfo['password'] = 'password'  
fromAdd = 'username@somehost.com'  
toAdd = ['someone@somehost.com', 'other@somehost.com']  
subject = '邮件主题'  
plainText = '这里是普通文本'  
htmlText = '<B>HTML文本</B>'  
sendEmail(authInfo, fromAdd, toAdd, subject, plainText, htmlText)  

  
  
文件形式的邮件

_复制代码_ 代码如下:

  
#!/usr/bin/env python3  
#coding: utf-8  
import smtplib  
from email.mime.text import MIMEText  
from email.header import Header  
  
sender = '***'  
receiver = '***'  
subject = 'python email test'  
smtpserver = 'smtp.163.com'  
username = '***'  
password = '***'  
  
msg = MIMEText('你好','text','utf-8')#中文需参数‘utf-8'，单字节字符不需要  
msg['Subject'] = Header(subject, 'utf-8')  
  
smtp = smtplib.SMTP()  
smtp.connect('smtp.163.com')  
smtp.login(username, password)  
smtp.sendmail(sender, receiver, msg.as_string())  
smtp.quit()  

HTML形式的邮件

_复制代码_ 代码如下:

  
#!/usr/bin/env python3  
#coding: utf-8  
import smtplib  
from email.mime.text import MIMEText

sender = '***'  
receiver = '***'  
subject = 'python email test'  
smtpserver = 'smtp.163.com'  
username = '***'  
password = '***'

msg = MIMEText('<html><h1>你好</h1></html>','html','utf-8')

msg['Subject'] = subject

smtp = smtplib.SMTP()  
smtp.connect('smtp.163.com')  
smtp.login(username, password)  
smtp.sendmail(sender, receiver, msg.as_string())  
smtp.quit()  

带图片的HTML邮件

_复制代码_ 代码如下:

  
#!/usr/bin/env python3  
#coding: utf-8  
import smtplib  
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  
from email.mime.image import MIMEImage

sender = '***'  
receiver = '***'  
subject = 'python email test'  
smtpserver = 'smtp.163.com'  
username = '***'  
password = '***'

msgRoot = MIMEMultipart('related')  
msgRoot['Subject'] = 'test message'

msgText = MIMEText('<b>Some <i>HTML</i> text</b> and an image.<br><img
src="cid:image1"><br>good!','html','utf-8')  
msgRoot.attach(msgText)

fp = open('h:\\python\\1.jpg', 'rb')  
msgImage = MIMEImage(fp.read())  
fp.close()

msgImage.add_header('Content-ID', '<image1>')  
msgRoot.attach(msgImage)

smtp = smtplib.SMTP()  
smtp.connect('smtp.163.com')  
smtp.login(username, password)  
smtp.sendmail(sender, receiver, msgRoot.as_string())  
smtp.quit()  

带附件的邮件

_复制代码_ 代码如下:

  
#!/usr/bin/env python3  
#coding: utf-8  
import smtplib  
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  
from email.mime.image import MIMEImage

sender = '***'  
receiver = '***'  
subject = 'python email test'  
smtpserver = 'smtp.163.com'  
username = '***'  
password = '***'

msgRoot = MIMEMultipart('related')  
msgRoot['Subject'] = 'test message'

#构造附件  
att = MIMEText(open('h:\\python\\1.jpg', 'rb').read(), 'base64', 'utf-8')  
att["Content-Type"] = 'application/octet-stream'  
att["Content-Disposition"] = 'attachment; filename="1.jpg"'  
msgRoot.attach(att)  
  
smtp = smtplib.SMTP()  
smtp.connect('smtp.163.com')  
smtp.login(username, password)  
smtp.sendmail(sender, receiver, msgRoot.as_string())  
smtp.quit()  

群邮件

_复制代码_ 代码如下:

  
#!/usr/bin/env python3  
#coding: utf-8  
import smtplib  
from email.mime.text import MIMEText

sender = '***'  
receiver = ['***','****',……]  
subject = 'python email test'  
smtpserver = 'smtp.163.com'  
username = '***'  
password = '***'

msg = MIMEText('你好','plain','utf-8')

msg['Subject'] = subject

smtp = smtplib.SMTP()  
smtp.connect('smtp.163.com')  
smtp.login(username, password)  
smtp.sendmail(sender, receiver, msg.as_string())  
smtp.quit()  

各种元素都包含的邮件

_复制代码_ 代码如下:

  
#!/usr/bin/env python3  
#coding: utf-8  
import smtplib  
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  
from email.mime.image import MIMEImage

sender = '***'  
receiver = '***'  
subject = 'python email test'  
smtpserver = 'smtp.163.com'  
username = '***'  
password = '***'

# Create message container - the correct MIME type is multipart/alternative.  
msg = MIMEMultipart('alternative')  
msg['Subject'] = "Link"

# Create the body of the message (a plain-text and an HTML version).  
text = "Hi!\nHow are you?\nHere is the link you
wanted:\nhttp://www.python.org"  
html = """\  
<html>  
<head></head>  
<body>  
<p>Hi!<br>  
How are you?<br>  
Here is the <a href="http://www.python.org">link</a> you wanted.  
</p>  
</body>  
</html>  
"""

# Record the MIME types of both parts - text/plain and text/html.  
part1 = MIMEText(text, 'plain')  
part2 = MIMEText(html, 'html')

# Attach parts into message container.  
# According to RFC 2046, the last part of a multipart message, in this case  
# the HTML message, is best and preferred.  
msg.attach(part1)  
msg.attach(part2)  
#构造附件  
att = MIMEText(open('h:\\python\\1.jpg', 'rb').read(), 'base64', 'utf-8')  
att["Content-Type"] = 'application/octet-stream'  
att["Content-Disposition"] = 'attachment; filename="1.jpg"'  
msg.attach(att)  
  
smtp = smtplib.SMTP()  
smtp.connect('smtp.163.com')  
smtp.login(username, password)  
smtp.sendmail(sender, receiver, msg.as_string())  
smtp.quit()  

基于SSL的邮件

_复制代码_ 代码如下:

  
#!/usr/bin/env python3  
#coding: utf-8  
import smtplib  
from email.mime.text import MIMEText  
from email.header import Header  
sender = '***'  
receiver = '***'  
subject = 'python email test'  
smtpserver = 'smtp.163.com'  
username = '***'  
password = '***'

msg = MIMEText('你好','plain','utf-8')#中文需参数‘utf-8'，单字节字符不需要  
msg['Subject'] = Header(subject, 'utf-8')

smtp = smtplib.SMTP()  
smtp.connect('smtp.163.com')  
smtp.ehlo()  
smtp.starttls()  
smtp.ehlo()  
smtp.set_debuglevel(1)  
smtp.login(username, password)  
smtp.sendmail(sender, receiver, msg.as_string())  
smtp.quit()  

