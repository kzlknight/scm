##  需求  

> 在画布上用鼠标画图，可以画圆或矩形，按m键在两种模式下切换。左键按下时开始画图，移动到哪儿画到哪儿，左键释放时结束画图。

##  实现思想  

> 用鼠标画图：需要定义鼠标的回调函数mouse_event  
>  画圆或矩形：需要定义一个画图的模式mode  
>  左键单击、移动、释放：需要捕获三个不同的事件  
>  开始画图，结束画图：需要定义一个画图的标记位drawing

##  实现代码

```python

    import cv2 as cv
    import numpy as np
    
    drawing = False # 是否开始画图
    mode = True # True：画矩形，False：画圆
    start = (-1, -1)
    
    # 鼠标的回调函数的参数格式是固定的，不要随意更改。
    def mouse_event(event, x, y, flags, param):
      global start, drawing, mode
    
      # 左键按下：开始画图
      if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        start = (x, y)
      # 鼠标移动，画图
      elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
          if mode:
            cv.rectangle(img, start, (x, y), (0, 255, 0), -1)
          else:
            cv.circle(img, (x, y), 5, (0, 0, 255), -1)
      # 左键释放：结束画图
      elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode:
          cv.rectangle(img, start, (x, y), (0, 255, 0), -1)
        else:
          cv.circle(img, (x, y), 5, (0, 0, 255), -1)
    
    
    img = np.zeros((512, 512, 3), np.uint8)
    cv.namedWindow('image')
    cv.setMouseCallback('image', mouse_event)
    
    while(True):
      cv.imshow('image', img)
      # 按下m切换模式
      if cv.waitKey(1) == ord('m'):
        mode = not mode
      # 按ESC键退出程序
      elif cv.waitKey(1) == 27:
        break
```

##  实验结果

![](https://img.jbzj.com/file_images/article/202012/2020121195859922.png?202011119597)

以上就是python 基于opencv 实现一个鼠标绘图小程序的详细内容，更多关于python 鼠标绘图的资料请关注脚本之家其它相关文章！

