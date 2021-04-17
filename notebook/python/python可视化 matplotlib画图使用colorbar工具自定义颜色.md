python matplotlib画图使用colorbar工具自定义颜色 colorbar（draw colorbar without any
mapple/plot）

自定义colorbar可以画出任何自己想要的colorbar，自由自在、不受约束，不依赖于任何已有的图(plot/mappable)。这里使用的是mpl.colorbar.ColorbarBase类，而colorbar类必须依赖于已有的图。

参数可以参考下面的描述-> [ matplotlib
](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.colorbar.html) ：

> class matplotlib.colorbar.ColorbarBase(ax, cmap=None, norm=None, alpha=None,
> values=None, boundaries=None, orientation=‘vertical', ticklocation=‘auto',
> extend=‘neither', spacing=‘uniform', ticks=None, format=None,
> drawedges=False, filled=True, extendfrac=None, extendrect=False,
> label='')[source]  
>

参数简单描述

  * ax :可用于设置colorbar的位置、长、宽 
  * 

