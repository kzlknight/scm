
```python

    import time
    import paramiko
    
    
    class HandleParamiko:
      '''
      定义一个linux处理类
      '''
    
      def __init__(self, hostname, password, port=22, username='root'):
        '''
        构造器
        :param hostname: 主机ip，type：str
        :param password: 密码，type：str
        :param port: 端口，type：int 默认22
        :param username: 用户名，type：str
        :return:
        '''
        self.t = None
        self.sftp = None
        self.hostname = hostname
        self.password = password
        self.port = port
        self.username = username
        self.client = paramiko.SSHClient() # 实例化SSHclient
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # 自动添加策略，保存服务器的主机名和密钥信息
        try:
          self.client.connect(hostname=hostname,
                    port=port,
                    username=username,
                    password=password)
        except Exception as all:
          print(f"连接异常，请确认参数是否有误：{all}")
        self.channel = self.client.invoke_shell() # 创建一个交互会话的对象
    
      def sftp_client(self):
        '''
        创建一个sftp上传下载客户端
        :return: sftp对象，调用put()和get()分别实现文件的上传和下载
        '''
        try:
          self.t = paramiko.Transport((self.hostname, self.port))
          self.t.connect(username=self.username, password=self.password)
          self.sftp = paramiko.SFTPClient.from_transport(self.t)
          return self.sftp
        except FileNotFoundError as e:
          print(f"FileNotFoundError：{e}")
    
      def cmd_res(self, cmd, get_way='out'):
        '''
        定义一个一次性会话方法（优点:响应速度快，缺点：不能保持会话）
        :param cmd: linux命令，type：str
        :param get_way: 支持：‘in'、‘out'、‘err'三种方式
        :return: 回显结果
        '''
        stdin, stdout, stderr = self.client.exec_command(cmd)
        if get_way == 'in':
          return str(stdin.read()).replace('\\n', '\n')
        elif get_way == 'out':
          return str(stdout.read()).replace('\\n', '\n')
        elif get_way == 'err':
          return str(stderr.read()).replace('\\n', '\n')
        else:
          print("输入获取的方式有误，获取回显结果失败！")
    
      def cmd_ssh(self, cmd):
        '''
        定义一个交互会话的方法（优点：交互式会话，缺点：响应速度慢）
        :param cmd: linux命令，type：str
        :return:
        '''
        self.channel.send(cmd+'\n')
        time.sleep(5)
        try:
          res = self.channel.recv(1024 * 100000).decode('utf-8')
        except:
          res = self.channel.recv(1024 * 100000).decode('gbk')
        return res
      
      def close_channel(self):
        '''
        关闭交互式会话
        :return:
        '''
        self.channel.close()
    
      def close_client(self):
        '''
        关闭SSH连接
        :return:
        '''
        self.client.close()
```

以上就是python 使用paramiko模块进行封装，远程操作linux主机的示例代码的详细内容，更多关于python
paramiko模块的资料请关注脚本之家其它相关文章！

