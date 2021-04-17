###  1.figure语法及操作  

**(1)figure语法说明**

  * figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True) 
  * num:图像编号或名称，数字为编号 ，字符串为名称 
  * figsize:指定figure的宽和高，单位为英寸； 
  * dpi参数指定绘图对象的分辨率，即每英寸多少个像素，缺省值为80 1英寸等于2.5cm,A4纸是 21*30cm的纸张 
  * facecolor:背景颜色 
  * edgecolor:边框颜色 
  * frameon:是否显示边框 

**(2)例子:**

```python

    import matplotlib.pyplot as plt
```

创建自定义图像  

```python

    fig=plt.figure(figsize=(4,3),facecolor=‘blue')
    plt.show()
```

###  2.subplot创建单个子图  

(1) subplot语法

```python

    subplot(nrows,ncols,sharex,sharey,subplot_kw,**fig_kw)
```

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010814251518.png)

**代码运行及演示**  
![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010814251519.png)  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010814251520.png)  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010814251521.png)  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010814251622.png)  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010814251623.png)  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010814251624.png)

###  plt.figure(figsize=(a,b))和plt.subplot()函数区别

**plt.figure(figsize=(6,8))**  
表示figure 的大小为宽、长（单位为inch）

> figsize : (float, float), optional, default: None  
>  width, height in inches. If not provided, defaults to  
>  rcParams[“figure.figsize”] = [6.4, 4.8].

**plt.subplot(121)**  
表示整个figure分成1行2列，共2个子图，这里子图在第一行第一列  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010814300025.png)

**plt.subplot(122)**  

表示子图在第一行第二列  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010814300026.png)

到此这篇关于plt.figure()参数使用详解及运行演示的文章就介绍到这了,更多相关plt.figure()参数内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

