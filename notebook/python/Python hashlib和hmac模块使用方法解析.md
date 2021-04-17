python之hashlib模块：主要提供字符加密功能，python3中将md5和sha模块整合到了hashlib模块，支持md5,sha1,
sha224, sha256, sha384, sha512等算法

```python

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    
    import hashlib
    # md5 加密算法
    a = hashlib.md5()
    a.update("Hello Lanten.".encode("utf-8"))
    print("md5 加密算法:", a.hexdigest())
    
    # sha224 加密算法
    b = hashlib.sha224()
    b.update("Hello Lanten.".encode("utf-8"))
    print("sha224 加密算法:", b.hexdigest())
    
    # sha256 加密算法
    c = hashlib.sha256()
    c.update("Hello Lanten.".encode("utf-8"))
    print("sha256 加密算法:", c.hexdigest())
    
    # sha384 加密算法
    d = hashlib.sha384()
    d.update("Hello Lanten.".encode("utf-8"))
    print("sha384 加密算法:", d.hexdigest())
    
    # sha512 加密算法
    e = hashlib.sha512()
    e.update("Hello Lanten.".encode("utf-8"))
    print("sha512 加密算法:", e.hexdigest())
```

python之hmac模块：可以对我们创建的key和内容进行处理后再进行加密

```python

    # hmac 加密算法模块
    import hmac
    message = b"Hello Lanten."
    key = b"secret"
    h = hmac.new(key, message, digestmod = "MD5")
    # h = hmac.new(key)
    # h.update(message)
    print("hmac 加密算法:", h.hexdigest())
```

输出结果：

![](https://img.jbzj.com/file_images/article/202012/2020120809320327.png)

以上就是本文的全部内容，希望对大家的学习有所帮助，也希望大家多多支持脚本之家。

