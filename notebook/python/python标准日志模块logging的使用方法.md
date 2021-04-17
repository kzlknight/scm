最近写一个爬虫系统，需要用到python的日志记录模块，于是便学习了一下。  
python的标准库里的日志系统从Python2.3开始支持。只要import logging这个模块即可使用。如果你想开发一个日志系统，
既要把日志输出到控制台， 还要写入日志文件，只要这样使用：  

_复制代码_ 代码如下:

  
import logging  
# 创建一个logger  
logger = logging.getLogger('mylogger')  
logger.setLevel(logging.DEBUG)  
# 创建一个handler，用于写入日志文件  
fh = logging.FileHandler('test.log')  
fh.setLevel(logging.DEBUG)  
# 再创建一个handler，用于输出到控制台  
ch = logging.StreamHandler()  
ch.setLevel(logging.DEBUG)  
# 定义handler的输出格式  
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -
%(message)s')  
fh.setFormatter(formatter)  
ch.setFormatter(formatter)  
# 给logger添加handler  
logger.addHandler(fh)  
logger.addHandler(ch)  
# 记录一条日志  
logger.info('foorbar')  

  
结合上面的例子，我们说下几个最常使用的API：  
logging.getLogger([name])  
返回一个logger实例，如果没有指定name，返回root
logger。只要name相同，返回的logger实例都是同一个而且只有一个，即name和logger实例是一一对应的。这意味着，无需把logger实例在各个模块中传递。只要知道name，就能得到同一个logger实例。  
Logger.setLevel(lvl)  
设置logger的level， level有以下几个级别：  
  
级别高低顺序：NOTSET < DEBUG < INFO < WARNING < ERROR < CRITICAL  
如果把looger的级别设置为INFO， 那么小于INFO级别的日志都不输出， 大于等于INFO级别的日志都输出  

_复制代码_ 代码如下:

  
logger.debug("foobar") # 不输出  
logger.info("foobar") # 输出  
logger.warning("foobar") # 输出  
logger.error("foobar") # 输出  
logger.critical("foobar") # 输出  

  
Logger.addHandler(hdlr)  
通过handler对象可以把日志内容写到不同的地方。比如简单的StreamHandler就是把日志写到类似文件的地方。python提供了十几种实用handler，比较常用有：  

_复制代码_ 代码如下:

  
StreamHandler: 输出到控制台  
FileHandler: 输出到文件  
BaseRotatingHandler 可以按时间写入到不同的日志中。比如将日志按天写入不同的日期结尾的文件文件。  
SocketHandler 用TCP网络连接写LOG  
DatagramHandler 用UDP网络连接写LOG  
SMTPHandler 把LOG写成EMAIL邮寄出去  

  
logging.basicConfig([**kwargs])* 这个函数用来配置root logger， 为root
logger创建一个StreamHandler，设置默认的格式。* 这些函数：
logging.debug()、logging.info()、logging.warning()、logging.error()、logging.critical()
如果调用的时候发现root logger没有任何handler，会自动调用basicConfig添加一个handler* 如果root
logger已有handler，这个函数不做任何事情使用basicConfig来配置root logger的输出格式和level：  

_复制代码_ 代码如下:

  
import logging  
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)  
logging.debug('This message should appear on the console')  

  
ogger对象直接提供日志接口。formatter描述日志的格式。handler把日志写到不同的地方，你可以把日志保存成本地文件，也可以每个小时写一个日志文件，还可以把日志通过socket传到别的机器上。  
从最简单的formatter对象来看。formatter指定的是每一条日志记录的抬头信息，也就是你可以指定日志记录的时间格式、进程号、文件名、函数名等信息。可以用这个方法来创建一个formatter对象：  

_复制代码_ 代码如下:

  
logging.Formatter.__init__( fmt=None, datefmt=None)  

  
fmt参数指定进程号、文件名、函数名等信息是否出现以及格式， datefmt为日期时间格式，默认的日期格式精确到微秒，例如‘2003-07-08
16:49:45,896'。fmt中可以指定多个字段，每个字段的格式为“%(<dictionary key>)s”，
例如你想打印时间、日志级别、日志信息可以用下面的format:  

_复制代码_ 代码如下:

  
'%(asctime)s - %(levelname)s - %(message)s'  

  
![](https://img.jbzj.com/file_images/article/201311/20131101094011.jpg?201310194044)
在记录爬虫系统日志的时候需要定义记录日志的级别，级别越高表示打出来的日志越详细。我们可以用一个字典来设置不同级别对应的不同日志信息：  

_复制代码_ 代码如下:

  
#用字典保存日志级别  
format_dict = {  
1 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),  
2 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),  
3 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),  
4 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'),  
5 : logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  
}  

  
将本文开始的代码封装在一个类中  

_复制代码_ 代码如下:

  
#开发一个日志系统， 既要把日志输出到控制台， 还要写入日志文件  
class Logger():  
def __init__(self, logname, loglevel, logger):  
'''  
指定保存日志的文件路径，日志级别，以及调用文件  
将日志存入到指定的文件中  
'''  
  
# 创建一个logger  
self.logger = logging.getLogger(logger)  
self.logger.setLevel(logging.DEBUG)  
  
# 创建一个handler，用于写入日志文件  
fh = logging.FileHandler(logname)  
fh.setLevel(logging.DEBUG)  
  
# 再创建一个handler，用于输出到控制台  
ch = logging.StreamHandler()  
ch.setLevel(logging.DEBUG)  
  
# 定义handler的输出格式  
#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -
%(message)s')  
formatter = format_dict[int(loglevel)]  
fh.setFormatter(formatter)  
ch.setFormatter(formatter)  
  
# 给logger添加handler  
self.logger.addHandler(fh)  
self.logger.addHandler(ch)  
  
  
def getlog(self):  
return self.logger  

  
再通过以下方式调用，便是一个简单的日志系统了  

_复制代码_ 代码如下:

  
logger = Logger(logname='log.txt', loglevel=1, logger="fox").getlog()  

