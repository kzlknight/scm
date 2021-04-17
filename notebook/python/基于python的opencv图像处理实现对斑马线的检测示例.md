**基本思路**

斑马线检测通过opencv图像处理来进行灰度值转换、高斯滤波去噪、阈值处理、腐蚀和膨胀后对图像进行轮廓检测，通过判断车辆和行人的位置，以及他们之间的距离信息，当车速到超过一定阈值时并且与行人距离较近时，则会被判定车辆为未礼让行人。

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202011/2020112916580390.jpg)

结果示例

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202011/2020112916580391.jpg)

**实验流程**

先通过视频截取一张图片来进行测试，如果结果满意之后再嵌套到视频中，从而达到想要的效果。

**1.预处理（灰度值转换、高斯滤波去噪、阈值处理、腐蚀和膨胀） > 根据自己的需求来修改一些值 **

```python

    #灰度值转换
    imgGray = cv2.cvtColor(copy_img,cv2.COLOR_BGR2GRAY)
    #高斯滤波去噪
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),0)
    #阈值处理
    ret,thresh = cv2.threshold(imgBlur,127,255,cv2.THRESH_BINARY)
    #腐蚀
    imgEro = cv2.erode(thresh,kernel1,iterations=2)
    #膨胀
    imgDia = cv2.dilate(imgEro,kernel2,iterations=4)
```

**预处理之后（如下图所示）：**  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202011/2020112916580392.jpg)

**2.轮廓检测**

```python

    #轮廓检测
    _,contouts,hie = cv2.findContours(imgDia,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    cnt = contouts
    cv2.drawContours(copy_img, cnt, -1, (0, 255, 0), 2)
    
```

**全部的轮廓（如下图所示）**  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202011/2020112916580493.jpg)

可以看到这并不是我们想要的，所以我们需要判断一下位置，选取我们感兴趣的区域。

**3.感兴趣区域**

根据自己图片或视频的需求来更改x，y，w，h位置信息数值。

```python

    for i in cnt:
      #坐标赋值
      x,y,w,h = cv2.boundingRect(i)
      #roi位置判断
      if y>350 and y<450 and x<1200 and w>50 and h>10:
        # 画出轮廓
        cv2.drawContours(copy_img, i, -1, (0, 255, 0), 2)
    
```

**获取roi后完整结果（如下图所示）**  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202011/2020112916580494.jpg)

**4.完整代码**

```python

    import cv2
    import numpy as np
    #定义两个核	（kernel_Ero用于腐蚀，kernel_Dia用于膨胀）
    kernel_Ero = np.ones((3,1),np.uint8)
    kernel_Dia = np.ones((3,5),np.uint8)
    
    img = cv2.imread("../images/bmx.png")
    copy_img = img.copy()
    #原图copy修改尺寸
    copy_img = cv2.resize(copy_img,(1600,800))
    #灰度值转换
    imgGray = cv2.cvtColor(copy_img,cv2.COLOR_BGR2GRAY)
    #高斯滤波去噪
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),0)
    #阈值处理
    ret,thresh = cv2.threshold(imgBlur,127,255,cv2.THRESH_BINARY)
    #腐蚀
    imgEro = cv2.erode(thresh,kernel_Ero,iterations=2)
    #膨胀
    imgDia = cv2.dilate(imgEro,kernel_Dia,iterations=4)
    
    #轮廓检测
    _,contouts,hie = cv2.findContours(imgDia,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    cnt = contouts
    
    for i in cnt:
      #坐标赋值
      x,y,w,h = cv2.boundingRect(i)
      #roi位置判断
      if y>350 and y<450 and x<1200 and w>50 and h>10:
        # 画出轮廓
        cv2.drawContours(copy_img, i, -1, (0, 255, 0), 2)
    
    cv2.imshow("img",copy_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
```

**总结**

在业务需求中这种流程做出来的结果并不可行，只不过是把想要的东西框了出来，但是如果想要对交通场景判别机动车是否礼让行人行为的话则需要对坐标进行判断，可以通过从第一个斑马线的坐标到最后一个斑马线的坐标(横向)来画出一个大的矩形框(roi区域)，然后根据这个矩形框的坐标来对机动车(已有坐标)坐标来进行行为判断，从而达到需求。

**最后！！！**

第一次接触opencv！所以请各位视觉领域的大佬们勿喷我这个小菜鸡！（/狗头）  

代码量非常少，无泛化能力，很low的一种做法。。。不过对于小白的我来说学习opencv还是很有帮助滴！干就完了！奥利给！

到此这篇关于基于python的opencv图像处理实现对斑马线的检测示例的文章就介绍到这了,更多相关opencv
斑马线检测内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

