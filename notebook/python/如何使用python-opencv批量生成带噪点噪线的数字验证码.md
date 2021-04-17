第一次使用csdn写一个文章，如果有什么写的不对的地方，欢迎在下面评论指正，谢谢各位。

###  1.明确要使用的包

首先就是opencv的函数库，还有python自带的random和PIL(Image、ImageDraw、ImageFont)，一般pthon3以上的版本都是内置安装的，如果没有安装可以通过pip
install的方法安装具体操作如图：  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020122112034873.png)  

输入完按回车键即可安装，因为我已经安装了，就不输入回车键了，安装完了之后可以通过import的方式检验是否安装成功。记住先输入python进入python的编程环境在输入import
PIL,否则就会报错

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020122112034874.png)

###  2.引入库

代码如下（示例）：

```python

    import cv2 as cv
    import random
    from PIL import Image
    from PIL import ImageDraw
    from PIL import ImageFont
```

###  3.生成随机的颜色组合get_random_color()

彩色图像是由RGB三色通道构成的，但是要注意在opencv里面的彩色图像是按照BGR的顺序来构成彩色图像的，与其他的地方采用图像的顺序不一样(例如halcon就是安装RGB的顺序来引用彩色图像)，  
采用函数的形式来形成一个三个数组，当函数返回的数值超过三个的时候，就会以数组的形式返回。  
代码如下（示例）：

```python

    # 随机生成不同颜色的组合
    def get_random_color():
      B = random.randint(0, 255)
      G = random.randint(0, 255)
      R = random.randint(0, 255)
      # 防止生成白色噪声噪线
      # 使用三个if条件判断防止三个通道的颜色都是255(虽然是不可能事件）
      if B == 255:
        B = 0
      elif G == 255:
        G = 0
      elif R == 255:
        R = 0
      return(B, G, R)
```

如果你不放心是否返回了一个数组，可以进行验证

```python

    #用于测试是否获得了数组
    a = get_random_color()
    print(a)
```

###  4.生成颜色随机，数值随机的数字生成函数get_random_number()

这个函数比较简单，原理也是和上面随机生成颜色组合一样。  
代码如下(示例)：

```python

    # 随机生成数字
    def get_random_number():
      random_num = str(random.randint(0, 9))
      return random_num
```

###  5.随机生成一张干净的(不带噪声噪线)数字验证码图像

使用PIL的Image、ImageDraw、ImageFont分别用于生成白色图像背景、定义画笔用于往图像写入数字、定义文字的字形和字体大小。  
代码如下(示例)：

```python

    def generate_image():
      # 生成白色图像，'RGB'类型，宽高为(150,50)，底色为白色(255,255,255)
      image = Image.new('RGB', (150, 50), (255,255,255))
      # 定义画笔，将图像与画笔关联
      draw = ImageDraw.Draw(image)
      # 定义文字字形以及字体大小
      font = ImageFont.truetype("arial.ttf", size=36)
    
      name = "" # 定义一个空的字符串，用于不断叠加数字，给图像命名
      for i in range(5):
        random_number = get_random_number()
        # 不断叠加随机生成的数字，用于给图像命名
        name += random_number
    
        # 在图片上写上数字，参数是：定位、数字(字符串)、颜色、字型
        draw.text((10+i*30, 0), random_number, get_random_color(), font=font)
      # 将图像保存到指定的文件夹，下面使用xxxx的形式代表文件夹
      image.save('G:\xxxxxx\xxxxxxxx\%s.png' % name)
```

字体可以根据自己电脑已有的字体来选择，具体路径是C:\Windows\Fonts，

```python

     font = ImageFont.truetype("arial.ttf", size=36)
```

###  6.往图像添加噪声噪线

函数的这一步不使用新的函数，继续接着上一个函数(
generate_image())输入代码，为什么不使用？因为在读取图像的时候我们会用到name这个函数，如果使用新的函数的话，就无法使用这个变量。当然也可以通过类的方法，实现两个函数之间的变量可以相互调用，这个就稍微麻烦点，这里就不过多讲述了。  
代码如下(示例)：  
(再次提醒下面代码是接着generate_image()的，所以下面代码都有一个缩进)

```python

    width = 150
      height = 50
      # 读取文件夹的图像，通过name来读取指定的图像，
      img = cv.imread('G:\xxxxxx\xxxxxxxxxxxx\%s.png' %name)
      # 绘制噪点
      for i in range(5):
        x = random.randint(0, width)
        y = random.randint(0, height)
        # 绘制实心圆，必须输入参数分别是：图像、圆心的位置、半径、颜色，
        #最后一个是thickness默认是None，绘制空心圆，指定为-1绘制实心圆
        cv.circle(img, (x,y), 1, get_random_color(), -1)
    
      # 绘制噪线
      for i in range(3):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        # 绘制线条，参数分别是：图像、左上角的坐标、右下角的坐标、颜色
        cv.line(img, (x1,y1), (x2,y2), get_random_color())
      # 保存图像
      cv.imwrite(r'G:\xxxxx\xxxxxxx\%s.png'%name, img)
```

###  7.调用函数生成数字验证码图像

所有的函数都已经写完，直接调用图像生成函数就行了。  
使用for循环，循环调用generate_image()即可实现批量生成图像，想要多少张就循环多少次。

```python

    for i in range(30):
      generate_image()
```

###  8.总结

到这一步所有的工作已经完成了，可以去保存的指定文件夹看一下，是否成功生成，一般程序没有报错基本都是可以生成的。  

第一次使用csdn写文章，肯定会有很多纰漏和不足，有什么建议和意见都可以在下面评论提出，我会一一更正，谢谢各位

到此这篇关于如何使用python-
opencv批量生成带噪点噪线的数字验证码的文章就介绍到这了,更多相关opencv批量生成噪点验证码内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

