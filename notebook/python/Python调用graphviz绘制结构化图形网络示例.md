首先要下载： [ Graphviz - Graph Visualization Software
](http://www.graphviz.org/download/)

安装完成后将安装目录的bin 路径加到系统路径中，有时候需要重启电脑。

**然后：**

```python

    pip install graphviz
    
    import graphviz as gz
    
```

**有向图**

```python

    dot = gz.Digraph()
    dot.node('1', 'Test1')
    dot.node('2', 'Test2')
    dot.node('3', 'Test3')
    dot.node('4', 'Test4')
    dot.edges(['12', '23', '34', '24'])
    dot
```

![](https://img.jbzj.com/file_images/article/201911/20191122110132.jpg)

**无向图**

```python

    dot = gz.Graph()
    dot.node('1', 'Test1')
    dot.node('2', 'Test2')
    dot.node('3', 'Test3')
    dot.node('4', 'Test4')
    dot.edges(['12', '23', '34', '24'])
    dot
```

![](https://img.jbzj.com/file_images/article/201911/20191122110140.jpg)

**来个随机点的复杂点的图**

```python

    import random
    
    dot = gz.Digraph()
    for i in range(10):
      dot.node('%s' % i, 'Test%s' % i)
    dot.edges([str(random.randint(10, 99)) for i in range(10)])
    dot
    
```

![](https://img.jbzj.com/file_images/article/201911/20191122110149.jpg)

**绘制神经网络简易图**

```python

    def neural_graph(inp=3, hide=(10, ), outp=3, inp_label='input', hide_label='hide', outp_label='output', dropout=True, style='h', size='2, 1'):
      """
      绘制简易神经网络图（有向图）
      :param inp: 输入神经元个数
      :param hide: 隐藏层神经元个数, 可迭代数组
      :param outp: 输出神经元个数
      :param inp_label: 输入名称显示
      :param hide_label: 隐藏层名称显示
      :param outp_label: 输出名称显示
      :param dropout: 是否全连接
      :param style: 水平或垂直显示， 可选项为 'h', 'v'
      :param size: 图像显示大小
      :return: 有向图
      """
    
      dot = gz.Digraph(name='neural network')
      dot.attr(size=size)
      if style == 'v':
        dot.attr(rankdir='LR')
    
      def draw(enter, exit, label1, label2):
        for i in range(enter):
          for j in range(exit):
            if dropout:
              if random.randint(0, max(enter, exit)):
                dot.edge('%s%s' % (label1, i), '%s%s' % (label2, j))
            else:
              dot.edge('%s%s' % (label1, i), '%s%s' % (label2, j))
      hide = list(hide)
      hide.insert(0, inp)
      hide.append(outp)
      for index, (i, j) in enumerate(zip(hide[:-1], hide[1:])):
        if index == 0:
          draw(i, j, inp_label, hide_label+str(index))
        elif index == len(hide) - 2:
          draw(i, j, hide_label+str(index-1), outp_label)
        else:
          draw(i, j, hide_label+str(index-1), hide_label+str(index))
    
      return dot
    
      #其他运行方式
      #return dot.view()
    
```

![](https://img.jbzj.com/file_images/article/201911/20191122110253.jpg)

![](https://img.jbzj.com/file_images/article/201911/20191122110302.jpg)

![](https://img.jbzj.com/file_images/article/201911/20191122110311.jpg)

![](https://img.jbzj.com/file_images/article/201911/20191122110321.jpg)

![](https://img.jbzj.com/file_images/article/201911/20191122110331.jpg)

![](https://img.jbzj.com/file_images/article/201911/20191122110345.jpg)

以上这篇Python调用graphviz绘制结构化图形网络示例就是小编分享给大家的全部内容了，希望能给大家一个参考，也希望大家多多支持脚本之家。

