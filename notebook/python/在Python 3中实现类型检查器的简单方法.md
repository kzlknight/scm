**示例函数**

为了开发类型检查器，我们需要一个简单的函数对其进行实验。欧几里得算法就是一个完美的例子：  
  

```python

    def gcd(a, b):
      
    '''Return the greatest common divisor of a and b.'''
      a = abs(a)
      b = abs(b)
      if a < b:
        a, b = b, a
      while b != 0:
        a, b = b, a % b
      return a
    
```

在上面的示例中，参数 a 和 b 以及返回值应该是 int 类型的。预期的类型将会以函数注解的形式来表达，函数注解是 Python 3
的一个新特性。接下来，类型检查机制将会以一个装饰器的形式实现，注解版本的第一行代码是：  
  

```python

    def gcd(a: int, b: int) -> int:
    
```

使用“gcd.__annotations__”可以获得一个包含注解的字典：  
  

```python

    >>> gcd.__annotations__
    {'return': <class 'int'>, 'b': <class 'int'>, 'a': <class 'int'>}
    >>> gcd.__annotations__['a']
    <class 'int'>
    
```

需要注意的是，返回值的注解存储在键“return”下。这是有可能的，因为“return”是一个关键字，所以不能用作一个有效的参数名。  
**检查返回值类型**

返回值注解存储在字典“__annotations__”中的“return”键下。我们将使用这个值来检查返回值（假设注解存在）。我们将参数传递给原始函数，如果存在注解，我们将通过注解中的值来验证其类型：  
  

```python

    def typecheck(f):
      def wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        return_type = f.__annotations__.get('return', None)
        if return_type and not isinstance(result, return_type):
          raise RuntimeError("{} should return {}".format(f.__name__, return_type.__name__))
        return result
      return wrapper
```

我们可以用“a”替换函数gcd的返回值来测试上面的代码：  

```python

     
    Traceback (most recent call last):
     File "typechecker.py", line 9, in <module>
      gcd(1, 2)
     File "typechecker.py", line 5, in wrapper
      raise RuntimeError("{} should return {}".format(f.__name__, return_type.__name__))
    RuntimeError: gcd should return int
    
```

由上面的结果可知，确实检查了返回值的类型。  
**检查参数类型**

函数的参数存在于关联代码对象的“co_varnames”属性中，在我们的例子中是“gcd.__code__.co_varnames”。元组包含了所有局部变量的名称，并且该元组以参数开始，参数数量存储在“co_nlocals”中。我们需要遍历包括索引在内的所有变量，并从参数“args”中获取参数值，最后对其进行类型检查。

得到了下面的代码：  
  

```python

    def typecheck(f):
      def wrapper(*args, **kwargs):
        for i, arg in enumerate(args[:f.__code__.co_nlocals]):
          name = f.__code__.co_varnames[i]
          expected_type = f.__annotations__.get(name, None)
          if expected_type and not isinstance(arg, expected_type):
            raise RuntimeError("{} should be of type {}; {} specified".format(name, expected_type.__name__, type(arg).__name__))
        result = f(*args, **kwargs)
        return_type = f.__annotations__.get('return', None)
        if return_type and not isinstance(result, return_type):
          raise RuntimeError("{} should return {}".format(f.__name__, return_type.__name__))
        return result
      return wrapper
    
```

在上面的循环中，i是数组args中参数的以0起始的索引，arg是包含其值的字符串。可以利用“f.__code__.co_varnames[i]”读取到参数的名称。类型检查代码与返回值类型检查完全一样（包括错误消息的异常）。

为了对关键字参数进行类型检查，我们需要遍历参数kwargs。此时的类型检查几乎与第一个循环中相同：  
  

```python

    for name, arg in kwargs.items():
      expected_type = f.__annotations__.get(name, None)
      if expected_type and not isinstance(arg, expected_type):
        raise RuntimeError("{} should be of type {}; {} specified".format(name, expected_type.__name__, type(arg).__name__))
    
```

得到的装饰器代码如下：  
  

```python

    def typecheck(f):
      def wrapper(*args, **kwargs):
        for i, arg in enumerate(args[:f.__code__.co_nlocals]):
          name = f.__code__.co_varnames[i]
          expected_type = f.__annotations__.get(name, None)
          if expected_type and not isinstance(arg, expected_type):
            raise RuntimeError("{} should be of type {}; {} specified".format(name, expected_type.__name__, type(arg).__name__))
        for name, arg in kwargs.items():
          expected_type = f.__annotations__.get(name, None)
          if expected_type and not isinstance(arg, expected_type):
            raise RuntimeError("{} should be of type {}; {} specified".format(name, expected_type.__name__, type(arg).__name__))
        result = f(*args, **kwargs)
        return_type = f.__annotations__.get('return', None)
        if return_type and not isinstance(result, return_type):
          raise RuntimeError("{} should return {}".format(f.__name__, return_type.__name__))
        return result
      return wrapper
    
```

将类型检查代码写成一个函数将会使代码更加清晰。为了简化代码，我们修改错误信息，而当返回值是无效的类型时，将会使用到这些错误信息。我们也可以利用
functools 模块中的 wraps 方法，将包装函数的一些属性复制到 wrapper 中（这使得 wrapper 看起来更像原来的函数）：  
  

```python

    def typecheck(f):
      def do_typecheck(name, arg):
        expected_type = f.__annotations__.get(name, None)
        if expected_type and not isinstance(arg, expected_type):
          raise RuntimeError("{} should be of type {} instead of {}".format(name, expected_type.__name__, type(arg).__name__))
     
      @functools.wraps(f)
      def wrapper(*args, **kwargs):
        for i, arg in enumerate(args[:f.__code__.co_nlocals]):
          do_typecheck(f.__code__.co_varnames[i], arg)
        for name, arg in kwargs.items():
          do_typecheck(name, arg)
     
        result = f(*args, **kwargs)
     
        do_typecheck('return', result)
        return result
      return wrapper
    
```

**结论**

注解是 Python 3
中的一个新元素，本文例子中的使用方法很普通，你也可以想象很多特定领域的应用。虽然上面的实现代码并不能满足实际产品要求，但它的目的本来就是用作概念验证。可以对其进行以下改善：

  * 处理额外的参数（ args 中意想不到的项目） 
  * 默认值类型检查 
  * 支持多个类型 
  * 支持模板类型（例如，int 型列表） 

