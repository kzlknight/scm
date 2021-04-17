**我就废话不多说了，直接上代码吧：**

```python

    from pandas import Series,DataFrame
    import pandas as pd
    import numpy as np
    from numpy import nan as NA
    from matplotlib import pyplot as plt
    ages = [20,22,25,27,21,23,37,31,61,45,41,32]
    #将所有的ages进行分组
    bins = [18,25,35,60,100]
    #使用pandas中的cut对年龄数据进行分组
    cats = pd.cut(ages,bins)
    #print(cats)
    #调用pd.value_counts方法统计每个区间的个数
    number=pd.value_counts(cats)
    #print(pd.value_counts(cats))
    #显示第几个区间index值
    index=pd.cut(ages,bins).codes
    #print(index)
    #为分类出来的每一组年龄加上标签
    group_names = ["Youth","YouthAdult","MiddleAged","Senior"]
    personType=pd.cut(ages,bins,labels=group_names)
    #print(personType)
    plt.hist(personType)
    #plt.show()
    #cut和qcut的用法
    data=[1,2,3,4,5,6,7,8,9,10]
    result=pd.qcut(data,4)
    print(' ',result)##qcut会将10个数据进行排序，然后再将data数据均分成四组
    #统计落在每个区间的元素个数
    print('dasdasdasdasdas:  ',pd.value_counts(result))
    #qcut : 跟cut一样也可以自定义分位数（0到1之间的数值，包括端点）
    results=pd.qcut(data,[0,0.1,0.5,0.9,1])
    print('results:  ',results)
    
```

```python

    import numpy as np
    import pandas as pd
    data = np.random.rand(20)
    print(data)
    #用cut函数将一组数据分割成n份
    #cut函数分割的方式：数据里的（最大值-最小值）/n=每个区间的间距
    #利用数据中最大值和最小值的差除以分组数作为每一组数据的区间范围的差值
    result = pd.cut(data,4,precision=2) #precision保留小数点的有效位数
    print(result)
    res_data=pd.value_counts(result)
    print(res_data)
    
```

以上这篇基于python cut和qcut的用法及区别详解就是小编分享给大家的全部内容了，希望能给大家一个参考，也希望大家多多支持脚本之家。

