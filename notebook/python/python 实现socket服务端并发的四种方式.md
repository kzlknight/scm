##  多进程&多线程  

服务端：多进程和多线程的开启方式相同。

缺点：<1> 由于Cpython的GIL，导致同一时间无法运行多个线程；<2> 不可能无限开进进程或线程

解决办法：多进程、concurrent.futures.ProcessPoolExecutor、线程池

```python

    import socket
    from multiprocessing import Process
    from threading import Thread
    
    
    class MyTcpServer:
      def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.server = socket.socket()
        self.server.bind((self.ip, self.port))
        self.server.listen(5)
    
      def wait_accept(self):
        conn, addr = self.server.accept()
        return conn, addr
    
      def handle_request(self, conn):
        while 1:
          try:
            data = conn.recv(1024)
            if not data: break
            conn.send(data.upper())
          except Exception as e:
            print(e)
            break
        conn.close()
    
    
    if __name__ == '__main__':
      server = MyTcpServer('127.0.0.1', 8888)
      while 1:
        conn, addr = server.wait_accept()
        p = Process(target=server.handle_request, args=(conn, ))	# 创建一个进程
        p.start()	# 告诉操作提供，开启这个进程
```

##  进程池&线程池  

异步提交任务，支持异步接收返回结果(submit返回一个futures对象，调用add_done_callback方法)

```python

    import socket
    from concurrent.futures import ProcessPoolExecutor
    # from concurrent.futures import ThreadPoolExecutor
    
    
    class MyTcpServer:
      def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.server = socket.socket()
        self.server.bind((self.ip, self.port))
        self.server.listen(5)
    
      def wait_accept(self):
        conn, addr = self.server.accept()
        return conn, addr
    
      def handle_request(self, conn):
        while 1:
          try:
            data = conn.recv(1024)
            if not data: break
            conn.send(data.upper())
          except Exception as e:
            print(e)
            break
        conn.close()
    
    
    if __name__ == '__main__':
      server = MyTcpServer('127.0.0.1', 8888)
      pool = ProcessPoolExecutor(5)    # 5个进程一直服务
    
      while 1:
        conn, addr = server.wait_accept()
        pool.submit(server.handle_request, conn)	# 异步提交任务
```

##  socketserver  

优点：简化socket服务端创建流程。  
提供服务端串行和并发两种服务模式（TCPServer，ThreadingTCPServer）  
缺点：windows上无法使用多进程实现并发

```python

    import socketserver
    
    
    class MyTcpHandler(socketserver.BaseRequestHandler):
      def handle(self):		# 通信循环
        while 1:
          try:
            data = self.request.recv(1024)
            if not data: break
            self.request.send(data.upper())
          except Exception as e:
            print(e)
            break
        self.request.close()
    
    
    if __name__ == '__main__':
      ip_port = '127.0.0.1', 8888
      server = socketserver.ThreadingTCPServer(ip_port, MyTcpHandler) # 异步处理 
      server.serve_forever()		# 连接循环
```

**协程**

优点：单线程内实现并发，代码级别模拟IO切换，提高程序运行效率

```python

    from gevent import spawn, monkey;monkey.patch_all()		# 猴子补丁，补丁:常规IO
    import socket
    
    
    class MyTcpServer:
      def __init__(self, ip, port, my_spawn):
        self.ip = ip
        self.port = port
        self.server = socket.socket()
        self.server.bind((self.ip, self.port))
        self.server.listen(5)
        self.spawn = my_spawn		# 保存spawn本地
    
      def wait_accept(self):
        while 1:
          conn, addr = self.server.accept()
          self.spawn(self.handle_request, conn)	# 检测 handle_request的io
    
      def handle_request(self, conn):
        while 1:
          try:
            data = conn.recv(1024)
            if not data: break
            conn.send(data.upper())
          except Exception as e:
            print(e)
            break
        conn.close()
    
    
    if __name__ == '__main__':
      server = MyTcpServer('127.0.0.1', 8888, spawn)
      g1 = server.spawn(server.wait_accept)	# 检测wait_accept的io
      g1.join()	# 等待g1运行结束，即一直在循环检测io
```

以上就是python 实现socket服务端并发的四种方式的详细内容，更多关于python socket服务端并发的资料请关注脚本之家其它相关文章！

