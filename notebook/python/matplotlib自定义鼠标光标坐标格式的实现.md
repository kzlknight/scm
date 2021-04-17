` matplotlib ` 默认在图像Windows窗口中显示当前鼠标光标所在位置的坐标，格式为 ` x=xx, y=xx ` 。  

鼠标光标的坐标格式由子图模块 ` Axes ` 中的 ` format_coord ` 函数控制。  

通过重写 ` format_coord ` 函数即可实现坐标的自定义格式。  

注意：调用 ` format_coord ` 函数的对象是子图对象，常见的错误主要在没有正确的获取当前子图对象。  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010810140014.png)

` format_coord ` 函数源码

```python

    matplotlib.axes.Axes.format_coord
    
    def format_coord(self, x, y):
      """Return a format string formatting the *x*, *y* coordinates."""
      if x is None:
        xs = '???'
      else:
        xs = self.format_xdata(x)
      if y is None:
        ys = '???'
      else:
        ys = self.format_ydata(y)
      return 'x=%s y=%s' % (xs, ys)
```

自定义坐标格式实现

```python

    import matplotlib.pyplot as plt
    
    def format_coord(x, y):
      return 'x坐标为%1.4f, y坐标为%1.4f' % (x, y)
    #获取当前子图
    ax=plt.gca()
    ax.format_coord = format_coord
    plt.show()
```

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010810140015.png)

到此这篇关于matplotlib自定义鼠标光标坐标格式的实现的文章就介绍到这了,更多相关matplotlib自定义鼠标光标坐标内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

