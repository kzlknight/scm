编译 pycaffe时报错：fatal error: numpy/arrayobject.h没有那个文件或目录

![](https://img.jbzj.com/file_images/article/202011/202011292331179.png)

其实numpy已经是安装的，anaconda2里面有，python中import numpy也没有问题，但就是在此处报错，解决方法：

> sudo apt-get install python-numpy

然后

> sudo make pycaffe -j16

pycaffe就编译成功了

![](https://img.jbzj.com/file_images/article/202011/2020112923312110.jpg)

如果还是不行，可以试试：

> import numpy as npnp.get_include()

得到：

/usr/local/lib/python2.7/dist-packages/numpy/core/include

在Makefile.config找到PYTHON_INCLUDE，发现有点不同：

> PYTHON_INCLUDE := /usr/include/python2.7 \  
>  /usr/lib/python2.7/dist-packages/numpy/core/include

要加一个local，变成：

> PYTHON_INCLUDE := /usr/include/python2.7 \  
>  /usr/local/lib/python2.7/dist-packages/numpy/core/include

再make pycaffe就ok了

很奇怪在caffe/build目录下编译pycaffe报错：No rule to make target 'pycaffe' 。在caffe根目录下就可以

![](https://img.jbzj.com/file_images/article/202011/2020112923312411.jpg)

**解决方法**

1.命令行输入进python

> import numpy as np  
>  np.get_include()

得到numpy的安装路径：

/usr/local/lib/python2.7/dist-packages/numpy/core/include

在Makefile.config找到PYTHON_INCLUDE，发现有点不同：

> PYTHON_INCLUDE := /usr/include/python2.7 \  
>  /usr/lib/python2.7/dist-packages/numpy/core/include

要加一个local，变成：

> PYTHON_INCLUDE := /usr/include/python2.7 \  
>  /usr/local/lib/python2.7/dist-packages/numpy/core/include

再make pycaffe就ok了

2.直接安装模块 numpy

> suod apt-get install python-numpy

到此这篇关于编译 pycaffe时报错：fatal error:
numpy/arrayobject.h没有那个文件或目录的文章就介绍到这了,更多相关fatal error:
numpy/arrayobject.h内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

