本文实例讲述了Python爬虫实现简单的爬取有道翻译功能。分享给大家供大家参考，具体如下：

```python

    # -*- coding:utf-8 -*-
    #!python3
    import urllib.request
    import urllib.parse
    import json
    while True :
      content = input("请输入需要翻译的内容:(按q退出)")
      if content == 'q' :
        break
      url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link'
      head = {}
      head[ 'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
      data = {}
      data['type'] = 'AUTO'
      data['i'] = content
      data['doctype'] = 'json'
      data['xmlVersion'] = '1.8'
      data['keyfrom'] = 'fanyi.web'
      data['ue'] = 'UTF-8'
      data['action'] = 'FY_BY_CLICKBUTTON'
      data['typoResult'] = 'true'
      data = urllib.parse.urlencode(data).encode('utf-8')
      req = urllib.request.Request(url,data,head)
      response = urllib.request.urlopen(req)
      html = response.read().decode('utf-8')
      target = json.loads(html)
      print("翻译结果：%s" %(target['translateResult'][0][0]['tgt']))
    
    
```

更多关于Python相关内容可查看本站专题：《 [ Python Socket编程技巧总结
](//www.jb51.net/Special/648.htm) 》、《 [ Python正则表达式用法总结
](//www.jb51.net/Special/667.htm) 》、《 [ Python数据结构与算法教程
](//www.jb51.net/Special/663.htm) 》、《 [ Python函数使用技巧总结
](//www.jb51.net/Special/642.htm) 》、《 [ Python字符串操作技巧汇总
](//www.jb51.net/Special/636.htm) 》、《 [ Python入门与进阶经典教程
](//www.jb51.net/Special/520.htm) 》及《 [ Python文件与目录操作技巧汇总
](//www.jb51.net/Special/516.htm) 》

希望本文所述对大家Python程序设计有所帮助。

