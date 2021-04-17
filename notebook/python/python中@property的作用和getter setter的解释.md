###  @property作用：

python的@property是python的一种装饰器，是用来修饰方法的。

我们可以使用@property装饰器来创建只读属性，@property装饰器会将方法转换为相同名称的只读属性,可以与所定义的属性配合使用，这样可以防止属性被修改。

###  1.修饰方法，让方法可以像属性一样访问。

```python

    class DataSet(object):
     @property
     def method_with_property(self): ##含有@property
       return 15
     def method_without_property(self): ##不含@property
       return 15
    
    l = DataSet()
    print(l.method_with_property) # 加了@property后，可以用调用属性的形式来调用方法,后面不需要加（）。
    print(l.method_without_property()) #没有加@property , 必须使用正常的调用方法的形式，即在后面加()#两个都输出为15。
```

如果使用property进行修饰后，又在调用的时候，方法后面添加了()， 那么就会显示错误信息：TypeError: 'int' object is not
callable，也就是说添加@property 后，这个方法就变成了一个属性，如果后面加入了

()，那么就是当作函数来调用，而它却不是callable（可调用）的。

###  2.与所定义的属性配合使用，这样可以防止属性被修改。

由于python进行属性的定义时，没办法设置私有属性，因此要通过@property的方法来进行设置。这样可以隐藏属性名，让用户进行使用的时候无法随意修改。

```python

    class DataSet(object):
      def __init__(self):
        self._images = 1
        self._labels = 2 #定义属性的名称
      @property
      def images(self): #方法加入@property后，这个方法相当于一个属性，这个属性可以让用户进行使用，而且用户有没办法随意修改。
        return self._images 
      @property
      def labels(self):
        return self._labels
    l = DataSet()
    #用户进行属性调用的时候，直接调用images即可，而不用知道属性名_images，因此用户无法更改属性，从而保护了类的属性。
    print(l.images) # 加了@property后，可以用调用属性的形式来调用方法,后面不需要加（）。
```

###  getter和setter方法:

把一个getter方法变成属性，只需要加上 ` @property ` 就可以了，此时， ` @property ` 本身又创建了另一个装饰器 `
@score.setter ` ，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：

```python

    class Student(object):
    
      @property
      def score(self):
        return self._score
    
      @score.setter
      def score(self, value):
        if not isinstance(value, int):
          raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
          raise ValueError('score must between 0 ~ 100!')
        self._score = value
```

我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。

还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：

```python

    class Student(object):
    
      @property
      def birth(self):
        return self._birth
    
      @birth.setter #设置属性
      def birth(self, value):
        self._birth = value
    
      @property
      def age(self):
        return 2015 - self._birth
```

上面的 ` birth ` 是可读写属性，而 ` age ` 就是一个只读属性，因为 ` age ` 可以根据 ` birth ` 和当前时间计算出来。

小结

` @property ` 广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。

到此这篇关于python中@property的作用和getter
setter的解释的文章就介绍到这了,更多相关python中@property的作用和getter
setter内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

