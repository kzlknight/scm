笔者之前用R开发评分卡时，需要进行分箱计算woe及iv值，采用的R包是smbinning,它可以自动进行分箱。近期换用python开发，
也想实现自动分箱功能，找到了一个woe包，地址 [ https://pypi.org/project/woe/
](https://pypi.org/project/woe/) ，可以直接 pip install woe安装。

由于此woe包官网介绍及给的例子不是很好理解，关于每个函数的使用也没有很详细的说明，经过一番仔细探究后以此文记录一下该woe包的使用及其计算原理。

**例子**

官方给的例子不是很好理解，以下是我写的一个使用示例。以此例来说明各主要函数的使用方法。计算woe的各相关函数主要在feature_process.py中定义。

```python

    import woe.feature_process as fp
    import woe.eval as eval
     
    #%% woe分箱, iv and transform
    data_woe = data #用于存储所有数据的woe值
    civ_list = []
    n_positive = sum(data['target'])
    n_negtive = len(data) - n_positive
    for column in list(data.columns[1:]):
     if data[column].dtypes == 'object':
     civ = fp.proc_woe_discrete(data, column, n_positive, n_negtive, 0.05*len(data), alpha=0.05)
     else:  
     civ = fp.proc_woe_continuous(data, column, n_positive, n_negtive, 0.05*len(data), alpha=0.05)
     civ_list.append(civ)
     data_woe[column] = fp.woe_trans(data[column], civ)
     
    civ_df = eval.eval_feature_detail(civ_list,'output_feature_detail_0315.csv')
    #删除iv值过小的变量
    iv_thre = 0.001
    iv = civ_df[['var_name','iv']].drop_duplicates()
    x_columns = iv.var_name[iv.iv > iv_thre]
```

**计算分箱，woe,iv**

核心函数主要是freature_process.proc_woe_discrete()与freature_process.proc_woe_continuous()，分别用于计算连续变量与离散变量的woe。它们的输入形式相同：

```python

    proc_woe_discrete(df,var,global_bt,global_gt,min_sample,alpha=0.01)
    
    proc_woe_continuous(df,var,global_bt,global_gt,min_sample,alpha=0.01)
    
```

输入：

df: DataFrame，要计算woe的数据，必须包含'target'变量，且变量取值为{0，1}

var:要计算woe的变量名

global_bt:全局变量bad total。df的正样本数量

global_gt:全局变量good total。df的负样本数量

min_sample:指定每个bin中最小样本量，一般设为样本总量的5%。

alpha:用于自动计算分箱时的一个标准，默认0.01.如果iv_划分>iv_不划分*（1+alpha)则划分。

输出：一个自定义的InfoValue类的object，包含了分箱的一切结果信息。

该类定义见以下一段代码。

```python

    class InfoValue(object):
     '''
     InfoValue Class
     '''
     def __init__(self):
     self.var_name = []
     self.split_list = []
     self.iv = 0
     self.woe_list = []
     self.iv_list = []
     self.is_discrete = 0
     self.sub_total_sample_num = []
     self.positive_sample_num = []
     self.negative_sample_num = []
     self.sub_total_num_percentage = []
     self.positive_rate_in_sub_total = []
     self.negative_rate_in_sub_total = []
     
     def init(self,civ):
     self.var_name = civ.var_name
     self.split_list = civ.split_list
     self.iv = civ.iv
     self.woe_list = civ.woe_list
     self.iv_list = civ.iv_list
     self.is_discrete = civ.is_discrete
     self.sub_total_sample_num = civ.sub_total_sample_num
     self.positive_sample_num = civ.positive_sample_num
     self.negative_sample_num = civ.negative_sample_num
     self.sub_total_num_percentage = civ.sub_total_num_percentage
     self.positive_rate_in_sub_total = civ.positive_rate_in_sub_total
     self.negative_rate_in_sub_total = civ.negative_rate_in_sub_total
```

**打印分箱结果**

```python

    eval.eval_feature_detail(Info_Value_list,out_path=False)
```

**输入：**

Info_Value_list:存储各变量分箱结果(proc_woe_continuous/discrete的返回值）的List.

out_path:指定的分箱结果存储路径，输出为csv文件

**输出：**

各变量分箱结果的DataFrame。各列分别包含如下信息：

|  
---|---  
var_name  |  变量名  
split_list  |  划分区间  
sub_total_sample_num  |  该区间总样本数  
positive_sample_num  |  该区间正样本数  
negative_sample_num  |  该区间负样本数  
sub_total_num_percentage  |  该区间总占比  
positive_rate_in_sub_total  |  该区间正样本占总正样本比例  
woe_list  |  woe  
iv_list  |  该区间iv  
iv  |

该变量iv(各区间iv之和）  
  
输出结果一个示例（截取部分）：

![](https://img.jbzj.com/file_images/article/201911/20191122095656.jpg)

**woe转换**

得到分箱及woe,iv结果后，对原数据进行woe转换，主要用以下函数

woe_trans(dvar,civ): replace the var value with the given woe value

输入：

dvar: 要转换的变量，Series

civ: proc_woe_discrete或proc_woe_discrete输出的分箱woe结果，自定义的InfoValue类

输出：

var: woe转换后的变量，Series

**分箱原理**

该包中对变量进行分箱的原理类似于二叉决策树，只是决定如何划分的目标函数是iv值。

**1）连续变量分箱**

首先简要描述分箱主要思想：

1.初始化数据集D =D0为全量数据。转步骤2

2.对于D，将数据按从小到大排序并按数量等分为10份，记录各划分点。计算不进行仍何划分时的iv0，转步骤3.

3.遍历各划分点，计算利用各点进行二分时的iv。

如果最大iv>iv0*(1+alpha)（用户给定，默认0.01）:
则进行划分，且最大iv对应的即确定为此次划分点。它将D划分为左右两个结点，数据集分别为DL, DR.转步骤4.

否则：停止。

4.分别令D=DL,D=DR,重复步骤2.

为了便于理解，上面简化了一些条件。实际划分时还设计到一些限制条件，如不满足会进行区间合并。

主要限制条件有以下2个：

a.每个bin的数量占比>min_sample(用户给定）

b.每个bin的target取值个数>1，即每个bin必须同时包含正负样本。

**2）连续变量分箱**

对于离散变量分箱后续补充 to be continued...

以上这篇python自动分箱,计算woe,iv的实例代码就是小编分享给大家的全部内容了，希望能给大家一个参考，也希望大家多多支持脚本之家。

