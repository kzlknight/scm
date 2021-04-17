string模块可以追溯到早期版本的Python。  
以前在本模块中实现的许多功能已经转移到str物品。  
这个string模块保留了几个有用的常量和类来处理str物品。  

**字符串-文本常量和模板**  

目的：包含用于处理文本的常量和类。

**功能**  

功能capwords()将字符串中的所有单词大写。  
字符串capwords.py  

```python

    import string
    
    s = 'The quick brown fox jumped over the lazy dog.'
    
    print(s)
    print(string.capwords(s))
    
    
```

结果与调用split()，将结果列表中的单词大写，然后调用join()把结果结合起来。  

```python

    $ python3 string_capwords.py
    
    The quick brown fox jumped over the lazy dog.
    The Quick Brown Fox Jumped Over The Lazy Dog.
    
    
```

**模板**  

字符串模板作为PEP
292作为内建内插语法的替代。带着string.Template内插，变量通过在名称前加上(例如，(例如，(例如，var)。或者，如果需要的话，也可以用花括号(例如，${var}).  
此示例使用%运算符和新的格式字符串语法。str.format().  

```python

    #字符串模板
    
    import string
    
    values = {'var': 'foo'}
    
    t = string.Template("""
    Variable    : $var
    Escape     : $$
    Variable in text: ${var}iable
    """)
    
    print('TEMPLATE:', t.substitute(values))
    
    s = """
    Variable    : %(var)s
    Escape     : %%
    Variable in text: %(var)siable
    """
    
    print('INTERPOLATION:', s % values)
    
    s = """
    Variable    : {var}
    Escape     : {{}}
    Variable in text: {var}iable
    """
    
    print('FORMAT:', s.format(**values))
    
    
```

在前两种情况下，触发器字符($或%)是通过重复两次来逃脱的。对于格式语法，两者都是{和}需要通过重复它们来逃脱。  

```python

    $ python3 string_template.py
    
    TEMPLATE:
    Variable    : foo
    Escape     : $
    Variable in text: fooiable
    
    INTERPOLATION:
    Variable    : foo
    Escape     : %
    Variable in text: fooiable
    
    FORMAT:
    Variable    : foo
    Escape     : {}
    Variable in text: fooiable
    
    
```

模板与字符串内插或格式化之间的一个关键区别是，参数的类型没有被考虑在内。将值转换为字符串，并将字符串插入到结果中。没有可用的格式设置选项。例如，无法控制用于表示浮点值的数字数。  

不过，有一个好处是，使用safe_substitute()方法可以避免异常，如果不是以参数形式提供模板所需的所有值。  

```python

    #字符串模板丢失.py
    
    import string
    
    values = {'var': 'foo'}
    
    t = string.Template("$var is here but $missing is not provided")
    
    try:
      print('substitute()   :', t.substitute(values))
    except KeyError as err:
      print('ERROR:', str(err))
    
    print('safe_substitute():', t.safe_substitute(values))
    
    
```

因为没有价值missing在值字典中，KeyError是由substitute()。  

而不是提高错误，safe_substitute()捕获它并将变量表达式单独保留在文本中。  

```python

    $ python3 string_template_missing.py
    
    ERROR: 'missing'
    safe_substitute(): foo is here but $missing is not provided
    
```

**高级模板**  

string.Template可以通过调整用于在模板正文中查找变量名称的正则表达式模式来更改。一个简单的方法是更改delimiter和idpattern类属性。  

```python

    #字符串模板
    
    import string
    
    
    class MyTemplate(string.Template):
      delimiter = '%'
      idpattern = '[a-z]+_[a-z]+'
    
    
    template_text = '''
     Delimiter : %%
     Replaced : %with_underscore
     Ignored  : %notunderscored
    '''
    
    d = {
      'with_underscore': 'replaced',
      'notunderscored': 'not replaced',
    }
    
    t = MyTemplate(template_text)
    print('Modified ID pattern:')
    print(t.safe_substitute(d))
    
    
```

在本例中，替换规则被更改，因此分隔符是%而不是$变量名必须包括中间的下划线。  

模式%notunderscored不会被任何东西替换，因为它不包含下划线字符。  

```python

    $ python3 string_template_advanced.py
    
    Modified ID pattern:
    
     Delimiter : %
     Replaced : replaced
     Ignored  : %notunderscored
    
    
```

对于更复杂的更改，可以重写pattern属性并定义一个全新的正则表达式。  

提供的模式必须包含四个命名组，用于捕获转义分隔符、命名变量、变量名的大括号版本和无效分隔符模式。  

```python

    #字符串模板_defaultpattern.py
    
    import string
    
    t = string.Template('$var')
    print(t.pattern.pattern)
    
    
```

价值t.pattern是已编译的正则表达式，但原始字符串可通过其pattern属性。  

```python

    \$(?:
     (?P<escaped>\$) |        # two delimiters
     (?P<named>[_a-z][_a-z0-9]*)  | # identifier
     {(?P<braced>[_a-z][_a-z0-9]*)} | # braced identifier
     (?P<invalid>)          # ill-formed delimiter exprs
    )
    
```

此示例定义一个新模式以创建一种新类型的模板，使用{{var}}作为变量语法。  

```python

    #字符串模板_newsyntax.py
    
    import re
    import string
    
    
    class MyTemplate(string.Template):
      delimiter = '{{'
      pattern = r'''
      \{\{(?:
      (?P<escaped>\{\{)|
      (?P<named>[_a-z][_a-z0-9]*)\}\}|
      (?P<braced>[_a-z][_a-z0-9]*)\}\}|
      (?P<invalid>)
      )
      '''
    
    
    t = MyTemplate('''
    {{{{
    {{var}}
    ''')
    
    print('MATCHES:', t.pattern.findall(t.template))
    print('SUBSTITUTED:', t.safe_substitute(var='replacement'))
    
    
```

named和braced模式都必须单独提供，即使它们是相同的。运行示例程序将生成以下输出：  

```python

    $ python3 string_template_newsyntax.py
    
    MATCHES: [('{{', '', '', ''), ('', 'var', '', '')]
    SUBSTITUTED:
    {{
    replacement
    
    
```

**格式化程序**  

这个Formatter类实现与format()方法str。它的功能包括类型强制、对齐、属性和字段引用、命名和位置模板参数以及特定于类型的格式选项。大多数时候format()方法是这些特性的更方便的接口，但是Formatter作为构建子类的一种方法，用于需要变体的情况下。  

**常数**  

这个string模块包括一些与ASCII和数字字符集相关的常量。  

```python

    #字符串常数.py
    
    import inspect
    import string
    
    
    def is_str(value):
      return isinstance(value, str)
    
    
    for name, value in inspect.getmembers(string, is_str):
      if name.startswith('_'):
        continue
      print('%s=%r\n' % (name, value))
    
    
```

这些常量在处理ASCII数据时很有用，但是由于在某种形式的Unicode中遇到非ASCII文本越来越常见，因此它们的应用受到限制。  

```python

    $ python3 string_constants.py
    
    ascii_letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW
    XYZ'
    
    ascii_lowercase='abcdefghijklmnopqrstuvwxyz'
    
    ascii_uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    digits='0123456789'
    
    hexdigits='0123456789abcdefABCDEF'
    
    octdigits='01234567'
    
    printable='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQ
    RSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
    
    punctuation='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    
    whitespace=' \t\n\r\x0b\x0c'
    
    
```

到此这篇关于详解Python中string模块除去Str还剩下什么的文章就介绍到这了,更多相关Python
string模块内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！  

