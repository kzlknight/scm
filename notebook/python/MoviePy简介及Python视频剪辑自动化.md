**视频地址** :https://www.bilibili.com/video/BV1mv411k7Qv?p=1

##  moviepy是啥

![](https://img.jbzj.com/file_images/article/202012/2020121810263320.png)

` MoviePy ` 是一个用于视频编辑的 ` Python ` 模块。

可用于基本操作（如剪切、拼接、字幕插入）、视频合成、视频处理或创建高级效果等。

它可以读写最常见的视频(甚至GIF)、音频格式。

![](https://img.jbzj.com/file_images/article/202012/2020121810263321.png)

在一定程度上，它可以取代 ` Premiere ` 。

##  moviepy能做啥

批量加片头、片尾

比如你有一堆已经做好的视频，你想给它们加上片头，但不想用 ` PR ` 一个个地处理:

![](https://img.jbzj.com/file_images/article/202012/2020121810263422.jpg)

轻松从MV中提取音乐

比如你有周董 ` Mojito ` 的MV, 你想白嫖MP3:

![](https://img.jbzj.com/file_images/article/202012/2020121810263423.jpg)

将图片合成视频

有PY大牛封装 ` moviepy ` 做了个视频转字符动画的工具:

![](https://img.jbzj.com/file_images/article/202012/2020121810263424.jpg)

加字幕、标题、水印

你有一个很棒的视频，并且不满意 ` B站 ` 自动添加的水印，想自己做:

![](https://img.jbzj.com/file_images/article/202012/2020121810263425.jpg)
![](https://img.jbzj.com/file_images/article/202012/2020121810263426.jpg)

做一些炫酷的特效

` moviepy ` 自带了很多视频、音频的效果，除此之外，你还可以制作自己的效果:

![](https://img.jbzj.com/file_images/article/202012/2020121810263527.jpg)
![](https://img.jbzj.com/file_images/article/202012/2020121810263528.gif)

![](https://img.jbzj.com/file_images/article/202012/2020121810263529.gif)

##  moviepy的优缺点

优点 **简单直观** ：基本操作可以一行完成，代码对于新手来说很容易学习、理解 **灵活** ：完全控制视频和音频的帧，容易创建自己的效果 **轻便的**
：不需要复杂的配置，几乎可以在所有已安装Python的计算机上运行缺点

不支持流形式的视频(stream video)，比如从摄像头读取的视频。

##  moviepy的工作方式

![](https://img.jbzj.com/file_images/article/202012/2020121810263630.jpg)

利用 ` ffmpeg ` (多媒体处理软件) **读取** 和 **导出** 视频和音频文件利用 ` ImageMagick ` (图片处理软件)
**生成文字** 利用 ` numpy ` 、 ` PIL ` 、 ` scipy ` 、 ` opencv ` 等 ` Python `
库来处理各种媒体总结

` moviepy ` 很NB，如果你觉得好玩，不妨上车

![](https://img.jbzj.com/file_images/article/202012/2020121810263631.gif)

到此这篇关于MoviePy简介及Python视频剪辑自动化的文章就介绍到这了,更多相关MoviePy
Python视频剪辑自动化内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

