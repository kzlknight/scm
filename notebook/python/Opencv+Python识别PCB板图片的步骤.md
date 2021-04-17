##  任务要求：

基于模板匹配算法识别PCB板型号

##  使用工具：

Python3、OpenCV

使用模板匹配算法，模板匹配是一种最原始、最基本的模式识别方法，研究某一特定对象物的图案位于图像的什么地方，进而识别对象物，模板匹配具有自身的局限性，主要表现在它只能进行平行移动，即原图像中的匹配目标不能发生旋转或大小变化。

事先准备好待检测PCB与其对应的模板：

![](https://img.jbzj.com/file_images/article/202101/202117162721882.png?202107162735)

子模版：

![](https://img.jbzj.com/file_images/article/202101/202117162756554.png?20210716284)

##  基本流程如下：

1、在整个图像区域发现与给定子图像匹配的小块区域

2、选取模板图像T（给定的子图像）

3、另外需要一个待检测的图像――源图像S

4、工作方法：在检测图像上，从左到右，从上到下计算模板图像与重叠， 子图像的匹配度，匹配程度越大，两者相同的可能性就越大。

OpenCV提供了6种模板匹配算法：

平方差匹配法CV_TM_SQDIFF；

归一化平方差匹配法CV_TM_SQDIFF_NORMED；

相关匹配法CV_TM_CCORR；

归一化相关匹配法CV_TM_CCORR_NORMED；

相关系数匹配法CV_TM_CCOEFF；

归一化相关系数匹配法CV_TM_CCOEFF_NORMED；

后面经过实验，我们主要是从以上的六种中选择了归一化相关系数匹配法CV_TM_CCOEFF_NORMED，基本原理公式为：

##  代码部分展示：

```python

    import cv2
    import numpy as np
    from matplotlib import pyplot as plt
    
    #读取检测图像
    img = cv2.imread('img8.bmp', 0)
    #读取模板图像
    template1=cv2.imread('moban1.bmp', 0)
    template2=......
    #建立模板列表
    template=[template1,template2,template3,template4]
    # 模板匹配：归一化相关系数匹配方法
    res1=cv2.matchTemplate(img, template1, cv2.TM_CCOEFF_NORMED)
    res2=cv2.matchTemplate(......)
    #提取相关系数
    min_val1, max_val1, min_loc1, max_loc1 =cv2.minMaxLoc(res1)
    min_val2, ......
    
    #相关系数对比（max_val),越接近1，匹配程度越高
    max_val=[1-max_val1,1-max_val2,1-max_val3,1-max_val4]
    j=max_val.index(min(max_val))
    
    #根据提取的相关系数得出对应匹配程度最高的模板
    h, w = template[j].shape[:2]  # 计算模板图像的高和宽 rows->h, cols->w
    pes=cv2.matchTemplate(img, template[j], cv2.TM_CCOEFF_NORMED) #模板匹配
    in_val, ax_val, in_loc, ax_loc =cv2.minMaxLoc(pes)
    
    #在原图中框出模板匹配的位置
    left_top = ax_loc  # 左上角
    right_bottom = (left_top[0] + w, left_top[1] + h)  # 右下角
    cv2.rectangle(img, left_top, right_bottom, 255, 2) # 画出矩形位置
    #绘制模板图像
    plt.subplot(121), plt.imshow(template[j], cmap='gray')
    plt.title('pcb type'),plt.xticks([]), plt.yticks([])
    #绘制检测图像
    plt.subplot(122), plt.imshow(img, cmap='gray')
    plt.title('img'), plt.xticks([]), plt.yticks([])
    plt.show()
```

##  实验结果：

![](https://img.jbzj.com/file_images/article/202101/202117162856850.png?20210716293)

需要完整代码以及图片素材的，请留下评论可与博主进行联系。

以上就是Opencv+Python识别PCB板图片的步骤的详细内容，更多关于Opencv+Python识别PCB板的资料请关注脚本之家其它相关文章！

