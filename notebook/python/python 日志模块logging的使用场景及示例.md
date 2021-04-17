##  前言

日志是对于软件执行所发生的事件的一种追踪记录方式。日常使用过程中对代码执行的错误和问题会进行查看日志来分析定位问题所在。平常编写代码以及调试也经常用到。通常的新手的做法是直接print打印，但是打印的结果只在控制台显示。今天我们学习一种高级的日志打印和记录模块logging。

logging提供了一系列的函数，它们是debug(), info(), warning(), error(), 和critical()。

他们的使用场景请看下表

你想要执行的任务  |  此任务的最好的工具  
---|---  
对于命令行或程序的应用，结果显示在控制台。  |  print()  
在对程序的普通操作发生时提交事件报告(比如：状态监控和错误调查)  |  logging.info() 函数(当有诊断目的需要详细输出信息时使用
logging.debug() 函数)  
提出一个警告信息基于一个特殊的运行时事件  |
warnings.warn()位于代码库中，该事件是可以避免的，需要修改客户端应用以消除告警logging.warning()
不需要修改客户端应用，但是该事件还是需要引起关注  
对一个特殊的运行时事件报告错误  |  引发异常  
报告错误而不引发异常(如在长时间运行中的服务端进程的错误处理)  |  logging.error(), logging.exception() 或
logging.critical()分别适用于特定的错误及应用领域  
  
日志功能分别对各种事件和严重性都进行分级。

名称  |  何时使用  |  等级  
---|---|---  
DEBUG  |  细节信息，仅当诊断问题时适用。  |  10  
INFO  |  确认程序按预期运行  |  20  
WARNING  |  表明有已经或即将发生的意外（例如：磁盘空间不足）。程序仍按预期进行  |  30  
ERROR  |  由于严重的问题，程序的某些功能已经不能正常执行  |  40  
CRITICAL  |  严重的错误，表明程序已不能继续执行  |  50  
  
##  示例

###  简单示例

因为是python自带的所以无需安装，默认的级别是WARNING，所以下面只显示一条warning信息。

```python

    import logging
    logging.warning('this is warning')
    logging.info('this is info')
```

![](https://img.jbzj.com/file_images/article/202101/20211484951967.png?2021048503)

###  更改级别

我们将默认的级别改成最低级别，则会打印同级别以及高级别的日志信息

```python

    import logging 
    logging.basicConfig(level=logging.DEBUG)
    logging.debug('this is debug')
    logging.info('this is info')
    logging.warning('this is warning')
    logging.error('this is error')
```

![](https://img.jbzj.com/file_images/article/202101/20211485039484.png?20210485046)

###  保存日志

只是打印到控制台对于少量信息倒是可控，但是信息量大的时候就不方便查找了。那么我们需要将其保存到文件中。

```python

    import logging 
    logging.basicConfig(level=logging.DEBUG,filename='log.log',format='%(asctime)s - %(lineno)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    logger.debug('this is debug')
    logger.info('this is info')
    logger.warning('this is warning')
    logger.error('this is error')
```

![](https://img.jbzj.com/file_images/article/202101/20211485125410.png?20210485133)

上面我们在保存的时候，同时还添加了其他描述信息，比如执行时间，执行代码行数，日志级别，打印消息。当然方法远不止这些，具体请看下表

属性名称  |  格式  |  描述  
---|---|---  
ARGS  |  你不需要自己设置格式。  |  参数元组被合并到msg中以产生消息，或者其值被用于合并的词典（当只有一个参数时，它是一个字典）。  
asctime  |  ％（asctime）类  |  创建时的可读时间。默认情况下，这是'2003-07-08
16：49：45,896'的格式（逗号之后的数字是毫秒部分）。  
created  |  ％（created）的F  |  创建的时间（由time.time（）返回）。  
exc_info  |  你不需要自己设置格式。  |  异常元组（àla sys.exc_info）或，如果没有发生异常，则为无。  
filename  |  ％（filename）类  |  路径名的文件名部分。  
funcName  |  ％（funcName）类  |  包含日志记录调用的函数的名称。  
levelname  |  ％（levelname）■  |
文本消息级别（'DEBUG'，'INFO'，'WARNING'，'ERROR'，'CRITICAL'）。  
levelno  |  ％（levelno）s  |  消息的数字记录级别（DEBUG，INFO，WARNING，ERROR，CRITICAL）。  
lineno  |  ％（lineno）d  |  发出日志记录调用的源行号。  
module  |  ％（module）类  |  模块（文件名称部分）。  
msecs  |  ％（msecs）d  |  创建时的毫秒部分。  
message  |  ％（message）类  |  记录的消息，计算为msg％args。这是在调用Formatter.format（）时设置的。  
msg  |  你不需要自己设置格式。  |  在原始日志记录调用中传递的格式字符串。与args合并生成消息或任意对象（请参阅使用任意对象作为消息）。  
name  |  ％（name）类  |  用于记录呼叫的记录器的名称。  
pathname  |  ％（filename）类  |  发出日志记录调用的源文件的完整路径名。  
process  |  ％（process）d  |  进程ID。  
processName  |  ％（processName）类  |  进程名称。  
relativeCreated  |  ％（relativeCreated）d  |
相对于加载日志记录模块的时间，LogRecord创建时的时间（以毫秒为单位）。  
thread  |  ％（thread）d  |  线程ID。  
threadName  |  ％（threadName）类  |  线程名称。  
  
###  日志输出进阶

首先了解以下进阶的方法的说明：

StreamHandler 类位于核心 logging 包，它可将日志记录输出发送到数据流例如 sys.stdout, sys.stderr
或任何文件类对象（或者更精确地说，任何支持 write() 和 flush() 方法的对象

FileHandler 类位于核心 logging 包，它可将日志记录输出到磁盘文件中。 它从 StreamHandler 继承了输出功能。

我们需要通过调用 Logger 类（以下称为 loggers ， 记录器）的实例来执行日志记录。

Logger 对象有三个常见的方法：

  * Logger.setLevel() 指定记录器将处理的最低严重性日志消息，其中 debug 是最低内置严重性级别， critical 是最高内置严重性级别。 例如，如果严重性级别为 INFO ，则记录器将仅处理 INFO 、 WARNING 、 ERROR 和 CRITICAL 消息，并将忽略 DEBUG 消息。 
  * Logger.addHandler() 和 Logger.removeHandler() 从记录器对象中添加和删除处理程序对象。处理程序在以下内容中有更详细的介绍 处理程序 。 
  * Logger.addFilter() 和 Logger.removeFilter() 可以添加或移除记录器对象中的过滤器。 Filter 对象 包含更多的过滤器细节。 

下面示例采用添加日志记录器对象输出和上面一样在控制台打印

```python

    import logging
     
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(lineno)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
     
    logger.info('This is a log info')
    logger.debug('Debugging')
    logger.warning('Warning exists')
    logger.info('Finish')
```

![](https://img.jbzj.com/file_images/article/202101/20211485306751.png?20210485314)

当然也同样能保存到文件，为了演示修改了文件名称为put.log

```python

    import logging
     
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.INFO)
    handler = logging.FileHandler('put.log')
    formatter = logging.Formatter('%(asctime)s - %(lineno)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
     
     
    logger.info('This is a log info')
    logger.debug('Debugging')
    logger.warning('Warning exists')
    logger.info('Finish')
```

![](https://img.jbzj.com/file_images/article/202101/20211485341902.png?20210485347)

###  日志双向输出

```python

    import logging
    
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.INFO)
    handler1 = logging.FileHandler('output.log')
    handler2 = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(lineno)s - %(levelname)s - %(message)s')
    handler1.setFormatter(formatter)
    handler2.setFormatter(formatter)
    logger.addHandler(handler1)
    logger.addHandler(handler2)
    
    logger.info('This is a log info')
    logger.debug('Debugging')
    logger.warning('Warning exists')
    logger.info('Finish')
```

![](https://img.jbzj.com/file_images/article/202101/20211485429911.png?20210485436)

![](https://img.jbzj.com/file_images/article/202101/20211485449971.png?20210485456)

以上就是python 日志模块logging的使用场景及示例的详细内容，更多关于python 日志模块logging的使用的资料请关注脚本之家其它相关文章！

