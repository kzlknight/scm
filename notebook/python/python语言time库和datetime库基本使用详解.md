今天是边复习边创作博客的第三天，我今年大二，我们专业开的有这门课程，因为喜欢所以更加认真学习，本以为没人看呢，看了后台浏览量让我更加认真创作，这篇博客花了2个半小时的时间，结合自己所学，所思，所想写作，目的是为了方便喜欢Python的小白学习，也是一种自我鞭策吧！

python语言使用内置time库和datetime库来处理日期时间

相关术语的解释

  * UTC time Coordinated Universal Time，世界协调时，又称 格林尼治天文时间、世界标准时间。与UTC time对应的是各个时区的local time，东N区的时间比UTC时间早N个小时，因此UTC time + N小时 即为东N区的本地时间；而西N区时间比UTC时间晚N个小时，即 UTC time - N小时 即为西N区的本地时间； 中国在东8区，因此比UTC时间早8小时，可以以UTC+8进行表示。 
  * epoch time 表示时间开始的起点；它是一个特定的时间，不同平台上这个时间点的值不太相同，对于Unix而言，epoch time为 1970-01-01 00:00:00 UTC。 
  * timestamp（时间戳） 也称为Unix时间 或 POSIX时间；它是一种时间表示方式，表示从格林尼治时间1970年1月1日0时0分0秒开始到现在所经过的毫秒数，其值为float类型。 但是有些编程语言的相关方法返回的是秒数（Python就是这样），这个需要看方法的文档说明。需要说明的是时间戳是个差值，其值与时区无关。 

###  调用库的三种方式：  

以time库为例，调用其它库类似

```python

    from time import * (*代表time包含所有的时间处理函数，用到某个也可单定义，调用函数时直接使用，比如：clock())
    import time  (调用函数方式,比如：time.clock())
    import time as t (自定义库的名称，调用时方便，比如：t.clock())
```

###  time库的主要的三类函数：  

以上面第三种库调用方式举例

1.时间获取：t.time();t.ctime();t.gmtime() #每种获取时间不一样，根据需求使用  
2.程序计时：t.clock();t.perf_counter() #使用方式一样  
3.时间格式化：t.strftime(format,t);t.strptime(string,format)  
#format表示要定义的格式，t表示获取的时间，string表示字符串类型时间  
字符串格式化：%y 两位数的年份表示（00-99）  
%Y 四位数的年份表示（000-9999）  
%m 月份（01-12）  
%d 月内中的一天（0-31）  
%H 24小时制小时数（0-23）  
%I 12小时制小时数（01-12）  
%M 分钟数（00=59）  
%S 秒（00-59）  
4.程序休眠：t.sleep()  

```python

    #使用举例
    import time as t
    t0=t.gmtime()
    print(t0)
    t1="2020-12-23 19:23:20"
    t2 = t.strptime(t1,"%Y-%m-%d %H:%M:%S")
    t3 = t.strftime("%y/%m/%d %H:%M:%S")
    print(t2)
    print(t3)
```

> 打印结果：  
>  C:\Users\86185\PycharmProjects\untitled\venv\Scripts\python.exe
> C:/Users/86185/PycharmProjects/untitled/Python复习/hk.py  
>  time.struct_time(tm_year=2020, tm_mon=12, tm_mday=23, tm_hour=12,
> tm_min=22, tm_sec=39, tm_wday=2, tm_yday=358, tm_isdst=0)  
>  time.struct_time(tm_year=2020, tm_mon=12, tm_mday=23, tm_hour=19,
> tm_min=23, tm_sec=20, tm_wday=2, tm_yday=358, tm_isdst=-1)  
>  20/12/23 20:22:39
>
> Process finished with exit code 0

time模块主要用于时间访问和转换，这个模块提供了各种与时间相关的函数。

方法/属性  |  描述  
---|---  
time.altzone  |  返回与utc时间的时间差，以秒为单位（西区该值为正，东区该值为负）。其表示的是本地DST
时区的偏移量，只有daylight非0时才使用。  
time.clock()  |
返回当前进程所消耗的处理器运行时间秒数（不包括sleep时间），值为小数；该方法Python3.3改成了time.process_time()  
time.asctime([t])  |
将一个tuple或struct_time形式的时间（可以通过gmtime()和localtime()方法获取）转换为一个24个字符的时间字符串，格式为:
"Fri Aug 19 11:14:16 2016"。如果参数t未提供，则取localtime()的返回值作为参数。  
time.ctime([secs])  |
功能同上，将一个秒数时间戳表示的时间转换为一个表示当前本地时间的字符串。如果参数secs没有提供或值为None，则取time()方法的返回值作为默认值。ctime(secs)等价于asctime(localtime(secs))  
time.time()  |  返回时间戳（自1970-1-1 0:00:00 至今所经历的秒数）  
time.localtime([secs])  |  返回以指定时间戳对应的本地时间的 struct_time对象（可以通过下标，也可以通过 .属性名
的方式来引用内部属性）格式  
time.localtime(time.time() + n*3600)  |  返回n个小时后本地时间的
struct_time对象格式（可以用来实现类似crontab的功能）  
time.gmtime([secs])  |  返回指定时间戳对应的utc时间的 struct_time对象格式（与当前本地时间差8个小时）  
time.gmtime(time.time() + n*3600)  |  返回n个小时后utc时间的 struct_time对象（可以通过 .属性名
的方式来引用内部属性）格式  
time.strptime(time_str, time_format_str)  |
将时间字符串转换为struct_time时间对象，如：time.strptime('2017-01-13 17:07', '%Y-%m-%d %H:%M')  
time.mktime(struct_time_instance)  |  将struct_time对象实例转换成时间戳  
time.strftime(time_format_str[, struct_time_instance])  |
将struct_time对象实例转换成字符串，如果struct_time_instance不指定则取当前本地时间对应的time_struct对象  
  
###  datetime库主要的四类函数：  

datetime库是基于time库进行了封装；以import datetime as dt 为datetime库调用方式

1.date：表示的是日期对象 #dt.date  
2.time；表示的是时间对象 #dt.time ;一般不用date和time函数，datetime函数包含其功能  
3.datetime:表示的是日期时间对象#dt.datetime.now()表示获取当前时间；dt.strftime(format) # 按照
format 进行格式化输出  
4.timedelta:主要用于定义计算时间跨度 #t=dt.timedelat(hours=10)表示定义时间跨度是10小时  

用分隔符'''分类展示如下：

```python

    import datetime as dt
    now = dt.datetime.now() # 获取当前datetime
    print(now)
    输出结果：2019-05-07 16:28:07.198690
    '''
    d = dt.date(2020, 12, 23)
    print(d)
    print('year:', d.year)
    print('month:', d.month)
    print('day:', d.day)
    输出结果：
    2020-12-23
    year: 2020
    month: 12
    day: 23
    '''
    '''
    date1=dt.date(2020,12,23)
    timedel=dt.timedelta(days=4)#表示时间跨度为4天
    print('四天后的日期是：', date1+timedel)
    输出结果：四天后的日期是：2020-12-27
    '''
```

最后配上一段小程序：文本进度条打印程序分析

```python

    import time
    scale = 100 #这个可以随意设置，看需求
    print("执行开始".center(scale//2,'-'))# .center(a,'b')函数是居中符，这条程序是将“执行开始”居中占字符为scale//2（可看需求自定义）,b为填充符
    starttime = time.clock() #time库内置函数，第一次使用是开始计时
    for i in range(scale+1):
      a = '*' * i  #将'*'字符随i的增加而增加
      b = '.' * (scale - i) #将'.'字符随‘*'增加而减少，两个字符总数是scale的初始值数量
      c = (i/scale) * 100 #求百分比
      t = time.clock()-starttime #计算时间，第二次调用time.clock函数表示计时结束
      print("\r{:^3.0f}%[{}->{}]{:.2}s".format(c,a,b,t),end="")#字符格式化，看需求，自己玩就是咋好看咋格式化
      time.sleep(0.05) #time.sleep()函数表示让程序休眠，里面参数是休眠时间根据需求随意定义
    print("\n"+"执行结束".center(scale//2,'-'))#同上;"\n表示换行打印"；"+"连接符，具有连接功能
    
```

关于datetime模块的datetime类会在下面做详细讲解，这里简单说下time.struct_time。

time.struct_time包含如下属性：

下标/索引  |  属性名称  |  描述  
---|---|---  
0  |  tm_year  |  年份，如 2017  
1  |  tm_mon  |  月份，取值范围为[1, 12]  
2  |  tm_mday  |  一个月中的第几天，取值范围为[1-31]  
3  |  tm_hour  |  小时， 取值范围为[0-23]  
4  |  tm_min  |  分钟，取值范围为[0, 59]  
5  |  tm_sec  |  秒，取值范围为[0, 61]  
6  |  tm_wday  |  一个星期中的第几天，取值范围为[0-6]，0表示星期一  
7  |  tm_yday  |  一年中的第几天，取值范围为[1, 366]  
8  |  tm_isdst  |  是否为夏令时，可取值为：0 , 1 或 -1  
  
属性值的获取方式有两种：

  * 可以把它当做一种特殊的有序不可变序列通过 下标/索引 获取各个元素的值，如t[0] 
  * 也可以通过 .属性名 的方式来获取各个元素的值，如t.tm_year。 

需要说明的是struct_time实例的各个属性都是只读的，不可修改。

到此这篇关于python语言time库和datetime库基本使用详解的文章就介绍到这了,更多相关python
time库和datetime库内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

