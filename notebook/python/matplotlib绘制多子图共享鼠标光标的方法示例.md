` matplotlib ` 官方除了提供了鼠标十字光标的示例，还提供了同一图像内多子图共享光标的示例，其功能主要由 ` widgets ` 模块中的 `
MultiCursor ` 类提供支持。

` MultiCursor ` 类与 ` Cursor ` 类参数类似，差异主要在：

  * ` Cursor ` 类参数只有一个 ` ax ` ，即需要显示光标的子图； ` MultiCursor ` 类参数为 ` canvas ` 和 ` axes ` ，其中 ` axes ` 为需要共享光标的子图列表。 
  * ` Cursor ` 类中，光标默认是十字线； ` MultiCursor ` 类中，光标默认为竖线。 

官方示例

```python

    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.widgets import MultiCursor
    
    t = np.arange(0.0, 2.0, 0.01)
    s1 = np.sin(2*np.pi*t)
    s2 = np.sin(4*np.pi*t)
    
    fig, (ax1, ax2) = plt.subplots(2, sharex=True)
    ax1.plot(t, s1)
    ax2.plot(t, s2)
    
    multi = MultiCursor(fig.canvas, (ax1, ax2), color='r', lw=1)
    plt.show()
```

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010811463716.png)

简易修改版

```python

    multi = MultiCursor(fig.canvas, (ax1, ax2), color='r', lw=1, horizOn=True, vertOn=True)
```

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010811463717.png)

` MultiCursor ` 类源码

```python

    class MultiCursor(Widget):
      """
      Provide a vertical (default) and/or horizontal line cursor shared between
      multiple axes.
    
      For the cursor to remain responsive you must keep a reference to it.
    
      Example usage::
    
        from matplotlib.widgets import MultiCursor
        import matplotlib.pyplot as plt
        import numpy as np
    
        fig, (ax1, ax2) = plt.subplots(nrows=2, sharex=True)
        t = np.arange(0.0, 2.0, 0.01)
        ax1.plot(t, np.sin(2*np.pi*t))
        ax2.plot(t, np.sin(4*np.pi*t))
    
        multi = MultiCursor(fig.canvas, (ax1, ax2), color='r', lw=1,
                  horizOn=False, vertOn=True)
        plt.show()
    
      """
      def __init__(self, canvas, axes, useblit=True, horizOn=False, vertOn=True,
             **lineprops):
    
        self.canvas = canvas
        self.axes = axes
        self.horizOn = horizOn
        self.vertOn = vertOn
    
        xmin, xmax = axes[-1].get_xlim()
        ymin, ymax = axes[-1].get_ylim()
        xmid = 0.5 * (xmin + xmax)
        ymid = 0.5 * (ymin + ymax)
    
        self.visible = True
        self.useblit = useblit and self.canvas.supports_blit
        self.background = None
        self.needclear = False
    
        if self.useblit:
          lineprops['animated'] = True
    
        if vertOn:
          self.vlines = [ax.axvline(xmid, visible=False, **lineprops)
                  for ax in axes]
        else:
          self.vlines = []
    
        if horizOn:
          self.hlines = [ax.axhline(ymid, visible=False, **lineprops)
                  for ax in axes]
        else:
          self.hlines = []
    
        self.connect()
        
      def connect(self):
        """Connect events."""
        self._cidmotion = self.canvas.mpl_connect('motion_notify_event',
                             self.onmove)
        self._ciddraw = self.canvas.mpl_connect('draw_event', self.clear)
    
      def disconnect(self):
        """Disconnect events."""
        self.canvas.mpl_disconnect(self._cidmotion)
        self.canvas.mpl_disconnect(self._ciddraw)
    
      def clear(self, event):
        """Clear the cursor."""
        if self.ignore(event):
          return
        if self.useblit:
          self.background = (
            self.canvas.copy_from_bbox(self.canvas.figure.bbox))
        for line in self.vlines + self.hlines:
          line.set_visible(False)
    
      def onmove(self, event):
        if self.ignore(event):
          return
        if event.inaxes is None:
          return
        if not self.canvas.widgetlock.available(self):
          return
        self.needclear = True
        if not self.visible:
          return
        if self.vertOn:
          for line in self.vlines:
            line.set_xdata((event.xdata, event.xdata))
            line.set_visible(self.visible)
        if self.horizOn:
          for line in self.hlines:
            line.set_ydata((event.ydata, event.ydata))
            line.set_visible(self.visible)
        self._update()
    
    
      def _update(self):
        if self.useblit:
          if self.background is not None:
            self.canvas.restore_region(self.background)
          if self.vertOn:
            for ax, line in zip(self.axes, self.vlines):
              ax.draw_artist(line)
          if self.horizOn:
            for ax, line in zip(self.axes, self.hlines):
              ax.draw_artist(line)
          self.canvas.blit()
        else:
          self.canvas.draw_idle()
```

到此这篇关于matplotlib绘制多子图共享鼠标光标的方法示例的文章就介绍到这了,更多相关matplotlib
多子图鼠标光标内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

