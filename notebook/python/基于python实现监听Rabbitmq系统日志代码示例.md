**介绍  
**

rabbitmq默认有7个交换机，其中amq.rabbitmq.log为系统日志的交换机，这个日志为topic类型，会有三个等级的（routing_key）的日志发送到这个交换机上。

**代码如下**

```python

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    
    
    import pika
    # ########################### 订阅者 ###########################
    credentials = pika.PlainCredentials("用户名","密码")
    connection = pika.BlockingConnection(pika.ConnectionParameters(
      'ip',
      5672,
      '/',
      credentials=credentials))
    
    channel = connection.channel()
    
    
    # 声明队列
    channel.queue_declare(queue='info_queue',durable=True)
    channel.queue_declare(queue='error_queue',durable=True)
    channel.queue_declare(queue='warning_queue',durable=True)
    
    # 绑定
    channel.queue_bind(exchange='amq.rabbitmq.log',queue="info_queue",routing_key="info")
    channel.queue_bind(exchange='amq.rabbitmq.log',queue="error_queue",routing_key="error")
    channel.queue_bind(exchange='amq.rabbitmq.log',queue="warning_queue",routing_key="warning")
    
    print(' [*] Waiting for logs. To exit press CTRL+C')
    
    def callback(ch, method, properties, body):
      print(" [x] %r" % body)
      print(" [x] Done")
      ch.basic_ack(delivery_tag=method.delivery_tag)
    
    channel.basic_consume("info_queue",callback,auto_ack=False)
    channel.basic_consume("error_queue",callback,auto_ack=False)
    channel.basic_consume("warning_queue",callback,auto_ack=False)
    
    channel.start_consuming()
    '''
    然后发布者只需要给exchange发送消息，然后exchange绑定的多个队列都有这个消息了。订阅者就收到这个消息了。
    '''
```

以上就是本文的全部内容，希望对大家的学习有所帮助，也希望大家多多支持脚本之家。

