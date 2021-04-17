本文介绍了python画图时设置分辨率和画布大小的实现，主要使用plt.figure()，下面就一起来了解一下

###  plt.figure()

**示例：**

```python

    import numpy as np
    import pandas as pd
    import warnings
    warnings.filterwarnings('ignore')
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    #读取示例数据
    df = pd.read_csv(  'https://labfile.oss.aliyuncs.com/courses/1283/telecom_churn.csv')
    #sns.countplot(x='State', hue='Churn', data=df)
    
    #画分布图
    sns.countplot(x=df['State'], hue=df['Churn'])
```

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010809471812.png)  

**调整后：**

```python

    # 分辨率参数-dpi，画布大小参数-figsize
    plt.figure(dpi=300,figsize=(24,8))
    # 改变文字大小参数-fontsize
    plt.xticks(fontsize=10)
    
    #画分布图
    sns.countplot(x=df['State'], hue=df['Churn'])
```

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010809471813.png)

到此这篇关于python画图时设置分辨率和画布大小的实现(plt.figure())的文章就介绍到这了,更多相关python
设置分辨率和画布内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

