**介绍**

init 方法通常用在初始化一个类实例时候，但其实它不是实例化一个类的时候第一个被调用 的方法。当使用 Student(id, name)
这样的表达式来实例化一个类时，最先被调用的方法 其实是 new 方法。

new方法接受的参数虽然也是和init一样，但init是在类实例创建之后调用，而 new方法正是创建这个类实例的方法。

new为对象分配空间，是内置的静态方法，new在内存中为对象分配了空间也返回了对象的引用，init获得了这个引用才初始化这个实例。

**示例**

一个非常简单的单例

```python

    class A:
     instance = None
     def __new__(cls, *args, **kwargs):
      if cls.instance is None:
       cls.instance = super().__new__(cls)
      return cls.instance
```

因为new方法是一个静态方法（也就是在定义的时候就没有cls参数），所以在这里要传入一个cls参数，而且这里的new你改造过了，所以要返回爸爸的new方法。

按造这个方法改造的单例怎么new都是同一个实例，但init仍然会被执行多次，也就是创建了几个对象就调用几次初始化方法。所以还要对init再进行一些判断。

```python

    class A:
     instance = None
     init_flag = False # 初始化标记
    
     def __new__(cls, *args, **kwargs):
      if cls.instance is None:
       cls.instance = super().__new__(cls)
      return cls.instance
    
     def __init__(self):
      if A.init_flag:
       return
      print('执行了初始化方法')
      A.init_flag = True
    
    if __name__ == '__main__':
     a = A()
     b = A()
     print(a)
     print(b)
    
```

**输出结果：**

执行了初始化方法

> <main.A object at 0x00000210E6F09320>
>
> <main.A object at 0x00000210E6F09320>

**总结**

通过重载new方法，可以比较简单地实现单例，Python还有很多有趣的内置函数，有空可以再研究研究。

**补充知识：** **Python饿汉式和懒汉式单例模式的实现**

看代码吧~

```python

    # 饿汉式
    class Singleton(object):
     # 重写创建实例的__new__方法
     def __new__(cls):
      # 如果类没有实例属性，进行实例化，否则返回实例
      if not hasattr(cls, 'instance'):
       cls.instance = super(Singleton, cls).__new__(cls)
      return cls.instance
```

饿汉式在创建的时候就会生成实例

```python

    # 懒汉式
    class Singleton(object):
     __instance = None
     def __init__(self):
      if not self.__instance:
       print('调用__init__， 实例未创建')
      else:
       print('调用__init__，实例已经创建过了:', __instance)
    
     @classmethod
     def get_instance(cls):
      # 调用get_instance类方法的时候才会生成Singleton实例
      if not cls.__instance:
       cls.__instance = Singleton()
      return cls.__instance
    
```

以上这篇Python 用__new__方法实现单例的操作就是小编分享给大家的全部内容了，希望能给大家一个参考，也希望大家多多支持脚本之家。

