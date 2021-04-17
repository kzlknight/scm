不知道大家有没有过这种经历，就是想要判断两个数组运算后得到的新数组中的各个元素值是否相同。这里给出一种使用np.unique()的方法，代码如下：

```python

    import numpy as np
    
    
    class Debug:
     @staticmethod
     def isAllElementSame():
     x1 = np.array([[1, 2, 3], [3, 4, 5], [6, 7, 8]])
     x2 = np.array([[81., 162., 243., ], [243., 324., 405.], [486., 567., 648.]])
     print('The result if x2/x1 is:')
     print(x2 / x1)
     print('Judge whether all elements in array are same or not')
     print(len(np.unique(x2 / x1)) == 1)
    
    
    if __name__ == '__main__':
     debug = Debug()
     debug.isAllElementSame()
    """
    The result if x2/x1 is:
    [[81. 81. 81.]
     [81. 81. 81.]
     [81. 81. 81.]]
    Judge whether all elements in array are same or not
    True
    """
    
```

可以看到，当输出为True的时候，表明数组中的所有元素的值均一致，反之，当为False的时候，数组中存在不一样的元素值。

如果数组中的元素是复数呢？

```python

    import numpy as np
    
    
    class Debug:
     @staticmethod
     def isAllElementSame():
      x1 = np.array([complex(1, 2), complex(2, 4)])
      x2 = np.array([complex(2, 4), complex(4, 8)])
      print('The result if x2/x1 is:')
      print(x2 / x1)
      print('Judge whether all elements in array are same or not')
      print(len(np.unique(x2 / x1)) == 1)
    
    
    if __name__ == '__main__':
     debug = Debug()
     debug.isAllElementSame()
    """
    The result if x2/x1 is:
    [2.+0.j 2.+0.j]
    Judge whether all elements in array are same or not
    True
    """
    
```

可以看到，当数组元素为复数时，该方法仍然适用。然而当数组元素为小数时，可能会失效，如果失效，加上np.round()函数并设定所需要保留的有效位小数即可，例如：print(len(np.unique(np.round(x2
/ x1))) == 1)。

到此这篇关于利用python查看数组中的所有元素是否相同的文章就介绍到这了,更多相关python查看数组元素相同内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

