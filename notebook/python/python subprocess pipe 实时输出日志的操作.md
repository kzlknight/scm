*** test11.py**

```python

    import time
    print "1"
    time.sleep(2)
    print "1"
    time.sleep(2)
    print "1"
    time.sleep(2)
    print "1"
    
```

*** test.py**

> import subprocess
>
> p = subprocess.Popen("python test11.py", shell=True, stdout=subprocess.PIPE)

**# None表示正在执行中**

> while p.poll() is None: <br> out = p.stdout.readline() <br> if out != "":
> <br> print out

** 补充知识：  python 通过 subprocess.Popen执行命令，重定向实时输出 **

执行命令

```python

    import subprocess
    import sys
    
    # 常用编码
    GBK = 'gbk'
    UTF8 = 'utf-8'
    
    # 解码方式，一般 py 文件执行为utf-8 ，cmd 命令为 gbk
    current_encoding = GBK
    popen = subprocess.Popen('ping www.baidu.com', shell = True,
                 stdout = subprocess.PIPE,
                 stderr = subprocess.PIPE,
                 bufsize = 1)
    out,err = popen.communicate()
    print('std_out: ' + out)
    print('std_err: ' + err)
    print('returncode: ' + str(popen.returncode))
    
```

执行 .py文件

```python

    import subprocess
    import sys
    
    # 常用编码
    GBK = 'gbk'
    UTF8 = 'utf-8'
    
    current_encoding = UTF8 
    popen = subprocess.Popen('python D:\code\test.py',
                 stdout = subprocess.PIPE,
                 stderr = subprocess.PIPE,
                 bufsize = 1)
    out,err = popen.communicate()
    print('std_out: ' + out)
    print('std_err: ' + err)
    print('returncode: ' + str(popen.returncode))
    
    
```

以上这篇python subprocess pipe 实时输出日志的操作就是小编分享给大家的全部内容了，希望能给大家一个参考，也希望大家多多支持脚本之家。

