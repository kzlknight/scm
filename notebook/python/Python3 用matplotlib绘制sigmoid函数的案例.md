我就废话不多说了，大家还是直接看代码吧~

```python

    import matplotlib.pyplot as plt
    import numpy as np 
    def sigmoid(x):
      # 直接返回sigmoid函数
      return 1. / (1. + np.exp(-x)) 
     
    def plot_sigmoid():
      # param:起点，终点，间距
      x = np.arange(-8, 8, 0.2)
      y = sigmoid(x)
      plt.plot(x, y)
      plt.show() 
     
    if __name__ == '__main__':
      plot_sigmoid()
```

如图：

![](https://img.jbzj.com/file_images/article/202012/20201211100438.jpg)

**补充知识：** **python：实现并绘制 sigmoid函数，tanh函数，ReLU函数，PReLU函数**

如下所示：

```python

    # -*- coding:utf-8 -*-
    from matplotlib import pyplot as plt
    import numpy as np
    import mpl_toolkits.axisartist as axisartist 
     
    def sigmoid(x):
      return 1. / (1 + np.exp(-x)) 
     
    def tanh(x):
      return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x)) 
     
    def relu(x):
      return np.where(x<0,0,x) 
     
    def prelu(x):
      return np.where(x<0,0.5*x,x)
     
    def plot_sigmoid():
      x = np.arange(-10, 10, 0.1)
      y = sigmoid(x)
      fig = plt.figure()
      # ax = fig.add_subplot(111)
      ax = axisartist.Subplot(fig,111)
      ax.spines['top'].set_color('none')
      ax.spines['right'].set_color('none')
      # ax.spines['bottom'].set_color('none')
      # ax.spines['left'].set_color('none')
      ax.axis['bottom'].set_axisline_style("-|>",size=1.5)
      ax.spines['left'].set_position(('data', 0))
      ax.plot(x, y)
      plt.xlim([-10.05, 10.05])
      plt.ylim([-0.02, 1.02])
      plt.tight_layout()
      plt.savefig("sigmoid.png")
      plt.show() 
     
    def plot_tanh():
      x = np.arange(-10, 10, 0.1)
      y = tanh(x)
      fig = plt.figure()
      ax = fig.add_subplot(111)
      ax.spines['top'].set_color('none')
      ax.spines['right'].set_color('none')
      # ax.spines['bottom'].set_color('none')
      # ax.spines['left'].set_color('none')
      ax.spines['left'].set_position(('data', 0))
      ax.spines['bottom'].set_position(('data', 0))
      ax.plot(x, y)
      plt.xlim([-10.05, 10.05])
      plt.ylim([-1.02, 1.02])
      ax.set_yticks([-1.0, -0.5, 0.5, 1.0])
      ax.set_xticks([-10, -5, 5, 10])
      plt.tight_layout()
      plt.savefig("tanh.png")
      plt.show() 
     
    def plot_relu():
      x = np.arange(-10, 10, 0.1)
      y = relu(x)
      fig = plt.figure()
      ax = fig.add_subplot(111)
      ax.spines['top'].set_color('none')
      ax.spines['right'].set_color('none')
      # ax.spines['bottom'].set_color('none')
      # ax.spines['left'].set_color('none')
      ax.spines['left'].set_position(('data', 0))
      ax.plot(x, y)
      plt.xlim([-10.05, 10.05])
      plt.ylim([0, 10.02])
      ax.set_yticks([2, 4, 6, 8, 10])
      plt.tight_layout()
      plt.savefig("relu.png")
      plt.show() 
     
    def plot_prelu():
      x = np.arange(-10, 10, 0.1)
      y = prelu(x)
      fig = plt.figure()
      ax = fig.add_subplot(111)
      ax.spines['top'].set_color('none')
      ax.spines['right'].set_color('none')
      # ax.spines['bottom'].set_color('none')
      # ax.spines['left'].set_color('none')
      ax.spines['left'].set_position(('data', 0))
      ax.spines['bottom'].set_position(('data', 0))
      ax.plot(x, y)
      plt.xticks([])
      plt.yticks([])
      plt.tight_layout()
      plt.savefig("prelu.png")
      plt.show() 
     
    if __name__ == "__main__":
      plot_sigmoid()
      plot_tanh()
      plot_relu()
      plot_prelu()
```

以上这篇Python3 用matplotlib绘制sigmoid函数的案例就是小编分享给大家的全部内容了，希望能给大家一个参考，也希望大家多多支持脚本之家。

