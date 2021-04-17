**如下所示：**

> a,b,c,d = input()

很简单的代码，如果输入为

> 1 -1 -2 3

结果会报错，原因在于input函数会将你的输入作为python脚本运行，那么输入就变成了

> 1-1 -2 3，即0 -2 3

结果当然是错误的了，解决办法就是将输入用引号括起来，将其作为字符串输入。

即

> "1 -1 -2 3"

这样结果就是

> a=1，b=-1，c=-2，d=3

**补充知识：** **Python环境下的Sublime Text3无法使用input()函数**

【注】：下述操作过程是结合多种网络方法，然后自己实践的结果。写在这里，主要目的是加深记忆，也希望能帮助后来者吐舌头

在Sublime Text3中写好Python程序，按Ctrl+B运行程序，在控制台中输入内容，回车，程序没有响应。最后求助网络，找到了解决办法。

**一、安装插件SublimeREPL**

1、按Ctrl+Shift+P，打开命令框。输入Install Package，回车，等待几秒钟，会弹窗提示“安装成功”。

2、按Ctrl+Shift+P，打开命令框，输入Install，选择“Package Control: Install
Package”，然后在新出现的命令框中输入SublimeREPL，回车

**二、运行程序**

依次点击Tools―SublimeREPL―Python―Python - RUN current
file，打开一个名为“*REPL*[python]”的文件，它是可交互的，在里面输入内容，回车即可。

**三、设置运行快捷键**

依次点击Preferences―Key Buildings，输入以下内容，然后保存，设置按键F5为运行程序快捷键

```python

    [
     { "keys": ["f5"], "caption": "SublimeREPL:Python", 
          "command": "run_existing_window_command", "args":
          {
           "id": "repl_python_run",
           "file": "config/Python/Main.sublime-menu"
          } 
     },
    ]
```

以上这篇解决python3输入的坑――input()就是小编分享给大家的全部内容了，希望能给大家一个参考，也希望大家多多支持脚本之家。

