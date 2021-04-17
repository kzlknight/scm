今天在学python的时候遇到一个问题，循环一个数组 指定一个数，如果数组内有相同的元素就删除。

1. 前提是不能新增内存，就在该数组内处理 
```python

    nums = [0,1,2,2,3,0,4,2]
    val = 2
    for i in nums:
     if(i == val):
      idx = nums.index(i)
      nums.pop(idx)
    print(nums)
```

一开始写成这样时候输出

> [0, 1, 2, 3, 0, 4] //中间的2居然没有删除

然后我修改了一下 把每一次循环都打出来看看

```python

    0loop [0, 1, 2, 2, 3, 0, 4, 2]
    1loop [0, 1, 2, 2, 3, 0, 4, 2]
    2loop [0, 1, 2, 3, 0, 4, 2]//这里被跳过了
    3loop [0, 1, 2, 3, 0, 4, 2]
    4loop [0, 1, 2, 3, 0, 4, 2]
    5loop [0, 1, 2, 3, 0, 4, 2]
    6loop [0, 1, 2, 3, 0, 4]
```

原因是因为Python中for循环用迭代器实现，而pop方法删除了当前元素后，被删除的位置由后面的填补，而循环自动指到下一个元素，也就相当于那个2被跳过了。

网上搜的一些处理方法 比较适合这个的是用

```python

    for i in nums[:]: //在这里nums[:]相当于复制了一份，但是并不是同一份。
      if(i == val):
        idx = nums.index(i)
        nums.pop(idx)
```

输出

> [0, 1, 3, 0, 4]

**补充知识：** **python 中for循环（continue, break, pass）用法**

1、continue 跳过当前继续执行下一个循环

```python

    l = ['a','b','c','d','e']
    for i in l:    #i遍历l列表中的每一个元素
      if i == 'c':
        continue   #continue以下的代码不执行直接进入下一个循环
      print(i)
```

![](https://img.jbzj.com/file_images/article/202012/20201211142333.jpg)

2、break 直接中断循环，不再执行

```python

    l = ['a','b','c','d','e']
    for i in l:
      if i == 'c':
        break #break直接跳出循环，break以下代码全部不执行
      print(i)
```

![](https://img.jbzj.com/file_images/article/202012/20201211142344.jpg)

3、pass 什么都不操作，接着循环

```python

    l = ['a','b','c','d','e']
    for i in l:  #i遍历l列表中的每一个元素
      if i == 'c':
        pass
      print(i)
```

![](https://img.jbzj.com/file_images/article/202012/20201211142358.jpg)

以上为个人经验，希望能给大家一个参考，也希望大家多多支持脚本之家。如有错误或未考虑完全的地方欢迎留言讨论，望不吝赐教。

