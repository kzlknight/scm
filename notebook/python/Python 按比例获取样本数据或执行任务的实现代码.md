按比例获取样本数据或执行任务

By:授客 QQ：1033553122

开发环境

win 10

python 3.6.5

需求

已知每种分类的样本占比数，及样本总数，需要按比例获取这些分类的样本。比如，我有4种任务要执行，分别为任务A，任务B，任务C，任务D,
要求执行的总任务次数为100000，且不同分类任务执行次数占比为 A:B:C:D = 3:5:7:9，且在宏观上这些任务同时进行

代码实现

```python

    #!/usr/bin/env python
    # -*- coding:utf-8 -*-
     
     
    __author__ = 'shouke'
     
    import time
    from copy import deepcopy
     
     
    def main():
     
      class_propotion_map = {'A':3, 'B':5, 'C':7, 'D':7} # 分类及样本数比例映射
      class_list = [] # 分类
      class_proption_list = [] # 存放分类样本数比例
     
      for class_type, propotion in class_propotion_map.items(): # 同一个循环，可以保证比例索引和对应分类索引一一对应
        class_list.append(class_type)
        class_proption_list.append(propotion)
     
      temp_class_propotion_list = deepcopy(class_proption_list)
      result = []
     
      t1 = time.time()
      total_sample_num = 100000 #任务执行次数
      for i in range(1, total_sample_num+1):
        max_propotion = max(temp_class_propotion_list)
        if max_propotion > 0:
          index = temp_class_propotion_list.index(max_propotion)
          result.append(class_list[index])
          temp_class_propotion_list[index] -= 1
        elif max_propotion == 0 and min(temp_class_propotion_list) == 0:
          temp_class_propotion_list = deepcopy(class_proption_list)
          index = temp_class_propotion_list.index(max(temp_class_propotion_list))
          result.append(class_list[index])
          temp_class_propotion_list[index] -= 1
    
      t2 = time.time()
      from collections import Counter
      c = Counter(result)
      for item in c.items():
        print(item[0], item[1]/total_sample_num)
      print('耗时：%s'%(t2-t1))
     
    main()
```

运行结果

![](https://img.jbzj.com/file_images/article/202012/202012393505371.png?202011393544)

说明

以上方式大致实现思路就是，获取每种分类样本数所占比例副本数据列表，然后每次从中获取最大比例值，并查找该比例值对应的分类(获取分类后就可以根据需要构造、获取分类样本数据)，找到目标分类后，把比例数据副本中该比例值减1，直到最大比例和最小比例都等于0，接着重置比例副本数据为样本数比例值，重复前面的过程，直到样本数达到目标样本总数，这种方式实现的前提是得提前知道样本总数及不同分类样本数所占比例，且比例值为整数

到此这篇关于Python
按比例获取样本数据或执行任务的文章就介绍到这了,更多相关Python获取样本数据执行任务内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

