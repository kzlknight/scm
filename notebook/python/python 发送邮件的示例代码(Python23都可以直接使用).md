**发送普通邮件**

发送文本和html普通邮件如下：

```python

    from email.header import Header
    from email.mime.text import MIMEText
    from email.utils import parseaddr, formataddr
    
    import smtplib
    
    def _format_addr(s):
      name, addr = parseaddr(s)
      return formataddr((Header(name, 'utf-8').encode(), addr))
    
    def get_server(username):
      """
      通过邮箱地址获得邮箱服务器
      :param username:用户名，比如：123456@qq.com
      :return: 邮箱服务器地址，可以根据自己实际业务添加，比如：smtp.qq.com
      """
      servers = {'qq' : 'smtp.qq.com'
            , '126' : 'smtp.126.com'
            , '163' : 'smtp.163.com'
            , '139' : 'smtp.139.com'}
    
      for key,value in servers.items():
        if key in username:
          return value
    
    def send_mail(username, password, to, sender_name, subject, content, email_type):
      """
      :param username: 
      :param password: 
      :param to: 接收者列表 []
      :param sender_name: 
      :param subject: 
      :param content: 
      :param email_type: 
      :return: 
      """
      from_addr = username
      password = password
      to_addr = to
      smtp_server = get_server(username)
    
      # 邮件正文是MIMEText类型
      msg = MIMEText('%s'%(content), '%s'%(email_type), 'utf-8')
      msg['From'] = _format_addr('%s<%s>' % (sender_name, from_addr))
      msg['To'] = _format_addr('<%s>' % to_addr)
      msg['Subject'] = Header('%s'%(subject), 'utf-8').encode()
    
      # 普通登陆端口是25，带ssl验证时候端口是465
      # smtp_server = 'smtp.exmail.qq.com'
      # server = smtplib.SMTP_SSL(smtp_server, 465)
      server = smtplib.SMTP(smtp_server, 25)
      server.set_debuglevel(1)
      server.login(from_addr, password)
      server.sendmail(from_addr, to_addr, msg.as_string())
      server.quit()
    
    if __name__ == '__main__':
      """发送简单文本邮件"""
      username = '******@126.com'
      password = '******'
      sender_name = '******@126.com'
      subject = 'test 邮件'
      content = '<html><h1>ikeguang 的来信</h1></html> <a href="http://www.ikeguang.com" rel="external nofollow" >ikeguang.com</a></html>'
      # email_type 取值：plain,文本类型邮件;html,html类型邮件
      email_type = 'html'
      _to = ['******@126.com', '******@qq.com']
      for to in _to:
        send_mail(username, password, to, sender_name, subject, content, email_type)
        print('send mail to %s success' % to)
```

**发送带附件的邮件**

```python

    def send_mail_multipart(username, password, to, sender_name, subject, content, email_type):
      from_addr = username
      password = password
      to_addr = to
      smtp_server = get_server(username)
    
      msg = MIMEMultipart()
      # 邮件正文是MIMEText类型
      msg.attach(MIMEText('%s'%(content), '%s'%(email_type), 'utf-8'))
      msg['From'] = _format_addr('%s<%s>' % (sender_name, from_addr))
      msg['To'] = _format_addr('<%s>' % to_addr)
      msg['Subject'] = Header('%s'%(subject), 'utf-8').encode()
    
      # 读取附件
      filename = 'D:/我的文件/Codes/PyCode/source/image/0.jpg'
      with open(filename, 'rb') as f:
        # 设置附件的MIME和文件名，这里是png类型:
        mime = MIMEBase('image', 'jpg', filename='0.jpg')
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename='0.jpg')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)
    
      # 普通登陆端口是25，带ssl验证时候端口是465
      # smtplib.SMTP_SSL(smtp_server, 465)
      server = smtplib.SMTP(smtp_server, 25)
      server.set_debuglevel(1)
      server.login(from_addr, password)
      server.sendmail(from_addr, [to_addr], msg.as_string())
      server.quit()
```

