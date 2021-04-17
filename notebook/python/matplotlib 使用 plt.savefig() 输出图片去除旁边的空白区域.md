最近在作图时需要将输出的图片紧密排布，还要去掉坐标轴，同时设置输出图片大小。  

要让程序自动将图表保存到文件中，代码为：  

```python

    plt.savefig('squares_plot.png', bbox_inches='tight')
    
```

  * 第一个实参指定要以什么样的文件名保存图表，这个文件将存储到scatter_squares.py所在的目录中。   

  * 第二个实参指定将图表多余的空白区域裁减掉。如果要保留图表周围多余的空白区域，可省略这个实参。   

但是发现matplotlib使用plt.savefig()保存的图片

周围有一圈空白。那么如何去掉该空白呢？

首先，关闭坐标轴显示：

```python

    plt.axis('off')
    
```

但是，这样只是关闭显示而已，透明的坐标轴仍然会占据左下角位置，导致输出的图片偏右。  
要想完全去掉坐标轴，需要改为以下代码：

```python

    plt.axis('off')
    fig = plt.gcf()
    fig.set_size_inches(7.0/3,7.0/3) #dpi = 300, output = 700*700 pixels
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
    plt.margins(0,0)
    fig.savefig(out_png_path, format='png', transparent=True, dpi=300, pad_inches = 0)
    
```

即可完成去掉空白。

注：如果不采用 subplot_adjust + margin(0,0)，而是在fig.savefig()的参数中添加bbox_inches =
'tight'，也可以达到

去除空白的效果； 但是，这样会导致对图片输出大小的设置失效。  

到此这篇关于matplotlib 使用 plt.savefig() 输出图片去除旁边的空白区域的文章就介绍到这了,更多相关matplotlib
plt.savefig() 内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

