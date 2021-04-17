###  创建测试数据：

```python

    import pandas as pd
    import numpy as np
     
    #Create a DataFrame
    df1 = {
      'Subject':['semester1','semester2','semester3','semester4','semester1',
            'semester2','semester3'],
      'Score':[62,47,55,74,31,77,85]}
     
    df2 = {
      'Subject':['semester1','semester2','semester3','semester4'],
      'Score':[90,47,85,74]}
     
     
    df1 = pd.DataFrame(df1,columns=['Subject','Score'])
    df2 = pd.DataFrame(df2,columns=['Subject','Score'])
     
    print(df1)
    print(df2)
```

运行结果：  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020121310242252.png)

###  求两个dataframe的交集

```python

    intersected_df = pd.merge(df1, df2, how='inner')
    print(intersected_df)
```

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020121310242253.png)  

也可以指定求交集的列：

```python

    intersected_df = pd.merge(df1, df2, on=['Subject'], how='inner')
    print(intersected_df)
```

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020121310242254.png)

###  求差集

df2-df1：

```python

    set_diff_df = pd.concat([df2, df1, df1]).drop_duplicates(keep=False)
    print(set_diff_df)
```

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020121310242255.png)

df1-df2：

```python

    set_diff_df = pd.concat([df1, df2, df2]).drop_duplicates(keep=False)
    print(set_diff_df)
    
```

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020121310242356.png)  

另一种求差集的方法是：  

以df1-df2为例：

```python

    df1 = df1.append(df2)
    df1 = df1.append(df2)
    set_diff_df = df1.drop_duplicates(subset=['Subject', 'Score'],keep=False)
    print(set_diff_df)
```

得到的df1-df2结果是一样的：  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020121310242357.png)

到此这篇关于Pandas中两个dataframe的交集和差集的示例代码的文章就介绍到这了,更多相关Pandas
dataframe交集差集内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

