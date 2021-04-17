我们可以把表里每一个横行的数据，看成是不同的元组。在理解了这个概念后，昨天我们学了不少的namedtuple类，是否也能把元组转换成namedtuple呢？当然这是一个尝试，很多小伙伴平时使用的时候会很少用到，而且资料的搜集方面也比较难找。小编也搜集了很久才有收获，本篇就为大家带来元组在python中转换为namedtuple的方法。

之前我们了解了为什么使用namedtuple，现在该学习如何将常规元组和转换为namedtuple了。假设由于某种原因，有包含彩色RGBA值的实例。如果要将其转换为Color
namedtuple，则可以按以下步骤进行：

```python

    >>> c = {"r": 50, "g": 205, "b": 50, "alpha": alpha}
    >>> Color(**c)
    >>> Color(r=50, g=205, b=50, alpha=0)
```

我们可以利用该**结构将包解压缩dict为namedtuple。

元组类似于列表，是一个基于位置的有序对象集合，但是元组一旦创建之后就不能更改，因此列表中修改元素的操作对于元组都不适用。

使用()就可以创建元组，元素之间使用英文逗号,隔开。

```python

    num_tuple = (1, 2, 3)
    string_tuple = ("a", )
```

如果我想从dict创建一个namedtupe，如何做？

```python

    >>> c = {"r": 50, "g": 205, "b": 50, "alpha": alpha}
    >>> Color = namedtuple("Color", c)
    >>> Color(**c)
    Color(r=50, g=205, b=50, alpha=0)
```

过将dict实例传递给namedtuple工厂函数，它将为你创建字段。然后，Color像上边的例子一样解压字典c，创建新实例。

运行代码后，就可以把元组转换为namedtuple了。

元组转换为namedtuple实例扩展：

在内部使用namedtuples，但我想保持与提供普通元组的用户的兼容性。

```python

    from collections import namedtuple
    tuplePi=(1,3.14,"pi") #Normal tuple 
    Record=namedtuple("MyNamedTuple", ["ID", "Value", "Name"])
    namedE=Record(2, 2.79, "e") #Named tuple
    namedPi=Record(tuplePi) #Error
    TypeError: __new__() missing 2 required positional arguments: 'Value' and 'Name'
    tuplePi.__class__=Record
    TypeError: __class__ assignment: only for heap types
```

到此这篇关于python中把元组转换为namedtuple方法的文章就介绍到这了,更多相关元组在python中如何转换为namedtuple内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

