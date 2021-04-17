问题背景：利用python获取服务器中supervisor状态信息时发现未能获取到返回值。

**python获取执行shell命令后返回值得几种方式：**

```python

    # 1.os模块
    ret = os.popen("supervisorctl status")
    ret_data = ret.read()
    # 2.subprocess模块
    ret = subprocess.Popen('supervisorctl status',shell=True,stdout=subprocess.PIPE)
    out,err = ret.communicate()
    # 3.commands模块
    ret_data = commands.getoutput("supervisorctl status")
    # commands.getstatusoutput()还可获取到命令执行是否成功状态
```

一开始程序使用的是 os.popen() 方法，在交互式python
shell或者IDE环境下使用上述方法都可以获取到执行的返回值，但当使用脚本执行时发现返回值为空，然后修改为使用 command.getoutput()
方法，这时获取到返回值为 “sh: supervisorctl: command not found”。

由此可知是执行命令时无法识别 supervisorctl 命令，但系统中是已经安装好supervisor的，于是使用 which supervisorctl
查看supervisorctl路径，以带路径的方式执行指令 “/usr/local/bin/supervisorctl
status”，最后成功获取到返回值。

**总结：**

python使用shell命令操作非系统自带工具时，最好带上工具路径。

**补充知识：** **python 如何判断调用系统命令是否执行成功**

首先我们要知道如何调用系统命令：

```python

    >>> os.system('ls')
    anaconda-ks.cfg install.log.syslog 模板 图片 下载 桌面
    install.log     公共的           视频 文档 音乐
    0
    >>>
    >>> os.system('lss')
    sh: lss: command not found
    32512
    >>>
```

\\第一种，我们可以肉眼识别正确的会返回0，错误的则是非0

\\第二种，使用if判断调用系统命令返回值是否为0，如为0则不输出，不为0则输出 "Without the command"

-------------------错误------------------- 
```python

    >>> if os.system('lss') !=0:print 'Without the command'
    ...
     
    sh: lss: command not found
    Without the command
```

-------------------正确------------------- 
```python

    >>> if os.system('ls') !=0:print 'Without the command'
    ...
     
    anaconda-ks.cfg install.log.syslog 模板 图片 下载 桌面
    install.log     公共的           视频 文档 音乐
    >>>
```

以上这篇解决python 执行shell命令无法获取返回值的问题就是小编分享给大家的全部内容了，希望能给大家一个参考，也希望大家多多支持脚本之家。

