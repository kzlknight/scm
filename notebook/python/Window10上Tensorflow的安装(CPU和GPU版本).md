之前摸索tensorflow的时候安装踩坑的时间非常久，主要是没搞懂几个东西的关系，就在瞎调试，以及当时很多东西不懂，很多报错也一知半解的。这次重装系统后正好需要再配置一次，把再一次的经历记录一下。我的电脑是华为的matebook13，intel
i5-8625U，MX250显卡，win10系统。（不得不吐槽很垃圾，只能满足测试测试调调代码的需求）

深度学习利用Tensorflow平台，其中的Keras Sequential API对新用户非常的友好，可以将各基础组件组合在一起来构建模型。

（官网： [ https://tensorflow.google.cn/?hl=zh-cn
](https://tensorflow.google.cn/?hl=zh-cn) ）

![](https://img.jbzj.com/file_images/article/202012/2020121511070455.jpg)

![](https://img.jbzj.com/file_images/article/202012/2020121511070456.jpg)

###  安装Tensorflow 分为 tensorflow_cpu 和 tensorflow_gpu版本

GPU就是用来渲染计算的，GPU版本计算性能是CPU的百倍之快。如果电脑没有独立显卡只能用CPU版本计算。

![](https://img.jbzj.com/file_images/article/202012/2020121511070557.jpg)

###  CPU版本安装：

**tensorflow_cpu版本只需要安装anaconda后在anaconda prompt里面pip install
tensorflow_cpu==（版本号） 即可。** 安装anaconda的方法见GPU版本里面。

注意查下python和tensorflow_cpu适配的版本号。

![](https://img.jbzj.com/file_images/article/202012/2020121511070558.jpg)

###  GPU版本安装

**tensorflow_gpu版本安装大致分为三步：1、安装anaconda 2、安装cuda和cdunn
3、安装tensorflow_gpu。其中第一步和第二步的顺序可以调换，就是安装完了前面三个东西再安装tensorflow即可。**

tensorflow最近出了2.0版本，和1.0大版本有一些区别。具体我还没有去了解，代码不一定兼容，需要注意一下。这三个步骤的版本需要格外的注意，一旦三个自己的版本互相不兼容或者和电脑的显卡不兼容，就用不了。所以安装前看看要安装的tensorflow版本。先查好显卡的算力，然后适配的相应版本再安装，否则踩坑要很久。

首先确定电脑所能支持的tensorflow版本，根据tensorflow官网所给配置，我们要去检查电脑gpu的cuda支持版本，再去对应下载python版本和tensorflow版本。

**右键 桌面 >NVIDIA控制面板>帮助>系统信息>组件 **

![](https://img.jbzj.com/file_images/article/202012/2020121511070559.jpg)

上图说明我的显卡所支持的cuda版本为11.1（向下兼容）

**Tensorflow配置window官网：[ https://tensorflow.google.cn/install/source_windows
](https://tensorflow.google.cn/install/source_windows) **

![](https://img.jbzj.com/file_images/article/202012/2020121511070560.jpg)

以我电脑为例，之前我用的是3.7.3的版本。这次重装系统后安装的是3.8.3。

**cmd查看python版本：**
![](https://img.jbzj.com/file_images/article/202012/2020121511070661.jpg)

我之前tensorflow用的是1.13的版本，这次因为已经安装了python3.8，因此打算安装2.0版本。如果仍需要低版本需要重新安装python较低的版本或者搭一个虚拟环境（但不是很建议）。

**第一步，安装** **anaconda**

anaconda会对应安装python环境，不一定要最新的， 最新的python版本不一定有兼容的cuda加速，有cuda加速也不一定支持电脑的显卡。

官网安装： [ https://www.anaconda.com/products/individual
](https://www.anaconda.com/products/individual) ，之前版本如果官网没有可能需要找资源。

**第二步，安装** **cuda** **工具包**

**（官网：https://developer.nvidia.com/zh-cn/cuda-toolkit）**

CUDA是 NVIDIA 专为图形处理单元 (GPU) 上的通用计算开发的并行计算平台和编程模型。借助 CUDA，开发者能够利用 GPU
的强大性能显著加速计算应用。在经 GPU 加速的应用中，工作负载的串行部分在 CPU 上运行，且 CPU
已针对单线程性能进行优化，而应用的计算密集型部分则以并行方式在数千个 GPU 核心上运行。使用 CUDA 时，开发者使用主流语言（如
C、C++、Fortran、Python 和
MATLAB）进行编程，并通过扩展程序以几个基本关键字的形式来表示并行性。由于tensorflow最高版本对应的是cuda10.1版本，那下载cuda10.1即可。
**安装包链接：https://developer.nvidia.com/cuda-toolkit-archive**

![](https://img.jbzj.com/file_images/article/202012/2020121511070662.jpg)

![](https://img.jbzj.com/file_images/article/202012/2020121511070663.jpg)

![](https://img.jbzj.com/file_images/article/202012/2020121511070664.jpg)

CUDA的下载需要挂载VPN，否则下下来只有1kb (好像后面又不一定需要VPN，可以直接下载试试）

自定义安装，安装的东西全选了，尽量不要改安装位置

![](https://img.jbzj.com/file_images/article/202012/2020121511070765.jpg)

安装完之后安装cuDNN, cuDNN是用于深度神经网络的GPU加速库.注意安装的版本，选择自身cuda版本对应的cudnn下载。

**官网：** [ https://developer.nvidia.com/rdp/cudnn-archive
](https://developer.nvidia.com/rdp/cudnn-archive) **** ，cuDNN的下载需要注册官网的账号

![](https://img.jbzj.com/file_images/article/202012/2020121511070766.jpg)

下载好的cudnn文件解压后，将文件夹内的文件放到cuda对应文件夹下， **注意：是文件夹内的文件，而不要直接复制替换文件夹**

![](https://img.jbzj.com/file_images/article/202012/2020121511070767.jpg)

**第三步，安装** **tensorflow―gpu**

在anaconda prompt里面安装：pip install tensorflow-gpu ， 后面可以指定版本号，下载慢挂载一个镜像源 -i
https://pypi.tuna.tsinghua.edu.cn/simple

![](https://img.jbzj.com/file_images/article/202012/2020121511070768.jpg)

安装完成：

![](https://img.jbzj.com/file_images/article/202012/2020121511070769.jpg)

测试是否安装成功：

```python

    import tensorflow as tf
    tf.test.is_gpu_available()
```

![](https://img.jbzj.com/file_images/article/202012/2020121511070870.jpg)

![](https://img.jbzj.com/file_images/article/202012/2020121511070871.jpg)

True即表示安装成功了。

**查看版本号：** ![](https://img.jbzj.com/file_images/article/202012/2020121511070872.jpg)

至此安装成功，可以跑一个小程序测试一下。

```python

    import tensorflow as tf
    import os
    os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
     
    a = tf.constant(1.)
    b = tf.constant(2.)
    print(a+b)
    print('GPU:', tf.test.is_gpu_available())
```

显示“GPU True”, 也即代表GPU版本安装成功。

经过几天调了一下代码之后发现tensorflow2相对与1还是有挺多改动的，1里面能够运行的代码可能2里面需要一定的修改。

关于Tensorflow2和1上面keras的一些区别可以搜一下相关的资料。

到此这篇关于Window10上Tensorflow的安装(CPU和GPU版本)的文章就介绍到这了,更多相关Window10安装Tensorflow
内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

