**在使用pymongo时遇到了一个小坑：**

在Flask框架中，将字典插入mongodb后再返回就报错

```python

    @app.route('xxxx')
    def main():
     ...
     data = {
     'a':'a',
     'b':'b'
     }
     mycol.insert_one(data)
     return data
```

```python

    Traceback (most recent call last):
     File "/home/xiang/.local/lib/python3.6/site-packages/flask/app.py", line 2464, in __call__
     return self.wsgi_app(environ, start_response)
     File "/home/xiang/.local/lib/python3.6/site-packages/flask/app.py", line 2450, in wsgi_app
     response = self.handle_exception(e)
     File "/home/xiang/.local/lib/python3.6/site-packages/flask/app.py", line 1867, in handle_exception
     reraise(exc_type, exc_value, tb)
     File "/home/xiang/.local/lib/python3.6/site-packages/flask/_compat.py", line 39, in reraise
     raise value
     File "/home/xiang/.local/lib/python3.6/site-packages/flask/app.py", line 2447, in wsgi_app
     response = self.full_dispatch_request()
     File "/home/xiang/.local/lib/python3.6/site-packages/flask/app.py", line 1953, in full_dispatch_request
     return self.finalize_request(rv)
     File "/home/xiang/.local/lib/python3.6/site-packages/flask/app.py", line 1968, in finalize_request
     response = self.make_response(rv)
     File "/home/xiang/.local/lib/python3.6/site-packages/flask/app.py", line 2112, in make_response
     rv = jsonify(rv)
     File "/home/xiang/.local/lib/python3.6/site-packages/flask/json/__init__.py", line 370, in jsonify
     dumps(data, indent=indent, separators=separators) + "\n",
     File "/home/xiang/.local/lib/python3.6/site-packages/flask/json/__init__.py", line 211, in dumps
     rv = _json.dumps(obj, **kwargs)
     File "/home/xiang/.local/lib/python3.6/site-packages/simplejson/__init__.py", line 412, in dumps
     **kw).encode(obj)
     File "/home/xiang/.local/lib/python3.6/site-packages/simplejson/encoder.py", line 298, in encode
     chunks = list(chunks)
     File "/home/xiang/.local/lib/python3.6/site-packages/simplejson/encoder.py", line 696, in _iterencode
     for chunk in _iterencode_dict(o, _current_indent_level):
     File "/home/xiang/.local/lib/python3.6/site-packages/simplejson/encoder.py", line 652, in _iterencode_dict
     for chunk in chunks:
     File "/home/xiang/.local/lib/python3.6/site-packages/simplejson/encoder.py", line 716, in _iterencode
     o = _default(o)
     File "/home/xiang/.local/lib/python3.6/site-packages/flask/json/__init__.py", line 100, in default
     return _json.JSONEncoder.default(self, o)
     File "/home/xiang/.local/lib/python3.6/site-packages/simplejson/encoder.py", line 273, in default
     o.__class__.__name__)
    TypeError: Object of type ObjectId is not JSON serializable
    
```

这是由于pymongo在进行插入操作时，如果字典中没有‘_id'，会自动添加‘_id'，而它的值为ObjectId实例，flask在对返回值进行编码时无法编码ObjectId类型实例，所以报错，解决办法就是去掉‘_id'或者mycol.insert_one(data.copy())

![](https://img.jbzj.com/file_images/article/202012/20201205104207.jpg)

**补充知识：** **pymongo去重: 插入数据时,不存在则插入,存在则不执行**

爬虫想把爬取的数据存入到mongoDB中, 这时候经常遇到的一个需求就是插入的数据已经存在数据库中, 因此插入前去重就是一个经常性的课题.

**我的想法是：**

如果数据库中已经存在这个数据, 那么就什么也不操作

如果数据不存在, 则插入这个数据

为了实现这个想法, 查了很多文献, 发现使用update 可以实现

下面就是我测试的代码

```

```python

