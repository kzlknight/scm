本文实例讲述了Python使用pickle模块实现序列化功能。分享给大家供大家参考，具体如下：

Python内置的pickle模块能够将Python对象序列成字节流，也可以把字节流反序列成对象。

```python

    import pickle
    class Student:
      def __init__(self, name, age):
        self.name = name
        self.age = age
      def say(self):
        print("I am", self.name)
    >>> t = Student('Tom', 23)
    >>> t.say()
    I am Tom
    >>>
    >>> save_path = './tom_msg'
    >>> with open(save_path, 'wb') as f:    # 字节流写入
    ...   pickle.dump(t, f)      # 序列化数据保存在文件中
    >>>
    >>> with open(save_path, 'rb') as f:    # 字节流读出
    ...   after_t = pickle.load(f)    # 读取文件信息反序列化成对象
    ...
    >>> after_t.__dict__
    {'name': 'Tom', 'age': 23}
    >>> after_t.say()
    I am Tom
    >>>
    >>>
    >>> l = Student('Lisa', 23)
    >>> serialized = pickle.dumps(l)
    >>> serialized
    b'\x80\x03c__main__\nStudent\nq\x00)\x81q\x01}q\x02(X\x04\x00\x00\x00nameq\x03X\x04\x00\x00\x00Lisaq\x04X\x03\x00\x00\x00ageq\x05K\x17ub.'
    >>> after_l = pickle.loads(serialized)
    >>> after_l.say()
    I am Lisa
    >>> after_l.__dict__
    {'name': 'Lisa', 'age': 23
    
    
```

如果比较复杂的操作(对象属性更变，添加删除)， ` pickle ` 模块可能会出问题，那时候应该结合 ` copyreg ` 来使用

更多关于Python相关内容感兴趣的读者可查看本站专题：《 [ Python编码操作技巧总结
](//www.jb51.net/Special/788.htm) 》、《 [ Python数据结构与算法教程
](//www.jb51.net/Special/663.htm) 》、《 [ Python Socket编程技巧总结
](//www.jb51.net/Special/648.htm) 》、《 [ Python函数使用技巧总结
](//www.jb51.net/Special/642.htm) 》、《 [ Python字符串操作技巧汇总
](//www.jb51.net/Special/636.htm) 》、《 [ Python入门与进阶经典教程
](//www.jb51.net/Special/520.htm) 》及《 [ Python文件与目录操作技巧汇总
](//www.jb51.net/Special/516.htm) 》

希望本文所述对大家Python程序设计有所帮助。

