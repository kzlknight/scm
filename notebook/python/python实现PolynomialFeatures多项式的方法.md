###  sklearn生成多项式

```python

    import numpy as np
    from sklearn.preprocessing import PolynomialFeatures  #这哥用于生成多项式
    x=np.arange(6).reshape(3,2) #生成三行二列数组
    reg = PolynomialFeatures(degree=3) #这个3看下面的解释
    reg.fit_transform(x)
```

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/20210106160918106.png)  

x是下面这样：  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/20210106160918107.png)  

我们发现规律如下：

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/20210106160918108.png)

###  Python生成多项式

编写实现函数如下：

```python

    def multi_feature(x,n):
      c = np.empty((x.shape[0],0)) #np.empty((3,1))并不会生成一个3行1列的空数组,np.empty((3,0))才会生成3行1列空数组
      for i in range(n+1):
        for m in range(i,-1,-1):
          h=(x[:,0]**m) * (x[:,1]**(i-m))
          c=np.c_[c,h]
      return c
    
    multi_feature(x,3)
```

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/20210106160918109.png)  

和上面实现的一模一样

```python

    print('n=4时，sklearn的输出是：')
    reg = PolynomialFeatures(degree=4) 
    print(reg.fit_transform(x))
    print('\n')
    
    #对比
    print('n=4时，函数的输出是：')
    print(multi_feature(x,4))
```

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/20210106160918110.png)  

也是一样的，当然这个函数仅适用于2维数组，如果是n维数组，又该怎么实现呢？

到此这篇关于python实现PolynomialFeatures多项式的方法的文章就介绍到这了,更多相关python
PolynomialFeatures多项式内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

