**1.获取当前时间的两种方法：**

_复制代码_ 代码如下:

  
import datetime,time  
now = time.strftime("%Y-%m-%d %H:%M:%S")  
print now  
now = datetime.datetime.now()  
print now  

**2.获取上个月最后一天的日期(本月的第一天减去1天)**

_复制代码_ 代码如下:

  
last =
datetime.date(datetime.date.today().year,datetime.date.today().month,1)-datetime.timedelta(1)  
print last  

**3.获取时间差(时间差单位为秒，常用于计算程序运行的时间)**

_复制代码_ 代码如下:

  
starttime = datetime.datetime.now()  
#long running  
endtime = datetime.datetime.now()  
print (endtime - starttime).seconds  

**4.计算当前时间向后10个小时的时间  
**  

_复制代码_ 代码如下:

  
d1 = datetime.datetime.now()  
d3 = d1 + datetime.timedelta(hours=10)  
d3.ctime()  

其本上常用的类有：datetime和timedelta两个。它们之间可以相互加减。每个类都有一些方法和属性可以查看具体的值，如
datetime可以查看：天数(day)，小时数(hour)，星期几(weekday())等;timedelta可以查看：天数(days)，秒数
(seconds)等。  
  
**5.python中时间日期格式化符号：**  
  
%y 两位数的年份表示（00-99）  
%Y 四位数的年份表示（000-9999）  
%m 月份（01-12）  
%d 月内中的一天（0-31）  
%H 24小时制小时数（0-23）  
%I 12小时制小时数（01-12）  
%M 分钟数（00=59）  
%S 秒（00-59）  
  
%a 本地简化星期名称  
%A 本地完整星期名称  
%b 本地简化的月份名称  
%B 本地完整的月份名称  
%c 本地相应的日期表示和时间表示  
%j 年内的一天（001-366）  
%p 本地A.M.或P.M.的等价符  
%U 一年中的星期数（00-53）星期天为星期的开始  
%w 星期（0-6），星期天为星期的开始  
%W 一年中的星期数（00-53）星期一为星期的开始  
%x 本地相应的日期表示  
%X 本地相应的时间表示  
%Z 当前时区的名称  
%% %号本身

