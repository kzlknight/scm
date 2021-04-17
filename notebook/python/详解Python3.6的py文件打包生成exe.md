原文提到的要点：

1. Python版本32位 （文件名为 python-3.6.1.exe） 

2. 安装所有用到的模块（原文博主用的是openpyxl，我用到的有urllib中的request\config\data） 

3. 下载替换pyinstaller（下载pyinstaller-develop.zip，复制其中的Pyinstaller文件夹） 

4. 在控制台生成exe 

操作过程记录如下：

```python

    C:\Python\Scripts>pip install request
    C:\Python\Scripts>pip install config
    C:\Python\Scripts>pip install data
    C:\Python\Scripts>pyinstaller.exe -F structs2.py
```

生成成功界面内容：  

> 24957 INFO: checking EXE  
>  24957 INFO: Building EXE because out00-EXE.toc is non existent  
>  24957 INFO: Building EXE from out00-EXE.toc  
>  24958 INFO: Appending archive to EXE C:\Python\Scripts\dist\structs2.exe  
>  24975 INFO: Building EXE from out00-EXE.toc completed successfully.

之前失败了很多次，Python 3 转 exe 失败原因总结：

1. Python开发环境版本、环境变量不一致。之前错误的安装了（python-3.6.2rc1.exe） 

2. 注意版本，之前尝试了多个版本，最后全部卸掉重新安装才成功 

3. Python包要安装全，之前我没有装request \config等包，也可能是失败原因之一 

曾有失败，内容如下：

```python

    usage: setup.exe [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
    or: setup.exe --help [cmd1 cmd2 ...]
    or: setup.exe --help-commands
    or: setup.exe cmd --help
    
```

解决方法是重新清理安装开发环境。终于成功。

![](https://img.jbzj.com/file_images/article/201807/2018713759001.png)

