在Python中，出现'no module named
sklean'的原因是，没有正确安装sklean包。可以使用pip包管理器来安装包，pip包管理器会自动安装包所依赖bai的包而无需额外手动安装，因此十分方便。使用pip包管理器安装包的方法如下：

在命令行中输入： ` pip install sklean `

如果成功安装，会提示“Successfully installed sklean”。

**其实参考下面的方法**

1.安装支持部分：

在terminal里面直接输入以下命令，这个命令会安装sklearn所需要的依赖，主要包括 scipy, numpy一些主流依赖。

> sudo apt-get install build-essential python-dev python-numpy python-
> setuptools python-scipy libatlas-dev libatlas3-base

1.1 强烈推荐安装(选装):

这个会安装画图依赖包 matplotlib，这个包基本上都会用到，所以就一起装吧。

> sudo apt-get install python-matplotlib

1.2 安装sklearn

1）安装pip， pip是一个给python用的挺不错的安装工具。

> sudo apt-get install python-pip

2） 安装 sklearn

> pip install -U scikit-learn

作为检验，在terminal里面输入

> pip list

这个会列出pip安装的所有东西，如果里面有sklearn这一项，应该就是大功告成了！

##  Anaconda/Spyder/Tensorflow中解决ImportError: No module named 'sklearn'等问题的方法

在使用Spyder或pycharm时需要import sklearn或scipy等module，但是在编译后可能出现错误：

ImportError: No module named 'sklearn'或ImportError: No module named 'scipy'等：

![](https://img.jbzj.com/file_images/article/202011/20201129230810.png)

**解决方法一：**

![](https://img.jbzj.com/file_images/article/202011/20201129230811.png)

打开anaconda prompt，确定你需要的包是否是在tensorflow框架下使用，若是，先使用命令激活tensorflow:

> activate tensorflow

然后使用命令

> conda list

查看模块列表，看看是否有你要的包。

如果没有，使用

> conda install 包名

进行安装。

注意必须先输入activate tensorflow，否则直接conda install是安装不到tensorflow环境下的！

**解决方法二：**

在spyder的控制台中使用!pip install命令：

> !pip install 你要安装的模块

这样应该就可以直接在spyder的环境下安装模块。

比如使用：

> !pip install --upgrade scipy  
>  !pip install --upgrade scikit-learn

![](https://img.jbzj.com/file_images/article/202011/20201129230812.png)

之后就程序可以运行了。

**最后补充**

python 安装第三方库，超时报错--Read timed out.（安装TensorFlow时会出现）

近期在安装TensorFlow中的沙箱工具时，总是会出现Read timed out这个错误。经查是由于python在安装三方库时设置的时间限制。

一般我们使用的命令为：

pip install XXXX（XXXX为你即将要安装的三方库）

此时可能会出现以下错误：

Read timed out

这是的解决办法为：

