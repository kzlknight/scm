本文实例讲述了Python面向对象程序设计之继承与多继承。分享给大家供大家参考，具体如下：

**1. 继承**

在C++和Java中，使用继承时，子类的构造函数会自动调用父类的构造函数，但在Python中，子类必须显式的在 ` __init__() `
函数中再次调用父类中的 ` __init__() ` 函数。如下例：

```python

    class Employee(object):
      def __init__(self, name, salary = 0):
        self.name = name
        self.salary = salary
      def raisesalary(self, percent):
        self.salary = self.salary * (1 + percent)
      def work(self):
        print self.name, "writes computer code"
    class Designer(Employee):
      def __init__(self, name):
        Employee.__init__(self, name, 5000)
      def work(self):
        print self.name, "writes design document"
    
    
```

子类Designer也可以使用 ` super ` 来进行初始化。

```python

    class Designer(Employee):
      def __init__(self, name):
        super(Designer, self).__init__(name, 5000)
      def work(self):
        print self.name, "writes design document"
    
    
```

**2. 多继承**

在C++中，使用虚继承来实现多继承，以避免子类在继承时多次调用基类的构造函数，而在Java中，则取消了多继承，使用接口来达到多继承的效果。在Python中的解决方案是MRO即Method
Resolution Order，方法解析顺序。主要是通过 ` super ` 方法实现的。但如果用 ` super `
方法来解决多继承问题，由于各个父类中的 ` __init__() ` 函数中参数的数量可能不同，那应该怎么初始化呢？如下例。

```python

    class A(object):
      def __init__(self, a):
        print a
    class B(object):
      def __init__(self, a, b):
        print a+b
    class C(A, B):
      def __init__(self):
        super(C,self).__init__(?)
    c = C()
    
    
```

则？处应该填几个参数？

答案是1个参数，因为按照继承的顺序，A类中的构造需要1个参数初始化即可。即 ` super ` 函数与父类的继承顺序有关，且初始化父类继承顺序中，最先有 `
__init__() ` 方法的那个。

` super ` 方法的使用仍在继续探索中。。。

更多关于Python相关内容感兴趣的读者可查看本站专题：《 [ Python面向对象程序设计入门与进阶教程
](//www.jb51.net/Special/684.htm) 》、《 [ Python数据结构与算法教程
](//www.jb51.net/Special/663.htm) 》、《 [ Python函数使用技巧总结
](//www.jb51.net/Special/642.htm) 》、《 [ Python字符串操作技巧汇总
](//www.jb51.net/Special/636.htm) 》、《 [ Python编码操作技巧总结
](//www.jb51.net/Special/788.htm) 》及《 [ Python入门与进阶经典教程
](//www.jb51.net/Special/520.htm) 》

希望本文所述对大家Python程序设计有所帮助。

