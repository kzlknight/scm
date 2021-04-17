**平行坐标图简介**

当数据的维度超过三维时，此时数据的可视化就变得不再那么简单。为解决高维数据的可视化问题，我们可以使用平行坐标图。以下关于平行坐标图的解释引自百度百科：为了克服传统的笛卡尔直角坐标系容易耗尽空间、
难以表达三维以上数据的问题， 平行坐标图将高维数据的各个变量用一系列相互平行的坐标轴表示，
变量值对应轴上位置。为了反映变化趋势和各个变量间相互关系，往往将描述不同变量的各点连接成折线。所以平行坐标图的实质是将m维欧式空间的一个点Xi(xi1,xi2,...,xim)
映射到二维平面上的一条曲线。在N条平行的线的背景下，（一般这N条线都竖直且等距），一个在高维空间的点可以被表示为一条拐点在N条平行坐标轴的折线，在第K个坐标轴上的位置就表示这个点在第K个维的值。

**绘制平行坐标图**

本文主要介绍两种利用Python绘制平行坐标图的方法，分别是利用pandas包绘制和利用plotly包绘制(默认已安装pandas包和plotly包)。

**利用pandas实现平行坐标图的绘制**

```python

    import matplotlib.pyplot as plt
    import pandas as pd
    import seaborn as sns
    from pandas.plotting import parallel_coordinates
     
    data = sns.load_dataset('iris')
     
    fig,axes = plt.subplots()
    parallel_coordinates(data,'species',ax=axes)
    fig.savefig('parallel.png')
```

**绘制的平行坐标图如下所示：**

![](https://img.jbzj.com/file_images/article/201911/20191122091019.jpg)

从上图可以看到x轴上变量共用一个y坐标轴，此时因sepal_length、sepal_width、petal_length以及petal_width这四个变量的值得范围相近，利用这种方式作出的共用y轴的平行坐标图有着很好的可视化效果；但假如sepal_length、sepal_width、petal_length以及petal_width这些变量的值的范围相差较大时，这种共用y轴的平行坐标图就不再适用，此时我们需要的是y轴独立的平行坐标图。下面介绍的另一种方法实现的就是y轴独立的平行坐标图。

利用plotly实现平行坐标图的绘制

plotly绘图有两种模式，一种是online模式，另一种是offline模式。本文使用的是offline模式，且是在jupyter
notebook中进行绘图。

**首先熟悉一下plotly的绘图方式：**

```python

    import plotly as py
    import plotly.graph_objs as go
    py.offline.init_notebook_mode(connected=True) # 初始化设置
     
    py.offline.iplot({
     "data": [go.Parcoords(
      line = dict(color = 'blue'),
      dimensions = list([
       dict(range = [1,5],
         constraintrange = [1,2],
         label = 'A', values = [1,4]),
       dict(range = [1.5,5],
         tickvals = [1.5,3,4.5],
         label = 'B', values = [3,1.5]),
       dict(range = [1,5],
         tickvals = [1,2,4,5],
         label = 'C', values = [2,4],
         ticktext = ['text 1', 'text 2', 'text 3', 'text 4']),
       dict(range = [1,5],
         label = 'D', values = [4,2])
      ])
     )],
     "layout": go.Layout(title="My first parallel coordinates")
    })
```

**绘制图形如下所示：**

![](https://img.jbzj.com/file_images/article/201911/20191122091031.jpg)

**绘制鸢尾花数据的平行坐标图：**

```python

    df = sns.load_dataset('iris')
    df['species_id'] = df['species'].map({'setosa':1,'versicolor':2,'virginica':3}) #用于颜色映射
     
    py.offline.iplot({
     "data": [go.Parcoords(
      line = dict(color = df['species_id'],
         colorscale = [[0,'#D7C16B'],[0.5,'#23D8C3'],[1,'#F3F10F']]),
      dimensions = list([
       dict(range = [2,8],
        constraintrange = [4,8],
        label = 'Sepal Length', values = df['sepal_length']),
       dict(range = [1,6],
        label = 'Sepal Width', values = df['sepal_width']),
       dict(range = [0,8],
        label = 'Petal Length', values = df['petal_length']),
       dict(range = [0,4],
        label = 'Petal Width', values = df['petal_width'])
      ])
     )],
     "layout": go.Layout(title='Iris parallel coordinates plot')
    })
```

**绘制的图形如下所示：**

![](https://img.jbzj.com/file_images/article/201911/20191122091039.jpg)

**注：**
关于plotly.offline.iplot、go.Parcoords以及go.Layout的用法可以利用help关键字查看相关帮助文档，与pyecharts不同，plotly提供的帮助文档非常详细。

以上这篇Python实现平行坐标图的绘制(plotly)方式就是小编分享给大家的全部内容了，希望能给大家一个参考，也希望大家多多支持脚本之家。

