**一、subprocess.Popen()**

subprocess模块定义了一个类： Popen

类原型：

```python

    class subprocess.Popen( args, 
      bufsize = 0, 
      executable = None, 
      stdin = None, 
      stdout = None, 
      stderr = None, 
      preexec_fn = None, 
      close_fds = False, 
      shell = False, 
      cwd = None, 
      env = None, 
      universal_newlines = False, 
      startupinfo = None, 
      creationflags = 0)
```

我们只需要关注其中几个参数：

  * args： 

args参数。可以是一个字符串，可以是一个包含程序参数的列表。要执行的程序一般就是这个列表的第一项，或者是字符串本身。

  * shell=True： 

在Linux下，当shell=True时，如果arg是个字符串，就使用shell来解释执行这个字符串。如果args是个列表，则第一项被视为命令，其余的都视为是给shell本身的参数。也就是说，等效于：  
subprocess.Popen(['/bin/sh', '-c', args[0], args[1], ...])

  * stdin stdout和stderr： 

stdin
stdout和stderr，分别表示子程序的标准输入、标准输出和标准错误。可选的值有PIPE或者一个有效的文件描述符（其实是个正整数）或者一个文件对象，还有None。如果是PIPE，则表示需要创建一个新的管道，如果是None，不会做任何重定向工作，子进程的文件描述符会继承父进程的。另外，stderr的值还可以是STDOUT，表示子进程的标准错误也输出到标准输出。

**二、粘包现象**

所谓粘包问题主要还是因为接收方不知道消息之间的界限，还有系统缓存区的问题，时间差的原因，不知道一次性提取多少字节的数据所造成的。

须知：只有TCP有粘包现象，UDP永远不会粘包

粘包不一定会发生，如果发生了：1.可能是在客户端已经粘了；2.客户端没有粘，可能是在服务端粘了

缓冲区的作用：存储少量数据

如果你的网络出现短暂的异常或者波动，接收数据就会出现短暂的中断，影响你的下载或者上传的效率。但是，缓

冲区解决了上传下载的传输效率的问题，带来了黏包问题。

收发的本质：不一定是一收一发

**三、为什么出现粘包?**

1，接收方没有及时接收缓冲区的包，造成多个包接收（客户端发送了一段数据，服务端只收了一小部分，服务端下次再收的时候还是从缓冲区拿上次遗留的数据，产生粘包）recv会产生黏包（如果recv接受的数据量(1024)小于发送的数据量，第一次只能接收规定的数据量1024，第二次接收剩余的数据量）

2，发送端需要等缓冲区满才发送出去，造成粘包（发送数据时间间隔很短，数据也很小，会合到一起，产生粘包）send
也可能发生粘包现象。（连续send少量的数据发到输出缓冲区，由于缓冲区的机制，也可能在缓冲区中不断积压，多次写入的数据被一次性发送到网络）

出现粘包现象的代码实例

server. py

```python

    import socket
    import subprocess
    
    # 建立
    phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # 绑定
    phone.bind(('127.0.0.1', 8081))
    
    # 监听
    phone.listen(5)
    
    # 通信循环
    while True:
      # 接收客户端连接请求
      conn, client_addr = phone.accept()
      while True:
        # 接收客户端数据/命令
        cmd = conn.recv(1024)
        if not cmd:
          break
        # 创建管道
        obj = subprocess.Popen(cmd.decode('utf-8'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout = obj.stdout.read()
        stderr = obj.stderr.read()
        # 向客户端发送数据
        conn.send(stdout)
        conn.send(stderr)
      # 结束连接
      conn.close()
    
    # 关闭套接字
    phone.close()
    
    
```

client. py

```python

    import socket
    
    # 建立
    phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 连接
    phone.connect(('127.0.0.1', 8081))
    while True:
      cmd = input('>>> ').strip()
      if not cmd:
        continue
      if cmd == 'quit':
        break
      # 给服务端发送数据/命令
      phone.send(cmd.encode('utf-8'))
      # 接收服务端数据/命令
      data = phone.recv(1024)
      print(data.decode('utf-8'))
    
    # 关闭套接字
    phone.close()
    
    
```

粘包现象运行结果

![](https://img.jbzj.com/file_images/article/202012/202012593101642.png?202011593110)

![](https://img.jbzj.com/file_images/article/202012/202012593127489.jpg?202011593137)

![](https://img.jbzj.com/file_images/article/202012/202012593152485.jpg?202011593159)

可以观察到执行两次ls命令后，服务端返回的仍然是ifconfig命令的结果，最后一次ls命令的末尾才出现ls命令返回的部分结果

**四、解决粘包问题的代码实例**  
server. py

```python

    import socket
    import subprocess
    import json
    import struct
    
    # 建立
    phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # 绑定
    phone.bind(('127.0.0.1', 8081))
    
    # 监听
    phone.listen(5)
    
    # 通信循环
    while True:
      # 接收客户端连接请求
      conn, client_addr = phone.accept()
      while True:
        # 接收客户端数据/命令
        cmd = conn.recv(1024)
        if not cmd:
          continue
        # 创建数据流管道
        obj = subprocess.Popen(cmd.decode('utf-8'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout = obj.stdout.read()
        stderr = obj.stderr.read()
        # 向客户端发送数据
    
        # 解决粘包问题
        # 1.制作固定长度的报头
        header_dic = {
          'filename': 'a.txt',
          'total_size': len(stdout)+len(stderr)
        }
        # 序列化报头
        header_json = json.dumps(header_dic) # 序列化为byte字节流类型
        header_bytes = header_json.encode('utf-8') # 编码为utf-8（Mac系统）
        # 2.先发送报头的长度
        # 2.1 将byte类型的长度打包成4位int
        conn.send(struct.pack('i', len(header_bytes)))
        # 2.2 再发报头
        conn.send(header_bytes)
        # 2.3 再发真实数据
        conn.send(stdout)
        conn.send(stderr)
      # 结束连接
      conn.close()
    
    # 关闭套接字
    phone.close()
    
```

client. py

```python

    import socket
    import struct
    import json
    
    # 建立
    phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 连接
    phone.connect(('127.0.0.1', 8081))
    while True:
      cmd = input('>>> ').strip()
      if not cmd:
        continue
      if cmd == 'quit':
        break
      # 给服务端发送命令
      phone.send(cmd.encode('utf-8'))
      # 接收服务端数据
    
      # 1.先收报头长度
      obj = phone.recv(4)
      header_size = struct.unpack('i', obj)[0]
      # 2.收报头
      header_bytes = phone.recv(header_size)
      # 3.从报头中解析出数据的真实信息（报头字典）
      header_json = header_bytes.decode('utf-8')
      header_dic = json.loads(header_json)
      total_size = header_dic['total_size']
      # 4.接受真实数据
      recv_size = 0
      recv_data = b''
      while recv_size < total_size:
        res = phone.recv(1024)
        recv_data += res
        recv_size += len(res)
      print(recv_data.decode('utf-8'))
    
    # 关闭套接字
    phone.close()
    
```

以上就是python基于socket模拟实现ssh远程执行命令的详细内容，更多关于python基于socket实现ssh远程执行命令的资料请关注脚本之家其它相关文章！

以上就是python基于socket模拟实现ssh远程执行命令的详细内容，更多关于python socket的资料请关注脚本之家其它相关文章！

