**前言**

数据驱动测试：

  * 避免编写重复代码 
  * 数据与测试脚本分离 
  * 通过使用数据驱动测试，来验证多组数据测试场景 
  * 通常来说，多用于单元测试和接口测试   

**ddt介绍  
**

Data-Driven Tests（DDT）即数据驱动测试，可以实现不同数据运行同一个测试用例。ddt本质其实就是装饰器，一组数据一个场景。

ddt模块包含了一个类的装饰器ddt和三个个方法的装饰器：

data：包含多个你想要传给测试用例的参数，可以为列表、元组、字典等；

file_data:会从json或yaml中加载数据；

unpack:分割元素，如以下示例：

@data([a,d],[c,d])

如果没有@unpack，那么[a,b]当成一个参数传入用例运行

如果有@unpack，那么[a,b]被分解开，按照用例中的两个参数传递

**安装  
**

pip install ddt  

**使用data装饰器**  

传递整体列表，字典、元组

```python

    import unittest
    from ddt import ddt,data,unpack
    def add(a,b):
      return a+b
    @ddt
    class MyTest(unittest.TestCase):
      # @data([1,2,3,4,5,6,7])
      @data({"a":"1","b":2})
      # @data((1,2,3))
      def test(self,data):
        print(data)
    if __name__ == '__main__':
      unittest.main(verbosity=2)
```

嵌套列表、元组、字典的整体传递方式

```python

    import unittest
    from ddt import ddt,data,unpack
    def add(a,b):
      return a+b
    @ddt
    class MyTest(unittest.TestCase):
      # @data(*[[1,2,3],[1,0,1],[0,0,0],[1,1,3]])
      # @data(*[{"a":1}, {"a":2}, {"a":3}, {"a":4}])
      @data(*[(1,5), (4,2), (6,7), (5,6)])
      def test(self,data):
        print(data)
    
    if __name__ == '__main__':
      unittest.main(verbosity=2)
```

**使用unpack装饰器  
**

**unpack 依次传递元组**

```python

    import unittest
    from ddt import ddt,data,unpack
    def add(a,b):
      return a+b
    @ddt
    class MyTest(unittest.TestCase):
      @data((1,2,3),(1,0,1),(0,0,0),(1,1,3))
      @unpack
      def test(self,a,b,c):
        print(a,b,c)
        if a+b == c:
          print(True)
        else:
          print(False)
    if __name__ == '__main__':
      unittest.main(verbosity=2)
```

输出结果：

> 1 2 3  
>  True  
>  1 0 1  
>  True  
>  0 0 0  
>  True  
>  1 1 3  
>  False  
>

依次传递字典

```python

    import unittest
    from ddt import ddt,data,unpack
    
    def add(a,b):
      return a+b
    @ddt
    class MyTest(unittest.TestCase):
      @data({"a":1,"b":1,"c":2},
         {"a":0,"b":0,"c":0},
         {"a":-1,"b":1,"c":0})
      @unpack
      def test(self,a,b,c):
        print(a,b,c)
        if a + b == c:
          print(True)
        else:
          print(False)
    
    if __name__ == '__main__':
      unittest.main(verbosity=2)
```

输出结果：

> 1 1 2  
>  True  
>  0 0 0  
>  True  
>  -1 1 0  
>  True  
>

依次传递列表

```python

    import unittest
    from ddt import ddt,data,unpack
    
    def add(a,b):
      return a+b
    @ddt
    class MyTest(unittest.TestCase):
      @data([1,2,3],[1,0,1],[0,0,0],[1,1,3])
      @unpack
      def test(self,a,b,c):
        print(a,b,c)
        if a + b == c:
          print(True)
        else:
          print(False)
    
    if __name__ == '__main__':
      unittest.main(verbosity=2)
```

输出结果：

> 1 2 3  
>  True  
>  1 0 1  
>  True  
>  0 0 0  
>  True  
>  1 1 3  
>  False

**使用file_data装饰器**  

ddt支持从文件中加载数据，@file_data()装饰器会从json或yaml中加载数据。只有以“.yml” 和 “.yaml”
结尾的文件被加载为Yaml文件。所有其他格式文件都作为json文件加载，比如txt。

传递json数据

test.json文件

```python

    {
      "case1": {
        "a": 1,
        "b": 1,
        "c": 2
      },
      "case2": {
        "a": -1,
        "b": 1,
        "c": 0
      },
      "case3": {
        "a": 0,
        "b": 0,
        "c": 0
      }
    }
```

```python

    import unittest
    from ddt import ddt,file_data
    
    def add(a,b):
      return a+b
    
    @ddt
    class MyTest(unittest.TestCase):
      @file_data("test.json")
      def test(self, a, b, c):
        print(a,b,c)
    
    
    if __name__ == '__main__':
      unittest.main(verbosity=2)
```

传递多层json文件  

test.json文件  

```python

    {
      "case1": {
        "data": {
          "a": 1,
          "b": 1
        },
        "result": 2
      },
      "case2": {
        "data": {
          "a": 0,
          "b": 1
        },
        "result": 1
      },
      "case3": {
        "data": {
          "a": 0,
          "b": 0
        },
        "result": 0
      }
    }
```

```python

    import unittest
    from ddt import ddt,file_data
    
    def add(a,b):
      return a+b
    
    @ddt
    class MyTest(unittest.TestCase):
      @file_data("test.json")
      def test(self,data,result):
        print(data,result)
    
    if __name__ == '__main__':
      unittest.main(verbosity=2)
```

**传递yml数据**

yml 需要安装yml（pip install PyYAML）  

test.yml

![](https://img.jbzj.com/file_images/article/202011/20201130113101427.png?20201030113115)

```python

    def add(a,b):
      return a+b
    @ddt
    class MyTest(unittest.TestCase):
      @file_data("test.yml")
      def test(self,a,b,c):
        print(a,b,c)
```

以上就是本文的全部内容，希望对大家的学习有所帮助，也希望大家多多支持脚本之家。

