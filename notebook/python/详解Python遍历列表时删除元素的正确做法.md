###  一.问题描述

这是在工作中遇到的一段代码，原理大概和下面类似(判断某一个元素是否符合要求，不符合删除该元素，最后得到符合要求的列表)：

```python

    a = [1,2,3,4,5,6,7,8]
    for i in a:
      if i>5:
        pass
      else:
        a.remove(i)
      print(a)
```

运行结果：

![](https://img.jbzj.com/file_images/article/202101/202101070856321.png)

###  二.问题分析

因为删除元素后，整个列表的元素会往前移动，而i却是在最初就已经确定了，是不断增大的，所以并不能得到想要的结果。

###  三.解决方法

**1.遍历在新的列表操作，删除是在原来的列表操作**

```python

    a = [1,2,3,4,5,6,7,8]
    print(id(a)) 
    print(id(a[:])) 
    for i in a[:]:
      if i>5:
        pass
      else:
        a.remove(i)
      print(a)
    print('-------------------------')
    print(id(a))
```

运行结果：

![](https://img.jbzj.com/file_images/article/202101/202101070856332.png)

**2.filter**

内建函数filter()官方文档参考： [ https://docs.python.org/3/library/functions.html#filter
](https://docs.python.org/3/library/functions.html#filter)

```python

    a = [1,2,3,4,5,6,7,8]
    b = filter(lambda x: x>5,a)
    print(list(b))
```

运行结果：

![](https://img.jbzj.com/file_images/article/202101/202101070856333.png)

**3.列表解析**

```python

    a = [1,2,3,4,5,6,7,8]
    b = [i for i in a if i >5]
    print(b)
```

运行结果：

![](https://img.jbzj.com/file_images/article/202101/202101070856334.png)

**4.倒序删除**

因为列表总是“向前移”，所以可以倒序遍历，即使后面的元素被修改了，还没有被遍历的元素和其坐标还是保持不变的。

```python

    a = [1,2,3,4,5,6,7,8]
    print(id(a))
    for i in range(len(a)-1,-1,-1):
      if a[i] > 5:
        pass
      else:
        a.remove(a[i])
    print(id(a))
    print('--------------------')
    print(a)
```

运行结果：

![](https://img.jbzj.com/file_images/article/202101/202101070856335.png)

到此这篇关于详解Python遍历列表时删除元素的正确做法的文章就介绍到这了,更多相关Python遍历列表删除元素内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

