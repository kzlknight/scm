logging模块是Python的一个标准库模块，开发过程中，可以通过该模块，灵活的完成日志的记录。

logging模块提供了两种记录日志的方式：  

1）使用logging提供的模块级别的函数（logging.basicConfig，logging.debug，logging.info...）  

2）使用logging模块的组件（loggers，handlers，filters，formatters）

简单示例

```python

    import json
    import logging
    
    
    class JsonFilter(logging.Filter):
      #此处定义字段的默认值,如果打印信息时不设置对应字段，则为默认值
      #服务服务名或者服务主机
      server = ""
      #访问ip
      ip = ""
      #访问资源路径
      sourceurl = ""
      #访问方式
      method = ""
      # 访问设备
      devices = ""
      # 访问协议
      Protocols = ""
      #访问结果的HTTP状态码
      result_Httpstatus = ""
      #访问结果的状态码
      result_status = ""
      #访问结果的msg信息
      result_msg = ""
      #访问结果的数据大小
      result_msgsize = ""
      def filter(self, record):
        record.server = self.server
        record.ip = self.ip
        record.sourceurl = self.sourceurl
        record.method = self.method
        record.devices = self.devices
        record.Protocols = self.Protocols
        record.result_Httpstatus = self.result_Httpstatus
        record.result_status = self.result_status
        record.result_msg = self.result_msg
        record.result_msgsize = self.result_msgsize
        return True
    
    
    
    if __name__ == '__main__':
    
      formate = json.dumps({
      "time": "%(asctime)s",
      "levelname": "%(levelname)s",
      "server": "%(server)s",
      "ip": "%(ip)s",
      "sourceurl": "%(sourceurl)s",
      "method": "%(method)s",
      "devices": "%(devices)s",
      "Protocols": "%(Protocols)s",
      "result_Httpstatus": "%(result_Httpstatus)s",
      "result_status": "%(result_status)s",
      "result_msg": "%(result_msg)s",
      "result_msgsize": "%(result_msgsize)s",
      })
      logging.basicConfig(level=logging.DEBUG,format=formate)
      logger = logging.getLogger()
      filter_ = JsonFilter()
      logger.addFilter(filter_)
    
      filter_.server = '127.0.0.1:8100'
      filter_.ip = '127.0.0.1'
      filter_.sourceurl = 'http://127.0.0.1:8100/test'
      filter_.method = 'Get'
      filter_.devices = 'Chrome'
      filter_.Protocols = 'HTTP'
      filter_.result_Httpstatus = '200'
      filter_.result_status = '1001'
      filter_.result_msg = '增加成功'
      filter_.result_msgsize = '4296'
      logger.info("") #如果你需要在打印字段中设置
```

一个完整的例子

```python

    import logging
    import os
    from logging import handlers
    
    
    class JsonFilter(logging.Filter):
      # 此处定义字段的默认值,如果打印信息时不设置对应字段，则为默认值
      # 服务服务名或者服务主机
      server = ""
      # 访问ip
      ip = ""
      # 访问资源路径
      sourceurl = ""
      # 访问方式
      method = ""
      # 访问设备
      devices = ""
      # 访问协议
      Protocols = ""
      # 访问结果的HTTP状态码
      result_Httpstatus = ""
      # 访问结果的状态码
      result_status = ""
      # 访问结果的msg信息
      result_msg = ""
      # 访问结果的数据大小
      result_msgsize = ""
      def filter(self, record):
        record.server = self.server
        record.ip = self.ip
        record.sourceurl = self.sourceurl
        record.method = self.method
        record.devices = self.devices
        record.Protocols = self.Protocols
        record.result_Httpstatus = self.result_Httpstatus
        record.result_status = self.result_status
        record.result_msg = self.result_msg
        record.result_msgsize = self.result_msgsize
        return True
    
    
    class CommonLog(object):
      """
      日志记录
      """
      def __init__(self, logger, logname='Access_log'):
        self.logname = os.path.join("D:\python protest\protest", '%s' % logname)
        self.logger = logger
        self.logger.setLevel(logging.INFO)
        self.logger.propagate = False
        self.filter_ = JsonFilter()
        self.logger.addFilter(self.filter_)
        self.formatter = logging.Formatter("time:%(asctime)s - levelname:%(levelname)s - server:%(server)s - ip:%(ip)s - sourceurl:%(sourceurl)s - method:%(method)s - devices:%(devices)s - Protocols:%(Protocols)s - result_Httpstatus:%(result_Httpstatus)s - result_status:%(result_status)s - result_msg:%(result_msg)s - result_msgsize:%(result_msgsize)s ")
      def console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        fh = logging.handlers.TimedRotatingFileHandler(self.logname, when='MIDNIGHT', interval=1, encoding='utf-8')
        fh.suffix = '%Y-%m-%d.log'
        fh.setLevel(logging.INFO)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)
    
        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)
    
        if level == 'info':
          self.logger.info(message)
        elif level == 'debug':
          self.logger.debug(message)
        elif level == 'warning':
          self.logger.warning(message)
        elif level == 'error':
          self.logger.error(message)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()
    
      def debug(self, message):
        self.console('debug', message)
    
      def info(self, message):
        self.console('info', message)
    
      def warning(self, message):
        self.console('warning', message)
    
      def error(self, message):
        self.console('error', message)
    
    
    if __name__ == '__main__':
      logger = logging.getLogger()
      log = CommonLog(logger)
      log.filter_.server = '127.0.0.1:8100'
      log.filter_.ip = '127.0.0.1'
      log.filter_.sourceurl = 'http://127.0.0.1:8100/test'
      log.filter_.method = 'Get'
      log.filter_.devices = 'Chrome'
      log.filter_.Protocols = 'HTTP'
      log.filter_.result_Httpstatus = '200'
      log.filter_.result_status = '1001'
      log.filter_.result_msg = '增加成功'
      log.filter_.result_msgsize = '4296'
      log.info("")
```

设置日志打印颜色

```python

    # coding:utf-8
    import logging
    import os
    from logging.handlers import RotatingFileHandler # 
    import colorlog # 控制台日志输入颜色
    
    
    
    
    log_colors_config = {
      'DEBUG': 'cyan',
      'INFO': 'green',
      'WARNING': 'yellow',
      'ERROR': 'red',
      'CRITICAL': 'red',
    }
    
    
    class Log:
      def __init__(self, logname='Access_log'):
        self.logname = os.path.join("D:\python_protest\protest", '%s' % logname)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.formatter = colorlog.ColoredFormatter(
        '%(log_color)s[%(asctime)s] [%(filename)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s',
        log_colors=log_colors_config) # 日志输出格式
      def console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        fh = logging.handlers.TimedRotatingFileHandler(self.logname, when='MIDNIGHT', interval=1, encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)
    
        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)
    
        if level == 'info':
          self.logger.info(message)
        elif level == 'debug':
          self.logger.debug(message)
        elif level == 'warning':
          self.logger.warning(message)
        elif level == 'error':
          self.logger.error(message)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        fh.close() # 关闭打开的文件
    
      def debug(self, message):
        self.console('debug', message)
    
      def info(self, message):
        self.console('info', message)
    
      def warning(self, message):
        self.console('warning', message)
    
      def error(self, message):
        self.console('error', message)
    
    
    if __name__ == "__main__":
      log = Log()
      log.info("测试1") # 如果你需要在打印字段中设置
      log.debug("测试2") # 如果你需要在打印字段中设置
```

以上就是本文的全部内容，希望对大家的学习有所帮助，也希望大家多多支持脚本之家。

