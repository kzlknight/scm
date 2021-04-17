最近在做一任务时，遇到需要延迟处理的数据，最开始的做法是现将数据存储在数据库，然后写个脚本，隔五分钟扫描数据表再处理数据，实际效果并不好。因为系统本身一直在用RabbitMQ做异步处理任务的中间件，所以想到是否可以利用RabbitMQ实现延迟队列。功夫不负有心人，RabbitMQ虽然没有现成可用的延迟队列，但是可以利用其两个重要特性来实现之：1、Time
To Live(TTL)消息超时机制；2、Dead Letter Exchanges（DLX）死信队列。下面将具体描述实现原理以及实现代

**延迟队列的基础原理Time To Live(TTL)**

RabbitMQ可以针对Queue设置x-expires 或者 针对Message设置 x-message-
ttl，来控制消息的生存时间，如果超时(两者同时设置以最先到期的时间为准)，则消息变为dead letter(死信)  
RabbitMQ消息的过期时间有两种方法设置。

通过队列（Queue）的属性设置，队列中所有的消息都有相同的过期时间。（本次延迟队列采用的方案）对消息单独设置，每条消息TTL可以不同。

如果同时使用，则消息的过期时间以两者之间TTL较小的那个数值为准。消息在队列的生存时间一旦超过设置的TTL值，就成为死信（dead letter）

**Dead Letter Exchanges（DLX）**

RabbitMQ的Queue可以配置x-dead-letter-exchange 和x-dead-letter-routing-
key（可选）两个参数，如果队列内出现了dead letter，则按照这两个参数重新路由转发到指定的队列。

  * x-dead-letter-exchange：出现死信（dead letter）之后将dead letter重新发送到指定exchange 
  * x-dead-letter-routing-key：出现死信（dead letter）之后将dead letter重新按照指定的routing-key发送 

队列中出现死信（dead letter）的情况有：

  * 消息或者队列的TTL过期。（延迟队列利用的特性） 
  * 队列达到最大长度 
  * 消息被消费端拒绝（basic.reject or basic.nack）并且requeue=false 

综合上面两个特性，将队列设置TTL规则，队列TTL过期后消息会变成死信，然后利用DLX特性将其转发到另外的交换机和队列就可以被重新消费，达到延迟消费效果。

![](https://img.jbzj.com/file_images/article/202011/2020112815104615.png)

延迟队列设计及实现（Python）

从上面描述，延迟队列的实现大致分为两步：

产生死信，有两种方式Per-Message TTL和 Queue TTL，因为我的需求中是所有的消息延迟处理时间相同，所以本实现中采用 Queue
TTL设置队列的TTL，如果需要将队列中的消息设置不同的延迟处理时间，则设置Per-Message TTL（ [ 官方文档
](http://www.rabbitmq.com/ttl.html) ）

设置死信的转发规则,Dead Letter Exchanges设置方法（ [ 官方文档
](http://www.rabbitmq.com/dlx.html) ）  

完整代码如下：

```python

    """
    Created on Fri Aug 3 17:00:44 2018
    
    @author: Bge
    """
    import pika,json,logging
    class RabbitMQClient:
      def __init__(self, conn_str='amqp://user:pwd@host:port/%2F'):
        self.exchange_type = "direct"
        self.connection_string = conn_str
        self.connection = pika.BlockingConnection(pika.URLParameters(self.connection_string))
        self.channel = self.connection.channel()
        self._declare_retry_queue() #RetryQueue and RetryExchange
        logging.debug("connection established")
      def close_connection(self):
        self.connection.close()
        logging.debug("connection closed")
      def declare_exchange(self, exchange):
        self.channel.exchange_declare(exchange=exchange,
                       exchange_type=self.exchange_type,
                       durable=True)
      def declare_queue(self, queue):
        self.channel.queue_declare(queue=queue,
                      durable=True,)
      def declare_delay_queue(self, queue,DLX='RetryExchange',TTL=60000):
        """
        创建延迟队列
        :param TTL: ttl的单位是us，ttl=60000 表示 60s
        :param queue:
        :param DLX:死信转发的exchange
        :return:
        """
        arguments={}
        if DLX:
          #设置死信转发的exchange
          arguments[ 'x-dead-letter-exchange']=DLX
        if TTL:
          arguments['x-message-ttl']=TTL
        print(arguments)
        self.channel.queue_declare(queue=queue,
                      durable=True,
                      arguments=arguments)
      def _declare_retry_queue(self):
        """
        创建异常交换器和队列，用于存放没有正常处理的消息。
        :return:
        """
        self.channel.exchange_declare(exchange='RetryExchange',
                       exchange_type='fanout',
                       durable=True)
        self.channel.queue_declare(queue='RetryQueue',
                      durable=True)
        self.channel.queue_bind('RetryQueue', 'RetryExchange','RetryQueue')
      def publish_message(self,routing_key, msg,exchange='',delay=0,TTL=None):
        """
        发送消息到指定的交换器
        :param exchange: RabbitMQ交换器
        :param msg: 消息实体，是一个序列化的JSON字符串
        :return:
        """
        if delay==0:
          self.declare_queue(routing_key)
        else:
          self.declare_delay_queue(routing_key,TTL=TTL)
        if exchange!='':
          self.declare_exchange(exchange)
        self.channel.basic_publish(exchange=exchange,
                      routing_key=routing_key,
                      body=msg,
                      properties=pika.BasicProperties(
                        delivery_mode=2,
                        type=exchange
                      ))
        self.close_connection()
        print("message send out to %s" % exchange)
        logging.debug("message send out to %s" % exchange)
      def start_consume(self,callback,queue='#',delay=1):
        """
        启动消费者，开始消费RabbitMQ中的消息
        :return:
        """
        if delay==1:
          queue='RetryQueue'
        else:
          self.declare_queue(queue)
        self.channel.basic_qos(prefetch_count=1)
        try:
          self.channel.basic_consume( # 消费消息
            callback, # 如果收到消息，就调用callback函数来处理消息
            queue=queue, # 你要从那个队列里收消息
          )
          self.channel.start_consuming()
        except KeyboardInterrupt:
          self.stop_consuming()
      def stop_consuming(self):
        self.channel.stop_consuming()
        self.close_connection()
      def message_handle_successfully(channel, method):
        """
        如果消息处理正常完成，必须调用此方法，
        否则RabbitMQ会认为消息处理不成功，重新将消息放回待执行队列中
        :param channel: 回调函数的channel参数
        :param method: 回调函数的method参数
        :return:
        """
        channel.basic_ack(delivery_tag=method.delivery_tag)
      def message_handle_failed(channel, method):
        """
        如果消息处理失败，应该调用此方法，会自动将消息放入异常队列
        :param channel: 回调函数的channel参数
        :param method: 回调函数的method参数
        :return:
        """
        channel.basic_reject(delivery_tag=method.delivery_tag, requeue=False)
```

发布消息代码如下：

```python

    from MQ.RabbitMQ import RabbitMQClient
    print("start program")
    client = RabbitMQClient()
    msg1 = '{"key":"value"}'
    client.publish_message('test-delay',msg1,delay=1,TTL=10000)
    print("message send out")
```

消费者代码如下：

```python

    from MQ.RabbitMQ import RabbitMQClient
    import json
    print("start program")
    client = RabbitMQClient()
    def callback(ch, method, properties, body):
        msg = body.decode()
        print(msg)
        # 如果处理成功，则调用此消息回复ack，表示消息成功处理完成。
        RabbitMQClient.message_handle_successfully(ch, method)
    queue_name = "RetryQueue"
    client.start_consume(callback,queue_name,delay=0)
```

以上就是本文的全部内容，希望对大家的学习有所帮助，也希望大家多多支持脚本之家。

