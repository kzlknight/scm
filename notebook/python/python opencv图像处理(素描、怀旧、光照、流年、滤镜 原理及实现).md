##  **图像素描特效  
**

图像素描特效主要经过以下几个步骤：

调用cv.cvtColor()函数将彩色图像灰度化处理；  
通过cv.GaussianBlur()函数实现高斯滤波降噪；  
边缘检测采用Canny算子实现；  
最后通过cv.threshold()反二进制阈值化处理实现素描特效。

```python

    #coding:utf-8
    import cv2 as cv
    import numpy as np
    
    #读取原始图像
    img = cv.imread('d:/paojie.png')
    
    #图像灰度处理
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    
    #高斯滤波降噪
    gaussian = cv.GaussianBlur(gray, (5,5), 0)
     
    #Canny算子
    canny = cv.Canny(gaussian, 50, 150)
    
    #阈值化处理
    ret, result = cv.threshold(canny, 0, 255, cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
    
    #显示图像
    #cv.imshow('src', img)
    #cv.imshow('result', result)
    cv.imshow('result',np.vstack((gray,result)))
    cv.waitKey()
    cv.destroyAllWindows()
```

###  图像素描特效展示

![](https://img.jbzj.com/file_images/article/202012/20201210163057158.png?2020111016316)

**图像怀旧特效**

怀旧特效是将图像的RGB三个分量分别按照一定比例进行处理的结果，其怀旧公式如下所示：

![](https://img.jbzj.com/file_images/article/202012/20201210163125887.png?20201110163133)

```python

    #coding:utf-8
    import cv2 as cv
    import numpy as np
    
    #读取原始图像
    img = cv.imread('d:/paojie.png')
    
    #获取图像行和列
    rows, cols = img.shape[:2]
    
    #新建目标图像
    dst = np.zeros((rows, cols, 3), dtype="uint8")
    
    #图像怀旧特效
    for i in range(rows):
      for j in range(cols):
        B = 0.272*img[i,j][2] + 0.534*img[i,j][1] + 0.131*img[i,j][0]
        G = 0.349*img[i,j][2] + 0.686*img[i,j][1] + 0.168*img[i,j][0]
        R = 0.393*img[i,j][2] + 0.769*img[i,j][1] + 0.189*img[i,j][0]
        if B>255:
          B = 255
        if G>255:
          G = 255
        if R>255:
          R = 255
        dst[i,j] = np.uint8((B, G, R))
        
    #显示图像
    cv.imshow('result',np.vstack((img,dst)))
    cv.waitKey()
    cv.destroyAllWindows()
```

###  图像怀旧特效展示

![](https://img.jbzj.com/file_images/article/202012/20201210163223928.png?20201110163230)

##  图像光照特效  

图像光照特效是指图像存在一个类似于灯光的光晕特效，图像像素值围绕光照中心点呈圆形范围内的增强。  
python实现代码主要是通过双层循环遍历图像的各像素点，寻找图像的中心点，再通过计算当前点到光照中心的距离（平面坐标系中两点之间的距离），判断该距离与图像中心圆半径的大小关系，中心圆范围内的图像灰度值增强，范围外的图像灰度值保留，并结合边界范围判断生成最终的光照效果。

```python

    #coding:utf-8
    import cv2 as cv
    import math
    import numpy as np
    
    #读取原始图像
    img = cv.imread('d:/paojie.png')
    
    #获取图像行和列
    rows, cols = img.shape[:2]
    
    #设置中心点和光照半径
    centerX = rows / 2 - 20
    centerY = cols / 2 + 20
    radius = min(centerX, centerY)
    
    #设置光照强度
    strength = 100
    
    #新建目标图像
    dst = np.zeros((rows, cols, 3), dtype="uint8")
    
    #图像光照特效
    for i in range(rows):
      for j in range(cols):
        #计算当前点到光照中心距离(平面坐标系中两点之间的距离)
        distance = math.pow((centerY-j), 2) + math.pow((centerX-i), 2)
        #获取原始图像
        B = img[i,j][0]
        G = img[i,j][1]
        R = img[i,j][2]
        if (distance < radius * radius):
          #按照距离大小计算增强的光照值
          result = (int)(strength*( 1.0 - math.sqrt(distance) / radius ))
          B = img[i,j][0] + result
          G = img[i,j][1] + result
          R = img[i,j][2] + result
          #判断边界 防止越界
          B = min(255, max(0, B))
          G = min(255, max(0, G))
          R = min(255, max(0, R))
          dst[i,j] = np.uint8((B, G, R))
        else:
          dst[i,j] = np.uint8((B, G, R))
        
    #显示图像
    cv.imshow('result',np.vstack((img,dst)))
    cv.waitKey()
    cv.destroyAllWindows()
```

###  图像光照特效展示

![](https://img.jbzj.com/file_images/article/202012/20201210163336128.png?20201110163344)

##  图像流年特效  

流年是用来形容如水般流逝的光阴或年华，图像处理中特指将原图像转换为具有时代感或岁月沉淀的特效。python实现代码如下，它将原始图像的蓝色（B）通道的像素值开根号，再乘以一个权重参数，产生最终的流年效果。

```python

    #coding:utf-8
    import cv2 as cv
    import math
    import numpy as np
    
    #读取原始图像
    img = cv.imread('d:/paojie.png')
    
    #获取图像行和列
    rows, cols = img.shape[:2]
    
    #新建目标图像
    dst = np.zeros((rows, cols, 3), dtype="uint8")
    
    #图像流年特效
    for i in range(rows):
      for j in range(cols):
        #B通道的数值开平方乘以参数12
        B = math.sqrt(img[i,j][0]) * 12
        G = img[i,j][1]
        R = img[i,j][2]
        if B>255:
          B = 255
        dst[i,j] = np.uint8((B, G, R))
        
    #显示图像
    cv.imshow('result',np.vstack((img,dst)))
    cv.waitKey()
    cv.destroyAllWindows()
```

###  图像流年特效展示

![](https://img.jbzj.com/file_images/article/202012/20201210163428550.png?20201110163438)

##  图像滤镜特效  

滤镜主要是用来实现图像的各种特殊效果，它在Photoshop中具有非常神奇的作用。滤镜通常需要同通道、图层等联合使用，才能取得最佳艺术效果。本小节将讲述一种基于颜色查找表（Look
up Table）的滤镜处理方法，它通过将每一个原始颜色进行转换之后得到新的颜色。比如，原始图像的某像素点为红色（R-255, G-0,
B-0），进行转换之后变为绿色（R-0, G-255,
B-0），之后所有是红色的地方都会被自动转换为绿色，而颜色查找表就是将所有的颜色进行一次（矩阵）转换，很多的滤镜功能就是提供了这么一个转换的矩阵，在原始色彩的基础上进行颜色的转换。  
假设现在存在一张新的滤镜颜色查找表，如图所示，它是一张512×512大小，包含各像素颜色分布的图像。下面这张图片另存为本地，即可直接用于图像滤镜处理。

![](https://img.jbzj.com/file_images/article/202012/20201210163504020.png?20201110163514)

```python

    #coding:utf-8
    import cv2 as cv 
    import numpy as np
    
    #获取滤镜颜色
    def getBGR(img, table, i, j):
      #获取图像颜色
      b, g, r = img[i][j]
      #计算标准颜色表中颜色的位置坐标
      x = int(g/4 + int(b/32) * 63)
      y = int(r/4 + int((b%32) / 4) * 63)
      #返回滤镜颜色表中对应的颜色
      return lj_map[x][y]
    
    #读取原始图像
    img = cv.imread('d:/paojie.png')
    lj_map = cv.imread('lvjing.png')
    
    #获取图像行和列
    rows, cols = img.shape[:2]
    
    #新建目标图像
    dst = np.zeros((rows, cols, 3), dtype="uint8")
    
    #循环设置滤镜颜色
    for i in range(rows):
      for j in range(cols):
        dst[i][j] = getBGR(img, lj_map, i, j)
        
    #显示图像
    cv.imshow('result',np.vstack((img,dst)))
    
    cv.waitKey()
    cv.destroyAllWindows()
```

###  图像滤镜特效展示

![](https://img.jbzj.com/file_images/article/202012/20201210163552665.png?2020111016360)

以上就是python opencv图像处理(素描、怀旧、光照、流年、滤镜 原理及实现)的详细内容，更多关于python
opencv图像处理的资料请关注脚本之家其它相关文章！

