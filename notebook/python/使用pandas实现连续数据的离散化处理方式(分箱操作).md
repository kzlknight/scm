Python实现连续数据的离散化处理主要基于两个函数，pandas.cut和pandas.qcut，前者根据指定分界点对连续数据进行分箱处理，后者则可以根据指定箱子的数量对连续数据进行等宽分箱处理，所谓等宽指的是每个箱子中的数据量是相同的。

**下面简单介绍一下这两个函数的用法：**

```python

    # 导入pandas包
    import pandas as pd
    ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32] # 待分箱数据
    bins = [18, 25, 35, 60, 100] # 指定箱子的分界点
```

**pandas.cut函数 ：**

```python

    cats1 = pd.cut(ages, bins)
    cats1
```

**cats1结果：**

```python

    [(18, 25], (18, 25], (18, 25], (25, 35], (18, 25], ..., (25, 35], (60, 100], (35, 60],
    (35, 60], (25, 35]]
    Length: 12
    Categories (4, interval[int64]): [(18, 25] < (25, 35] < (35, 60] < (60, 100]]
    # labels参数为False时，返回结果中用不同的整数作为箱子的指示符
    cats2 = pd.cut(ages, bins,labels=False) 
    cats2 # 输出结果中的数字对应着不同的箱子
```

**cats2结果：**

```python

     array([0, 0, 0, 1, 0, 0, 2, 1, 3, 2, 2, 1], dtype=int64)
    pd.value_counts(cats1) # 对不同箱子中的数进行计数
```

**计数结果：**

```python

    (18, 25]  5
    (35, 60]  3
    (25, 35]  3
    (60, 100] 1
    dtype: int64
    pd.cut(ages, [18, 26, 36, 61, 100], right=False) # 指定分箱区间是左闭右开
```

**改变区间开闭结果：**

```python

    [[18, 26), [18, 26), [18, 26), [26, 36), [18, 26), ..., [26, 36), [61, 100), [36, 61),
    [36, 61), [26, 36)]
    Length: 12
    Categories (4, interval[int64]): [[18, 26) < [26, 36) < [36, 61) < [61, 100)]
    # 可以将想要指定给不同箱子的标签传递给labels参数
    group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
    cuts3 = pd.cut(ages, bins, labels=group_names) 
    cuts3
```

**cats3结果：**

```python

    [Youth, Youth, Youth, YoungAdult, Youth, ..., YoungAdult, Senior, MiddleAged,
    MiddleAged, YoungAdult]
    Length: 12
    Categories (4, object): [Youth < YoungAdult < MiddleAged < Senior]
```

**pandas.qcut函数：**

```python

    qcats1 = pd.qcut(ages,q=4) # 参数q指定所分箱子的数量
    qcats1
```

**qcats1结果：**

```python

    [(19.999, 22.75], (19.999, 22.75], (22.75, 29.0], (22.75, 29.0], (19.999, 22.75], ...,
    (29.0, 38.0], (38.0, 61.0], (38.0, 61.0], (38.0, 61.0], (29.0, 38.0]]
    Length: 12
    Categories (4, interval[float64]): [(19.999, 22.75] < (22.75, 29.0] < (29.0, 38.0] <
    (38.0, 61.0]]
    qcats1.value_counts() # 从输出结果可以看到每个箱子中的数据量时相同的
```

**计数结果：**

```python

    (19.999, 22.75] 3
    (22.75, 29.0]  3
    (29.0, 38.0]  3
    (38.0, 61.0]  3
    dtype: int64
```

​​​参考：《利用Python进行数据分析》――Wes McKinney 第二版

以上这篇使用pandas实现连续数据的离散化处理方式(分箱操作)就是小编分享给大家的全部内容了，希望能给大家一个参考，也希望大家多多支持脚本之家。

