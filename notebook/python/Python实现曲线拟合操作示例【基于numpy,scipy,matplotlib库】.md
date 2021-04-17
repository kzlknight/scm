本文实例讲述了Python实现曲线拟合操作。分享给大家供大家参考，具体如下：

这两天学习了用python来拟合曲线。

##  一、环境配置

本人比较比较懒，所以下载的全部是exe文件来安装，安装按照顺利来安装。自动会找到python的安装路径，一直点下一步就行。还有其他的两种安装方式：一种是解压，一种是pip。我没有尝试，就不乱说八道了。

没有ArcGIS 环境的，可以不看下面这段话了。

在配置环境时遇见一个小波折，就是原先电脑装过ArcGIS10.2
,所以其会默认安装python2.7，而且python是32位的。且其目录为C:\Python27\ArcGIS10.2，所以引用环境变量时，要注意。并且在其引用的工具包中本身包含numpy，matplotlib的包。还是很方便的。但是因为之前想用PyQT来做曲线拟合的界面，安装QT时总是失败，所以最后放弃使用这个。在安装新的python时注意要把路径写到上面这个路径前面，意思就是说在安装上面的包的时候会找默认python路径。我新安装python路径为C:\Python2，要不然就会找到ArcGIS那个python包路径下了。

**1. 安装包**

> python2.7 (32位)https://www.python.org/downloads/  
>  numpy-1.8.1-win32-superpack-python2.7  
>  scipy-0.15.1-win32-superpack-python2.7  
>  matplotlib-1.3.1.win32-py2.7

**安装过程中遇见的问题**

提示

numpy是Python的一种开源的数值计算扩展，数学计算很方便。  
scipy是一款方便、易于使用、专为科学和工程设计的Python工具包.它包括统计,优化,整合,线性代数模块,傅里叶变换,信号和图像处理,常微分方程求解器等等.这次还没用到，看介绍很强大，是numpy的升级版。

matplotlib是Python的一种开源的扩展可以绘制各种各种的图表。

##  二、实例

曲线拟合的例子

```python

    import matplotlib.pyplot as plt
    import math
    import numpy as np
    import random
    import csv
    plt.rcParams['font.sans-serif'] = ['SimHei']#设置显示中文
    fig = plt.figure()
    ax = fig.add_subplot(111)#将画布分割成1行1列，图像画在从左到右从上到下的第1块
    #阶数为6阶
    order=6
    #生成曲线上的各个点
    dataMat = np.loadtxt(open("c:\\yandu.csv","rb"),delimiter=",",skiprows=0)
    size=dataMat.shape
    num=size[0]
    trandata=np.transpose(dataMat)#矩阵转置
    xa=trandata[0]#得到天数数组（横坐标）
    ya=trandata[1]#实测盐度值数组
    #数据筛选,去除盐度值为零的，提高拟合精度
    i=0
    x=[]
    y=[]
    for yy in ya:
      if yy>0:
        xx=xa[i]
        i+=1
        x.append(xx)
        y.append(yy)
    #绘制原始数据
    ax.plot(x,y,label=u'原始数据',color='m',linestyle='',marker='.')
    #计算多项式
    c=np.polyfit(x,y,order)#拟合多项式的系数存储在数组c中
    yy=np.polyval(c,x)#根据多项式求函数值
    #进行曲线绘制
    x_new=np.linspace(0, 365, 2000)
    f_liner=np.polyval(c,x_new)
    #ax.plot(x,y,color='m',linestyle='',marker='.')
    ax.plot(x_new,f_liner,label=u'拟合多项式曲线',color='g',linestyle='-',marker='')
    # labels标签设置
    ax.set_xlim(0, 366)
    ax.set_xlabel(u'天')
    ax.set_ylabel(u'盐度')
    ax.set_title(u'盐度的日变化', bbox={'facecolor':'0.8', 'pad':5})
    ax.legend()
    plt.show()
    
    
```

运行结果：

![](https://img.jbzj.com/file_images/article/201807/2018712103733658.jpg?2018612104140)

**PS：这里再为大家推荐两款相似的在线工具供大家参考：**

**在线多项式曲线及曲线函数拟合工具：  
** [ http://tools.jb51.net/jisuanqi/create_fun
](http://tools.jb51.net/jisuanqi/create_fun)

**在线绘制多项式/函数曲线图形工具：  
** [ http://tools.jb51.net/jisuanqi/fun_draw
](http://tools.jb51.net/jisuanqi/fun_draw)

更多关于Python相关内容感兴趣的读者可查看本站专题：《 [ Python数学运算技巧总结
](//www.jb51.net/Special/942.htm) 》、《 [ Python数据结构与算法教程
](//www.jb51.net/Special/663.htm) 》、《 [ Python函数使用技巧总结
](//www.jb51.net/Special/642.htm) 》、《 [ Python字符串操作技巧汇总
](//www.jb51.net/Special/636.htm) 》及《 [ Python入门与进阶经典教程
](//www.jb51.net/Special/520.htm) 》

希望本文所述对大家Python程序设计有所帮助。

