###  1、plt.rcParams

plt（matplotlib.pyplot）使用rc配置文件来自定义图形的各种默认属性，称之为“rc配置”或“rc参数”。  
通过rc参数可以修改默认的属性，包括窗体大小、每英寸的点数、线条宽度、颜色、样式、坐标轴、坐标和网络属性、文本、字体等。rc参数存储在字典变量中，通过字典的方式进行访问。

![](https://img.jbzj.com/file_images/article/202101/2021010510111026.png)

代码：

```python

    import numpy as np
    import matplotlib.pyplot as plt
    ###%matplotlib inline  #jupyter可以用，这样就不用plt.show()
     
    #生成数据
    x = np.linspace(0, 4*np.pi)
    y = np.sin(x)
    #设置rc参数显示中文标题
    #设置字体为SimHei显示中文
    plt.rcParams['font.sans-serif'] = 'SimHei'
    #设置正常显示字符
    plt.rcParams['axes.unicode_minus'] = False
    plt.title('sin曲线')
    #设置线条样式
    plt.rcParams['lines.linestyle'] = '-.'
    #设置线条宽度
    plt.rcParams['lines.linewidth'] = 3
    #绘制sin曲线
    plt.plot(x, y, label='$sin(x)$')
     
    plt.savefig('sin.png')
    plt.show()
```

![](https://img.jbzj.com/file_images/article/202101/2021010510111027.png)

参数：

```python

    plt.rcParams['savefig.dpi'] = 300 #图片像素
    plt.rcParams['figure.dpi'] = 300 #分辨率
    plt.savefig(‘plot123_2.png', dpi=200)#指定分辨率
    # 默认的像素：[6.0,4.0]，分辨率为100，图片尺寸为 600&400
    # 指定dpi=200，图片尺寸为 1200*800
    # 指定dpi=300，图片尺寸为 1800*1200
     
     
    plt.rcParams['figure.figsize'] = (8.0, 4.0)    # 图像显示大小
    plt.rcParams['image.interpolation'] = 'nearest' # 最近邻差值: 像素为正方形
    #Interpolation/resampling即插值，是一种图像处理方法，它可以为数码图像增加或减少象素的数目。
     
    plt.rcParams['image.cmap'] = 'gray' # 使用灰度输出而不是彩色输出
     
    plt.axis('off')  #打印图片的时候不显示坐标轴
```

from： [ https://www.jb51.net/article/203481.htm
](https://www.jb51.net/article/203481.htm)

更详细的配置参见： [ https://my.oschina.net/swuly302/blog/94805
](https://my.oschina.net/swuly302/blog/94805)

###  2、matshow函数

这是一个绘制矩阵的函数: ` matplotlib.pyplot.matshow ` ( _A_ , _fignum=None_ , _**kwargs_
)

A是绘制的矩阵，一个矩阵元素对应一个图像像素。

例如： ` plt.matshow(Mat, cmap=plt.cm.gray) ` ，cmap代表一种颜色映射方式。

![](https://img.jbzj.com/file_images/article/202101/2021010510111028.png)

实例：

```python

    plt.plot(A, "r-+", linewidth=2, label="train")
      plt.plot(B, "b-", linewidth=3, label="val")
      plt.legend(loc="upper right", fontsize=14)  # 设置位置
      plt.xlabel("Training set size", fontsize=14) # 标签
      plt.ylabel("RMSE", fontsize=14) 
    plt.axis([0, 80, 0, 3])#表示要显示图形的范围
    plt.xticks(np.arange(0, 81, step=20))#设置刻度
    plt.yticks(np.arange(0, 4, step=1))
```

![](https://img.jbzj.com/file_images/article/202101/2021010510111129.png)

**Axes - Subplot - Axis 之间到底是个什么关系**

用matplotlib.pyplot绘图需要知道以下几个概念：

  * 画图板/画布：这是一个基础载体，类似实际的画图板，用pyplot.figure()函数创建，程序中允许创建多个画图板，具体操作的画板遵循就近原则（操作是在最近一次调用的画图板上实现），缺省条件下内部默认调用pyplot.figure(1)。 
  * 图形区/绘图区：用来绘图的实际区域，一般不直接获取，直接设定方式为pyplot.axes([x, y, w, h])，即axes函数直接确定了该区域在画图板/画布中的位置为x,y 尺寸为w,h 
  * 标签区：用来展示图形相关标签的地方，一般不直接设定（未仔细研究过），该区域根据图形区进行扩展，与该区域有关联的函数是pyplot.xlabel()、pyplot.ylabel()、pyplot.title()等 

```python

    fig = plt.figure() 
    plt.show()
     
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)
```

用画板和画纸来做比喻的话，figure就好像是画板，是画纸的载体， 但是具体画画等操作是在画纸上完成的。
在pyplot中，画纸的概念对应的就是Axes/Subplot。

![](https://img.jbzj.com/file_images/article/202101/2021010510111130.png)

###  对比:

**figure (1) VS figure()**  
figure()操作就是创建或者调用画图板，缺省情况下系统会创建figure(1)作为画图板。使用时遵循就近原则，所有画图操作是在最近一次调用的画图板上实现。

**axes() VS subplot()**  
pyplot.axes([x, y, w,
h])是用来在画图板上确认图形区的位置和大小的函数，x,y表示图形区左下角相对于画图板的坐标，w,h表示图形区的宽高。（缺省时该操作在figure(1)上操作）

pyplot.subplot(abc)本质也是用来确认图形区在画图板上位置大小的函数，区别是该函数将画图板按a行b列等分，然后逐行编号，并选择编号为c的区域作为图形区用来绘图。这是一个axes()操作的高级封装，方便用户使用。subplot(233)表示2行3列的第3个位置（即，第1行第三个区域）

同时，pyplot.show()实际展示的区域是画图板上所有图形区的最小包围区，不是整个画图板，即如果仅仅调用了subplot(224)结果只展示右下角的4号区域，而不是1、2、3、4都展示，因此会存在一定的错觉。

**axes() VS axis()**  
axes([x, y, w, h])用来设定图形区;

axis([x_left, x_right, y_bottom,
y_top])是用来设置所绘制图形的视窗大小的，表示直接展示的图形是需要满足参数中范围的值，直观表现是绘图区实际展示的坐标范围。

注：axis作用的图形区依旧遵守就近原则。

**subplot() VS plot()**  
subplot用来生成图形区;

plot是实际使用的绘图函数，类似的函数还有hist等，plot操作遵守就近原则，即作用在最近一次使用的图形区上。

官网： [ https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html
](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html)

到此这篇关于matplotlib常见函数之plt.rcParams、matshow的使用(坐标轴设置)的文章就介绍到这了,更多相关matplotlib
plt.rcParams、matshow内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

