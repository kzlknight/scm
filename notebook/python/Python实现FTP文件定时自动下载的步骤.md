之前遇到技术问题总能在技术博客上得到启发，十分感谢各位的无私分享。而自己却很少发文，固然是水平有限，但也限制了知识积累和总结。今后多总结分享，回馈博客的同时也希望大家多多批评。

##  一、需求：

某数据公司每日15:00~17:00之间，在其FTP发布当日数据供下载，我方需及时下载当日数据至指定本地目录。

##  二、分析：

1、需实现FTP登陆、查询、下载功能；

解答：使用内置的ftplib模块中FTP类；

2、需判断文件是否下载；

解答：使用os模块中path.exists方法；

3、需判断在指定时间段内才执行下载任务；

解答：使用内置的time模块抓取当前时间，并与指定时间做比较；

4、需考虑日期切换问题；

解答：使用内置的time模块抓取当前日期，并与变量中的日期做比较。

##  三、代码实现

```python

    #!/usr/bin/env python
    # _*_ coding:utf-8 _*_
    
    '''
    @Time  : 2019-11-11 13:30
    @Author : Peanut_C
    @FileName: ftp_auto_download.py
    '''
    
    
    import time
    from ftplib import FTP
    import os
    
    
    remote_path = "/xxx/yy/z/" # 远端目录
    begin_time = 1500 # 任务开始时间
    end_time = 1700 # 任务结束时间
    
    
    today = time.strftime("%Y%m%d") # 当天日期
    today_file = today + 'test.txt' # 得到当天日期的目标文件名
    remote_file = remote_path + today_file # 远端文件名
    local_file = '\\\\local\\' + today + '\\' + today_file # 本地文件名
    log_file = 'C:\\\\log\\ftp_log.txt'
    
    
    def ftp_connect():
      """用于FTP连接"""
      ftp_server = 'w.x.y.z' # ftp站点对应的IP地址
      username = 'ftpuser' # 用户名
      password = 'ftppass' # 密码
      ftp = FTP()
      ftp.set_debuglevel(0) # 较高的级别方便排查问题
      ftp.connect(ftp_server, 21)
      ftp.login(username, password)
      return ftp
    
    def remote_file_exists():
      """用于FTP站点目标文件存在检测"""
      ftp = ftp_connect()
      ftp.cwd(remote_path) # 进入目标目录
      remote_file_names = ftp.nlst() # 获取文件列表
      ftp.quit()
      if today_file in remote_file_names:
        return True
      else:
        return False
    
    def download_file():
      """用于目标文件下载"""
      ftp = ftp_connect()
      bufsize = 1024
      fp = open(local_file, 'wb')
      ftp.set_debuglevel(0) # 较高的级别方便排查问题
      ftp.retrbinary('RETR ' + remote_file, fp.write, bufsize)
      fp.close()
      ftp.quit()
    
    
    while True:
      if int(time.strftime("%H%M")) in range(begin_time, end_time): # 判断是否在执行时间范围
        if int(time.strftime("%Y%m%d")) - int(today) == 0: # 判断是否跨日期
          while not os.path.exists(local_file): # 判断本地是否已有文件
            if remote_file_exists(): # 判断远端是否已有文件
              download_file()
              with open(log_file, 'a') as f:
                f.write('\n' + time.strftime("%Y/%m/%d %H:%M:%S") + " 今日文件已下载！")
              time.sleep(60) # 下载完毕静默1分钟
            else:
              time.sleep(180)
              break # 注意，此处跳出循环重新判断日期，避免周末或当天没文件时陷入内层循环
          else:
            time.sleep(180)
        else:
          """如果跨日期，则根据当前日期，更新各文件日期"""
          today = time.strftime("%Y%m%d") # 当天日期
          today_file = today + 'test.txt' # 得到当天日期的目标文件名
          remote_file = remote_path + today_file # 远端文件名
          local_file = '\\\\local\\' + today + '\\' + today_file # 本地文件名
          with open(log_file, 'a') as f:
            f.write('\n' + time.strftime("%Y/%m/%d %H:%M:%S") + " 任务启动, 文件日期已更新。")
      else:
        time.sleep(1800)
```

##  四、运行情况

保存为pyw文件，任务在后台持续运行，不需要计划任务，省心省力。

不用下载标记，一则较为简洁，二则本地文件如果被人误删或移动可自动重新下载。

日志中，每天仅写入任务启动和文件已下载标志，并记录对应时间，如有需要可再添加。

希望能帮到有需要的朋友。

多多指教！

以上就是Python实现FTP文件定时自动下载的步骤的详细内容，更多关于python ftp文件定时下载的资料请关注脚本之家其它相关文章！

