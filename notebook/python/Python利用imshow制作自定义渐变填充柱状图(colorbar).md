###  目的

在各种各样的理论计算中，常常需要绘制各种填充图，绘制完后需要加渐变填充的colorbar。可是有些软件如VMD，colorbar渲染后颜色分布有些失真，不能较准确的表达各颜色对应的数值。用ps中的渐变填充可以解决该问题，但很多电脑配置较低，不能很好的运行ps。Python也可以直接绘制colorbar，填充颜色就好。如cmap中的bwr渐变本人就比较常用。然而，有时候颜色范围是负数范围多于正数范围（如：colorbar需要表示
[-60，40]这段，蓝色表示负数，红色表示正数，白色应该在colorbar由下往上60%处），bwr渐变将white置于50%处显得不够合理，因此需要自定义填充。本文以imshow()
函数来进行填充柱状图达到自定义colorbar的目的。interpolation=‘bicubic' 可以很好的做出渐变效果。

代码

```python

    # -*- coding: utf-8 -*-
    """
    Created on Wed Dec 9 10:36:54 2020
    
    @author: fya
    """
    
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.colors import ListedColormap,LinearSegmentedColormap
    import matplotlib as mpl
    
    fig, ax = plt.subplots(dpi=96)
    ax.set(xlim=(1,10), ylim=(-0.1,101), autoscale_on=False) #创建图像范围
    
    a = np.array([[1, 1],
           [2, 2],
           [3, 3],
           [4, 4],
           [5, 5]]) #每种渐变色分成五段（array五行），数字表示在colormap对应的深浅
    print(a.shape)
    
    clist=['white','blue'] #线性变化颜色由上面array值 小到大，越小，越白，达到上白下蓝的渐变效果
    clist2=['red','white'] #渐变色2，用于白色到红色填充，array越小，越红，达到上红下白的效果
    newcmp = LinearSegmentedColormap.from_list('chaos',clist)
    newcmp2 = LinearSegmentedColormap.from_list('chaos',clist2)
    
    
    plt.imshow(a,cmap=newcmp,interpolation='bicubic',extent=(1,10,0,60))#60%都是蓝色到白色渐变
    plt.imshow(a,cmap=newcmp2,interpolation='bicubic',extent=(1,10,60,100)) #白色设置在60%处
    
    frame = plt.gca() #读取当前图层
    ax.yaxis.tick_right() #纵坐标移到右边
    ax.set_yticklabels(('-80','-60','-40','-20','0','20','40')) #自定义yticks显示的值，第一个label不显示
    frame.spines['top'].set_visible(False) #上框线不显示
    frame.spines['bottom'].set_visible(False)
    frame.spines['right'].set_visible(False)
    frame.spines['left'].set_visible(False)
    plt.xticks([]) #x坐标不要
    
    
    plt.show()
    fig.savefig('colorbar.tif',dpi=600,format='tif')
    print('Done!')
    
    #N = 10
    #x = np.arange(N) + 0.15
    #y = np.random.rand(N)
    
    #width = 0.4
    #for x, y in zip(x, y):
      #ax.imshow(a, interpolation='bicubic', extent=(x, x+width, 0, y), cmap=plt.cm.Blues_r)
    
    #ax.set_aspect('auto')
    #plt.show()
```

代码2，渐变色分100段

```python

    # -*- coding: utf-8 -*-
    """
    Created on Wed Dec 9 10:36:54 2020
    
    @author: fanyiang
    """
    
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.colors import ListedColormap,LinearSegmentedColormap
    import matplotlib as mpl
    import pandas as pd
    import os
    
    fig, ax = plt.subplots(dpi=96)
    ax.set(xlim=(1,10), ylim=(-0.1,101), autoscale_on=False)
    
    #a = np.array([[1, 1],
           #[2, 2],
           #[3, 3],
           #[4, 4],
           #[5, 5]]) #每种渐变色分成五段（array五行），数字表示在colormap对应的深浅
    avalue=locals() 
    dfvalue=locals()      
    for i in range(1,101):
      avalue['a'+str(i)]=np.array([[i,i]]) #渐变色分为100段，分的更细
      dfvalue['df'+str(i)]=pd.DataFrame(avalue['a'+str(i)]) #转dataframe
      df=dfvalue['df'+str(i)]
      df.to_csv("temp.csv", mode='a',header=None) #暂存csv文件，第一列会把每一次循环的index放进去
    df3=pd.read_csv('temp.csv',header=None)#读取csv
    df3.columns=['序号','x','y']#column命名，第一列废弃
    df3=df3.drop('序号',axis=1)#删除第一列
    a=np.array(df3) #转array
    print(df3.head())
    
                                                                          
                                                                      
    #a=np.vstack((a1,a2,a3,a4,a5,a6,a7,a8,a9,a10))
    
    print(a)
    
    clist=['white','blue'] #线性变化颜色由上面array值 小到大
    clist2=['red','white']
    newcmp = LinearSegmentedColormap.from_list('chaos',clist)
    newcmp2 = LinearSegmentedColormap.from_list('chaos',clist2)
    
    
    plt.imshow(a,cmap=newcmp,interpolation='bicubic',extent=(1,10,0,60))
    plt.imshow(a,cmap=newcmp2,interpolation='bicubic',extent=(1,10,60,100)) #白色设置在60%处
    
    frame = plt.gca() #读取当前图层
    ax.yaxis.tick_right() #纵坐标移到右边
    ax.set_yticklabels(('-80','-60','-40','-20','0','20','40')) #自定义yticks显示的值，第一个label不显示
    frame.spines['top'].set_visible(False) #上框线不显示
    frame.spines['bottom'].set_visible(False)
    frame.spines['right'].set_visible(False)
    frame.spines['left'].set_visible(False)
    plt.xticks([]) #x坐标不要
    
    
    plt.show()
    fig.savefig('colorbar.tif',dpi=600,format='tif')
    os.remove("temp.csv") #删除临时的csv文件
    print('Done!')
    
    #N = 10
    #x = np.arange(N) + 0.15
    #y = np.random.rand(N)
    
    #width = 0.4
    #for x, y in zip(x, y):
      #ax.imshow(a, interpolation='bicubic', extent=(x, x+width, 0, y), cmap=plt.cm.Blues_r)
    
    #ax.set_aspect('auto')
    #plt.show()
```

###  效果

效果1

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020121011471499.png)

效果2

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/20201210114714100.png)

到此这篇关于Python利用imshow制作自定义渐变填充柱状图(colorbar)的文章就介绍到这了,更多相关Python
渐变填充柱状图内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

