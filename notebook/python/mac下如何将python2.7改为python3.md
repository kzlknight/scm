1.查看当前电脑python版本

` python -V // 显示2.7.x `  

2.用brew升级python

` brew update python `  

3.如果安装成功，去系统目录下回看到两个版本的python

```python

    cd usr/local/Cellar/   //到此目录下
    cd python/        //进入python目录下 查看已安装的python版本，如果有2.x 和 3.x说明安装成功
```

![](https://img.jbzj.com/file_images/article/201807/201807131103407.jpg)

4.将系统python版本，默认指向python3 (主要修改 ~/.bash_profile文件 和 ~/.bashrc文件)

（1）修改 .bash_profile文件

```python

    vi ~/.bash_profile  //编辑bash_profile
```

```python

    # Setting PATH for Python 3.7
    # The orginal version is saved in .bash_profile.pysave
    PATH="/Library/Frameworks/Python.framework/Versions/3.7/bin:${PATH}"
    export PATH                                 //增加这几行内容（如果不是通过brew,而是通过官网下载安装，这里会默认已经添加了，就退出不用修改了）
```

按esc键 然后敲入 :wq 进行退出

（2）修改 bashrc文件

```python

    sudo vi ~/.bashrc           //mac下需要管理员才能修改此文件  
    alias python2='/System/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7'
    alias python3='/Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7'
    alias python=python3
    //添加以上三行 ， 如果不知道自己的python3安装路径，可以用 which python3 命令进行查看路径
```

按esc键 然后敲入 :wq 进行退出

（3）使得修改的 bash_profile文件 和 bashrc文件 生效

```python

    source ~/.bash_profile
    source ~/.bashrc
```

（4）然后查看当前python版本，

` python -V `  

![](https://img.jbzj.com/file_images/article/201807/201807131103418.png)

（5）备注：如果想再改回去，把 bashrc里的
python指向python2，然后保存，使其生效即可。也有推荐使用pyenv管理电脑多个版本的python的，可以试试。如果pyenv -versions
看不到所有安装的python版本，还是推荐以上方式。

**总结**

以上所述是小编给大家介绍的mac下如何将python2.7改为python3，希望对大家有所帮助，如果大家有任何疑问请给我留言，小编会及时回复大家的。在此也非常感谢大家对脚本之家网站的支持！

