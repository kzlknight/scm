###  1，概念及原理：  

膨胀（Dilating） （或）  
（1）将图像 A 与任意形状的内核 (B)，通常为正方形或圆形，进行卷积。  
（2）内核 B 有一个可定义的 锚点, 通常定义为内核中心点。  
（3）进行膨胀操作时，将内核 B 划过图像A,将内核 B
覆盖区域的最大相素值提取，并代替锚点位置的相素。显然，这一最大化操作将会导致图像中的亮区开始”扩展” (因此有了术语膨胀 dilation )。  

以3*3的内核为例：  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020122114280887.png)

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020122114280888.png)  

腐蚀（Eroding） （与）  
（1）腐蚀在形态学操作家族里是膨胀操作的孪生姐妹。它提取的是内核覆盖下的相素最小值。  
（2）进行腐蚀操作时，将内核 B 划过图像,将内核 B 覆盖区域的最小相素值提取，并代替锚点位置的相素。

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020122114280889.png)

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020122114280890.png)

值得注意的是：腐蚀和膨胀是对白色部分（高亮部分）而言的，不是黑色部分。
膨胀就是图像中的高亮部分进行膨胀，“邻域扩张”，效果图拥有比原图更大的高亮区域。腐蚀就是原图中高亮部分被腐蚀，“邻域被蚕食”，效果图拥有比原图更小的高亮区域。

源代码：

```python

    import cv2 as cv
    import numpy as np
    
    
    def erode_demo(image):
      # print(image.shape)
      gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
      ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
      #cv.imshow("binary", binary)
      kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 15))#定义结构元素的形状和大小
      dst = cv.erode(binary, kernel)#腐蚀操作
      cv.imshow("erode_demo", dst)
    
    
    def dilate_demo(image):
      #print(image.shape)
      gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
      ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
      #cv.imshow("binary", binary)
      kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))#定义结构元素的形状和大小
      dst = cv.dilate(binary, kernel)#膨胀操作
      cv.imshow("dilate_demo", dst)
    
    
    
    src = cv.imread("F:/images/test01.png")
    cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
    cv.imshow("input image", src)
    erode_demo(src)
    dilate_demo(src)
    
    cv.waitKey(0)
    
    cv.destroyAllWindows()
```

运行结果：  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020122114280891.png)  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020122114280892.png)  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020122114280893.png)

到此这篇关于OpenCV+python实现膨胀和腐蚀的示例的文章就介绍到这了,更多相关OpenCV
膨胀和腐蚀内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

