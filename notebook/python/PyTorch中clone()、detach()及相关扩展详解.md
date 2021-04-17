**clone() 与 detach() 对比**

Torch 为了提高速度，向量或是矩阵的赋值是指向同一内存的，这不同于 Matlab。如果需要保存旧的tensor即需要开辟新的存储地址而不是引用，可以用
clone() 进行深拷贝，

首先我们来打印出来clone()操作后的数据类型定义变化：

**(1). 简单打印类型**

```python

    import torch
    
    a = torch.tensor(1.0, requires_grad=True)
    b = a.clone()
    c = a.detach()
    a.data *= 3
    b += 1
    
    print(a) # tensor(3., requires_grad=True)
    print(b)
    print(c)
    
    '''
    输出结果：
    tensor(3., requires_grad=True)
    tensor(2., grad_fn=<AddBackward0>)
    tensor(3.) # detach()后的值随着a的变化出现变化
    '''
    
```

grad_fn=<CloneBackward>，表示clone后的返回值是个中间变量，因此支持梯度的回溯。clone操作在一定程度上可以视为是一个identity-
mapping函数。

detach()操作后的tensor与原始tensor共享数据内存，当原始tensor在计算图中数值发生反向传播等更新之后，detach()的tensor值也发生了改变。

**注意：**
在pytorch中我们不要直接使用id是否相等来判断tensor是否共享内存，这只是充分条件，因为也许底层共享数据内存，但是仍然是新的tensor，比如detach()，如果我们直接打印id会出现以下情况。

```python

    import torch as t
    a = t.tensor([1.0,2.0], requires_grad=True)
    b = a.detach()
    #c[:] = a.detach()
    print(id(a))
    print(id(b))
    #140568935450520
    140570337203616
    
```

显然直接打印出来的id不等，我们可以通过简单的赋值后观察数据变化进行判断。

**(2). clone()的梯度回传  
**

detach()函数可以返回一个完全相同的tensor,与旧的tensor共享内存，脱离计算图，不会牵扯梯度计算。

而clone充当中间变量，会将梯度传给源张量进行叠加，但是本身不保存其grad，即值为None

```python

    import torch
    a = torch.tensor(1.0, requires_grad=True)
    a_ = a.clone()
    y = a**2
    z = a ** 2+a_ * 3
    y.backward()
    print(a.grad) # 2
    z.backward()
    print(a_.grad)　　　# None. 中间variable，无grad
    print(a.grad) 
    '''
    输出：
    tensor(2.) 
    None
    tensor(7.) # 2*2+3=7
    '''
    
```

使用torch.clone()获得的新tensor和原来的数据不再共享内存，但仍保留在计算图中，clone操作在不共享数据内存的同时支持梯度梯度传递与叠加，所以常用在神经网络中某个单元需要重复使用的场景下。

通常如果原tensor的requires_grad=True，则：

  * clone()操作后的tensor requires_grad=True 
  * detach()操作后的tensor requires_grad=False。   

```python

    import torch
    torch.manual_seed(0)
    
    x= torch.tensor([1., 2.], requires_grad=True)
    clone_x = x.clone() 
    detach_x = x.detach()
    clone_detach_x = x.clone().detach() 
    
    f = torch.nn.Linear(2, 1)
    y = f(x)
    y.backward()
    
    print(x.grad)
    print(clone_x.requires_grad)
    print(clone_x.grad)
    print(detach_x.requires_grad)
    print(clone_detach_x.requires_grad)
    '''
    输出结果如下：
    tensor([-0.0053, 0.3793])
    True
    None
    False
    False
    '''
    
```

另一个比较特殊的是当源张量的 require_grad=False，clone后的张量
require_grad=True，此时不存在张量回传现象，可以得到clone后的张量求导。

如下：

```python

    import torch
    a = torch.tensor(1.0)
    a_ = a.clone()
    a_.requires_grad_() #require_grad=True
    y = a_ ** 2
    y.backward()
    print(a.grad) # None
    print(a_.grad) 
    '''
    输出：
    None
    tensor(2.)
    '''
    
```

了解了两者的区别后我们常与其他函数进行搭配使用，实现数据拷贝后的其他需要。

比如我们经常使用view()函数对tensor进行reshape操作。返回的新Tensor与源Tensor可能有不同的size，但是是共享data的，即其中的一个发生变化，另外一个也会跟着改变。

需要注意的是view返回的Tensor与源Tensor是共享data的，但是依然是一个新的Tensor（因为Tensor除了包含data外还有一些其他属性），两者id（内存地址）并不一致。

```python

    x = torch.rand(2, 2)
    y = x.view(4)
    x += 1
    print(x)
    print(y) # 也加了1
    
```

view()
仅仅是改变了对这个张量的观察角度，内部数据并未改变。这时候想返回一个真正新的副本（即不共享data内存）该怎么办呢？Pytorch还提供了一个reshape()可以改变形状，但是此函数并不能保证返回的是其拷贝，所以不推荐使用。推荐先用clone创造一个副本然后再使用view。
[ 参考此处 ](https://stackoverflow.com/questions/49643225/whats-the-difference-
between-reshape-and-view-in-pytorch)

```python

    x = torch.rand(2, 2)
    x_cp = x.clone().view(4)
    x += 1
    print(id(x))
    print(id(x_cp))
    print(x)
    print(x_cp)
    '''
    140568935036464
    140568935035816
    tensor([[0.4963, 0.7682],
     [0.1320, 0.3074]])
    tensor([[1.4963, 1.7682, 1.1320, 1.3074]]) 
    '''
    
```

另外使用clone()会被记录在计算图中，即梯度回传到副本时也会传到源Tensor。 [ 在上一篇中有总结
](//www.jb51.net/article/201724.htm) 。

**总结：**

  * torch.detach() ― 新的tensor会脱离计算图，不会牵扯梯度计算 
  * torch.clone() ― 新的tensor充当中间变量，会保留在计算图中，参与梯度计算（回传叠加），但是一般不会保留自身梯度。   
原地操作(in-place, such as resize_ / resize_as_ / set_ / transpose_)
在上面两者中执行都会引发错误或者警告。

  * 共享数据内存是底层设计，并不能简单的通过直接打印tensor的id地址进行判断，需要在进行赋值或运算操作后打印比较数据的变化进行判断。 
  * 复制操作可以根据实际需要进行结合使用。   

引用官方文档的话：如果你使用了in-place operation而没有报错的话，那么你可以确定你的梯度计算是正确的。另外尽量避免in-place的使用。

像y = x +
y这样的运算会新开内存，然后将y指向新内存。我们可以使用Python自带的id函数进行验证：如果两个实例的ID相同，则它们所对应的内存地址相同。

到此这篇关于PyTorch中clone()、detach()及相关扩展详解的文章就介绍到这了,更多相关PyTorch中clone()、detach()及相关扩展内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

