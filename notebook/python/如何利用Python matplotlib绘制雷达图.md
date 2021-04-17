本篇文章介绍使用matplotlib绘制雷达图。

雷达图也被称为网络图，蜘蛛图，星图，蜘蛛网图，是一个不规则的多边形。雷达图可以形象地展示相同事物的多维指标，雷达图几乎随处可见，应用场景非常多。

###  一、matplotlib绘制圆形雷达图

```python

    # coding=utf-8
    import numpy as np
    import matplotlib.pyplot as plt
     
     
    results = [{"大学英语": 87, "高等数学": 79, "体育": 95, "计算机基础": 92, "程序设计": 85},
       {"大学英语": 80, "高等数学": 90, "体育": 91, "计算机基础": 85, "程序设计": 88}]
    data_length = len(results[0])
    # 将极坐标根据数据长度进行等分
    angles = np.linspace(0, 2*np.pi, data_length, endpoint=False)
    labels = [key for key in results[0].keys()]
    score = [[v for v in result.values()] for result in results]
    # 使雷达图数据封闭
    score_a = np.concatenate((score[0], [score[0][0]]))
    score_b = np.concatenate((score[1], [score[1][0]]))
    angles = np.concatenate((angles, [angles[0]]))
    labels = np.concatenate((labels, [labels[0]]))
    # 设置图形的大小
    fig = plt.figure(figsize=(8, 6), dpi=100)
    # 新建一个子图
    ax = plt.subplot(111, polar=True)
    # 绘制雷达图
    ax.plot(angles, score_a, color='g')
    ax.plot(angles, score_b, color='b')
    # 设置雷达图中每一项的标签显示
    ax.set_thetagrids(angles*180/np.pi, labels)
    # 设置雷达图的0度起始位置
    ax.set_theta_zero_location('N')
    # 设置雷达图的坐标刻度范围
    ax.set_rlim(0, 100)
    # 设置雷达图的坐标值显示角度，相对于起始角度的偏移量
    ax.set_rlabel_position(270)
    ax.set_title("计算机专业大一（上）")
    plt.legend(["弓长张", "口天吴"], loc='best')
    plt.show()
```

运行结果：

![](https://img.jbzj.com/file_images/article/202012/20201221143840012.png?20201121143855)

绘制雷达图需要先建立极坐标系，关于极坐标系可以自己了解一下。建立好极坐标后可以在极坐标中绘制折线图、柱状图等，大部分情况，都是用折线图，形成一个不规则的闭合多边形。本文中用某高校大一的期末考试成绩作为例子来演示雷达图的效果。

linspace():
用于将极坐标根据数据的维度进行等分，第一个参数传入起始角度，第二参数传入结束角度，第三个参数传入分成多少等份。其他参数根据需要传入，如endpoint默认为True，最后一个数据处于结束的角度，根据本例中前面的参数0~2π，应该设置为False，否则最后一个数据与第一个数据角度重叠了。

concatenate():
使雷达图的数据是环形封闭的，concatenate()函数的第一个参数是一个元组，元组中的每个元素是一个数组，concatenate()函数将这些数组连接到一起，组成一个新的数组。要让绘制的雷达图封闭，将数据的第一个值连接到数据的结尾即可。

本文用折线图plot()来绘制雷达图，使用figure()函数设置好图形的大小和清晰度，然后使用subplot()函数来创建一张子图。subplot()函数的第一个参数传入长度为3的数字，第一个数字表示将画布分成几行，第二个数字表示将画布分成几列，第三个数字表示当前的子图处于哪个位置(按从左至右、从上到下的顺序排序)，第三个数字不能超出前两个数字切分的子图数范围。如111表示将画布分成一行一列(只有一张子图)，当前的子图处于第一张子图中。在subplot()函数中，将polar参数设置True，得到的图形才是极坐标。

极坐标系设置完成后，使用子图对象ax调用折线图函数plot()，即可绘出雷达图。如果有多组数据，多次调用plot()函数即可。

使用set_thetagrids()函数设置雷达图中每个维度的标签和显示位置。使用set_theta_zero_location()函数设置雷达图的0度位置，可以传入"N"、"NW"、"W"、"SW"、"S"、"SE"、"E"、"NE"八个方位缩写。使用set_rlim()函数设置极坐标上的刻度范围。使用set_rlabel_position()函数设置极坐标上的刻度标签显示位置，传入一个相对于雷达图0度的角度值。当然还可以根据需要设置其他属性，如标题、图例等。

在上面的例子中，将两位同学的考试成绩绘制成了雷达图，通过雷达图，可以看出两个人的单科成绩互有高低，而整体来看，两位同学成绩都很优秀。上面的雷达图中，网格线都是圆形的，而用折线图连接的雷达图两个维度之间是直接连接的，所以将网格线换成多边形会更合理一点。

###  二、matplotlib绘制多边形雷达图

```python

    import numpy as np
    import matplotlib.pyplot as plt
     
     
    results = [{"大学英语": 87, "高等数学": 79, "体育": 95, "计算机基础": 92, "程序设计": 85},
       {"大学英语": 80, "高等数学": 90, "体育": 91, "计算机基础": 85, "程序设计": 88}]
    data_length = len(results[0])
    angles = np.linspace(0, 2*np.pi, data_length, endpoint=False)
    labels = [key for key in results[0].keys()]
    score = [[v for v in result.values()] for result in results]
    score_a = np.concatenate((score[0], [score[0][0]]))
    score_b = np.concatenate((score[1], [score[1][0]]))
    angles = np.concatenate((angles, [angles[0]]))
    labels = np.concatenate((labels, [labels[0]]))
    fig = plt.figure(figsize=(10, 6), dpi=100)
    fig.suptitle("计算机专业大一（上）")
    ax1 = plt.subplot(121, polar=True)
    ax2 = plt.subplot(122, polar=True)
    ax, data, name = [ax1, ax2], [score_a, score_b], ["弓长张", "口天吴"]
    for i in range(2):
     for j in np.arange(0, 100+20, 20):
      ax[i].plot(angles, 6*[j], '-.', lw=0.5, color='black')
     for j in range(5):
      ax[i].plot([angles[j], angles[j]], [0, 100], '-.', lw=0.5, color='black')
     ax[i].plot(angles, data[i], color='b')
     # 隐藏最外圈的圆
     ax[i].spines['polar'].set_visible(False)
     # 隐藏圆形网格线
     ax[i].grid(False)
     for a, b in zip(angles, data[i]):
      ax[i].text(a, b+5, '%.00f' % b, ha='center', va='center', fontsize=12, color='b')
     ax[i].set_thetagrids(angles*180/np.pi, labels)
     ax[i].set_theta_zero_location('N')
     ax[i].set_rlim(0, 100)
     ax[i].set_rlabel_position(0)
     ax[i].set_title(name[i])
    plt.show()
```

运行结果：

![](https://img.jbzj.com/file_images/article/202012/20201221143930900.png?20201121143936)

在极坐标系中，极径值相等的点在一个圆上，所以绘制的雷达图中，网格线默认都是圆形的。如果要绘制多边形的雷达图，则需要将圆形的网格线隐藏，然后根据刻度范围绘制出多边形的网格线。

首先使用plot()函数，根据刻度范围，绘制出同心的多个多边形和多个维度方向的极轴，作为雷达图的网格线，形成一张“网”。

链式调用极坐标的spines['polar'].set_visible()函数，传入参数False，将极坐标系最外圈的圆形隐藏。调用grid()函数，传入参数False，将极坐标系中的的圆形网格线隐藏。

修改完网格线后，即可达到多边形的效果。在第二次绘制雷达图时，将两位同学的成绩分到两张不同的雷达图中，并用text()设置了每个维度的数据标注，使用suptitle()函数来设置整张图形的标题。

上面的两次绘图，将两位同学的成绩绘制在同一张雷达图时，更方便对比两位同学的成绩，如比较谁更全面、更优秀。分开绘制时，更方便分析个人的成绩情况，如是否偏科。而相对于圆形的雷达图，在多边形的雷达图中，不会出现雷达图与网格线的不合理交叉(雷达图与网格线交叉两次)，使用多边形网格线更合理。

到此这篇关于如何利用Python matplotlib绘制雷达图的文章就介绍到这了,更多相关Python
matplotlib绘制雷达图内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

