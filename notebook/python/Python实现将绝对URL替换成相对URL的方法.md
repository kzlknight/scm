本文实例讲述了Python实现将绝对URL替换成相对URL的方法。分享给大家供大家参考。具体分析如下：

一、问题：

公司一个项目需要上传图片,一开始同事将图片上传后结合当前主机拼成了一个绝对的URL(http://192.168.1.1:888/m/getimg?filename=xxx.jpg)由于同时给手机终端提供接口,在手机终端会引起一些bug,改完代码后要求将以前的uri替换成相对的URL(/m/getimg?filename=xxx.jpg),由于图片是用img标签嵌入到内容同时用a标签括起显示大图的,所以需要读取数据库并对内容进行替换

二、解决方法：

```python

    #!/usr/bin/env python
    #-*- coding:utf-8 -*-
    #
    #
    # author : cold night
    # email  : wh_linux@126.com
    #
    import pymongo
    import re
    from StringIO import StringIO
    conn = pymongo.Connection()
    db = conn.test
    def replace_url():
      regex = re.compile(r'([href¦src])=["¦\']http://.*?(/m/getimg\?.*?)["¦\']')
      results = db['test'].find()
      db_coll = db['test']
      def replace(r):
        content = r.get('content')
        if not content: return
        content = StringIO(content)
        content.seek(0)
        result = StringIO()
        for line in content.readlines():
          t = regex.sub(r'\1="\2"', line)
          result.write(t)
        result.seek(0)
        content = result.read()
        if content:
          r['content'] = content
        _id = r.get('_id')
        db_coll.update({'_id':_id}, r)
      results = [replace(i) for i in results]
    if __name__=="__main__":replace_url()
    
    
```

希望本文所述对大家的Python程序设计有所帮助。

