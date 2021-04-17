##  基本思路  

现在有这么一个需求需要实现自动化：需要实时获取服务器cpu，gpu温度以及传感器信息上报情况，对高低温环境下对于设备运行状态的影响进行测试。基本思路为利用paramiko
ssh到服务器上，起一个线程用tail -f命令实时获取日志输出，起另外一个线程用‘cat
/sys/class/thermal/thermal_zone0/temp'命令定时获取cpu，gpu温度。

##  代码  

```python

     def get_report_info_perid(self, cmd, diff_time, thre_time):
      # 发送要执行的命令
      pre_time_stamp = [0] * 4
      self._channel.send(cmd + '\r')
      # 回显很长的命令可能执行较久，通过循环分批次取回回显
      time_stamp_arr = []
      index = [0] * 4
      current_line = b''
      line_counter = 0
      line_feed_byte = '\n'.encode(self.encoding)
      while True:
       buffer = self._channel.recv(1)
       if len(buffer) == 0:
        logger.info('end______________')
        break
       current_line += buffer
       if buffer == line_feed_byte:
        line = current_line.decode(self.encoding)
        logger.debug('shell显示：%s'%line)
        if not line.startswith(self.rq):
         line_counter += 1
         current_line = b''
         continue
        col = self.check_type(line)
        time_stamp = int(time.mktime(time.strptime(' '.join([line[:8], line[9:17]]), "%Y%m%d %H:%M:%S")))
        time_stamp_dec = line[18: 21] # 精确到毫秒
        time_stamp = time_stamp * 1000 + int(time_stamp_dec)
        logger.info('%s:%s' % (senior_name[col], time_stamp))
        self.write_xl(index[col] + 1, col, time_stamp)
        index[col] += 1
        if pre_time_stamp[col] == 0:
         pre_time_stamp[col] = time_stamp
        else:
         if abs((time_stamp - pre_time_stamp[col]) - diff_time[col]) > thre_time[col]:
          logger.error(
           '两帧数据间隔为{}ms,时间戳分别为:({},{}),行号：{}'.format(time_stamp - pre_time_stamp[col], time_stamp, pre_time_stamp[col],
                      index[col]))
        pre_time_stamp[col] = time_stamp
        line_counter += 1
        current_line = b''
    
    
     def get_temp_info(self, col, max_number):
      index = 0
      cpu_arr, gpu_arr = [], []
      while True:
       cpu_temp, gpu_temp = self.get_cpu_gpu_temp()
       logger.info('cpu_temp:%s, gpu_temp:%s' % (cpu_temp, gpu_temp))
       cpu_arr.append(cpu_temp)
       gpu_arr.append(gpu_temp)
       self.write_xl(index + 1, col, cpu_temp)
       self.write_xl(index + 1, col + 1, cpu_temp)
       time.sleep(60)
       index += 1
       if max_number == index:
        break
      return cpu_arr, gpu_arr
    
```

##  遇到问题  

**1.问题1  
**

一开始的cmd命令为 tail -f log.txt | grep -aE “a|b”

结果出现一个问题，在代码运行几分钟之后，就获取不到数据了

一开始以为是paramiko的问题，会在一定时间之后自动关闭client，但是经过调试之后发现是阻塞在_channel.recv，一直收不到服务端的数据导致。

经过百度之后发现由于linux的缓冲机制影响导致tail -f 结合管道|的时候会输出延迟

缓冲是一种有效提高IO效率的方法，把频繁的读写请求积累到一定程度后再一次性的与IO设备交互操作。

IO缓冲有3种，无缓冲，行缓冲，和全缓冲。

  * 无缓冲，就是不使用缓冲机制。面向字节的设备？（stderr） 
  * 行缓冲，缓冲，直到遇到换行符。一般用于终端设备。 
  * 全缓冲，缓冲，直到buffer满。一般用于块设备。 

在终端窗口中执行tail命令，是面向终端设备的，会使用行缓冲，所以日志中每写入一行，立刻就会输出。

当使用管道时，会变为使用全缓冲，这样一来，就要等到日志中写入的字节数填满buffer后才会输出。

解决方法：

把tail的标准输出重定向到标准错误上，并把标准错误也给管道。

因为stderr是无缓冲的。

例如 tail -f >&2 | grep

或者直接去掉管道

**2.问题2**

按照问题一的结论，我去掉了命令中的管道，直接使用 tail -f
log.txt命令，将过滤放到check_type函数中进行，发现运行几分钟之后获取不到数据的情况并没有解决。于是继续定位。最后经过一番挫折之后发现是使用的tail
-f命令有问题

tail -f

