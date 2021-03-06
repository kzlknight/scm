**时区的概念与转换**

首先要知道时区之间的转换关系，其实这很简单：把当地时间减去当地时区，剩下的就是格林威治时间了。
例如北京时间的18:00就是18:00+08:00，相减以后就是10:00+00:00，因此就是格林威治时间的10:00。  
而把格林威治时间加上当地时区，就能得到当地时间了。
例如格林威治时间的10:00是10:00+00:00，转换成太平洋标准时间就是加上-8小时，因此是02:00-08:00。  
而太平洋标准时间转换成北京时间转换也一样，时区相减即可。
例如太平洋标准时间的02:00-08:00，与北京时间相差-16小时，因此结果是18:00+08:00。

**Python时区的处理  
** 发现python没有简单的处理时区的方法，不明白为什么Python不提供一个时区模块来处理时区问题。
好在我们有个第三方pytz模块，能够帮我们解决一下时区问题。

**pytz简单教程**

pytz查询某个的时区  
可以根据国家代码查找这个国家的所有时区。

_复制代码_ 代码如下:

  
>>> import pytz  
>>> pytz.country_timezones('cn')  
['Asia/Shanghai', 'Asia/Harbin', 'Asia/Chongqing', 'Asia/Urumqi',
'Asia/Kashgar']  

pytz创建时区对象  
根据上面得到的时区信息，就可以创建指定的时区对象。比如创建上海时区对象：

_复制代码_ 代码如下:

  
tz = pytz.timezone('Asia/Shanghai')  

得到某个时区的时间  
然后在创建时间对象时进行指定上面时区，就可以得到指定时区的日期时间：

_复制代码_ 代码如下:

  
>>> import datetime  
>>> datetime.datetime.now(tz)  

