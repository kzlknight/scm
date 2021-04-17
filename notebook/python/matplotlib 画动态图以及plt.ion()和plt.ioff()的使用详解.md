学习python的道路是漫长的，今天又遇到一个问题，所以想写下来自己的理解方便以后查看。

在使用matplotlib的过程中，常常会需要画很多图，但是好像并不能同时展示许多图。这是因为python可视化库matplotlib的显示模式默认为阻塞（block）模式。什么是阻塞模式那？我的理解就是在plt.show()之后，程序会暂停到那儿，并不会继续执行下去。如果需要继续执行程序，就要关闭图片。那如何展示动态图或多个窗口呢？这就要使用plt.ion()这个函数，使matplotlib的显示模式转换为交互（interactive）模式。即使在脚本中遇到plt.show()，代码还是会继续执行。下面这段代码是展示两个不同的窗口：

```python

      import matplotlib.pyplot as plt
      plt.ion()  # 打开交互模式
      # 同时打开两个窗口显示图片
      plt.figure() #图片一
      plt.imshow(i1)
      plt.figure()  #图片二
      plt.imshow(i2)
      # 显示前关掉交互模式
      plt.ioff()
      plt.show()
    
```

在plt.show()之前一定不要忘了加plt.ioff()，如果不加，界面会一闪而过，并不会停留。那么动态图像是如何画出来的，请看下面这段代码，具体的解释就不在这里阐述了，以后有时间再更新：

```python

    import tensorflow as tf
    import numpy as np
    import matplotlib.pyplot as plt
     
    def add_layer(inputs,in_size,out_size,activation_funiction=None):
     
      Weights = tf.Variable(tf.random_normal([in_size,out_size]))
      biases = tf.Variable(tf.zeros([1,out_size]) +0.1)
      Wx_plus_b = tf.matmul(inputs,Weights)+biases
      if activation_funiction is None:
        outputs = Wx_plus_b
      else:
        outputs = activation_funiction(Wx_plus_b)
      return outputs
     
    x_data = np.linspace(-1,1,300)[:,np.newaxis]
    noise = np.random.normal(0,0.05,x_data.shape)
    y_data = np.square(x_data)-0.5 +noise
     
    xs = tf.placeholder(tf.float32,[None,1])  
    ys = tf.placeholder(tf.float32,[None,1])
     
    #add hidden layer
    l1 = add_layer(xs,1,10,activation_funiction=tf.nn.relu)
    #add output layer
    prediction = add_layer(l1,10,1,activation_funiction=None)
     
    #the error between prediction and real data
    loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),reduction_indices=[1]))
    train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
     
    init =tf.initialize_all_variables()
     
    with tf.Session() as sess:
      sess.run(init)
     
      fig = plt.figure()
      ax = fig.add_subplot(1,1,1)
      ax.scatter(x_data,y_data)
      plt.ion()  #将画图模式改为交互模式
     
      for i in range(1000):
        sess.run(train_step,feed_dict={xs:x_data,ys:y_data})
        if i%50 ==0:
          plt.pause(0.1)
          try:
            ax.lines.remove(lines[0])
          except Exception:
            pass
          prediction_value = sess.run(prediction,feed_dict={xs:x_data})
          lines = ax.plot(x_data,prediction_value,'r-',lw=5)
     
     
          print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))
     
      plt.ioff()
      plt.show()
    
```

上面这段代码执行之后就会看到一条曲线在动态的拟合数据，直到训练结束。

下面就来讲讲matplotlib这两种模式具体的区别

在交互模式下：

1、plt.plot(x)或plt.imshow(x)是直接出图像，不需要plt.show()

2、如果在脚本中使用ion()命令开启了交互模式，没有使用ioff()关闭的话，则图像会一闪而过，并不会常留。要想防止这种情况，需要在plt.show()之前加上ioff()命令。

在阻塞模式下：

1、打开一个窗口以后必须关掉才能打开下一个新的窗口。这种情况下，默认是不能像Matlab一样同时开很多窗口进行对比的。

2、plt.plot(x)或plt.imshow(x)是直接出图像，需要plt.show()后才能显示图像

到此这篇关于matplotlib 画动态图以及plt.ion()和plt.ioff()的使用详解的文章就介绍到这了,更多相关matplotlib
plt.ion() plt.ioff()内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

