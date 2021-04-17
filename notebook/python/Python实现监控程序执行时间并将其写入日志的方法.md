本文实例讲述了Python实现监控程序执行时间并将其写入日志的方法。分享给大家供大家参考。具体实现方法如下：

```python

    # /usr/bin/python
    # -*- coding:utf-8 -*-
    from time import time
    def logged(when):
      def log(f,*args,**kargs):
        print '''
             called:
              functions:%s
              args: %r
              kargs: %r
        '''  % (f,args,kargs)
      def pre_logged(f):
        def wrapper(*args,**kargs):
          log(f,*args,**kargs)
          return f(*args,**kargs)
        return wrapper
      def post_logged(f):
        def wrapper(*args,**kargs):
          now = time()
          try:
            return f(*args,**kargs)
          finally:
            log(f,*args,**kargs)
            print "time delta:%s" % (time()-now)
        return wrapper
      try:
        return {"pre":pre_logged,"post":post_logged}[when]
      except KeyError,e:
        raise ValueError(e),'must be "pre" or "post"'
    @logged("post")
    def hello(name):
      print "hello,",name
    hello("world!")
    '''
    等同于： hello = logged("post")(hello("world!"))
    '''
    
    
```

希望本文所述对大家的Python程序设计有所帮助。

