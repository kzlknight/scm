一场大雪，覆盖了华北、华东。天地连成一片，城市银装素裹，处处诗情画意、人人兴高采烈。朋友圈被雪景图和调侃路滑摔跤的段子刷屏，气氛比过年还要热烈几分。我也来凑个热闹，用python为2020年的第一场雪锦上添花。

绘制雪花图案，网上有很多文章介绍，但几乎都是用 Python 的内置模块 turtle
绘制的，这个模块适合用来引导孩子学习编程，很难真正用在项目开发上。也有用 pygame 实现的，不过 pygame
追求的是动画效果，雪花图案是随机生成的圆，效果很一般。

用 matplotlib 绘制雪花，重点是生成科赫曲线（Koch
Curve）。科赫曲线是一种分形，其形态似雪花，又称科赫雪花、雪花曲线。给定线段pq，k阶科赫曲线可以由以下步骤生成：

  * 找出三等分点u、v 
  * 以线段uv为底，向外（或内外）画等边三角形uwv 
  * 将线段uv移除 
  * 对pq之间的每一段重复上述操作k-1次 

科赫雪花是以等边三角形三边生成的科赫曲线组成的。基于上述分析，我们可以很容易地写出科赫雪花的生成函数：给定一个等边三角形，和科赫曲线阶数k，返回科赫雪花图案中的所有点。

```python

    import numpy as np
    
    plt.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
    plt.rcParams['axes.unicode_minus'] = False #解决中文显示为方块的问题
    
    def rotate(p, d):
      """返回点p绕原点逆时针旋转d度的坐标"""
      
      a = np.radians(d)
      m = np.array([[np.cos(a), np.sin(a)],[-np.sin(a), np.cos(a)]])
      return np.dot(p, m)
    
    def koch_curve(p, q):
      """将线段pq生成科赫曲线，返回uvw三个点"""
      
      p, q = np.array(p), np.array(q)
      u = p + (q-p)/3 # 三等分点u的坐标
      v = q - (q-p)/3 # 三等分点V的坐标
      w = rotate(v-u, 60) + u # 线段uv绕u点逆时针旋转60°得到点w的坐标
      
      return u.tolist(), v.tolist(), w.tolist()
      
    def snow(triangle, k):
      """给定三角形，生成封闭的科赫雪花"""
      
      for i in range(k):
        result = list()
        t_len = len(triangle)
        for j in range(t_len):
          p = triangle[j]
          q = triangle[(j+1)%t_len]
          u, v, w = koch_curve(p, q)
          result.extend([p, u, w, v])
        triangle = result.copy()
      
      triangle.append(triangle[0])
      return triangle
```

有了雪花图案的数据，接下来使用 matplotlib 绘图就非常轻松了：

```python

    import numpy as np
    import matplotlib.pyplot as plt
    
    def plot_snow(snow_list):
      """绘制雪花"""
      
      for triangle, k in snow_list:
        data = np.array(snow(triangle, k))
        x, y = np.split(data, 2, axis=1)
        plt.plot(x, y)
      
      plt.axis('equal') 
      plt.show()
    
    snow_list = [
      ([(0,0), (0.5,0.8660254), (1,0)], 5),
      ([(1.1,0.4), (1.35,0.8330127), (1.6,0.4)], 4),
      ([(1.1,-0.1), (1.25,0.15980761), (1.4,-0.1)], 3)
    ]
    plot_snow(snow_list)
```

来看看我们的雪花效果。从小到大，3片雪花分别对应的是3阶、4阶、5阶的科赫雪花。  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010510284932.png)  

更进一步，我们还可以把雪花画在背景图上，配合大小浓淡的变化，画出另一种韵味的雪景图。

```python

    import numpy as np
    import matplotlib.pyplot as plt
    from PIL import Image
    
    def draw_scenery():
      """绘制雪景图"""
      
      im = Image.open('brage.png')
      bg = np.array(im)
      plt.imshow(bg) # 绘制背景图
      
      for i in range(80):
        x = np.random.randint(80, im.size[0]-80)
        y = np.random.randint(30, im.size[1]-30)
        r = np.random.randint(5, 20)
        a = np.random.random()*0.6 + 0.2
        v = np.array((x-r/2, y))
        u = np.array((x+r/2, y))
        w = rotate(v-u, 60) + u
        
        data = np.array(snow([(u[0],u[1]),(w[0],w[1]),(v[0],v[1])], 5))
        x, y = np.split(data, 2, axis=1)
        plt.plot(x, y, c='#AABBCC', lw=1, ls='-', alpha=a)
      
      plt.axis('equal') 
      plt.show()
    
    draw_scenery()
```

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010510284933.png)

到此这篇关于为2021年的第一场雪锦上添花:用matplotlib绘制雪花和雪景的文章就介绍到这了,更多相关matplotlib绘制雪花和雪景内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

