在pandas中怎么样实现类似mysql查找语句的功能：

```python

    select * from table where column_name = some_value;
```

pandas中获取数据的有以下几种方法：

  * 布尔索引 
  * 位置索引 
  * 标签索引 
  * 使用API 

假设数据如下:

```python

    import pandas as pd
    import numpy as np
    
    df = pd.DataFrame({'A': 'foo bar foo bar foo bar foo foo'.split(),
              'B': 'one one two three two two one three'.split(),
              'C': np.arange(8), 'D': np.arange(8) * 2})
```

![](https://img.jbzj.com/file_images/article/202012/2020121310181546.png)

###  布尔索引

该方法其实就是找出每一行中符合条件的真值(true value)，如找出列A中所有值等于foo

```python

    df[df['A'] == 'foo'] # 判断等式是否成立
```

![](https://img.jbzj.com/file_images/article/202012/2020121310181547.png)

###  位置索引

使用iloc方法，根据索引的位置来查找数据的。这个例子需要先找出符合条件的行所在位置

```python

    mask = df['A'] == 'foo'
    pos = np.flatnonzero(mask) # 返回的是array([0, 2, 4, 6, 7])
    df.iloc[pos]
    
    #常见的iloc用法
    df.iloc[:3,1:3]
```

![](https://img.jbzj.com/file_images/article/202012/2020121310181548.png)

###  标签索引

如何DataFrame的行列都是有标签的，那么使用loc方法就非常合适了。

```python

    df.set_index('A', append=True, drop=False).xs('foo', level=1) # xs方法适用于多重索引DataFrame的数据筛选
    
    # 更直观点的做法
    df.index=df['A'] # 将A列作为DataFrame的行索引
    df.loc['foo', :]
    
    # 使用布尔
    df.loc[df['A']=='foo']
```

![](https://img.jbzj.com/file_images/article/202012/2020121310181549.png)

**使用API**

` pd.DataFrame.query ` 方法在数据量大的时候，效率比常规的方法更高效。

```python

    df.query('A=="foo"')
    
    # 多条件
    df.query('A=="foo" | A=="bar"')
```

![](https://img.jbzj.com/file_images/article/202012/2020121310181550.png)

**数据提取不止前面提到的情况，第一个答案就给出了以下几种常见情况：**  

1、筛选出列值等于标量的行，用==

```python

    df.loc[df['column_name'] == some_value]
```

2、筛选出列值属于某个范围内的行，用isin

```python

    df.loc[df['column_name'].isin(some_values)] # some_values是可迭代对象
```

3、多种条件限制时使用&，&的优先级高于>=或<=，所以要注意括号的使用

```python

    df.loc[(df['column_name'] >= A) & (df['column_name'] <= B)]
```

4、筛选出列值不等于某个/些值的行

```python

    df.loc[df['column_name'] != 'some_value']
    
    df.loc[~df['column_name'].isin('some_values')] #~取反
```

到此这篇关于使用pandas实现筛选出指定列值所对应的行的文章就介绍到这了,更多相关pandas
筛选指定列值内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

