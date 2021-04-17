Python编程时，经常需要跳过第一行读取文件内容。简单的做法是为每行设置一个line_num，然后判断line_num是否为1，如果不等于1，则进行读取操作。

**相应的Python代码如下：**

```python

    input_file = open("C:\\Python34\\test.csv") 
    line_num = 0 
    for line in input_file: 
      line_num += 1 
      if (line_num != 1): 
        do_readline() 
```

然而这样每次迭代都需要判断一次,增加了时间开销，一种高效的做法是导入islice这个函数，islice函数使用说明如下

```python

    islice(seq,start,stop,step)
    for example
    islice('ABCDEF',2,None) 输出'CDEF '
```

**因此在读取文件跳过第一行内容代码可以如下：**

```python

    from itertools import islice 
    input_file = open("C:\\Python34\\test.csv") 
    for line in islice(input_file, 1, None): 
      do_readline() 
```

以上这篇python跳过第一行快速读取文件内容的实例就是小编分享给大家的全部内容了，希望能给大家一个参考，也希望大家多多支持脚本之家。

