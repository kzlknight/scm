本文主要介绍Python中单词字符串的列表(list)，找出列表中所有单词中前一个单词首字母和后一个单词尾字母相同，组成最长的单词链方法代码，并且每个单词不能多次使用。  

例如：

```python

    words = ['giraffe', 'elephant', 'ant', 'tiger', 'racoon', 'cat', 'hedgehog', 'mouse']
    
```

最长的单词链列表：

```python

    ['hedgehog', 'giraffe', 'elephant', 'tiger', 'racoon']
    
```

###  1、用递归方法查找

```python

    words = ['giraffe', 'elephant', 'ant', 'tiger', 'racoon', 'cat', 'hedgehog', 'mouse']
    def get_results(_start, _current, _seen):
     if all(c in _seen for c in words if c[0] == _start[-1]):
      yield _current
     else:
       for i in words:
        if i[0] == _start[-1]:
         yield from get_results(i, _current+[i], _seen+[i])
    
    new_d = [list(get_results(i, [i], []))[0] for i in words]
    final_d = max([i for i in new_d if len(i) == len(set(i))], key=len)
    
    
```

输出结果：

> ['hedgehog', 'giraffe', 'elephant', 'tiger', 'racoon']  
>

###  2、使用networkx查找

```python

    import networkx as nx
    import matplotlib.pyplot as plt
    words = ['giraffe', 'elephant', 'ant', 'tiger', 'racoon', 'cat',
         'hedgehog', 'mouse']
    G = nx.DiGraph()
    G.add_nodes_from(words)
    for word1 in words:
      for word2 in words:
        if word1 != word2 and word1[-1] == word2[0]:
          G.add_edge(word1, word2)
    nx.draw_networkx(G)
    plt.show()
    print(nx.algorithms.dag.dag_longest_path(G))
    
    
```

到此这篇关于Python 找出英文单词列表(list)中最长单词链的文章就介绍到这了,更多相关Python
列表最长单词链内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

