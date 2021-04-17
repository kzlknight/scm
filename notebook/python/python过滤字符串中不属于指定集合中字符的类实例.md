本文实例讲述了python过滤字符串中不属于指定集合中字符的类。分享给大家供大家参考。具体如下：

```python

    # -*- coding: utf-8 -*-
    import sets
    class Keeper(object):
      def __init__(self, keep):
        self.keep = sets.Set(map(ord, keep))
      def __getitem__(self, n):
        if n not in self.keep:
          return None
        return unichr(n)
      def __call__(self, s):
        return s.translate(self)
    makefilter = Keeper
    if __name__ == '__main__':
      just_vowels = makefilter('aeiouy')
      print just_vowels(u'four score and seven years ago')
      # 输出: ouoeaeeyeaao
      print just_vowels(u'tiger, tiger burning bright')
      # 输出: ieieuii
    
    
```

希望本文所述对大家的Python程序设计有所帮助。

