##  **1、简单应用**  

代码如下：

```python

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    # @File : jieba.analyse.py
    # @Author: 赵路仓
    # @Date : 2020/3/14
    # @Desc : 提取关键字
    # @Contact : 398333404@qq.com
    
    import jieba.analyse
    
    
    text='安全、防止水合物和段塞生成的重要措施之一。因此，针对未来还上油田开发技术，我们预先开展了水深1500米管道式油气水分离器的概念设计。通过该研究，提出适合海洋环境的体积小、重量轻、分离效率高、便于操作和维护的新型油气水三相分离器，使其成为海洋深水油气田开'
    Key=jieba.analyse.extract_tags(text,topK=3)
    print(Key)
```

![](https://img.jbzj.com/file_images/article/202012/20201217163144363.png?20201117163153)

##  2、含参使用

```python

    keywords = jieba.analyse.extract_tags(content, topK=5, withWeight=True, allowPOS=()) 
```

  * 第一个参数：待提取关键词的文本 
  * 第二个参数：返回关键词的数量，重要性从高到低排序 
  * 第三个参数：是否同时返回每个关键词的权重 
  * 第四个参数：词性过滤，为空表示不过滤，若提供则仅返回符合词性要求的关键词 

代码如下：

```python

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    # @File : jieba.analyse.py
    # @Author: 赵路仓
    # @Date : 2020/3/14
    # @Desc : 提取关键字
    # @Contact : 398333404@qq.com
    
    import jieba.analyse
    
    
    # 字符串前面加u表示使用unicode编码
    content = u'安全、防止水合物和段塞生成的重要措施之一。因此，针对未来还上油田开发技术，我们预先开展了水深1500米管道式油气水分离器的概念设计。通过该研究，提出适合海洋环境的体积小、重量轻、分离效率高、便于操作和维护的新型油气水三相分离器，使其成为海洋深水油气田开'
    
    keywords = jieba.analyse.extract_tags(content, topK=5, withWeight=True, allowPOS=())
    # 访问提取结果
    for item in keywords:
      # 分别为关键词和相应的权重
      print(item[0], item[1])
```

![](https://img.jbzj.com/file_images/article/202012/20201217163411382.png?20201117163419)

以上就是python 利用jieba.analyse进行 关键词提取的详细内容，更多关于python 关键词提取的资料请关注脚本之家其它相关文章！

