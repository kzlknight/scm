**视频地址** :https://www.bilibili.com/video/BV1mv411k7Qv?p=4

##  导入方式

![](https://img.jbzj.com/file_images/article/202012/2020121810325333.jpg)

所有的剪辑类都可以从 ` moviepy.editor ` 模块中导入

##  Clip

所有 **剪辑类的基类** , 也可以简单的将它称为:

![](https://img.jbzj.com/file_images/article/202012/2020121810325334.png)

###  VideoClip

所有 **视频剪辑的基类** , 可以简单的将它称为:

![](https://img.jbzj.com/file_images/article/202012/2020121810325435.png)

很少用, 除非你要从零开始一帧一帧地构建视频。

####  VideoFileClip

最常用的视频剪辑类, 用于导入视频文件(mp4、avi等格式皆可)

![](https://img.jbzj.com/file_images/article/202012/2020121810325436.jpg)

####  ImageClip

常用的剪辑类, 用于导入图片文件(png、jpg等格式皆可)

![](https://img.jbzj.com/file_images/article/202012/2020121810325437.jpg)

####  ColorClip

比较少用, 可以把它当作是单一颜色的图片

![](https://img.jbzj.com/file_images/article/202012/2020121810325438.jpg)

如果是黑色, 就相当于是 ` Premiere ` 里面的黑场

####  TextClip

常用的剪辑类, 文字剪辑, 常用于给视频加字幕、水印、标题等

![](https://img.jbzj.com/file_images/article/202012/2020121810325439.jpg)

####  CompositeVideoClip

最常用剪辑类, 组合剪辑, 用于组合以上各种视频剪辑类

![](https://img.jbzj.com/file_images/article/202012/2020121810325540.jpg)

比如加水印这一功能就可以用它

###  AudioClip

所有 **音频剪辑的基类** , 同样称为:

![](https://img.jbzj.com/file_images/article/202012/2020121810325541.png)

同 ` VideoClip ` 一样很少用。

####  AudioFileClip

最常用音频剪辑类, 与 ` VideoFileClip ` 类似, 用于导入音频文件(mp3, m4a等)

![](https://img.jbzj.com/file_images/article/202012/2020121810325542.jpg)

####  CompositeAudioClip

与 ` CompositeVideoClip ` 类似, 是最常用的音频组合剪辑类, 就不多介绍了

##  总结

这节初步了解一下moviepy中的各种剪辑类, 下节讲如何导出剪辑～

到此这篇关于MoviePy常用剪辑类及Python视频剪辑自动化的文章就介绍到这了,更多相关Python视频剪辑自动化内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

