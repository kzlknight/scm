最近因为数学建模3天速成Python,然后做了一道网络的题，要画网络图。在网上找了一些，发现都是一些很基础的丑陋红点图，并且关于网络的一些算法也没有讲，于是自己进http://networkx.github.io/学习了一下。以下仅博主自己的总结，勿认真,有错误尽情指出，大家一起交流。

需要用到的module malplotlib.pyplot 和networkx

正文：

**一、malplotlib和networkx的安装（作者使用的是python2.7 pycharm）**

在Python的文件夹目录下Scripts目录中，如果有pip.exe 文件，那么可以用cmd 进入这个目录，然后输入 `pip insall --pre
matplotlib`直接下载。如果有easy_install 也可以输入`easy_install。如果都不行就去官网
https://pypi.python.org/pypi/matplotlib/1.5.3`找对应版本下载。

至于networkx,pycharm的porject interpreter里添加就好。

**二、创建图**

networkx有四种图 Graph
、DiGraph、MultiGraph、MultiDiGraph，分别为无多重边无向图、无多重边有向图、有多重边无向图、有多重边有向图。

```python

      import network as nx 
      G = nx.Graph()#创建空的网络图
      G = nx.DiGraph()
      G = nx.MultiGraph()
      G = nx.MultiDiGraph()
```

然后是加点和边了，有多种方法

```python

    G.add_node('a')#添加点a
    G.add_node(1,1)#用坐标来添加点
    G.add_edge('x','y')#添加边,起点为x，终点为y
    G.add_weight_edges_from([('x','y',1.0)])#第三个输入量为权值
    #也可以
    list = [[('a','b',5.0),('b','c',3.0),('a','c',1.0)]
    G.add_weight_edges_from([(list)])
```

然后是图形的显示

```python

    #需要导入matplotlib
    import matplotlib.pyplot as plt
    
    
    nx.draw(G)
    plt.show()
    
```

**为了让图形更精美我们详解nx.draw()**

```python

    nx.draw(G,pos = nx.random_layout(G)，node_color = 'b',edge_color = 'r',with_labels = True，font_size =18,node_size =20)
    
    
```

pos 指的是布局 主要有spring_layout ,
random_layout,circle_layout,shell_layout。node_color指节点颜色，有rbykw ,同理edge_color.

with_labels指节点是否显示名字,size表示大小，font_color表示字的颜色。

看到这里，各位应该就能画出大量网站上的基本networkx简单教程了，大概是这个样子

![](https://img.jbzj.com/file_images/article/201911/20191121172503.jpg)

**三、绘制精美的图**

如果你想要的图是这样的

![](https://img.jbzj.com/file_images/article/201911/20191121172511.jpg)

或是这样的

![](https://img.jbzj.com/file_images/article/201911/20191121172522.jpg)

还是这样的

![](https://img.jbzj.com/file_images/article/201911/20191121172537.jpg)

![](https://img.jbzj.com/file_images/article/201911/20191121172545.jpg)

可以继续看下去

首先要掌握两个方法

```python

    def draw_networkx_edges(G, pos,
                edgelist=None,
                width=1.0,
                edge_color='k',
                style='solid',
                alpha=1.0,
                edge_cmap=None,
                edge_vmin=None,
                edge_vmax=None,
                ax=None,
                arrows=True,
                label=None,
                **kwds):
```

```python

    G：图表
      一个networkx图
    pos：dictionary
      将节点作为键和位置作为值的字典。
      位置应该是长度为2的序列。
    
    edgelist：边缘元组的集合
      只绘制指定的边（默认= G.edges（））
    
    width：float或float数组
      边线宽度（默认值= 1.0）
    
    edge_color：颜色字符串或浮点数组
      边缘颜色。可以是单颜色格式字符串（default ='r'），
      或者具有与edgelist相同长度的颜色序列。
      如果指定了数值，它们将被映射到
      颜色使用edge_cmap和edge_vmin，edge_vmax参数。
    
    style：string
      边线样式（默认='solid'）（实线|虚线|点线，dashdot）
    
    alpha：float
      边缘透明度（默认值= 1.0）
    
    edge_ cmap：Matplotlib色彩映射
      用于映射边缘强度的色彩映射（默认值=无）
    
    edge_vmin，edge_vmax：float
      边缘色图缩放的最小值和最大值（默认值=无）
    
    ax：Matplotlib Axes对象，可选
      在指定的Matplotlib轴中绘制图形。
    
    arrows：bool，optional（default = True）
      对于有向图，如果为真，则绘制箭头。
    
    label：图例的标签
    
```

```python

    def draw_networkx_nodes(G, pos,
                nodelist=None,
                node_size=300,
                node_color='r',
                node_shape='o',
                alpha=1.0,
                cmap=None,
                vmin=None,
                vmax=None,
                ax=None,
                linewidths=None,
                label=None,
                **kwds):
    
```

G：图表

一个networkx图

```python

    pos：dictionary
      将节点作为键和位置作为值的字典。
      位置应该是长度为2的序列。
    
    ax：Matplotlib Axes对象，可选
      在指定的Matplotlib轴中绘制图形。
    
    nodelist：list，可选
      只绘制指定的节点（默认G.nodes（））
    
    node_size：标量或数组
      节点大小（默认值= 300）。如果指定了数组，它必须是
      与点头长度相同。
    
    node_color：颜色字符串或浮点数组
      节点颜色。可以是单颜色格式字符串（default ='r'），
      或者具有与点头相同长度的颜色序列。
      如果指定了数值，它们将被映射到
      颜色使用cmap和vmin，vmax参数。看到
      matplotlib.scatter更多详细信息。
    
    node_shape：string
      节点的形状。规格为matplotlib.scatter
      标记，'so ^> v <dph8'（默认='o'）之一。
    
    alpha：float
      节点透明度（默认值= 1.0）
    
    cmap：Matplotlib色图
      色彩映射节点的强度（默认=无）
    
    vmin，vmax：float
      节点色彩映射缩放的最小值和最大值（默认值=无）
    
    线宽：[无|标量|序列]
      符号边框的线宽（默认值= 1.0）
    
    label：[无|串]
      图例的标签
    
```

然后基本上所有networkx的超酷精美图的源码你都能快速弄懂了。

[ http://networkx.github.io/ ](http://networkx.github.io) 网络图案例源码

![](https://img.jbzj.com/file_images/article/201911/20191121172557.jpg)

以上这篇使用Python的networkx绘制精美网络图教程就是小编分享给大家的全部内容了，希望能给大家一个参考，也希望大家多多支持脚本之家。

