一、服务端(Server.py)  
服务端要做的事情是：  
1. 创建一个Socket对象   

![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) import  socket  
![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) s  =
socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

2. 绑定一个端口   

![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) s.bind((  ""
,  8081  ))

3. 接受来自客户端的消息   

![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) while  True:  
![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) #  Receive up
to 1,024 bytes in a datagram  
![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) data, addr  =
s.recvfrom(  1024  )  
![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) print  "
Received:  "  , data,  "  from  "  , addr

二、客户端(Client.py)  
客户端要做的事情是：  
1. 创建一个Socket对象。   

![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) import  socket  
![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) s  =
socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

2. 向某个服务器的指定的端口发送消息。由于使用UDP，如果服务器端未接收到将会丢弃数据包。   

![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) port  =  8081  
![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) host  =  "
localhost  "  
![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) while  True:  
![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) msg  =
raw_input()  
![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) s.sendto(msg,
(host, port))

三、运行试试  
![](http://images.cnblogs.com/cnblogs_com/coderzh/SocketPic.jpg)

