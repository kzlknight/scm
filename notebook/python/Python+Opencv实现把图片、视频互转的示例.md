##  1. 安装Opencv包

```python

    pip install opvencv-python
```

##  2.实现代码：  

视频转为图片：

```python

    import cv2
    cap=cv2.VideoCapture('E:/video/video-02.mp4') # 获取一个视频打开cap
    isOpened=cap.isOpened # 判断是否打开
    print(isOpened)
    fps=cap.get(cv2.CAP_PROP_FPS)
    print(fps)
    # 获取宽度
    width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    # 获取高度
    height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    i=0
    while(isOpened):
      # 保存前十帧
      if i==10:
        break
      else:
        i+=1
      (flag,frame)=cap.read() # 读取每一帧，一张图像flag 表明是否读取成果 frame内容
      fileName='E:/video/image'+str(i)+'.jpg'
      print(fileName)
      # flag表示是否成功读图
      if flag==True:
        # 控制质量
        cv2.imwrite(fileName,frame,[cv2.IMWRITE_JPEG_QUALITY,100])
    print('end!')
```

图片保存为视频：

```python

    import os
    import cv2
    import numpy as np
    
    path = 'E:/video/img'
    filelist = os.listdir(path)
    #fourcc = cv2.cv.CV_FOURCC('M','J','P','G') #opencv版本是2
    fourcc = cv2.VideoWriter_fourcc(*'XVID') #opencv版本是3
    
    fps = 5 # 视频每秒24帧
    size = (1920, 1080) # 需要转为视频的图片的尺寸
    # 可以使用cv2.resize()进行修改
    
    video = cv2.VideoWriter('E:/video/2.avi', fourcc, fps, size)
    # 视频保存在当前目录下
    
    for item in filelist:
      if item.endswith('.jpg'):
        # 找到路径中所有后缀名为.png的文件，可以更换为.jpg或其它
        item = path + item
        img = cv2.imread(item)
        video.write(img)
    video.release()
    cv2.destroyAllWindows()
```

以上就是Python+Opencv实现把图片、视频互转的示例的详细内容，更多关于python 图片、视频互转的资料请关注脚本之家其它相关文章！

