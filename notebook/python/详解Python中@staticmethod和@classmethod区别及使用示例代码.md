本文主要介绍Python中,class(类)的装饰器@staticmethod和@classmethod的使用示例代码和它们的区别。  

###  1、@staticmethod和@classmethod区别

@staticmethod：静态方法

@classmethod：类方法

一般来说，要使用某个类的方法，需要先实例化一个对象再调用方法。

而使用@staticmethod或@classmethod，就可以不需要实例化，直接通过类名就可以实现调用

使用：直接类名.方法名()来调用。@staticmethod和@classmethod都可以直接类名.方法名()来调用,

@staticmethod不需要表示自身对象的self和自身类的cls参数（这两个参数都不需要添加），就跟使用函数一样。

使用：直接类名.属性名或直接类名.方法名。

@classmethod也不需要self参数，但第一个参数需要是表示自身类的cls参数。

使用：直接类名.属性名或直接类名.方法名。

两者定义的装饰器调用方法一样，但是@classmethod装饰器定义的类方法需要传入类参数cls。

@staticmethod中要调用到这个类的一些属性方法，只能直接类名.属性名或类名.方法名。

而@classmethod有cls参数，可以来调用类的属性，类的方法，实例化对象等，避免硬编码更灵活。

###  2、@staticmethod和@classmethod使用示例代码

```python

    class A(object):
      def foo(self, x):
        print "executing foo(%s, %s)" % (self, x)
      @classmethod
      def class_foo(cls, x):
        print "executing class_foo(%s, %s)" % (cls, x)
      @staticmethod
      def static_foo(x):
        print "executing static_foo(%s)" % x  
    a = A()
    #通过实例调用方法，对象实例a作为第一个参数隐式传递。
    a.foo (1)
    # executing foo(<__main__.A object at 0xb7dbef0c>,1)
    #对于类方法，对象实例的类将隐式地作为第一个参数而不是传递self
    a.class_foo(1)
    # executing class_foo(<class '__main__.A'>,1)
    #使用这个类调用class_foo
    A.class_foo(1)
    # executing class_foo(<class '__main__.A'>,1)
    #对于staticmethods,self(对象实例)和cls(类)都不会作为第一个参数隐式传递。它们的行为类似普通函数，除了你可以从实例或类中调用它们
    a.static_foo(1)
    # executing static_foo(1)
    A.static_foo('hi')
    # executing static_foo(hi)
    print(a.foo)
    # <bound method A.foo of <__main__.A object at 0xb7d52f0c>>
    print(a.class_foo)
    # <bound method type.class_foo of <class '__main__.A'>>
    print(a.static_foo)
    # <function static_foo at 0xb7d479cc>
    print(a.static_foo)
    # <function static_foo at 0xb7d479cc>
     
```

总结一下彼此的调用区别：  

![](https://img.jbzj.com/file_images/article/202012/20201214100921565.png?2020111410942)

到此这篇关于详解Python中@staticmethod和@classmethod区别及使用示例代码的文章就介绍到这了,更多相关Python
@staticmethod和@classmethod内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

