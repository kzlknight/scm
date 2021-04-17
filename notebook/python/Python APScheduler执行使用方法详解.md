APScheduler就是定时进行周期性的运行某些程序，在语言程序编写中，一直会遇到些定时服务，有时是根据时间定时，有时在固定的位置上进行定制，还有一些是因为储蓄出现的定时，不管是处于哪一种定时类型，基本上都可以使用APScheduler模块进行协助工作，本文给大家介绍定时模块的使用方法。

APScheduler与第三方模块安装方式一样，使用pip，安装过程如下：

![](https://img.jbzj.com/file_images/article/202012/202012100817192.png)

###  **常见的使用方式**

**1、** **APScheduler支持触发器：**

```python

    DateTrigger
    IntervalTrigger
    CronTrigger
```

**2、** **APScheduler支持的Executor**

```python

    AsyncIOExecutor
    GeventExecutor
    ThreadPoolExecutor
```

**APScheduler** **使用示例：**

```python

    import asyncio
    import datetime
    scheduler.add_job(async_func, trigger, args=["jobstore second, executor = second"],
     id="cron_func_test_2",
     jobstore="second",
     executor="second")
```

大家带入执行代码看下输出结果，小编这篇内容只是举例常规内容，还有更多的比如在执行器任务完成是，使用调度器连接，进行添加，修改等等

知识点扩展：

###  在APScheduler中有四个组件

  1. 触发器(trigger)包含调度逻辑，每一个作业有它自己的触发器，用于决定接下来哪一个作业会运行。除了他们自己初始配置意外，触发器完全是无状态的。简单说就是应该说明一个任务应该在什么时候执行。   

  2. 作业存储(job store)存储被调度的作业，默认的作业存储是简单地把作业保存在内存中，其他的作业存储是将作业保存在数据库中。一个作业的数据将在保存在持久化作业存储时被序列化，并在加载时被反序列化。调度器不能分享同一个作业存储。   

  3. 执行器(executor)处理作业的运行，他们通常通过在作业中提交制定的可调用对象到一个线程或者进城池来进行。当作业完成时，执行器将会通知调度器。   

  4. 调度器(scheduler)任务控制器：通过配置executor、jobstore、trigger，使用线程池(ThreadPoolExecutor默认值20)或进程池(ProcessPoolExecutor 默认值5)并且默认最多3个(max_instances)任务实例同时运行，实现对job的增删改查等调度控制 

你需要选择合适的调度器，这取决于你的应用环境和你使用APScheduler的目的。通常最常用的两个：

BlockingScheduler：当调度器是你应用中唯一要运行的东西时使用。

BackgroundScheduler：当你不运行任何其他框架时使用，并希望调度器在你应用的后台执行。

