有时候，要把内存中的一个对象持久化保存到磁盘上，或者序列化成二进制流通过网络发送到远程主机上。Python中有很多模块提供了序列化与反序列化的功能，如：marshal,
pickle, cPickle等等。今天就讲讲marshal模块。

  * 注意： marshal并不是一个通用的模块，在某些时候它是一个不被推荐使用的模块，因为使用marshal序列化的二进制数据格式还没有文档化，在不同版本的Python中，marshal的实现可能不一样。也就是说，用python2.5序列为一个对象，用python2.6的程序反序列化所得到的对象，可能与原来的对象是不一样的。但这个模块存在的意义，正如Python手册中所说：The marshal module exists mainly to support reading and writing the “pseudo-compiled” code for Python modules of .pyc files. 

下面是marshal模块中定义的一些与序列化/反序列化有关的函数：  
**marshal.dump(value, file[, version])**

将值写入到一个打开的输出流里。参数value表示待序列化的值。file表示打开的输出流。如:以”wb”模式打开的文件，sys.stdout或者os.popen。对于一些不支持序列类的类型，dump方法将抛出ValueError异常。要特别说明一下，并不是所有类型的对象都可以使用marshal模块来序列化/反序列化的。在python2.6中，支持的类型包括：None,
integers, long integers, floating point numbers, strings, Unicode objects,
tuple, list, set, dict, 和 code objects。对于tuple, list, set,
dict等集合对象，其中的元素必须也是上述类型之一。  
**marshal.load(file)**

执行与marshal.dump相反的操作，将二进制数据反序列为Python对象。下面是一个例子，演示这两个方法的使用：  
  

```python

    # coding=gbk
     
    import  marshal ,  sys ,  os
     
    lst  =  [ 1 ,  ( 2 ,  " string " ) ,  { " key " :  " Value " } ]
     
    # 序列化到文件中
    fle  =  open ( os . path . join ( os . getcwd ( ) ,  ' fle . txt ' ) ,  ' wb ' )
    marshal . dump ( lst ,  fle )
    fle . close ( )
     
    # 反序列化
    fle1  =  open ( os . path . join ( os . getcwd ( ) ,  ' fle . txt ' ) ,  ' rb ' )
    lst1  =  marshal . load ( fle1 )
    fle1 . close ( )
     
    # 打印结果
    print  lst
    print  lst1
     
    # ----  结果  ----
    # [1,  (2,  'string'),  {'key':  'Value'}]
    # [1,  (2,  'string'),  {'key':  'Value'}]
    marshal.dumps(value[, version)
    
```

该方法与上面讲的marshal.dump()功能类似，只是它返回的是序列化之后的二进制流，而不是将这些数据直接写入到文件中。  
**marsahl.load(string)**

将二进制流反序列化为对象。下面的一段代码，演示这两个方法的使用：  
  

```python

    import  marshal ,  sys ,  os
     
    lst  =  [ 1 ,  ( 2 ,  " string " ) ,  { " key " :  " Value " } ]
     
    byt1  =  marshal . dumps ( lst )
    lst1  =  marshal . loads ( byt1 )
     
    # 打印结果
    print  lst
    print  lst1
     
    # ―-  结果  ―-
    # [1,  (2,  'string'),  {'key':  'Value'}]
    # [1,  (2,  'string'),  {'key':  'Value'}]
    
```

更多关于marshal的内容，请参考Python手册。  

