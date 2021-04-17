**元祖的创建**

元祖创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。

```python

    >>> temp=(1)
    >>> temp
    1
    >>> type(temp)
    <class 'int'>
```

```python

    >>> temp2=1,2,3,4,5
    >>> temp2
    (1, 2, 3, 4, 5)
    >>> type(temp2)
    <class 'tuple'>
```

```python

    >>> temp=[]
    >>> type(temp)
    <class 'list'>
```

```python

    >>> temp=()
    >>> type(temp)
    <class 'tuple'>
```

```python

    >>> temp=(1,)
    >>> temp
    (1,)
    >>> type(temp)
    <class 'tuple'>
```

**对元组各个元素进行命名**  

1，通过对元组索引值的命名

2，通过标准库中的 ` collections.nametuple ` 替代内置touple

通过对元组索引值的命名

好比在c中的defined详细见代码

```python

    name,gender,age = range(3)
    student = ("ruioniao","man","19")
    student["name"]
    student["age"]
    student["gender"]
    #输出
    #"ruoniao"
    #19
    #man
```

使用标准库中 ` collections.nametuple ` 代替内置的tuple

![](https://img.jbzj.com/file_images/article/201807/201871283551444.png?20186128364)

![](https://img.jbzj.com/file_images/article/201807/201871283625749.png?201861283633)

s这个变量名可以直接通过属性方式访问

Student是namedtuple的名称，后面的列表是其元素创建时还可以

```python

     s= Student(name="ruoniao",age="19",sex="man")
     #输出Student(name='ruoniao', age='19', sex='man')
```

可以通过‘点'像类访问属性那样进行访问

**总结**

以上就是这篇文章的全部内容了，希望本文的内容对大家的学习或者工作具有一定的参考学习价值，如果有疑问大家可以留言交流，谢谢大家对脚本之家的支持。  

