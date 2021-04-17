pytorch中index_select()的用法

```python

    index_select(input, dim, index)
    
```

功能:在指定的维度dim上选取数据,不如选取某些行,列

参数介绍

  * 第一个参数input是要索引查找的对象 
  * 第二个参数dim是要查找的维度,因为通常情况下我们使用的都是二维张量,所以可以简单的记忆: 0代表行,1代表列 
  * 第三个参数index是你要索引的序列,它是一个tensor对象 

刚开始学习pytorch，遇到了index_select(),一开始不太明白几个参数的意思，后来查了一下资料，算是明白了一点。

```python

    a = torch.linspace(1, 12, steps=12).view(3, 4)
    print(a)
    b = torch.index_select(a, 0, torch.tensor([0, 2]))
    print(b)
    print(a.index_select(0, torch.tensor([0, 2])))
    c = torch.index_select(a, 1, torch.tensor([1, 3]))
    print(c)
    
```

先定义了一个tensor，这里用到了linspace和view方法。  

第一个参数是索引的对象，第二个参数0表示按行索引，1表示按列进行索引，第三个参数是一个tensor，就是索引的序号，比如b里面tensor[0，
2]表示第0行和第2行，c里面tensor[1, 3]表示第1列和第3列。

输出结果如下：

> tensor([[ 1., 2., 3., 4.],  
>  [ 5., 6., 7., 8.],  
>  [ 9., 10., 11., 12.]])  
>  tensor([[ 1., 2., 3., 4.],  
>  [ 9., 10., 11., 12.]])  
>  tensor([[ 1., 2., 3., 4.],  
>  [ 9., 10., 11., 12.]])  
>  tensor([[ 2., 4.],  
>  [ 6., 8.],  
>  [10., 12.]])  
>

示例2

```python

    import torch
     
    x = torch.Tensor([[[1, 2, 3],
              [4, 5, 6]],
     
             [[9, 8, 7],
              [6, 5, 4]]])
    print(x)
    print(x.size())
    index = torch.LongTensor([0, 0, 1])
    print(torch.index_select(x, 0, index))
    print(torch.index_select(x, 0, index).size())
    print(torch.index_select(x, 1, index))
    print(torch.index_select(x, 1, index).size())
    print(torch.index_select(x, 2, index))
    print(torch.index_select(x, 2, index).size())
    
```

input的张量形状为2×2×3，index为[0, 0, 1]的向量

分别从0、1、2三个维度来使用index_select()函数，并输出结果和形状，维度大于2就会报错因为input最大只有三个维度

输出：

> tensor([[[1., 2., 3.],  
>  [4., 5., 6.]],  
>  
>  [[9., 8., 7.],  
>  [6., 5., 4.]]])  
>  torch.Size([2, 2, 3])  
>  tensor([[[1., 2., 3.],  
>  [4., 5., 6.]],  
>  
>  [[1., 2., 3.],  
>  [4., 5., 6.]],  
>  
>  [[9., 8., 7.],  
>  [6., 5., 4.]]])  
>  torch.Size([3, 2, 3])  
>  tensor([[[1., 2., 3.],  
>  [1., 2., 3.],  
>  [4., 5., 6.]],  
>  
>  [[9., 8., 7.],  
>  [9., 8., 7.],  
>  [6., 5., 4.]]])  
>  torch.Size([2, 3, 3])  
>  tensor([[[1., 1., 2.],  
>  [4., 4., 5.]],  
>  
>  [[9., 9., 8.],  
>  [6., 6., 5.]]])  
>  torch.Size([2, 2, 3])  
>

对结果进行分析：

index是大小为3的向量，输入的张量形状为2×2×3

dim = 0时，输出的张量形状为3×2×3

dim = 1时，输出的张量形状为2×3×3

dim = 2时，输出的张量形状为2×2×3

注意输出张量维度的变化与index大小的关系，结合输出的张量与原始张量来分析index_select()函数的作用

到此这篇关于pytorch中index_select()的用法详解的文章就介绍到这了,更多相关pytorch
index_select()内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

