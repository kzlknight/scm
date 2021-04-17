本文实例讲述了python检查序列seq是否含有aset中项的方法。分享给大家供大家参考。具体实现方法如下：

```python

    # -*- coding: utf-8 -*-
    def containsAny(seq, aset):
      """ 检查序列seq 是否含有aset 中的项 """
      for c in seq:
        if c in aset: return True
      return False
    seq = [1,2,3]
    aset = [3,4,5]
    print(containsAny(seq,aset))
    
    
```

希望本文所述对大家的Python程序设计有所帮助。

