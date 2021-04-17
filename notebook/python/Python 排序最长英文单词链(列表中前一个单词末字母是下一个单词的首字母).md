使用递归实现  

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

输出：

> ['hedgehog', 'giraffe', 'elephant', 'tiger', 'racoon']

工作原理类似于广度优先搜索，因为只要当前值之前没有被调用，get_results函数就会继续遍历整个列表。函数已经查找过的值被添加到_seen列表中，最终停止递归调用流。这个解决方案也会忽略重复的结果，

```python

    words = ['giraffe', 'elephant', 'ant', 'ning', 'tiger', 'racoon', 'cat', 'hedgehog', 'mouse',]
    new_d = [list(get_results(i, [i], []))[0] for i in words]
    final_d = max([i for i in new_d if len(i) == len(set(i))], key=len)
    
```

输出：

> ['ant', 'tiger', 'racoon', 'ning', 'giraffe', 'elephant']

到此这篇关于Python 排序最长英文单词链(列表中前一个单词末字母是下一个单词的首字母)的文章就介绍到这了,更多相关Python
排序最长英文单词链内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

