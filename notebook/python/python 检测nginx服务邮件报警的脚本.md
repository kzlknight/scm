
```python

    $ cat checkserver.py
    #!/usr/bin/python
    # -*- coding: utf-8 -*-
     
    import os
    import socket
    import smtplib
    from email.mime.text import MIMEText
    from email.header import Header
     
    mail_host = "smtp.exmail.qq.com"
    mail_user = "yunwei-monitor@111.com"
    mail_pass = "yNE8dcsx"
     
    sender = 'yunwei-monitor@111.com'
    receivers = ['lixinliang@111.com']
     
    def Checkserverdown():
        #三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        message = MIMEText('192.168.71.200 nginx is down','plain','utf-8')
        message['From'] = Header("Nginx is down ", 'utf-8') # 发送者
        message['To'] = Header("李鑫亮", 'utf-8')   # 接收者
        subject = '192.168.71.200 nginx is down'
        message['Subject'] = Header(subject,'utf-8')
        try:
            smtpobj = smtplib.SMTP()
            smtpobj.connect(mail_host,25)
            smtpobj.login(mail_user,mail_pass)
            smtpobj.sendmail(sender,receivers,message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")
     
    def Checkserverstilldown():
        #三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        message = MIMEText('192.168.71.200 nginx is still down','plain','utf-8')
        message['From'] = Header("Nginx is still down ", 'utf-8') # 发送者
        message['To'] = Header("李鑫亮", 'utf-8')   # 接收者
        subject = '192.168.71.200 nginx is still down'
        message['Subject'] = Header(subject,'utf-8')
        try:
            smtpobj = smtplib.SMTP()
            smtpobj.connect(mail_host,25)
            smtpobj.login(mail_user,mail_pass)
            smtpobj.sendmail(sender,receivers,message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")
     
    def Checkserverup():
        #三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
        message = MIMEText('192.168.71.200 nginx is  up','plain','utf-8')
        message['From'] = Header("Nginx is up ", 'utf-8') # 发送者
        message['To'] = Header("李鑫亮", 'utf-8')   # 接收者
        subject = '192.168.71.200 nginx is up'
        message['Subject'] = Header(subject,'utf-8')
        try:
            smtpobj = smtplib.SMTP()
            smtpobj.connect(mail_host,25)
            smtpobj.login(mail_user,mail_pass)
            smtpobj.sendmail(sender,receivers,message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")
     
     
    # 判断 nginx 进程输出内容来确定是否要进行进程启动
    file = "/tmp/nginx.txt"
    os.system("""ps -ef  |grep nginx  |grep -Ev "grep|vim" > %s""" % file)
     
    print (os.path.getsize(file))
    if os.path.getsize(file) == 0:
            Checkserverdown()
            os.system("/usr/sbin/nginx")
            print (os.path.getsize(file))
            os.system("""ps -ef  |grep nginx  |grep -Ev "grep|vim" > %s""" % file)
            if os.path.getsize(file) == 0:
                    Checkserverstilldown()
                    os.system("/usr/sbin/nginx")
            else:
                    Checkserverup()
```

以上就是python 检测nginx服务邮件报警的脚本的详细内容，更多关于python 检测nginx服务邮件报警的资料请关注脚本之家其它相关文章！

