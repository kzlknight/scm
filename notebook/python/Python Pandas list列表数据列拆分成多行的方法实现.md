###  1、实现的效果

示例代码：

```python

    df=pd.DataFrame({'A':[1,2],'B':[[1,2],[1,2]]})
    df
    Out[458]: 
      A    B
    0 1 [1, 2]
    1 2 [1, 2]
    
```

拆分成多行的效果：

> A B  
>  0 1 1  
>  1 1 2  
>  3 2 1  
>  4 2 2  
>

###  2、拆分成多行的方法

**1）通过apply和pd.Series实现**

容易理解，但在性能方面不推荐。

```python

    df.set_index('A').B.apply(pd.Series).stack().reset_index(level=0).rename(columns={0:'B'})
    Out[463]: 
      A B
    0 1 1
    1 1 2
    0 2 1
    1 2 2
    
```

**2）使用repeat和DataFrame构造函数**

性能可以，但不太适合多列

```python

    df=pd.DataFrame({'A':df.A.repeat(df.B.str.len()),'B':np.concatenate(df.B.values)})
    df
    Out[465]: 
      A B
    0 1 1
    0 1 2
    1 2 1
    1 2 2
    
```

或者

```python

    s=pd.DataFrame({'B':np.concatenate(df.B.values)},index=df.index.repeat(df.B.str.len()))
    s.join(df.drop('B',1),how='left')
    Out[477]: 
      B A
    0 1 1
    0 2 1
    1 1 2
    1 2 2
    
```

**3）创建新的列表**

```python

    pd.DataFrame([[x] + [z] for x, y in df.values for z in y],columns=df.columns)
    Out[488]: 
      A B
    0 1 1
    1 1 2
    2 2 1
    3 2 2
    
```

或者

```python

    #拆成多于两列的情况
    s=pd.DataFrame([[x] + [z] for x, y in zip(df.index,df.B) for z in y])
    s.merge(df,left_on=0,right_index=True)
    Out[491]: 
      0 1 A    B
    0 0 1 1 [1, 2]
    1 0 2 1 [1, 2]
    2 1 1 2 [1, 2]
    3 1 2 2 [1, 2]
    
```

**4）使用reindex和loc实现**

```python

    df.reindex(df.index.repeat(df.B.str.len())).assign(B=np.concatenate(df.B.values))
    Out[554]: 
      A B
    0 1 1
    0 1 2
    1 2 1
    1 2 2
    #df.loc[df.index.repeat(df.B.str.len())].assign(B=np.concatenate(df.B.values)
    
```

**5）使用numpy高性能实现**

```python

    newvalues=np.dstack((np.repeat(df.A.values,list(map(len,df.B.values))),np.concatenate(df.B.values)))
    pd.DataFrame(data=newvalues[0],columns=df.columns)
      A B
    0 1 1
    1 1 2
    2 2 1
    3 2 2
    
    
```

到此这篇关于Python Pandas list列表数据列拆分成多行的方法实现的文章就介绍到这了,更多相关Pandas
list列拆分成多行内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

