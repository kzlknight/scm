
```python

    # 基础版，不依赖环境
    
    import time
    import base64
    import hashlib
    class Token_hander():
      def __init__(self,out_time):
        self.out_time = out_time
        self.time = self.timer
        pass
      def timer(self):
        return time.time()
    
      def hax(self,str):
        """
        摘要算法加密
        :param str: 待加密字符串
        :return: 加密后的字符串
        """
        if not isinstance(str,bytes): # 如果传入不是bytes类型，则转为bytes类型
          try:
            str = bytes(str,encoding="utf8")
          except BaseException as ex:
            raise ValueError("'%s'不可被转换为bytes类型"%str)
    
        md5 = hashlib.md5()
        md5.update("天王盖地虎erafe23".encode(encoding='utf-8'))
        md5.update(str)
        md5.update("992ksd上山打老虎da".encode(encoding='utf-8'))
        return md5.hexdigest()
    
      def build_token(self,message):
        """
        hax_message: 待加密字符串内容 格式： '当前时间戳：message：过期时间戳'
        :param message: 需要生成token的字符串
        :param time: 过期时间
        :return: token
        """
        hax_message = "%s:%s:%s"%(str(self.time()),message,
    　　　　　　　　　　　　　　　　　　　　str(float(self.time())+float(self.out_time)))
        hax_res = self.hax(hax_message)
        token = base64.urlsafe_b64encode(("%s:%s"%(hax_message,hax_res)).encode(encoding='utf-8'))
        return token.decode("utf-8")
    
      def check_token(self,token):
        """
    
        :param token: 待检验的token
        :return: False  or new token
        """
        try:
          hax_res = base64.urlsafe_b64decode(token.encode("utf8")).decode("utf-8")
          message_list = hax_res.split(":")
          md5 = message_list.pop(-1)
          message = ':'.join(message_list)
          if md5 != self.hax(message):
            # 加密内容如果与加密后的结果不符即token不合法
            return False
          else:
            if self.time() - float(message_list.pop(-1)) >0:
              # 超时返回False
              return False
            else:
              # token验证成功返回新的token
              return self.build_token(message_list.pop(-1))
        except BaseException as ex:
          # 有异常表明验证失败或者传入参数不合法
          return False
    
    # 测试
    if __name__ == '__main__':
      token_hand = Token_hander(5)
      token = token_hand.build_token(b'dxxx')
      print(token_hand.check_token(token))
      time.sleep(5)
      print(token_hand.check_token(token))
```

```python

    # 封装成Django源码版
    # 依赖Django运行环境，不可单独测试，需运行Django环境，
    # 需要在settings配置文件中配置 OUT_TIME = 时间 ，以秒为单位
    
    import os
    import time
    import base64
    import hashlib
    import importlib
    ENVIRONMENT_VARIABLE = "DJANGO_SETTINGS_MODULE"
    
    
    class Token_hander():
      def __init__(self):
        self.out_time = self.getOutTime()
        self.time = self.timer
    
    
        pass
      def timer(self):
        return time.time()
    
    
      def getOutTime(self):
        module = importlib.import_module(os.environ.get(ENVIRONMENT_VARIABLE))
        return getattr(module, "OUT_TIME",60)  # 在settings配置文件中找 OUT_TIME 变量，如果没有，默认60秒
    
      def hax(self,str):
        """
        摘要算法加密
        :param str: 待加密字符串
        :return: 加密后的字符串
        """
        if not isinstance(str,bytes): # 如果传入不是bytes类型，则转为bytes类型
          try:
            str = bytes(str,encoding="utf8")
          except BaseException as ex:
            raise ValueError("'%s'不可被转换为bytes类型"%str)
    
        md5 = hashlib.md5()
        md5.update("天王盖地虎erafe23".encode(encoding='utf-8'))
        md5.update(str)
        md5.update("992ksd上山打老虎da".encode(encoding='utf-8'))
        return md5.hexdigest()
    
      def build_token(self,message):
        """
        hax_message: 待加密字符串内容 格式： '当前时间戳：message：过期时间戳'
        :param message: 需要生成token的字符串
        :param time: 过期时间
        :return: token
        """
        hax_message = "%s:%s:%s"%(str(self.time()),message,
    　　　　　　　　　　　　　　　　　　　　str(float(self.time())+float(self.out_time)))
        hax_res = self.hax(hax_message)
        token = base64.urlsafe_b64encode(("%s:%s"%(hax_message,hax_res)).encode(encoding='utf-8'))
        return token.decode("utf-8")
    
      def check_token(self,token):
        """
    
        :param token: 待检验的token
        :return: False  or new token
        """
        try:
          hax_res = base64.urlsafe_b64decode(token.encode("utf8")).decode("utf-8")
          message_list = hax_res.split(":")
          md5 = message_list.pop(-1)
          message = ':'.join(message_list)
          if md5 != self.hax(message):
            # 加密内容如果与加密后的结果不符即token不合法
            return False
          else:
            if self.time() - float(message_list.pop(-1)) >0:
              # 超时返回False
              return False
            else:
              # token验证成功返回新的token
              return self.build_token(message_list.pop(-1))
        except BaseException as ex:
          # 有异常表明验证失败或者传入参数不合法
          return False
```

```python

    # 封装成Django模块，也依赖Django运行环境 
    # 需要在settings配置文件中配置 OUT_TIME = 时间 ， 秒为单位
    
    
    import time
    import base64
    import hashlib
    from django.conf import settings
    
    
    class Token_hander():
      def __init__(self):
        self.out_time = self.getOutTime()
        self.time = self.timer
    
    
        pass
      def timer(self):
        return time.time()
    
    
      def getOutTime(self):
        try:
          return settings.__getattr__("OUT_time")  # 在导入的settings中找 OUT_TIME 变量
        except BaseException:
          return 60  # 找不到默认60 也可以设置直接抛异常
    
      def hax(self,str):
        """
        摘要算法加密
        :param str: 待加密字符串
        :return: 加密后的字符串
        """
        if not isinstance(str,bytes): # 如果传入不是bytes类型，则转为bytes类型
          try:
            str = bytes(str,encoding="utf8")
          except BaseException as ex:
            raise ValueError("'%s'不可被转换为bytes类型"%str)
    
        md5 = hashlib.md5()
        md5.update("天王盖地虎erafe23".encode(encoding='utf-8'))
        md5.update(str)
        md5.update("992ksd上山打老虎da".encode(encoding='utf-8'))
        return md5.hexdigest()
    
      def build_token(self,message):
        """
        hax_message: 待加密字符串内容 格式： '当前时间戳：message：过期时间戳'
        :param message: 需要生成token的字符串
        :param time: 过期时间
        :return: token
        """
        hax_message = "%s:%s:%s"%(str(self.time()),message,
    　　　　　　　　　　　　　　　　　　　　str(float(self.time())+float(self.out_time)))
        hax_res = self.hax(hax_message)
        token = base64.urlsafe_b64encode(("%s:%s"%(hax_message,hax_res)).encode(encoding='utf-8'))
        return token.decode("utf-8")
    
      def check_token(self,token):
        """
    
        :param token: 待检验的token
        :return: False  or new token
        """
        try:
          hax_res = base64.urlsafe_b64decode(token.encode("utf8")).decode("utf-8")
          message_list = hax_res.split(":")
          md5 = message_list.pop(-1)
          message = ':'.join(message_list)
          if md5 != self.hax(message):
            # 加密内容如果与加密后的结果不符即token不合法
            return False
          else:
            if self.time() - float(message_list.pop(-1)) >0:
              # 超时返回False
              return False
            else:
              # token验证成功返回新的token
              return self.build_token(message_list.pop(-1))
        except BaseException as ex:
          # 有异常表明验证失败或者传入参数不合法
          return False
```

以上就是Python用摘要算法生成token及检验token的示例代码的详细内容，更多关于Python用摘要算法生成token的资料请关注脚本之家其它相关文章！

