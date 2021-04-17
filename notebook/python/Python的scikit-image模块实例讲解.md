scikit-
image模块就是一个图像处理库，和其他图像处理库不同的是，功能全面且强大，主要的功能有导入彩色图像、进行图像分割、以及监督分割等等，现在大家可能对概念还是模棱两可，但是只要是和图像有关系的，基本上操作方式仅限那几个，所以大家不必担心，以下是为大家准备的使用技巧，一起来了解学习。

###  Linux安装方式：

```python

    pip install -U scikit-image
```

###  Windows安装方式：

```python

    pip install scikit-image
```

###  实例应用：

1、导入彩色图像

```python

    from skimage import data
    import numpy as np
    import matplotlib.pyplot as plt
    image = data.astronaut()
    plt.imshow(image);
```

2、分割操作

```python

    from skimage import io
    image = io.imread('girl.jpg') 
    plt.imshow(image);
```

到此这篇关于Python的scikit-image模块实例讲解的文章就介绍到这了,更多相关Python的scikit-
image模块是什么内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

