检测剪刀石头布三种手势，通过摄像头输入，方法如下：

  * 选用合适颜色空间及阈值提取皮肤部分 
  * 使用滤波腐蚀膨胀等方法去噪 
  * 边缘检测 
  * 寻用合适方法分类 

###  OpenCV用摄像头捕获视频

采用方法：调用OpenCV――cv2.VideoCapture()

```python

    def video_capture():
     cap = cv2.VideoCapture(0)
     while True:
     # capture frame-by-frame
     ret, frame = cap.read()
    
     # our operation on the frame come here
     # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 可选择灰度化
    
     # display the resulting frame
     cv2.imshow('frame', frame)
     if cv2.waitKey(1) & 0xFF == ord('q'): # 按q键退出
     break
     # when everything done , release the capture
     cap.release()
     cv2.destroyAllWindows()
```

效果如下  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020122112094575.jpg)

###  肤色识别――椭圆肤色检测模型

参考下述博文

[ https://www.jb51.net/article/202594.htm
](https://www.jb51.net/article/202594.htm)

代码如下

```python

    def ellipse_detect(img):
     # 椭圆肤色检测模型
     skinCrCbHist = np.zeros((256, 256), dtype=np.uint8)
     cv2.ellipse(skinCrCbHist, (113, 155), (23, 15), 43, 0, 360, (255, 255, 255), -1)
    
     YCRCB = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
     (y, cr, cb) = cv2.split(YCRCB)
     skin = np.zeros(cr.shape, dtype=np.uint8)
     (x, y) = cr.shape
     for i in range(0, x):
     for j in range(0, y):
     CR = YCRCB[i, j, 1]
     CB = YCRCB[i, j, 2]
     if skinCrCbHist[CR, CB] > 0:
     skin[i, j] = 255
     dst = cv2.bitwise_and(img, img, mask=skin)
     return dst
```

效果如下，可见与肤色相近的物体全被提取出来，包括桌子。。。  
识别时需寻找一无干扰环境  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020122112094576.jpg)

###  去噪――滤波、腐蚀和膨胀

参考下述博文

[ https://www.jb51.net/article/202599.htm
](https://www.jb51.net/article/202599.htm)

采用方法：高斯滤波 cv2.GaussianBlur() + 膨胀 cv2.dilate()，代码如下

```python

    # 膨胀
    def dilate_demo(image):
     # 灰度化
     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
     # 二值化
     ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
     # 定义结构元素的形状和大小
     kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
     # 膨胀操作
     dst = cv2.dilate(binary, kernel)
     return dst
    
    
    # 腐蚀
    def erode_demo(image):
     # 灰度化
     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
     # 二值化
     ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
     # 定义结构元素的形状和大小
     kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
     # 腐蚀操作
     dst = cv2.erode(binary, kernel)
     return dst
    
    
    # 滤波
    def img_blur(image):
     # 腐蚀操作
     # img_erode = erode_demo(image)
     # 膨胀操作
     img_dilate = dilate_demo(image)
    
     # 均值滤波
     # blur = cv2.blur(image, (5, 5))
     # 高斯滤波
     blur = cv2.GaussianBlur(img_dilate, (3, 3), 0)
     return blur
```

###  Canny边缘检测

参考OpenCV中文教程

[ https://www.kancloud.cn/aollo/aolloopencv/271603
](https://www.kancloud.cn/aollo/aolloopencv/271603)

代码如下

```python

    # Canny边缘检测v
    def canny_detect(image):
     edges = cv2.Canny(image, 50, 200)
     return edges
```

###  识别――轮廓匹配

Tensorflow框架实在太难搭，搭了半天没搭出来，还一堆错误。。。所以采用轮廓匹配 cv2.matchShapes() ，方案如下：

  * 划分出了一个手势识别区域，可避免周围环境的干扰，也可简化图像处理过程 
  * 寻找轮廓时采用寻找矩形框架 cv2.boundingRect(）的方法找到最大轮廓，即手势的轮廓 
  * 将找到的轮廓直接与标准图片进行匹配，简化识别过程 

但在匹配时发现“剪刀”的手势常与“石头”、“布”的手势匹配到一起。。。所以另辟蹊径，在匹配时加上了对于矩形框架面积的判断，一般来说有如下规律，石头<剪刀<布，代码如下

```python

     # 轮廓匹配
     value = [0, 0, 0]
     value[0] = cv2.matchShapes(img_contour, img1, 1, 0.0)
     value[1] = cv2.matchShapes(img_contour, img2, 1, 0.0)
     value[2] = cv2.matchShapes(img_contour, img3, 1, 0.0)
     min_index = np.argmin(value)
     if min_index == 0: # 剪刀
      print(text[int(min_index)], value)
     elif min_index == 1 and w*h < 25000: # 石头
      print(text[int(min_index)], value)
     elif min_index == 1 and w*h >= 25000: # 剪刀
      print(text[0], value)
     elif min_index == 2 and w * h > 30000: # 布
      print(text[int(min_index)], value)
     elif min_index == 2 and w * h <= 30000: # 剪刀
      print(text[0], value)
```

程序会根据匹配值和面积大小来决定识别结果，例如，下述结果，1.179515828609219, 0.9604643714904955,
0.9896353720020925分别对应剪刀、石头、布的匹配值，越小说明越吻合；结合最终识别情况来看，在三种手势中，石头的识别成功率最高，约98%；布其次，约88%；剪刀最低，约80%，而且结果易受环境亮度影响，环境过暗或过亮，有时候手势轮廓都出不来。。。看来仍有待改进，还是得用机器学习的方法

> 石头 [1.179515828609219, 0.9604643714904955, 0.9896353720020925]

程序效果如下，黄色矩形框为识别区域，gesture窗口为用于轮廓匹配的手势图  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020122112094577.jpg)  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020122112094678.jpg)  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020122112094679.jpg)

到此这篇关于OpenCV+Python3.5 简易手势识别的实现的文章就介绍到这了,更多相关OpenCV 手势识别
内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

