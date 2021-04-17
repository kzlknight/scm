具体代码如下所示：

```python

    from operator import itemgetter #itemgetter用来去dict中的key，省去了使用lambda函数
    from itertools import groupby #itertool还包含有其他很多函数，比如将多个list联合起来。。
    d1={'name':'zhangsan','age':20,'country':'China'}
    d2={'name':'wangwu','age':19,'country':'USA'}
    d3={'name':'lisi','age':22,'country':'JP'}
    d4={'name':'zhaoliu','age':22,'country':'USA'}
    d5={'name':'pengqi','age':22,'country':'USA'}
    d6={'name':'lijiu','age':22,'country':'China'}
    lst=[d1,d2,d3,d4,d5,d6]
    #通过country进行分组：
    lst.sort(key=itemgetter('country')) #需要先排序，然后才能groupby。lst排序后自身被改变
    lstg = groupby(lst,itemgetter('country')) 
    #lstg = groupby(lst,key=lambda x:x['country']) 等同于使用itemgetter()
    for key,group in lstg:
      for g in group: #group是一个迭代器，包含了所有的分组列表
        print key,g
```

返回：  

```python

    China {'country': 'China', 'age': 20, 'name': 'zhangsan'}
    China {'country': 'China', 'age': 22, 'name': 'lijiu'}
    JP {'country': 'JP', 'age': 22, 'name': 'lisi'}
    USA {'country': 'USA', 'age': 19, 'name': 'wangwu'}
    USA {'country': 'USA', 'age': 22, 'name': 'zhaoliu'}
    USA {'country': 'USA', 'age': 22, 'name': 'pengqi'}
    print [key for key,group in lstg] #返回：['China', 'JP', 'USA']
    print [(key,list(group)) for key,group in lstg]
    #返回的list中包含着三个元组：
    [('China', [{'country': 'China', 'age': 20, 'name': 'zhangsan'}, {'country': 'China', 'age': 22, 'name': 'lijiu'}]), ('JP', [{'country': 'JP', 'age': 22, 'name': 'lisi'}]), ('USA', [{'country': 'USA', 'age': 19, 'name': 'wangwu'}, {'country': 'USA', 'age': 22, 'name': 'zhaoliu'}, {'country': 'USA', 'age': 22, 'name': 'pengqi'}])]
    print dict([(key,list(group)) for key,group in lstg])
    #返回的是一个字典：
    {'JP': [{'country': 'JP', 'age': 22, 'name': 'lisi'}], 'China': [{'country': 'China', 'age': 20, 'name': 'zhangsan'}, {'country': 'China', 'age': 22, 'name': 'lijiu'}], 'USA': [{'country': 'USA', 'age': 19, 'name': 'wangwu'}, {'country': 'USA', 'age': 22, 'name': 'zhaoliu'}, {'country': 'USA', 'age': 22, 'name': 'pengqi'}]}
    print dict([(key,len(list(group))) for key,group in lstg])
    #返回每个分组的个数：
    {'JP': 1, 'China': 2, 'USA': 3}
    #返回包含有2个以上元素的分组
    print [key for key,group in groupby(sorted(lst,key=itemgetter('country')),itemgetter('country')) if len(list(group))>=2]
    #返回：['China', 'USA']
    lstg = groupby(sorted(lst,key=itemgetter('country')),key=itemgetter('country')) 
    lstgall=[(key,list(group)) for key,group in lstg ]
    print dict(filter(lambda x:len(x[1])>2,lstgall)) 
    #过滤出分组后的元素个数大于2个的分组，返回：
    {'USA': [{'country': 'USA', 'age': 19, 'name': 'wangwu'}, {'country': 'USA', 'age': 22, 'name': 'zhaoliu'}, {'country': 'USA', 'age': 22, 'name': 'pengqi'}]}
```

自定义分组：

```python

    from itertools import groupby
    lst=[2,8,11,25,43,6,9,29,51,66]
    def gb(num):
      if num <= 10:
        return 'less'
      elif num >=30:
        return 'great'
      else:
        return 'middle'
    print [(k,list(g))for k,g in groupby(sorted(lst),key=gb)]
```

返回：

```python

    [('less', [2, 6, 8, 9]), ('middle', [11, 25, 29]), ('great', [43, 51, 66])]
```

**总结**  

以上所述是小编给大家介绍的Python中的分组函数groupby和itertools），希望对大家有所帮助，如果大家有任何疑问请给我留言，小编会及时回复大家的。在此也非常感谢大家对脚本之家网站的支持！

