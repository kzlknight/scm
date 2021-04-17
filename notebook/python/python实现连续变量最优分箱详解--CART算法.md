关于变量分箱主要分为两大类：有监督型和无监督型

**对应的分箱方法：**

A. 无监督：(1) 等宽 (2) 等频 (3) 聚类

B. 有监督：(1) 卡方分箱法(ChiMerge) (2) ID3、C4.5、CART等单变量决策树算法 (3) 信用评分建模的IV最大化分箱 等

本篇使用python，基于CART算法对连续变量进行最优分箱

由于CART是决策树分类算法，所以相当于是单变量决策树分类。

**简单介绍下理论：**

CART是二叉树，每次仅进行二元分类，对于连续性变量，方法是依次计算相邻两元素值的中位数，将数据集一分为二，计算该点作为切割点时的基尼值较分割前的基尼值下降程度，每次切分时，选择基尼下降程度最大的点为最优切分点，再将切分后的数据集按同样原则切分，直至终止条件为止。

关于CART分类的终止条件：视实际情况而定，我的案例设置为 a.每个叶子节点的样本量>=总样本量的5%
b.内部节点再划分所需的最小样本数>=总样本量的10%

**python代码实现：**

```python

    import pandas as pd
    import numpy as np
     
    #读取数据集，至少包含变量和target两列
    sample_set = pd.read_excel('/数据样本.xlsx')
     
    def calc_score_median(sample_set, var):
      '''
      计算相邻评分的中位数，以便进行决策树二元切分
      param sample_set: 待切分样本
      param var: 分割变量名称
      '''
      var_list = list(np.unique(sample_set[var]))
      var_median_list = []
      for i in range(len(var_list) -1):
        var_median = (var_list[i] + var_list[i+1]) / 2
        var_median_list.append(var_median)
      return var_median_list
```

var表示需要进行分箱的变量名，返回一个样本变量中位数的list

```python

    def choose_best_split(sample_set, var, min_sample):
      '''
      使用CART分类决策树选择最好的样本切分点
      返回切分点
      param sample_set: 待切分样本
      param var: 分割变量名称
      param min_sample: 待切分样本的最小样本量(限制条件)
      '''
      # 根据样本评分计算相邻不同分数的中间值
      score_median_list = calc_score_median(sample_set, var)
      median_len = len(score_median_list)
      sample_cnt = sample_set.shape[0]
      sample1_cnt = sum(sample_set['target'])
      sample0_cnt = sample_cnt- sample1_cnt
      Gini = 1 - np.square(sample1_cnt / sample_cnt) - np.square(sample0_cnt / sample_cnt)
      
      bestGini = 0.0; bestSplit_point = 0.0; bestSplit_position = 0.0
      for i in range(median_len):
        left = sample_set[sample_set[var] < score_median_list[i]]
        right = sample_set[sample_set[var] > score_median_list[i]]
        
        left_cnt = left.shape[0]; right_cnt = right.shape[0]
        left1_cnt = sum(left['target']); right1_cnt = sum(right['target'])
        left0_cnt = left_cnt - left1_cnt; right0_cnt = right_cnt - right1_cnt
        left_ratio = left_cnt / sample_cnt; right_ratio = right_cnt / sample_cnt
        
        if left_cnt < min_sample or right_cnt < min_sample:
          continue
        
        Gini_left = 1 - np.square(left1_cnt / left_cnt) - np.square(left0_cnt / left_cnt)
        Gini_right = 1 - np.square(right1_cnt / right_cnt) - np.square(right0_cnt / right_cnt)
        Gini_temp = Gini - (left_ratio * Gini_left + right_ratio * Gini_right)
        if Gini_temp > bestGini:
          bestGini = Gini_temp; bestSplit_point = score_median_list[i]
          if median_len > 1:
            bestSplit_position = i / (median_len - 1)
          else:
            bestSplit_position = i / median_len
        else:
          continue
            
      Gini = Gini - bestGini
      return bestSplit_point, bestSplit_position
```

min_sample 参数为最小叶子节点的样本阈值，如果小于该阈值则不进行切分，如前面所述设置为整体样本量的5%

返回的结果我这里只返回了最优分割点，如果需要返回其他的比如GINI值，可以自行添加。

```python

    def bining_data_split(sample_set, var, min_sample, split_list):
      '''
      划分数据找到最优分割点list
      param sample_set: 待切分样本
      param var: 分割变量名称
      param min_sample: 待切分样本的最小样本量(限制条件)
      param split_list: 最优分割点list
      '''
      split, position = choose_best_split(sample_set, var, min_sample)
      if split != 0.0:
        split_list.append(split)
      # 根据分割点划分数据集，继续进行划分
      sample_set_left = sample_set[sample_set[var] < split]
      sample_set_right = sample_set[sample_set[var] > split]
      # 如果左子树样本量超过2倍最小样本量，且分割点不是第一个分割点，则切分左子树
      if len(sample_set_left) >= min_sample * 2 and position not in [0.0, 1.0]:
        bining_data_split(sample_set_left, var, min_sample, split_list)
      else:
        None
      # 如果右子树样本量超过2倍最小样本量，且分割点不是最后一个分割点，则切分右子树
      if len(sample_set_right) >= min_sample * 2 and position not in [0.0, 1.0]:
        bining_data_split(sample_set_right, var, min_sample, split_list)
      else:
        None
```

split_list 参数是用来保存返回的切分点，每次切分后返回的切分点存入该list

在这里判断切分点分割的左子树和右子树是否满足“内部节点再划分所需的最小样本数>=总样本量的10%”的条件，如果满足则进行递归调用。

```python

    def get_bestsplit_list(sample_set, var):
      '''
      根据分箱得到最优分割点list
      param sample_set: 待切分样本
      param var: 分割变量名称
      '''
      # 计算最小样本阈值（终止条件）
      min_df = sample_set.shape[0] * 0.05
      split_list = []
      # 计算第一个和最后一个分割点
      bining_data_split(sample_set, var, min_df, split_list)
      return split_list
```

最后整合以下来个函数调用，返回一个分割点list。

可以使用sklearn库的决策树测试一下单变量分类对结果进行验证，在分类方法相同，剪枝条件一致的情况下结果是一致的。

以上这篇python实现连续变量最优分箱详解--CART算法就是小编分享给大家的全部内容了，希望能给大家一个参考，也希望大家多多支持脚本之家。

