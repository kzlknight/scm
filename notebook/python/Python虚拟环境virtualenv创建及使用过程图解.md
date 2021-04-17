virtualenv 是用来创建一个虚拟的python环境的第三方包，一个专属于项目的python环境。

安装virtualenv（请确保python和pip成功安装）：

pip3 install virtualenv

![](https://img.jbzj.com/file_images/article/202012/202012080838561.png)

创建python虚拟环境：

> virtualenv [虚拟环境名称] # 会在当前目录下生成一个对应的文件夹  
>  virtualenv -p /usr/bin/python [虚拟环境名称] # 指定python解释器版本  
>

![](https://img.jbzj.com/file_images/article/202012/202012080838572.png)

进入python虚拟环境：

> Linux系统：  
>  cd my-env/  
>  source ./bin/activate

![](https://img.jbzj.com/file_images/article/202012/202012080838573.png)

> Windows系统：  
>  cd my-env\Scripts  
>  activate

![](https://img.jbzj.com/file_images/article/202012/202012080838574.png)

python虚拟环境下安装第三方包：

![](https://img.jbzj.com/file_images/article/202012/202012080838585.png)

退出python虚拟环境：

deactivate

![](https://img.jbzj.com/file_images/article/202012/202012080838586.png)

virtualenvwrapper：

virtualenvwrapper 是虚拟环境统一管理工具，可以使虚拟环境管理起来更加简单方便，不用像 virtualenv
那样需要先进入到指定目录下再通过activate命令激活虚拟环境。

安装virtualenvwrapper（同时会安装virtualenv）：

> Linux系统：  
>  pip3 install virtualenvwrapper
>
> Windows系统：  
>  pip3 install virtualenvwrapper-win

![](https://img.jbzj.com/file_images/article/202012/202012080838587.png)

设置环境变量（只展示Linux系统的设置）：

> cat >> .bash_profile << eof  
>  export WORKON_HOME=/data/Envs # 设置 virtualenv 的统一管理目录  
>  export VIRTUALENVWRAPPER_PYTHON=/usr/local/python3.7/bin/python3 # 指定
> python 解释器  
>  eof
>
> source /usr/local/python3.7/bin/virtualenvwrapper.sh # 执行 virtualenvwrapper
> 安装脚本
>
> source .bash_profile # 使配置生效

![](https://img.jbzj.com/file_images/article/202012/202012080838588.png)

virtualenvwrapper 基本使用：

1、创建虚拟环境：

> mkvirtualenv my_env # 创建一个 my_env 虚拟环境，并切换到当前虚拟环境  
>  mkvirtualenv --python==/usr/bin/python you_env # 创建一个指定 python 解析器的 you_env
> 虚拟环境，并切换到当前虚拟环境  
>

![](https://img.jbzj.com/file_images/article/202012/202012080838599.png)

2、进入和切换虚拟环境：

> [root@localhost ~]# workon my_env # 进入 my_env 虚拟环境  
>  (my_env) [root@localhost ~]# workon you_env # 从 my_env 虚拟环境切换到 you_env 虚拟环境  
>

![](https://img.jbzj.com/file_images/article/202012/2020120808385910.png)

3、进入当前激活的虚拟环境的目录中：

cdvirtualenv

![](https://img.jbzj.com/file_images/article/202012/2020120808385911.png)

4、退出当前虚拟环境：

deactivate

![](https://img.jbzj.com/file_images/article/202012/2020120808385912.png)

5、列出当前所有的虚拟环境：

lsvirtualenv

![](https://img.jbzj.com/file_images/article/202012/2020120808390013.png)

6、删除一个虚拟环境：

rmvirtualenv you_env

![](https://img.jbzj.com/file_images/article/202012/2020120808390014.png)

以上就是本文的全部内容，希望对大家的学习有所帮助，也希望大家多多支持脚本之家。

