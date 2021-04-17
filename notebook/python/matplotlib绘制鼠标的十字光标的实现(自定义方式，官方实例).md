matplotlib在widgets模块提供Cursor类用于支持十字光标的生成。另外官方还提供了自定义十字光标的实例。

###  widgets模块Cursor类源码  

```python

    class Cursor(AxesWidget):
      """
      A crosshair cursor that spans the axes and moves with mouse cursor.
    
      For the cursor to remain responsive you must keep a reference to it.
    
      Parameters
      ----------
      ax : `matplotlib.axes.Axes`
        The `~.axes.Axes` to attach the cursor to.
      horizOn : bool, default: True
        Whether to draw the horizontal line.
      vertOn : bool, default: True
        Whether to draw the vertical line.
      useblit : bool, default: False
        Use blitting for faster drawing if supported by the backend.
    
      Other Parameters
      ----------------
      **lineprops
        `.Line2D` properties that control the appearance of the lines.
        See also `~.Axes.axhline`.
    
      Examples
      --------
      See :doc:`/gallery/widgets/cursor`.
      """
    
      def __init__(self, ax, horizOn=True, vertOn=True, useblit=False,
             **lineprops):
        AxesWidget.__init__(self, ax)
    
        self.connect_event('motion_notify_event', self.onmove)
        self.connect_event('draw_event', self.clear)
    
        self.visible = True
        self.horizOn = horizOn
        self.vertOn = vertOn
        self.useblit = useblit and self.canvas.supports_blit
    
        if self.useblit:
          lineprops['animated'] = True
        self.lineh = ax.axhline(ax.get_ybound()[0], visible=False, **lineprops)
        self.linev = ax.axvline(ax.get_xbound()[0], visible=False, **lineprops)
    
        self.background = None
        self.needclear = False
    
      def clear(self, event):
        """Internal event handler to clear the cursor."""
        if self.ignore(event):
          return
        if self.useblit:
          self.background = self.canvas.copy_from_bbox(self.ax.bbox)
        self.linev.set_visible(False)
        self.lineh.set_visible(False)
        
      def onmove(self, event):
        """Internal event handler to draw the cursor when the mouse moves."""
        if self.ignore(event):
          return
        if not self.canvas.widgetlock.available(self):
          return
        if event.inaxes != self.ax:
          self.linev.set_visible(False)
          self.lineh.set_visible(False)
    
          if self.needclear:
            self.canvas.draw()
            self.needclear = False
          return
        self.needclear = True
        if not self.visible:
          return
        self.linev.set_xdata((event.xdata, event.xdata))
    
        self.lineh.set_ydata((event.ydata, event.ydata))
        self.linev.set_visible(self.visible and self.vertOn)
        self.lineh.set_visible(self.visible and self.horizOn)
    
        self._update()
    
      def _update(self):
        if self.useblit:
          if self.background is not None:
            self.canvas.restore_region(self.background)
          self.ax.draw_artist(self.linev)
          self.ax.draw_artist(self.lineh)
          self.canvas.blit(self.ax.bbox)
        else:
          self.canvas.draw_idle()
        return False
```

###  自定义十字光标实现  

简易十字光标实现  

首先在
Cursor类的构造方法__init__中，构造了十字光标的横线、竖线和坐标显示；然后在on_mouse_move方法中，根据事件数据更新横竖线和坐标显示，最后在调用时，通过mpl_connect方法绑定on_mouse_move方法和鼠标移动事件'motion_notify_event'。

```python

    import matplotlib.pyplot as plt
    import numpy as np
    
    
    class Cursor:
      """
      A cross hair cursor.
      """
      def __init__(self, ax):
        self.ax = ax
        self.horizontal_line = ax.axhline(color='k', lw=0.8, ls='--')
        self.vertical_line = ax.axvline(color='k', lw=0.8, ls='--')
        # text location in axes coordinates
        self.text = ax.text(0.72, 0.9, '', transform=ax.transAxes)
    
      def set_cross_hair_visible(self, visible):
        need_redraw = self.horizontal_line.get_visible() != visible
        self.horizontal_line.set_visible(visible)
        self.vertical_line.set_visible(visible)
        self.text.set_visible(visible)
        return need_redraw
    
      def on_mouse_move(self, event):
        if not event.inaxes:
          need_redraw = self.set_cross_hair_visible(False)
          if need_redraw:
            self.ax.figure.canvas.draw()
        else:
          self.set_cross_hair_visible(True)
          x, y = event.xdata, event.ydata
          # update the line positions
          self.horizontal_line.set_ydata(y)
          self.vertical_line.set_xdata(x)
          self.text.set_text('x=%1.2f, y=%1.2f' % (x, y))
          self.ax.figure.canvas.draw()
    
    
    x = np.arange(0, 1, 0.01)
    y = np.sin(2 * 2 * np.pi * x)
    
    fig, ax = plt.subplots()
    ax.set_title('Simple cursor')
    ax.plot(x, y, 'o')
    cursor = Cursor(ax)
    #关键部分，绑定鼠标移动事件处理
    fig.canvas.mpl_connect('motion_notify_event', cursor.on_mouse_move)
    plt.show()
```

###  优化十字光标实现  

在简易实现中，每次鼠标移动时，都会重绘整个图像，这样效率比较低。  
在优化实现中，每次鼠标移动时，只重绘光标和坐标显示，背景图像不再重绘。

```python

    import matplotlib.pyplot as plt
    import numpy as np
    
    
    class BlittedCursor:
      """
      A cross hair cursor using blitting for faster redraw.
      """
      def __init__(self, ax):
        self.ax = ax
        self.background = None
        self.horizontal_line = ax.axhline(color='k', lw=0.8, ls='--')
        self.vertical_line = ax.axvline(color='k', lw=0.8, ls='--')
        # text location in axes coordinates
        self.text = ax.text(0.72, 0.9, '', transform=ax.transAxes)
        self._creating_background = False
        ax.figure.canvas.mpl_connect('draw_event', self.on_draw)
    
      def on_draw(self, event):
        self.create_new_background()
    
      def set_cross_hair_visible(self, visible):
        need_redraw = self.horizontal_line.get_visible() != visible
        self.horizontal_line.set_visible(visible)
        self.vertical_line.set_visible(visible)
        self.text.set_visible(visible)
        return need_redraw
    
      def create_new_background(self):
        if self._creating_background:
          # discard calls triggered from within this function
          return
        self._creating_background = True
        self.set_cross_hair_visible(False)
        self.ax.figure.canvas.draw()
        self.background = self.ax.figure.canvas.copy_from_bbox(self.ax.bbox)
        self.set_cross_hair_visible(True)
        self._creating_background = False
    
      def on_mouse_move(self, event):
        if self.background is None:
          self.create_new_background()
        if not event.inaxes:
          need_redraw = self.set_cross_hair_visible(False)
          if need_redraw:
            self.ax.figure.canvas.restore_region(self.background)
            self.ax.figure.canvas.blit(self.ax.bbox)
        else:
          self.set_cross_hair_visible(True)
          # update the line positions
          x, y = event.xdata, event.ydata
          self.horizontal_line.set_ydata(y)
          self.vertical_line.set_xdata(x)
          self.text.set_text('x=%1.2f, y=%1.2f' % (x, y))
    
          self.ax.figure.canvas.restore_region(self.background)
          self.ax.draw_artist(self.horizontal_line)
          self.ax.draw_artist(self.vertical_line)
          self.ax.draw_artist(self.text)
          self.ax.figure.canvas.blit(self.ax.bbox)
    
    
    x = np.arange(0, 1, 0.01)
    y = np.sin(2 * 2 * np.pi * x)
    
    fig, ax = plt.subplots()
    ax.set_title('Blitted cursor')
    ax.plot(x, y, 'o')
    blitted_cursor = BlittedCursor(ax)
    fig.canvas.mpl_connect('motion_notify_event', blitted_cursor.on_mouse_move)
    plt.show()
```

###  捕捉数据十字光标实现  

在前面的两种实现中，鼠标十字光标可以随意移动。在本实现中，十字光标只会出现在离鼠标x坐标最近的数据点上。

```python

    import matplotlib.pyplot as plt
    import numpy as np
    
    
    class SnappingCursor:
      """
      A cross hair cursor that snaps to the data point of a line, which is
      closest to the *x* position of the cursor.
    
      For simplicity, this assumes that *x* values of the data are sorted.
      """
      def __init__(self, ax, line):
        self.ax = ax
        self.horizontal_line = ax.axhline(color='k', lw=0.8, ls='--')
        self.vertical_line = ax.axvline(color='k', lw=0.8, ls='--')
        self.x, self.y = line.get_data()
        self._last_index = None
        # text location in axes coords
        self.text = ax.text(0.72, 0.9, '', transform=ax.transAxes)
    
      def set_cross_hair_visible(self, visible):
        need_redraw = self.horizontal_line.get_visible() != visible
        self.horizontal_line.set_visible(visible)
        self.vertical_line.set_visible(visible)
        self.text.set_visible(visible)
        return need_redraw
    
      def on_mouse_move(self, event):
        if not event.inaxes:
          self._last_index = None
          need_redraw = self.set_cross_hair_visible(False)
          if need_redraw:
            self.ax.figure.canvas.draw()
        else:
          self.set_cross_hair_visible(True)
          x, y = event.xdata, event.ydata
          index = min(np.searchsorted(self.x, x), len(self.x) - 1)
          if index == self._last_index:
            return # still on the same data point. Nothing to do.
          self._last_index = index
          x = self.x[index]
          y = self.y[index]
          # update the line positions
          self.horizontal_line.set_ydata(y)
          self.vertical_line.set_xdata(x)
          self.text.set_text('x=%1.2f, y=%1.2f' % (x, y))
          self.ax.figure.canvas.draw()
    
    
    x = np.arange(0, 1, 0.01)
    y = np.sin(2 * 2 * np.pi * x)
    
    fig, ax = plt.subplots()
    ax.set_title('Snapping cursor')
    line, = ax.plot(x, y, 'o')
    snap_cursor = SnappingCursor(ax, line)
    fig.canvas.mpl_connect('motion_notify_event', snap_cursor.on_mouse_move)
    plt.show()
    
    
```

###  参考资料  

[ https://www.matplotlib.org.cn/gallery/misc/cursor_demo_sgskip.html
](https://www.matplotlib.org.cn/gallery/misc/cursor_demo_sgskip.html)

到此这篇关于matplotlib绘制鼠标的十字光标的实现(自定义方式，官方实例)的文章就介绍到这了,更多相关matplotlib鼠标十字光标
内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

