**日志相关概念**  

日志是一种可以追踪某些软件运行时所发生事件的方法。软件开发人员可以向他们的代码中调用日志记录相关的方法来表明发生了某些事情。一个事件可以用一个可包含可选变量数据的消息来描述。此外，事件也有重要性的概念，这个重要性也可以被称为严重性级别（level）。

**日志的作用**

通过log的分析，可以方便用户了解系统或软件、应用的运行情况；如果你的应用log足够丰富，也可以分析以往用户的操作行为、类型喜好、地域分布或其他更多信息；如果一个应用的log同时也分了多个级别，那么可以很轻易地分析得到该应用的健康状况，及时发现问题并快速定位、解决问题，补救损失。  

简单来讲就是，我们通过记录和分析日志可以了解一个系统或软件程序运行情况是否正常，也可以在应用程序出现故障时快速定位问题。比如，做运维的同学，在接收到报警或各种问题反馈后，进行问题排查时通常都会先去看各种日志，大部分问题都可以在日志中找到答案。再比如，做开发的同学，可以通过IDE控制台上输出的各种日志进行程序调试。对于运维老司机或者有经验的开发人员，可以快速的通过日志定位到问题的根源。可见，日志的重要性不可小觑。日志的作用可以简单总结为以下3点：

  * 程序调试 
  * 了解软件程序运行情况，是否正常 
  * 软件程序运行故障分析与问题定位   

如果应用的日志信息足够详细和丰富，还可以用来做用户行为分析，如：分析用户的操作行为、类型洗好、地域分布以及其它更多的信息，由此可以实现改进业务、提高商业利益。

**发现问题**

最近在用Python的logging模块记录日志时，遇到了重复记录日志的问题，第一条记录写一次，第二条记录写两次，第三条记录写三次。。。很头疼，这样记日志可不行。网上搜索到了原因与解决方案：

原因：没有移除handler  

解决：在日志记录完之后removeHandler

修改前示例代码：

```python

    import logging
    
    def log(message):
     logger = logging.getLogger('testlog')
    
     streamhandler = logging.StreamHandler()
     streamhandler.setLevel(logging.ERROR)
     formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
     streamhandler.setFormatter(formatter)
    
     logger.addHandler(streamhandler)
     logger.error(message)
    
    if __name__ == '__main__':
     log('hi')
     log('hi too')
     log('hi three')
```

修改前输出结果：

> 2016-07-08 09:17:29,740 - ERROR - testlog - hi  
>  2016-07-08 09:17:29,740 - ERROR - testlog - hi too  
>  2016-07-08 09:17:29,740 - ERROR - testlog - hi too  
>  2016-07-08 09:17:29,740 - ERROR - testlog - hi three  
>  2016-07-08 09:17:29,740 - ERROR - testlog - hi three  
>  2016-07-08 09:17:29,740 - ERROR - testlog - hi three  
>

修改后示例代码：

```python

    import logging
    
    def log(message):
     logger = logging.getLogger('testlog')
    
     streamhandler = logging.StreamHandler()
     streamhandler.setLevel(logging.ERROR)
     formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
     streamhandler.setFormatter(formatter)
    
     logger.addHandler(streamhandler)
     logger.error(message)
    
     # 添加下面一句，在记录日志之后移除句柄
     logger.removeHandler(streamhandler)
    
    if __name__ == '__main__':
     log('hi')
     log('hi too')
     log('hi three')
```

修改后输出结果：

> 2016-07-08 09:32:28,206 - ERROR - testlog - hi  
>  2016-07-08 09:32:28,206 - ERROR - testlog - hi too  
>  2016-07-08 09:32:28,206 - ERROR - testlog - hi three  
>

**深度解析：**

Google之后，大概搞明白了，就是你第二次调用log的时候，根据getLogger(name)里的name获取同一个logger，而这个logger里已经有了第一次你添加的handler，第二次调用又添加了一个handler，所以，这个logger里有了两个同样的handler，以此类推，调用几次就会有几个handler。。

所以这里有以下几个解决办法：

  * 每次创建不同name的logger，每次都是新logger，不会有添加多个handler的问题。（ps:这个办法太笨，不过我之前就是这么干的。。） 
  * 像上面一样每次记录完日志之后，调用removeHandler()把这个logger里的handler移除掉。 
  * 在log方法里做判断，如果这个logger已有handler，则不再添加handler。 
  * 与方法2一样，不过把用pop把logger的handler列表中的handler移除。 

下面是方法3与方法4的代码示例：

方法3：

```python

    import logging
    
    def log(message):
     logger = logging.getLogger('testlog')
    
     # 这里进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志
     if not logger.handlers:
     streamhandler = logging.StreamHandler()
     streamhandler.setLevel(logging.ERROR)
     formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
     streamhandler.setFormatter(formatter)
     logger.addHandler(streamhandler)
    
     logger.error(message)
    
    if __name__ == '__main__':
     log('hi')
     log('hi too')
     log('hi three')
```

方法4：

```python

    import logging
    
    def log(message):
     logger = logging.getLogger('testlog')
    
     streamhandler = logging.StreamHandler()
     streamhandler.setLevel(logging.ERROR)
     formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
     streamhandler.setFormatter(formatter)
    
     logger.addHandler(streamhandler)
    
     logger.error(message)
    
     # 用pop方法把logger.handlers列表中的handler移除，注意如果你add了多个handler，这里需多次pop，或者可以直接为handlers列表赋空值
     logger.handlers.pop()
     # logger.handler = []
    
    if __name__ == '__main__':
     log('hi')
     log('hi too')
     log('hi three')
```

这几种方法都亲试可行，个人觉得方法3判断更加优雅，你觉得呢？

**总结**

以上就是这篇文章的全部内容了，希望本文的内容对大家的学习或者工作具有一定的参考学习价值，如果有疑问大家可以留言交流，谢谢大家对脚本之家的支持。

