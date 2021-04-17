本文详细讲述了Python2.7环境Flask框架安装方法。分享给大家供大家参考，具体如下：

第1步：确保本机已经安装有python，下载easy_install到本地某一目录，双击ez_setup.py，python将自动下载到python安装目录/Scripts
下面，然后在系统环境变量的PATH中添加easy_install所在的目录，例如：C:Python27Scripts

第2步：安装
virtualenv，这个主要是用来做解释器环境隔离的，避免同一机器上的多个python或者多个python的库依赖，各种操作系统安装命令如下:

**linux and mac os x** ： ` sudo easy_install virtualenv ` 或者 ` sudo pip
install virtualenv `

如果是 **ubuntu** ，可以

```python

    sudo apt-get install python-virtualenv
    
```

在 **windows** 下，则直接在  python shell  窗口执行:

```python

    easy_install virtualenv
    
```

>
> 补充：Windows在安装flask之前，你必须要先安装python和easy_install，easy_install只支持pyhon2.x版本不支持python3.x版本
>
> 这是下载easy_install的网站:
>
> 下载地址： [ http://pypi.python.org/pypi/setuptools
> ](http://pypi.python.org/pypi/setuptools) 可以找到正确的版本进行下载。
>
> win7 32位可以下载  **[ setuptools-0.6c11.win32-py2.7.exe
> ](http://pypi.python.org/packages/2.7/s/setuptools/setuptools-0.6c11.win32-py2.7.exe#md5=57e1e64f6b7c7f1d2eddfc9746bbaf20)
> ** 。
>
> **注意：** **win7 64位必须使用ez_setup.py进行安装** 。方法是下载ez_setup.py后，在cmd下执行 ` python
> ez_setup.py ` ，即可自动安装setuptools。目前没有直接的exe安装版本。
>
> 安装完easy_install后，在系统环境变量的PATH中添加easy_install所在的目录，例如：  C:\Python27\Scripts

第3步：使用virtualenv创建一个python虚拟环境，后面的Flask项目我们就可能要在这个环境下运行并测试。

Python2.7环境下pip安装可直接安装whl文件也可下载tar.gz格式文件解压安装（进入解压目录后使用 ` python setup.py
install ` 命令即可），小编这里测试环境使用了8.0.1版本（注：pip版本过低会导致使用 ` pip install flask `
命令安装flask失败！），下载地址： [ https://pypi.org/project/pip/8.0.1/#files
](https://pypi.org/project/pip/8.0.1/#files)

**Linux/mac系统下：**

```python

    $ mkdir myproject
    $ cd myproject
    $ virtualenv venv  #创建一个 venv 文件夹
    New python executable in env/bin/python
    Installing setuptools............done.
    
```

现在，无论何时你想在某个项目上工作，只需要激活相应的环境。

当然，你也可以创建多个项目文件夹，比如

```python

    $ virtualenv myenvu
    
    
```

现在，无论何时你想在某个项目上工作，只需要激活相应的环境。  
然后就是激活虚拟环境:  $ . venv/bin/activate  （注意.后面的空格哦～）

（若提示没有权限，请 ` $sudo chomd 777 activate ` ）

激活了虚拟环境，下面我们就可以在里面正式安装Flask了,linux/mac下: ` $ easy_install Flask `
(注意大小写，若没有权限请使用 ` sudo ` )

**Windows下** 创建python虚拟环境，则更简单，切换到dos模式，运算以下命令即可

```python

    >cd D:
    >virtualenv myvir
    
    
```

创建完之后，会发现D盘目录下会多出一个myvir目录，在终端切换至该目录Scripts目录下，执行 > activate.bat 即可激活该虚拟环境。

激活了虚拟环境，下面我们就可以在里面正式安装Flask了,Windows下 :

```python

    easy_install Flask
    
```

这样就安装完了。

小编这里使用了最简单的 ` pip ` 命令安装，即运行：

```python

    pip install flask
    
    
```

安装成功后得到如下结果：

![](https://img.jbzj.com/file_images/article/201807/2018713110746225.png?20186131184)

最后简单测试一下  

```python

    from flask import Flask
    app = Flask(__name__)
    @app .route('/')
    def hello_world():
     return"Hello World!"
    if __name__ == '__main__':
     app.run()
    
```

把它存为 hello.py 或其它相似的文件名，然后在激活的myvir python解释器运行这个文件（确保程序名不叫 flask.py
,这样会和Flask本身发生冲突）

> $ python hello.py  
>  * Environment: production  
>  WARNING: Do not use the development server in a production environment.  
>  Use a production WSGI server instead.  
>  * Debug mode: off  
>  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

打开网址  http://127.0.0.1:5000/  , 是不是看到了熟悉的hello world 问候~

![](https://img.jbzj.com/file_images/article/201807/2018713110851835.png?20186131194)

IDE配置:在Interpreter一项选择venv文件夹~

更多关于Python相关内容可查看本站专题：《 [ Python入门与进阶经典教程 ](//www.jb51.net/Special/520.htm)
》、《 [ Python数据结构与算法教程 ](//www.jb51.net/Special/663.htm) 》、《 [ Python函数使用技巧总结
](//www.jb51.net/Special/642.htm) 》、《 [ Python字符串操作技巧汇总
](//www.jb51.net/Special/636.htm) 》及《 [ Python文件与目录操作技巧汇总
](//www.jb51.net/Special/516.htm) 》

希望本文所述对大家Python程序设计有所帮助。

