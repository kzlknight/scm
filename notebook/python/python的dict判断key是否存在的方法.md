大家在学会python中的字典，会发现，字典中是没有特殊顺序的，但是都存储在一个特定的key下面，key是什么呢？其实key是python字典中的键，可以是数字，也可以是字符串，可以存储任意类型的对象。那你知道如何判断字典中key的存在吗？下面小编就向大家介绍python中，判断字典中是否存在key的两种方法。

###  方法一：使用自带函数实现

```python

    dict = {'a': {}, 'b': {}, 'c': {}}
    print(dict.__contains__("b"))     返回：True
    print(dict.__contains__("d"))     返回：False
```

###  第二种方法：使用in方法

```python

    #生成一个字典
    d = {'a':{}, 'b':{}, 'c':{}}
    #打印返回值，其中d.keys()是列出字典所有的key
    print 'a' in d.keys()
    print 'a' in d
```

知识点扩展：

**python 判断dict当中key是否存在的两种方法**

如果key不存在，dict就会报错：

```python

    >>> d['Thomas']
    Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
    KeyError: 'Thomas'
```

要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：

```python

    >>> 'Thomas' in d
    False
```

二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：

```python

    >>> d.get('Thomas')
    >>> d.get('Thomas', -1)
    -1
```

注意：返回None的时候Python的交互式命令行不显示结果。

以上就是python的dict判断key是否存在的方法的详细内容，更多关于python的dict中如何判断key是否存在的资料请关注脚本之家其它相关文章！

