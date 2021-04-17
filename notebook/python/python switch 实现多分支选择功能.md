![](https://img.jbzj.com/file_images/article/202012/2020122109523216.png)

相信玩过几天 python 的小伙伴都知道，python 里并没有 switch 关键字实现，那这是为什么呢？

根据官方说法 PEP 3103 - A Switch/Case Statement.

实现 switch case 需要被判断的变量是可哈希和可比较的，这与 python 提倡的灵活性有冲突。在实现上优化不好做，可能到最后最差的情况汇编出来和
if else 组是一样的，所以 python 没有支持

但是没有 switch 关键字，不代表不能实现类似效果，接下来通过几个小程序来说明此类问题

###  if else 判断

我们通过最常用的 if else 判断来实现一段代码

```python

    def matching_if(type):
     if type == 0:
      return '优惠1块钱'
     elif type == 1:
      return '优惠10块钱'
     elif type == 2:
      return '优惠100块钱'
     return '无优惠'
    
    if __name__ == '__main__':
     print(matching_if(1))
     print(matching_if(999))
```

执行结果如下：

> '''  
>  打印输出：  
>  优惠10块钱  
>  无优惠  
>  '''

###  dict 字典

可以使用字典实现 switch case，这种方式易维护，同时也能够减少代码量。如下是使用字典模拟的 switch case 实现：

```python

    def matching_dict(type):
     types = {
      0: '优惠1块钱',
      1: '优惠10块钱',
      2: '优惠100块钱'
     }
     return types.get(type, '无优惠')
    
    if __name__ == '__main__':
     print(matching_dict(1))
     print(matching_dict(999))
```

代码从整体上看着简洁了很多，那还有没有别的方式呢？

###  函数判断

函数判断从代码数量来说并无优势，优势点在于其灵活性，如果根据不同的类型作出大量操作，函数运算无疑是最优的方式

```python

    def one():
     return '优惠1块钱'
    
    def two():
     return '优惠10块钱'
    
    def three():
     return '优惠100块钱'
    
    def default():
     return '无优惠'
    def matching_method(type):
     types = {
      0: one,
      1: two,
      2: three
     }
     method = types.get(type, default)
     return method()
    
    if __name__ == '__main__':
     print(matching_method(1))
     print(matching_method(999))
```

**优雅的代码是程序员的追求之一** ，作者本人也有一定程度的代码洁癖，所以涉及此类应用，会选择第二种 dict 字典类型应用

###  lambda 函数

这里推出一款 lambda 配合 dict 字典的方式，可以对运算条件作出更为精准的计算

```python

    def matching_lambda(type):
     matching_dict = lambda x: {
      x == 0: '优惠1块钱',
      x == 1: '优惠10块钱',
      x == 2: '优惠100块钱'
     }
     return matching_dict(type)[True]
    if __name__ == '__main__':
     print(matching_lambda(1))
     print(matching_lambda(2))
```

###  结言

由于作者水平有限, 欢迎大家能够反馈指正文章中错误不正确的地方, 感谢 🙏

到此这篇关于python switch 实现多分支选择功能的文章就介绍到这了,更多相关python switch
多分支实现内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

