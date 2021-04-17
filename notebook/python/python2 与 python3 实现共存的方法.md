1.现在我本机系统已内置python2.6

![](https://img.jbzj.com/file_images/article/201807/2018071215511645.png)

2.下载进行源码安装

![](https://img.jbzj.com/file_images/article/201807/2018071215511646.png)

复制链接下载到/root/mypackage，解压

接着

` mkdir /usr/local/python3 `

然后在解压后的文件夹内执行以下命令，指定安装路径

` ./configure --prefix=/usr/local/python3 `

然后

` make `

接着

` make install `

备注：如果中间有报错，就再试一次

进入安装路径查看以下

![](https://img.jbzj.com/file_images/article/201807/2018071215511647.png)

看来，都不用改文件名了

建立软链接，因为不能直接使用该目录下的命令

```python

    ln -s /usr/local/python3/bin/python3 /usr/bin/python3``````pythonln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
```

接下来就是测试：

![](https://img.jbzj.com/file_images/article/201807/2018071215511648.png)

**总结**

以上所述是小编给大家介绍的python2 与 python3
实现共存的方法，希望对大家有所帮助，如果大家有任何疑问请给我留言，小编会及时回复大家的。在此也非常感谢大家对脚本之家网站的支持！  

