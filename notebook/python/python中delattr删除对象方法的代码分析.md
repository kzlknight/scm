最近我们针对对象属性这块，介绍了不少关于测试属性的方法。在进行一系列测试后，我们发现这个属性并不需要，这时候就要用到删除的功能。在python中可以选择delattr函数删除对象的属性，基于它的删除功能，是否能扩展到删除的对象的方法上，在我们对delattr函数进行全面了解后，展开实例的测试。

**1.说明**

函数作用用来删除指定对象的指定名称的属性，和setattr函数作用相反。

不能删除对象的方法。

**2.参数**

object -- 对象。

name -- 必须是对象的属性。

**3.返回值**

无。

**4.实例**

```python

    >>> a.sayHello
    <bound method A.sayHello of <__main__.A object at 0x03F014B0>>
    >>> delattr(a,'sayHello') #不能用于删除方法
    Traceback (most recent call last):
     File "<pyshell#50>", line 1, in <module>
      delattr(a,'sayHello')
    AttributeError: sayHello
    >>>
```

通过测试的结果，我们可以看出delattr函数并不能删除对象的方法，只针对于属性有删除的功能，不然就会报错。相信本篇的实战代码演示能让大家对注意点有一个深刻的印象。

###  Python3基础 delattr 删除对象的属性

```python

    class MyClass:
      # num是类属性
      num = 1
    
      def __init__(self, name):
        self.name = name
    
    
    def main():
      test = MyClass("shemingli")
    
      # 删除类属性
      # 删除类属性要写类名，而不是实例名
      delattr(MyClass, "num")
    
      # 删除实例属性
      delattr(test, "name")
    
      """
        def delattr(o: Any, name: str)
        Inferred type: (o: Any, name: str) -> None
    
        Deletes the named attribute from the given object.
        delattr(x, 'y') is equivalent to ``del x.y''
      """
      # 注：如果属性不存在，就抛出异常
    
    
    if __name__ == '__main__':
      main()
    
```

到此这篇关于python中delattr删除对象方法的代码分析的文章就介绍到这了,更多相关python中delattr可以删除对象方法吗内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

