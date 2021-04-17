本文实例讲述了python实现在windows服务中新建进程的方法。分享给大家供大家参考。具体实现方法如下：

需要安装的软件：python和pywin32，我这里装的分别是python-2.6.amd64、pywin32-217.win-amd64-py2.6

文件名：dma_ws.py

```python

    #!python
    import win32serviceutil 
    import win32service 
    import win32event
    import os 
    from subprocess import Popen, PIPE
    import json
    import signal
    run_proc = None
    class DMA_WS(win32serviceutil.ServiceFramework): 
     _svc_name_ = "DMA_WS"
     _svc_display_name_ = "DMA_WS"
     def __init__(self, args): 
      win32serviceutil.ServiceFramework.__init__(self, args) 
      self.hWaitStop = win32event.CreateEvent(None, 0, 0, None) 
     def SvcStop(self):   
      self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING) 
      win32event.SetEvent(self.hWaitStop) 
     def SvcDoRun(self):
      f = file('C:/DXMonitorSystem/dma.conf')
      host = json.load(f)
      f.close()
      dxsrv = os.path.join(host['app_path'], 'DXHttpServer.py')
      run_proc = Popen([host['ironpython'], dxsrv],
          stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=False,
          cwd=host['app_path'])
          #这里新建进程，注意cwd参数必不可少且要是绝对路径
      #res, err = run_proc.communicate()
      #这个函数内的上面部分都是逻辑处理的部分，可以根据自己的需求订制，但下面这行代码任何服务都需要
      win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE) 
      run_proc.kill() # 用于关闭服务所创建的子进程
      #os.kill(run_proc.pid, signal.SIGTERM)
    if __name__=='__main__':
     win32serviceutil.HandleCommandLine(DMA_WS)
    
    
```

使用方法：

创建服务：Python dma_ws.py install

开始服务：python dma_ws.py start

停止服务：python dma_ws.py stop

希望本文所述对大家的Python程序设计有所帮助。

