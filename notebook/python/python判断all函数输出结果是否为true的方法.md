我们们都学会判断真假，根据条件的不同，最终输出的结果可能为真，可能为假。在python的函数中，也有一个内置函数需要进行条件判断，那么在什么样的情况下，我们才能确保它输出的结果是true呢？今天就all函数的判断，我们进行简单的代码体验，然后分析在不同条件下，all函数的输出情况。

###  内置函数all

接收一个可迭代对象，如果其中所有的元素都是True，或者该可迭代对象中没有元素，返回True

等价于

```python

    def all(iterable):
      for element in iterable:
        if not element:
          return False
    return True
```

说明：

**1. 接受一个可迭代器对象为参数，当参数为空或者不为可迭代器对象是报错**

```python

    >>> all(2) #传入数值报错
    Traceback (most recent call last):
     File "<pyshell#9>", line 1, in <module>
      all(2)
    TypeError: 'int' object is not iterable
```

**2. 如果可迭代对象中每个元素的逻辑值均为True时，返回True，否则返回False**

```python

    >>> all([1,2]) #列表中每个元素逻辑值均为True，返回True
    True
    >>> all([0,1,2]) #列表中0的逻辑值为False，返回False
    False
```

**3. 如果可迭代对象为空(元素个数为0)，返回True**

```python

    >>> all(()) #空元组
    True
    >>> all({}) #空字典
    True
```

以上就是我们对于判断all函数输出结果为true的分析，我们需要注意的是输出条件的改变，对应的结果也会出现变化。

到此这篇关于python判断all函数输出结果是否为true的方法的文章就介绍到这了,更多相关python中如何判断all函数输出结果为true内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

