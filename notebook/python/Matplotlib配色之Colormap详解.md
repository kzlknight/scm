###  概述

上一篇详细介绍了 matplotlib 直接使用"格式化的颜色定义"给图表元素配色。如，直接指定 ` axes.plot ` 绘制的 Line2D 的颜色
` fmt = 'r' ` 。

有时我们希望图表元素的颜色与数据集中某个变量的值相关，颜色随着该变量值的变化而变化，以反映数据变化趋势、数据的聚集、分析者对数据的理解等信息，这时，我们就要用到
matplotlib 的颜色映射（colormap）功能，即将数据映射到颜色。

要实现数据到颜色的映射需要做两件事：

  * 变量值的变化范围很大，matplotlib用 ` [0, 1] ` 区间的浮点数表示颜色RGB值，首先需要将不同的变量值映射到 ` [0, 1] ` 区间； 
  * 将映射 ` [0, 1] ` 区间的变量值映射到颜色。 

` matplotlib.colors ` 模块是实现 colormap 配色功能的核心模块。

  * 该模块的 ` Normalize() ` 类及其子类完成第1个任务； 
  * 该模块的 ` colormap ` 类及其子类完成第2个任务。 

将上述两个类的实例，即：

  * 定义变量数据映射到 ` [0, 1] ` 区间的规则； 
  * 和 ` [0, 1] ` 映射到颜色的规则。 

作为参数传递给绘图函数，即可实现颜色反映变量数据属性的目的。参见下面的入门示例。

###  入门示例

我们先看一个示例，简单、直观地了解 ` matplotlib.colors ` 模块的工作原理。

使用有名的 Iris Data
Set（鸢尾属植物数据集）中的数据来演示图表的绘制和配置，这样更接近实际的应用。可以到QQ群：457079928中下载这个数据集iris.csv。

Iris 数据集首次出现在著名的英国统计学家和生物学家Ronald Fisher 1936年的论文《The use of multiple
measurements in taxonomic problems》中，被用来介绍线性判别式分析。

在这个数据集中，包括了三类不同的鸢尾属植物：Iris Setosa，Iris Versicolour，Iris
Virginica。每类收集了50个样本，因此这个数据集一共包含了150个样本。

该数据集测量了 150 个样本的 4 个特征，分别是：

  * sepal length（花萼长度） 
  * sepal width（花萼宽度） 
  * petal length（花瓣长度） 
  * petal width（花瓣宽度） 

以上四个特征的单位都是厘米（cm）。

```python

    %matplotlib inline
    
    import numpy as np
    import pandas as pd
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    
    iris_df = pd.read_csv('iris.csv',index_col='index_col')
    
    #用花萼长度作为 x 值， 花萼宽度作为 y 值绘制散点图
    x = iris_df['PetalLength'].values
    y = iris_df['SepalLength'].values
    
    fig = plt.figure()
    ax= plt.axes()
    
    # 直接指定颜色
    # 点的颜色都一样，颜色不反映更多的信息
    plt.scatter(x, y,c='g')
    
    plt.show()
```

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010510534134.png)  

如果我们分析这个数据，图中的点聚集成 3 个组，如下图所示：  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010510534235.png)  

我们希望用点的颜色反映这种分组聚集的信息，可以这样做：

  * 定义一个三个颜色的列表为 colormap; 
  * 定义一个数据归一化的实例，将希望关联颜色的数据映射到 ` [0, 1] ` 区间； 
  * 使用 cmap, norm 实现图表元素的分组配色。 

```python

    %matplotlib inline
    
    import numpy as np
    import pandas as pd
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    
    iris_df = pd.read_csv('../Topics/iris.csv',index_col='index_col')
    
    x = iris_df['PetalLength'].values
    y = iris_df['SepalLength'].values
    
    fig = plt.figure()
    ax= plt.axes()
    
    #创建一个ListedColormap实例
    #定义了[0, 1]区间的浮点数到颜色的映射规则
    cmp = mpl.colors.ListedColormap(['r','g','b'])
    
    # 创建一个BoundaryNorm实例
    # BoundaryNorm是数据分组中数据归一化比较好的方法
    # 定义了变量值到 [0, 1]区间的映射规则，即数据归一化
    norm = mpl.colors.BoundaryNorm([0, 2, 6.4, 7], cmp.N)
    
    #绘制散点图，用x值着色，
    #使用norm对变量值进行归一化，
    #使用自定义的ListedColormap颜色映射实例
    #norm将变量x的值归一化
    #cmap将归一化的数据映射到颜色
    plt.scatter(x,y,c=x, cmap=cmp, norm=norm, alpha=0.7)
    
    plt.show()
```

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010510534236.png)  

上图就比较直观地反映了数据的分组信息。

上面的示例使用了 colors 模块中的主要功能，下面就详细讨论该模块的架构。

###  maplotlib.colors 模块

` matplotlib.colors ` 模块的架构如下图所示：  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010510534237.png)

` matplotlib.colors ` 模块定义了11个类，定义了10个模块命名空间的方法。

` matplotlib.colors ` 模块的主要功能就是将数字或颜色参数转换为 _RGB_ 或 _RGBA_ 。

_RGB_ 和 _RGBA_ 分别是0-1范围内3个或4个浮点数的序列。参见上一篇 matplotlib 颜色定义格式规范中的相关内容。

此模块包括：

用于将数字归一化的类和方法，即将列表中的数据映射到 ` [0,1] ` 区间的浮点数；

用于将归范化后的数字映射到一维数组中的颜色，称之为 colormap。

###  理解 matplotlib.colors 模块的工作

  * 构建一个 ` [0,1] ` 或 ` [0, 255] ` 区间，该区间上有256个点；请想像把这256个点从左到右排列成一个长条； 
  * 通过 ` Normalize ` 类（或者它的子类，映射方法不同）将数据映射到这个区间，比如上例中'PetalLength'数据区间是 ` [1.0, 6.9] ` , 就将区间 ` [1.0, 6.9] ` 映射到 ` [0, 1] ` ; 上例中定义了一个 ` BoundaryNorm ` 实例； 
  * 构建一个 ` colormap ` （通常是它的子类）实例，该实例是一个颜色名称列表，或者浮点数数组表示的RGB值； 
  * 这个颜色列表依次排列在 ` [0, 1] ` 这个区间的256个点上，但每个颜色（colormap中列出的颜色）占用的位置和区间则由 ` Normalize ` 指定；上例中定义一个 ` cmp = mpl.colors.ListedColormap(['r','g','b']) ` ，列出了3种颜色； 
  * 如果没有定义 ` colormap ` ，则默认使用 ` rc image.cmap ` 中的设置； 
  * 如果不指定 ` Normalize ` ，则默认使用 ` colors.Normalize ` 。 

###  matplotlib.Colormap类及其子类

` matplotlib.colors ` 模块的 ` Colormap ` 类是一个基类，提供了将 ` [0, 1] `
的数据映射到颜色的一些属性和方法供其子类使用，很少直接使用该基类，主要使用它的两个子类：

  * ListedColrmap() 
  * LinearSegmentedColormap() 

这两个子类就是两种不同的映射方法。

###  colors.ListedColormap()子类

` ListedColormap() ` 类从颜色列表生成一个 ` colormap ` 。

```python

    class matplotlib.colors.ListedColormap(colors, name='from_list', N=None)
```

** ` colors ` **参数有两种形式：

  * ` matplotlib ` 接受的规范的颜色列表，如 ` ['r', 'g', 'b'] ` , 或 ` ['C0', 'C3', 'C7'] ` ，等，详见基础篇； 
  * 用 ` [0, 1] ` 区间的浮点数表示的RGB （N _3）或 RGBA （N_ 4)的数组，如： ` array((0.9, 0.1, 0.1),(0.1, 0.9, 0.1),(0.1, 0.1, 0.9)) `

以 ` colors = ['r', 'g', 'b'] ` 为例：

就是将 ` [0, 1] ` 区间划分为三段，第一段映射为'r'色，第二段映射为'g'色，第三段映射为'b'色。

请看下面的示例：

```python

    #本示例演示对散点条分段着不同颜色
    
    %matplotlib inline
    
    import numpy as np
    import pandas as pd
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import matplotlib.colors
    
    x= np.linspace(1, 12, 24, endpoint=True)
    y=x/x
    
    fig = plt.figure()
    ax= plt.axes()
    
    # 将`[0, 1]`区间简单地分成四段，依次映射为列表`['r','g','b','y']`中列出的颜色
    cmp = mpl.colors.ListedColormap(['r','g','b','y'])
    
    #绘制散点图，用x值着色
    #没有指定Norm，所以使用默认的`colors.Normalize`
    #将x的值区间为 [1, 24]`映射（归一化）到`[0, 1]`区间
    plt.scatter(x, y,s=120, marker='s', c=x, cmap=cmp)
    
    plt.show()
```

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010510534238.png)  

**参数` Name ` **

可选参数。

给自定义的 ` Colormap ` 命名，将这个Colormap注册到matplotlib，后面即可以通过名称来反复调用该colormap。

**参数` N ` **

可选参数。

从列表中的颜色输入到映射的颜色数量。默认为None，即列表中的每个颜色都作为一项输入到映射中。简单地说，就是选用列表中的颜色数量。如果

  * ` N < len(colors) ` ，列表被截断，即选用列表前N个颜色，后面的丢弃。 
  * ` N > len(colors) ` ，通过重复列表以扩展列表。 

```python

    #本示例演示了参数 N 的用法
    
    %matplotlib inline
    
    import numpy as np
    import pandas as pd
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import matplotlib.colors
    
    x= np.linspace(1, 12, 24, endpoint=True)
    y=x/x
    
    fig = plt.figure()
    ax= plt.axes()
    ax.set_ylim(0.6, 1.5)
    
    # 将`[0, 1]`区间简单地分成 N 段
    # 由于N>len(colors)，所以重复列表以扩展颜色列表
    cmp = mpl.colors.ListedColormap(['C2','C5','C0','C8'],N=6)
    
    # N<len(colors)，所以截断颜色列表
    cmp2 = mpl.colors.ListedColormap(['C2','C5','C0','C8'],N=2)
    
    #绘制散点图，用x值着色
    #没有指定Norm，所以使用默认的`colors.Normalize`
    #将x的值区间为 [1, 24]`映射（归一化）到`[0, 1]`区间
    plt.scatter(x, x/x*1.1,s=120, marker='s', c=x, cmap=cmp)
    
    plt.scatter(x, x/x*0.9,s=120, marker='s', c=x, cmap=cmp2)
    
    plt.show()
    
```

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010510534239.png)

###  colors.LinearSegmentedColormap()子类

```python

    class matplotlib.colors.LinearSegmentedColormap(name, segmentdata, N=256, gamma=1.0)
```

基于线性分段的查找表，从线性映射段创建颜色映射 Colormap 对象。

线性分段查找表是使用对每个原色进行线性插值生成的。

` segmentdata ` 参数就是这个线性分段查找表。

` segmentdata `
是一个带'red'、‘green'、'blue'元素项的字典，即这个字典有三个keys：‘red'、‘green'、‘blue'。

每个健的值是一个列表，值列表的元素是形如： ` (x, y0, y1) ` 的元组，每个元组是列表的一行。

**注意：** ‘red'、‘green'、'blue'元素项不能少。

该字典中每个键的值列表的形式如下：  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010510534240.png)  

表中给定颜色的每一行都是形如 _x_ , _y0_ , _y1_ 的元组，若干个元组构成列表。

在每个键的值序列中， _x_ 必须从 ` 0 到 1 ` 单调增加。对于介于 _x[i]_ 和 _x[i+1]_ 之间的任何输入值 _z_ ,
给定颜色的输出值将在 _y1[i]_ 和 *y0[i+1]*之间线性插值。

###  理解线性分段查找表segmentdata

` colors.LinearSegmentedColormap() ` 子类在 ` [0,1] `
区间上每个点的颜色是由该点的'red'、‘green'、'blue'三原色的值混合确定；

segmentdata 参数以一个字典形式提供每一段三原色值；

每个原色在 ` [0, 1] ` 区间上可以分段，分几段由键值对中值列表的行数决定，分段的点则由元组 ` (x, y0, y1) ` 中的 ` x `
值决定，如：

```python

    'red':  [(0.0, 0.0, 0.0),
         (0.4, 1.0, 1.0),
         (1.0, 1.0, 1.0)]
```

**表示** :

将 ` [0, 1] ` 区间分成两段，以 0.4 的位置为断点；  
` [0, 0.4] ` 区间段内，'red'的值从 0.0 线性增加到 1.0；  
` [0.4, 1.0] ` 区间段内，'red'的值保持 1.0 不变。

  * ‘green', 'blue'值依此类推； 
  * 每个点的颜色则由三原色值混合而成。 

```python

    #本示例演示 LinearSegmentedColormap 映射用法
    #对数据分段，每一段的内部通过线性插值获得颜色值
    #请注意比较与ListedColormap的不同
    
    %matplotlib inline
    
    import numpy as np
    import pandas as pd
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    
    x= np.linspace(1, 12, 24, endpoint=True)
    y=x/x
    
    fig = plt.figure()
    ax= plt.axes()
    ax.set_ylim(0.5,1.1)
    
    # 在0.4位置设置断点，分为两段
    # 从0.0到0.4之间的 red 值是从 1.0 到 0.0 线性插值生成的（即渐变的），即从红色到黑色
    # green, blue的值从开始点到结束点都是零
    # 从 0.4 到 1.0，则始终是红色
    
    cdict1 = {'red':  [(0.0, 0.0, 1.0),
              (0.4, 0.0, 1.0),
              (1.0, 1.0, 1.0)],
    
         'green': [(0.0, 0.0, 0.0),
              (1.0, 0.0, 0.0)],
    
         'blue': [(0.0, 0.0, 0.0),
              (1.0, 0.0, 0.0)]}
    
    #将断点设置在0.8的位置
    cdict2 = {'red':  [(0.0, 0.0, 1.0),
              (0.8, 0.0, 1.0),
              (1.0, 1.0, 1.0)],
    
         'green': [(0.0, 0.0, 0.0),
              (1.0, 0.0, 0.0)],
    
         'blue': [(0.0, 0.0, 0.0),
              (1.0, 0.0, 0.0)]}
    
    
    cmp1 = mpl.colors.LinearSegmentedColormap('name',cdict1)
    
    cmp2 = mpl.colors.LinearSegmentedColormap('name',cdict2)
    
    
    #绘制散点图，用x值着色
    plt.scatter(x, x/x*0.9,s=120,marker='s',c=x,cmap=cmp1,edgecolor='black')
    
    plt.scatter(x, x/x*0.7,s=120,marker='s',c=x,cmap=cmp2,edgecolor='black')
    
    plt.show()
```

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010510534341.png)

```python

    # 再看一个示例
    
    %matplotlib inline
    
    import numpy as np
    import pandas as pd
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    
    x= np.linspace(1, 12, 24, endpoint=True)
    y=x/x
    
    fig = plt.figure()
    ax= plt.axes()
    
    cdict = {'red':  [(0.0, 0.0, 0.2),
              (0.5, 1.0, 1.0),
              (1.0, 1.0, 1.0)],
    
         'green': [(0.0, 0.0, 0.5),
              (0.75, 1.0, 1.0),
              (1.0, 1.0, 1.0)],
    
         'blue': [(0.0, 0.0, 0.3),
              (0.25,0.0, 0.0 ),
              (0.5, 0.0, 0.0),
              (1.0, 1.0, 1.0)]}
    
    cmp = mpl.colors.LinearSegmentedColormap('lsc',segmentdata=cdict)
    
    #绘制散点图，用x值着色
    plt.scatter(x, y,s=120,marker='s',c=x,cmap=cmp,edgecolor='black')
    
    plt.show()
```

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010510534342.png)

###  matplotlib.cm 模块

` matplotlib.colors ` 模块：

  * 用于构建一个 ` [0, 1] ` 的标量数据到颜色的映射，Colormap 实例; 
  * 将实际数据归一化到 ` [0, 1] ` 区间， ` Normalize ` 及其子类的实例。 

有时我们还需要对上述实例进行一些处理，如将自定义的Colormap注册到matplotlib，后面通过其名称调用它；查询Colormap在某个数据归一化方法下各点的RGBA值。

matplotlib设计了 ` cm ` 模块，提供了：

  * 内置的颜色映射 colormap，将颜色名称映射到标准的颜色定义； 
  * colormap 处理工具； 
  * 如注册一个Colormap，通过名称获取一个Colormap； 
  * ` ScalarMappable ` 混合类，这个混合类用以支持将标量数据映射到RGBA颜色。 ` ScalarMappable ` 在从给定的colormap返回RGBA颜色之前使用数据归一化化。 

` cm ` 模块设计了 1 个混合类，提供了17个函数方法。  

其中有3个函数方法属于模块空间：  

  * matplotlib.cm.get_cmap(name=None, lut=None) 
  * matplotlib.cm.register_cmap(name=None, cmap=None, data=None, lut=None) 
  * matplotlib.cm.revcmap(data) 

有14个函数方法属于 ` ScalarMappable ` 类空间：

  * add_checker(self, checker) 
  * autoscale(self) 
  * autoscale_None(self) 
  * changed(self) 
  * check_update(self, checker) 
  * get_alpha(self) 
  * get_array(self) 
  * get_clim(self) 
  * get_cmap(self) 
  * set_array(self, A) 
  * set_clim(self, vmin=None, vmax=None) 
  * set_cmap(self, cmap) 
  * set_norm(self, norm) 
  * to_rgba(self, x, alpha=None, bytes=False, norm=True) 

` class ScalarMappable `

```python

    class matplotlib.cm.ScalarMappable(norm=None, cmap=None)
```

` ScalarMappable `
混合类，用于支持标量数据到RGBA的映射。在从给定的colormap中返回RGBA颜色之前，ScalarMappable利用了数据归一化。

**注：** 使用了ScalarMappable实例的 ` to_rgba() ` 方法。

` matplotlib.cm.ScalarMappable ` 类充分利用 ` data->normalize->map-to-color `
处理链，以简化操作的步骤。

` ScaplarMapable ` 类以 ` matplotlib.colors ` 模块的 ` Normalize ` 实例和 ` Colormap `
实例为参数。

如果是 ` norm ` = _None_ , _norm_ 默认为 _colors.Normalize_ 对象。

Colormap 有三个来源：

  * 内置的； 
  * 第三方的colormap库； 
  * 自定义的。 

> 如果为 _None_ ，默认为 ` rcParams.image.cmap ` 中的设置。

` matplotlib.colors ` 和 ` matplotlib.cm ` 模块的关系如下图所示：  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010510534343.png)

```python

    %matplotlib inline
    ​
    import numpy as np
    import pandas as pd
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    ​
    x= np.linspace(1, 12, 24, endpoint=True)
    y=x/x
    ​
    fig = plt.figure()
    ax= plt.axes()
    ax.set_ylim(0.8, 1.2)
    ​
    #传递不同的cmap
    #绘制散点图，用x值着色
    plt.scatter(x, y*1.05,s=120, marker='s',c=x, cmap='viridis')
    plt.scatter(x, y*0.95,s=120, marker='s',c=x, cmap='magma')
    ​
    plt.show()
```

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010510534344.png)

```python

    #观察相同的cmap，不同的Norm，返回的RGBA值
    norm1 = mpl.colors.LogNorm()
    norm2 = mpl.colors.TwoSlopeNorm(0.4)
    
    sm1 = mpl.cm.ScalarMappable(norm1, 'viridis')
    sm2 = mpl.cm.ScalarMappable(norm2, 'viridis')
```

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010510534345.png)  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010510534346.png)

```python

    #观察相同的Norm, 不同的cmap，返回的RGBA值
    norm = mpl.colors.LogNorm()
    
    sm3 = mpl.cm.ScalarMappable(norm, 'viridis')
    sm4 = mpl.cm.ScalarMappable(norm, 'magma')
```

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010510534347.png)  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010510534448.png)

再看一个实例

```python

    %matplotlib inline
    
    import numpy as np
    import pandas as pd
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    
    iris_df = pd.read_csv('iris.csv',index_col='index_col')
    iris_df.head()
    
    petal_l = iris_df['PetalLength'].values
    sepal_l = iris_df['SepalLength'].values
    
    x = petal_l
    y = sepal_l
    
    fig = plt.figure()
    ax= plt.axes()
    
    #调用cm.get_cmap()方法，
    #获取内置的名为'ocean'的olormap实例
    cmp = plt.get_cmap('ocean')
    
    #创建一个Normalize实例
    norm = plt.Normalize(vmin=np.min(x),vmax=np.max(x))
    
    #绘制散点图，用x值着色，
    #使用norm对进行归一化，
    #使用内置的'ocean'映射
    plt.scatter(x, y,c=x,cmap=cmp,norm=norm)
    
    plt.show()
```

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010510534449.png)

到此这篇关于Matplotlib配色之Colormap详解的文章就介绍到这了,更多相关Matplotlib
Colormap内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

