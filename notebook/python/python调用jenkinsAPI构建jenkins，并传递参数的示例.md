**安装jenkins**  
安装jenkins很简单，可以用多种方式安装，这里知道的有：

  * 在官网下载rpm包，手动安装，最费事 
  * centos系统通过yum安装，ubuntu通过apt-get安装(不推荐，因为很多东西都使用了默认的) 
  * 直接下载官网上的war包 

我这里直接用的下载war包

**遇到的坑**  
在安装之前，公司的服务器上已经有一个版本的jekins在运行了，所有参数都已经被设置过了，所以，重新安装的版本，虽然文件夹，用户都和以前的版本不一样，但是每次jenkins页面都是直接跳转上个版本的，并不会进入首次激活jenkins的界面

原因是：公司的服务器上配置了JENKINS_HOME，但是jenkins在启动的时候，会首先获取JENKINS_HOME,并读取文件夹内的配置信息。

解决办法：这里取了个巧，在每次启动jenkins的时候，手动指定JENKINS_HOME=/data/jenkins2,这样就不会读取上个版本的信息了

**通过pythonAPI实现参数化jenkins构建**  
这里要实现的场景是，通过前端的页面，选择相应的下拉框，传递参数到后台jenkins，然后jenkins获取相应的参数，计算以这些参数为条件的数据。

**创建jenkins项目**  
这里创建的项目需要添加param

![](https://img.jbzj.com/file_images/article/202012/202012995612616.png?202011995619)

需要几个参数，就添加几个参数

**安装python-jenkins**

```python

    sudo pip install python-jenkins
```

直接上代码：

```python

    import jenkins
    server = jenkins.Jenkins('http://192.168.59.149:28080', username='jenkins', password='jenkins@!23')
    server.build_job('jxInstantQuery')
    server.build_job('jxInstantQuery2', {'param1': 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'param2': 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'})
```

里面的执行shell：

![](https://img.jbzj.com/file_images/article/202012/202012995714554.png?202011995722)

最终的效果：

![](https://img.jbzj.com/file_images/article/202012/202012995740080.png?202011995749)

以上就是python调用jenkinsAPI构建jenkins，并传递参数的示例的详细内容，更多关于python调用jenkinsAPI的资料请关注脚本之家其它相关文章！

