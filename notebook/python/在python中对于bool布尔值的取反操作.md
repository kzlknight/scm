**背景**

根据公司业务的需求，需要做一个对于mysql数据库的大批量更新。脚本嘛也是干干单单。使用了redis的队列做缓存，可以异步并发的多任务进行更新。

有点难受的地方在于，请求访问时，因为一些网速，速率之内的原因，导致正常的数据会请求失败。处理的方法呢，就是多请求几次。

不过，麻烦的地方在于，每次重新请求，都要讲原来get,和put的key转换。手动更换起来麻烦的一批。

所以就想做一个自动的转换小demo。

成熟的代码应该学会自己照顾自己。

自动转换的机制是: 每一次请求，判断bool值，依据bool值分别赋值，每次请求之前或者请求完成之后，需要修改Bool值。

这就涉及到今天的重点了，bool值的取反。

> b = True
>
> a = bool(1-b)

bool()函数中的1-bool值 就是取bool值的反值了。

实验的代码如下：

```python

    def negation_bool(b):
      b = bool(1 - b)
      return b
    
    def up(b):
      if b is True:
        unique1 = "map_url"
        unique2 = "map2_url"
      else:
    
        unique1 = "map2_url"
        unique2 = "map_url"
      return unique1, unique2
    
    b = True
    num = 5
    for i in range(num * 2):
      b = negation_bool(b)
      unique1, unique2 = up(b)
      print(unique1, unique2)
      print("+" * 50)
    
```

![](https://img.jbzj.com/file_images/article/202012/20201211163420.jpg)

可以看到每次的值都是相反的。

bool值的取反操作，可以用来做一些有规律行的修改变量操作。例如代码启动的指示变量，代码中关键的值等等。

我们的原则就是，能自动的绝不手动，能一键启动的，绝不会做多余的操作。

**补充：Python中bool类型转换**

在python中，以下数值会被认为是False：

1、为0的数字，包括0，0.0

2、空字符串，包括”，”“

3、表示空值的None

4、空集合，包括()，[]，{}

其他的值都认为是True。

None是python中的一个特殊值，表示什么都没有，它和0、空字符、False、空集合都不一样。

bool(‘False')的结果是True，因为‘False'是一个不为空的字符串，当被转换成bool类型之后，就得到True。

bool(' ‘)的结果是True，一个空格也不能算作空字符串。

bool(”)才是False。

以上为个人经验，希望能给大家一个参考，也希望大家多多支持脚本之家。如有错误或未考虑完全的地方，望不吝赐教。

