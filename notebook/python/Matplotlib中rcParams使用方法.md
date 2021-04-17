主要作用为指定图片像素：

```python

    matplotlib.rcParams[‘figure.figsize']#图片像素 
    matplotlib.rcParams[‘savefig.dpi']#分辨率 
    plt.savefig(‘plot123_2.png', dpi=200)#指定分辨率
```

```python

    %matplotlib inline
    import matplotlib # 注意这个也要import一次
    import matplotlib.pyplot as plt
    from IPython.core.pylabtools import figsize # import figsize
    #figsize(12.5, 4) # 设置 figsize
    plt.rcParams['savefig.dpi'] = 300 #图片像素
    plt.rcParams['figure.dpi'] = 300 #分辨率
    # 默认的像素：[6.0,4.0]，分辨率为100，图片尺寸为 600&400
    # 指定dpi=200，图片尺寸为 1200*800
    # 指定dpi=300，图片尺寸为 1800*1200
    # 设置figsize可以在不改变分辨率情况下改变比例
    
    myfont = matplotlib.font_manager.FontProperties(fname=r'C:/Windows/Fonts/msyh.ttf') # 这一行
    plt.plot((1,2,3),(4,3,-1))
    plt.xlabel(u'横坐标', fontproperties=myfont) # 这一段
    plt.ylabel(u'纵坐标', fontproperties=myfont) # 这一段
    #plt.show()
    plt.savefig('plot123_2.png', dpi=300) #指定分辨率保存
```

![这里写图片描述](https://img.jbzj.com/file_images/article/202101/2021010510133931.png)

一样的图片，像素大就更加高清了。

Matplotlib中plt.rcParams用法（设置图像细节）

```python

    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.colors import ListedColormap
    %matplotlib inline  
    
    # 生成数据
    x = np.linspace(0, 4*np.pi)
    y = np.sin(x)
    
    plt.rcParams['figure.figsize'] = (5.0, 4.0)   # 显示图像的最大范围
    plt.rcParams['image.interpolation'] = 'nearest' # 差值方式，设置 interpolation style
    plt.rcParams['image.cmap'] = 'gray'       # 灰度空间
    
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
     
    # plt.savefig('sin.png')
    # plt.show()
    
    
    x=np.array([1,2])
    y=np.array([1,4])
    z=np.array([[1,2], [3, 4]])
    plt.xlim(1,2)
    plt.ylim(1,4)
    
    plt.contourf(x, y, z, alpha=0.6)  
```

到此这篇关于Matplotlib中rcParams使用方法的文章就介绍到这了,更多相关Matplotlib
rcParams使用内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

