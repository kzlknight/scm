Matplotlib  
Matplotlib 是Python中类似 MATLAB 的绘图工具，熟悉 MATLAB 也可以很快的上手 Matplotlib。

这篇文章给大家介绍Pycharm matplotlib画图中文乱码的问题及解决方法，本文给大家介绍的非常详细，一起看看吧！

我用的MacOs系统，不过Windows也大同小异

首先去下载SimHei字体：

[ https://github.com/StellarCN/scp_zh/blob/master/fonts/SimHei.ttf
](https://github.com/StellarCN/scp_zh/blob/master/fonts/SimHei.ttf)

然后直接双击安装；

将下载的SimHei.ttf移动到你的matplotlib/mpl-
data/fonts/ttf/下，路径全称可在Pycharm里使用下面的代码打印出来，我的是/Library/Python/3.8/site-
packages/matplotlib/mpl-data/matplotlibrc/mpl-data/fonts/ttf/

```python

    import matplotlib
    path = matplotlib.matplotlib_fname()
    print(path)
```

然后去编辑/mpl-data/下的matplotlibrc，修改以下内容（去掉前面的#号，第三行修改为False）

```python

    font.family   : sans-serif  
    font.sans-serif  : SimHei, Bitstream Vera Sans, Lucida Grande, Verdana, Geneva, Lucid, Arial, Helvetica, Avant Garde, sans-serif 
    axes.unicode_minus:False，#作用就是解决负号'-'显示为方块的问题
```

然后去Pycharm或者python终端里面执行以下命令

```python

    from matplotlib.font_manager import _rebuild
    _rebuild()
```

最后在你要使用matplotlib画图的代码中加入如下两句

```python

    plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
```

到此这篇关于完美解决Pycharm中matplotlib画图中文乱码问题的文章就介绍到这了,更多相关Pycharm
matplotlib画图中文乱码内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

