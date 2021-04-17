**介绍**  

Fabirc是基于python实现的SSH命令行工具，非常适合应用的自动化部署，或者执行系统管理任务。

python2:pip3 install fabric

python3:pip3 install fabric3

简单的例子：

```python

    root@openstack:~# cat fabfile.py
    def hello():
      print('hello world!')
     
    root@openstack:~# fab hello
    hello world!
```

这个fab简单地导入了fabfile,并执行定义的hello函数。

**命令行启动  
**

fab作为Fabric程序的命令行入口，提供了丰富的参数调用，命令格式如下：

> root@openstack:~# fab --help  
>  Usage: fab [options] <command>[:arg1,arg2=val2,host=foo,hosts='h1;h2',...]
> ...  
>

各参数含义如下：

参数项  |  含义  
---|---  
-l  |  显示可用任务函数名   
-f  |  指定fab入口文件,默认为fabfile.py   
-g  |  指定网关（中转设备），比如堡垒机环境，填写堡垒机IP即可   
-H  |  指定目标主机，多台主机用“，”分隔   
-P  |  以异步并行方式运行多台主机任务，默认为串行运行   
-R  |  指定角色（Role）   
-t  |  设置设备连接超时时间   
-T  |  设置远程主机命令执行超时时间   
-w  |  当命令执行失败，发出告警，而非默认终止任务   
  
**fabfile全局属性设定**  

env对象的作用是定义fabfile的全局设定，各属性说明如下：

属性  |  含义  
---|---  
env.host  |  定义目标主机,以python的列表表示，如env.host=['xx.xx.xx.xx','xx.xx.xx.xx']  
env.exclude_hosts  |  排除指定主机，以python的列表表示  
env.port  |  定义目标主机端口，默认为22  
env.user  |  定义用户名  
env.password  |  定义密码  
env.passwords  |
与password功能一样，区别在于不同主机配置不同密码的应用情景,配置此项的时候需要配置用户、主机、端口等信息，如：env.passwords =
{'root@xx.xx.xx.xx:22': '123', 'root@xx.xx.xx.xx':'234'}  
env.getway  |  定义网关  
env.deploy_release_dir  |  自定义全局变量  
env.roledefs  |  定义角色分组  
  
**常用的API  
**

Fabric支持常用的方法及说明如下：

方法  |  说明  
---|---  
local  |  执行本地命令，如:local('hostname')  
lcd  |  切换本地目录,lcd('/root')  
cd  |  切换远程目录,cd('cd')  
run  |  执行远程命令，如：run('hostname')  
sudo  |  sudo执行远程命令，如：sudo('echo “123456″  |  passwd --stdin root')  
put  |  上传本地文件到远程主机,如：put(src,des)  
get  |  从远程主机下载文件到本地，如：get(des,src)  
prompt  |  获取用户输入信息，如：prompt（‘please enter a new password:'）  
confirm  |  获取提示信息确认，如：confirm('failed.Continue[Y/n]?')  
reboot  |  重启远程主机，reboot()  
@task  |  函数修饰符，标识的函数为fab可调用的  
@runs_once  |  函数修饰符，表示的函数只会执行一次  
  
**从一个实例入手  
**

假设我们需要为一个 web 应用创建 fabfile 。具体的情景如下：这个 web 应用的代码使用 git 托管在一台远程服务器 vcshost
上，我们把它的代码库克隆到了本地 localhost 中。我们希望在我们把修改后的代码 push 回 vcshost
时，自动把新的版本安装到另一台远程服务器 my_server 上。我们将通过自动化本地和远程 git 命令来完成这些工作。

关于 fabfile 文件放置位置的最佳时间是项目的根目录：

```python

    .
    |-- __init__.py
    |-- app.wsgi
    |-- fabfile.py <-- our fabfile!
    |-- manage.py
    `-- my_app
      |-- __init__.py
      |-- models.py
      |-- templates
      |  `-- index.html
      |-- tests.py
      |-- urls.py
      `-- views.py
```

**注解**

在这里我们使用一个 Django 应用为例――不过 Fabric 并s依赖于外部代码，除了它的 SSH 库。

作为起步，我们希望先执行测试准备好部署后，再提交到 VCS（版本控制系统）：

```python

    from fabric.api import local
    def prepare_deploy():
      local("./manage.py test my_app")
      local("git add -p && git commit")
      local("git push")
```

这段代码的输出会是这样：

```python

    $ fab prepare_deploy
    [localhost] run: ./manage.py test my_app
    Creating test database...
    Creating tables
    Creating indexes
    ..........................................
    ----------------------------------------------------------------------
    Ran 42 tests in 9.138s
    
    OK
    Destroying test database...
    
    [localhost] run: git add -p && git commit
    
    <interactive Git add / git commit edit message session>
    
    [localhost] run: git push
    
    <git push session, possibly merging conflicts interactively>
    
    Done.
```

这段代码很简单，导入一个 Fabric API： local ，然后用它执行本地 Shell 命令并与之交互，剩下的 Fabric API
也都类似――它们都只是 Python。

用你的方式来组织  

因为 Fabric “只是 Python”，所以你可以按你喜欢的方式来组织 fabfile 。比如说，把任务分割成多个子任务：

```python

    from fabric.api import local
    def test():
      local("./manage.py test my_app")
    
    def commit():
      local("git add -p && git commit")
    
    def push():
      local("git push")
    
    def prepare_deploy():
      test()
      commit()
      push()
```

这个 prepare_deploy 任务仍可以像之前那样调用，但现在只要你愿意，就可以调用更细粒度的子任务。

**故障  
**

我们的基本案例已经可以正常工作了，但如果测试失败了会怎样？我们应该抓住机会即使停下任务，并在部署之前修复这些失败的测试。

Fabric 会检查被调用程序的返回值，如果这些程序没有干净地退出，Fabric 会终止操作。下面我们就来看看如果一个测试用例遇到错误时会发生什么：

```python

    $ fab prepare_deploy
    [localhost] run: ./manage.py test my_app
    Creating test database...
    Creating tables
    Creating indexes
    .............E............................
    ======================================================================
    ERROR: testSomething (my_project.my_app.tests.MainTests)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
    [...]
    
    ----------------------------------------------------------------------
    Ran 42 tests in 9.138s
    
    FAILED (errors=1)
    Destroying test database...
    
    Fatal error: local() encountered an error (return code 2) while executing './manage.py test my_app'
    
    Aborting.
```

太好了！我们什么都不用做，Fabric 检测到了错误并终止，不会继续执行 commit 任务。

参见

[ Failure handling (usage documentation) ](https://fabric-
chs.readthedocs.io/zh_CN/chs/usage/execution.html#failures)

故障处理  
但如果我们想更加灵活，给用户另一个选择，该怎么办？一个名为 [ warn_only ](https://fabric-
chs.readthedocs.io/zh_CN/chs/usage/env.html#warn-only) 的设置（或着说 环境变量 ，通常缩写为 env
var ）可以把退出换为警告，以提供更灵活的错误处理。

让我们把这个设置丢到 test 函数中，然后注意这个 local 调用的结果：

```python

    from __future__ import with_statement
    from fabric.api import local, settings, abort
    from fabric.contrib.console import confirm
    
    def test():
      with settings(warn_only=True):
        result = local('./manage.py test my_app', capture=True)
      if result.failed and not confirm("Tests failed. Continue anyway?"):
        abort("Aborting at user request.")
    
    [...]
```

为了引入这个新特性，我们需要添加一些新东西：

在 Python 2.5 中，需要从 __future__ 中导入 with ；

Fabric contrib.console 子模块提供了 confirm 函数，用于简单的 yes/no 提示。

settings 上下文管理器提供了特定代码块特殊设置的功能。

local 这样运行命令的操作会返回一个包含执行结果（ .failed 或 .return_code 属性）的对象。

abort 函数用于手动停止任务的执行。

即使增加了上述复杂度，整个处理过程仍然很容易理解，而且它已经远比之前灵活。

**建立连接**  

让我们回到 fabfile 的主旨：定义一个 deploy 任务，让它在一台或多台远程服务器上运行，并保证代码是最新的：

> def deploy():  
>  code_dir = '/srv/django/myproject'  
>  with cd(code_dir):  
>  run("git pull")  
>  run("touch app.wsgi")  
>

这里再次引入了一些新的概念：

Fabric 是 Python――所以我们可以自由地使用变量、字符串等常规的 Python 代码；

cd 函数是一个简易的前缀命令，相当于运行 cd /to/some/directory ，和 lcd 函数类似，只不过后者是在本地执行。

~fabric.operations.run` 和 local 类似，不过是在 远程 而非本地执行。

我们还需要保证在文件顶部导入了这些新函数：

> from __future__ import with_statement  
>  from fabric.api import local, settings, abort, run, cd  
>  from fabric.contrib.console import confirm  
>

改好之后，我们重新部署：

> $ fab deploy  
>  No hosts found. Please specify (single) host string for connection:
> my_server  
>  [my_server] run: git pull  
>  [my_server] out: Already up-to-date.  
>  [my_server] out:  
>  [my_server] run: touch app.wsgi
>
> Done.  
>

我们并没有在 fabfile 中指定任何连接信息，所以 Fabric 依旧不知道该在哪里运行这些远程命令。遇到这种情况时，Fabric
会在运行时提示我们。连接的定义使用 SSH 风格的“主机串”（例如： user@host:port
），默认使用你的本地用户名――所以在这个例子中，我们只需要指定主机名 my_server 。

**与远程交互**  

如果你已经得到了代码，说明 git pull 执行非常顺利――但如果这是第一次部署呢？最好也能应付这样的情况，这时应该使用 git clone
来初始化代码库：

```python

    def deploy():
      code_dir = '/srv/django/myproject'
      with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
          run("git clone user@vcshost:/path/to/repo/.git %s" % code_dir)
      with cd(code_dir):
        run("git pull")
        run("touch app.wsgi")
```

和上面调用 local 一样， run 也提供基于 Shell 命令构建干净的 Python 逻辑。这里最有趣的部分是 git clone ：因为我们是用
git 的 SSH 方法来访问 git 服务器上的代码库，这意味着我们远程执行的 run 需要自己提供身份验证。

旧版本的 Fabric（和其他类似的高层次 SSH
库）像在监狱里一样运行远程命令，无法提供本地交互。当你迫切需要输入密码或者与远程程序交互时，这就很成问题。

Fabric 1.0 和后续的版本突破了这个限制，并保证你和另一端的会话交互。让我们看看当我们在一台没有 git checkout 的新服务器上运行更新后的
deploy 任务时会发生什么：

> $ fab deploy  
>  No hosts found. Please specify (single) host string for connection:
> my_server  
>  [my_server] run: test -d /srv/django/myproject
>
> Warning: run() encountered an error (return code 1) while executing 'test -d
> /srv/django/myproject'
>
> [my_server] run: git clone user@vcshost:/path/to/repo/.git
> /srv/django/myproject  
>  [my_server] out: Cloning into /srv/django/myproject...  
>  [my_server] out: Password: <enter password>  
>  [my_server] out: remote: Counting objects: 6698, done.  
>  [my_server] out: remote: Compressing objects: 100% (2237/2237), done.  
>  [my_server] out: remote: Total 6698 (delta 4633), reused 6414 (delta 4412)  
>  [my_server] out: Receiving objects: 100% (6698/6698), 1.28 MiB, done.  
>  [my_server] out: Resolving deltas: 100% (4633/4633), done.  
>  [my_server] out:  
>  [my_server] run: git pull  
>  [my_server] out: Already up-to-date.  
>  [my_server] out:  
>  [my_server] run: touch app.wsgi
>
> Done.  
>

注意那个 Password: 提示――那就是我们在 web 服务器上的远程 git 应用在请求 git
密码。我们可以在本地输入密码，然后像往常一样继续克隆。

参见

[ 与远程程序集成 ](https://fabric-
chs.readthedocs.io/zh_CN/chs/usage/interactivity.html)

**预定义连接  
**

在运行输入连接信息已经是非常古老的做法了，Fabric 提供了一套在 fabfile
或命令行中指定服务器信息的简单方法。这里我们不展开说明，但是会展示最常用的方法：设置全局主机列表 env.hosts 。

env 是一个全局的类字典对象，是 Fabric 很多设置的基础，也能在 with 表达式中使用（事实上，前面见过的
~fabric.context_managers.settings 就是它的一个简单封装）。因此，我们可以在模块层次上，在 fabfile
的顶部附近修改它，就像这样：

```python

    from __future__ import with_statement
    from fabric.api import *
    from fabric.contrib.console import confirm
    env.hosts = ['my_server']
    def test():
      do_test_stuff()
```

当 fab 加载 fabfile 时，将会执行我们对 env 的修改并保存设置的变化。最终结果如上所示：我们的 deploy 任务将在 my_server
上运行。

这就是如何指定 Fabric 一次性控制多台远程服务器的方法： env.hosts 是一个列表， fab 对它迭代，对每个连接运行指定的任务。

**总结**  

虽然经历了很多，我们的 fabfile 文件仍然相当短。下面是它的完整内容：

```python

    from __future__ import with_statement
    from fabric.api import *
    from fabric.contrib.console import confirm
    
    env.hosts = ['my_server']
    
    def test():
      with settings(warn_only=True):
        result = local('./manage.py test my_app', capture=True)
      if result.failed and not confirm("Tests failed. Continue anyway?"):
        abort("Aborting at user request.")
    
    def commit():
      local("git add -p && git commit")
    
    def push():
      local("git push")
    
    def prepare_deploy():
      test()
      commit()
      push()
    
    def deploy():
      code_dir = '/srv/django/myproject'
      with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
          run("git clone user@vcshost:/path/to/repo/.git %s" % code_dir)
      with cd(code_dir):
        run("git pull")
        run("touch app.wsgi")
```

但它已经涉及到了 Fabric 中的很多功能：

定义 fabfile 任务，并用 fab 执行；

用 local 调用本地 shell 命令；

通过 settings 修改 env 变量；

处理失败命令、提示用户、手动取消任务；

以及定义主机列表、使用 run 来执行远程命令。

还有更多这里没有涉及到的内容，你还可以看看所有“参见”中的链接，以及 索引页 的内容表。

更多请参考： [ https://fabric-chs.readthedocs.io/zh_CN/chs/tutorial.html
](https://fabric-chs.readthedocs.io/zh_CN/chs/tutorial.html)

**常用示例**

1、上传文件

fabric可以将本地文件上传到远程服务器上，这个操作要用到put函数

2、示例代码

```python

    #coding=utf-8
    from fabric.api import *
    from fabric.contrib.console import confirm
    import hashlib
    
    
    host = 'root@192.168.0.62:22'
    password = '123456'
    env.hosts=[host]
    env.password = password
    
    
    def md5sum(filename):
      fd = open(filename,"r")
      fcont = fd.read()
      fd.close()
      fmd5 = hashlib.md5(fcont)
      return fmd5
    
    def upload_file(filename):
      run("mkdir -p /root/upload")
      with cd('/root/upload'):
        with settings(warn_only=True):
          res = put(filename,filename)
        if res.failed and not confirm("put file failed, Continue[Y/N]?"):
          abort(u'终止上传文件')
    
    
    def checkmd5(filename):
      fmd5 = md5sum(filename)
      lmd5 = fmd5.hexdigest()
    
      target = '/root/upload/'+filename
      rmd5=run("md5sum " + target).split(' ')[0]
    
      if lmd5 == rmd5:
        print 'ok,the file uploaded'
      else:
        print 'error'
    def uploadfile(filename):
      upload_file(filename)
      checkmd5(filename)
```

执行命令 fab -f uploadfile.py uploadfile:filename=fabricdemo1.py

3、程序分析

在执行fab命令时，可以指定函数的参数,多个参数之间用逗号分隔  

with settings(warn_only=True) 的作用，是在发生错误时，不中断执行，只会输出警告信息  

4、上传文件夹

其实fabric也是可以上传文件夹的，但是很多教程里都没有提及，示例代码如下

```python

    def uploadfolder():
      run("mkdir -p /root/upload")
      with cd('/root/upload'):
        with settings(warn_only=True):
          res = put('testfolder','.')
```

在uploadfile.py
同目录下，有一个testfolder的文件夹，上面的代码可以将这个文件夹上传到/root/upload目录下，主要注意的是put的第二个参数，我这里放的是'.'，就表明要把本地的testfolder放到/root/upload目录下。

不同于上传文件，文件夹上上传过程中是不能设置目标文件夹的名字的，目标文件夹必须先存在

以上就是本文的全部内容，希望对大家的学习有所帮助，也希望大家多多支持脚本之家。

