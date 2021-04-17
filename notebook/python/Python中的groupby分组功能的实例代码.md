pandas中的DataFrame中可以根据某个属性的同一值进行聚合分组，可以选单个属性，也可以选多个属性：

代码示例：

```python

    import pandas as pd
    A=pd.DataFrame([['Beijing',1.68,2300,'city','Yes'],['Tianjin',1.13,1293,'city','Yes'],['Shaanxi',20.56,3732,'Province','Yes'],['Hebei',18.77,7185,'Province','No'],['Qinghai',72,560,'Province','No']],columns=['Name','Area','Population','Administrative_level','Have 985'])
    for name,group in A.groupby('Administrative_level'):
      print(name)
      print(group)
    for name,group in A.groupby(['Administrative_level','Have 985']):
      print(name)
      print(group)
```

先产生一个dataframe，如表所示

Name  |  Area  |  Population  |  Administrative_level  |  Have 985  
---|---|---|---|---  
Beijing  |  1.68  |  2300  |  city  |  Yes  
Tianjin  |  1.13  |  1293  |  city  |  Yes  
Shaanxi  |  20.56  |  3732  |  Province  |  Yes  
Hebei  |  18.77  |  7185  |  Province  |  No  
Qinghai  |  72  |  560  |  Province  |  No  
  
先按照行政级别一个属性划分，再按照行政级别和是否有985高校两个属性划分，结果如下：

![](https://img.jbzj.com/file_images/article/201807/2018711165014473.png?2018611165032)

**总结**

以上所述是小编给大家介绍的Python中的groupby分组功能的实例代码，希望对大家有所帮助，如果大家有任何疑问请给我留言，小编会及时回复大家的。在此也非常感谢大家对脚本之家网站的支持！

