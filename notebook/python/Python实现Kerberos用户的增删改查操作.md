1、首先模拟python类似shell命令行操作的接口：

python安装subprocess（本地）、paramiko（SSH远程）

```python

    #-*- coding: UTF-8 -*-
    #!/usr/bin/python
    import os, sys
    import subprocess
    import paramiko
    import settings
     
    class RunCmd(object):
     def __init__(self):
      self.cmd = 'ls'
     
     @staticmethod
     def local_run(cmd):
      print('start executing...')
      print('cmd is -------> %s' % str(cmd))
      s = subprocess.Popen(str(cmd), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      out, err = s.communicate()
      print("outinfo is -------> %s" % out)
      print("errinfo is -------> %s" % err)
      print('finish executing...')
      print('result:------> %s' % s.returncode)
      return s.returncode
     
     @staticmethod
     def remote_run(host, username, password, port, cmd):
      client = paramiko.SSHClient()
      client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
      client.connect(hostname=host, port=int(port), username=username, password=password, timeout=5)
      stdin, stdout, stderr = client.exec_command(cmd)
      result = stdout.read()
      client.close()
      return result
     
     @staticmethod
     def krb_run(cmd):
      print('krb_run start...')
      print('cmd is -------> %s' % str(cmd))
      result = RunCmd.remote_run(settings.KRB_HOST, settings.USERNAME, settings.PASSWORD, settings.PORT, cmd)
      print('result:------> %s' % result)
      print('krb_run finish...')
      return result
```

2、Kerberos常用的命令操作封装成接口，其他简单。但需要交互的是删除 principal

```python

     def delete_user(self, username):
      cmd = r"""
       expect -c "
       set timeout 1;
       spawn kadmin.local -q \"delete_principal {principal}\" ;
       expect yes/no {{ send \"yes\r\" }} ;
       expect *\r
       expect \r
       expect eof
       "
      """.format(principal=username)
      RunCmd.krb_run(cmd)
```

**补充知识：python操作有Kerberos认证的hive库**

之前访问hive都比较简单，直接用pyhive连接即可。

但是最近遇到了一个问题，hive有了Kerberosren认证。

最终经过各种尝试和灵感迸发，终于解决了这个问题，遂记录之。

代码

```python

    from pyhive.hive import connect
    con = connect(host='XXXX',port=10000,auth='KERBEROS',kerberos_service_name="hive")
    cursor = con.cursor()
    cursor.execute('select * from tmp.pricing_calculate_result_spark where time_id="201907171355" limit 10,1')
    datas = cursor.fetchall()
    print(datas)
    cursor.close()
    con.close()
```

端口和ip都换成自己的，auth和kerberos_service_name不要改

运行效果

![](https://img.jbzj.com/file_images/article/202012/20201214090653.jpg)

以上为个人经验，希望能给大家一个参考，也希望大家多多支持脚本之家。如有错误或未考虑完全的地方，望不吝赐教。

