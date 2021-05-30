#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scm.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
    content = """
    # 1 配置YUM源
## 1.1 下载MySQL官网的Yum源rpm安装包
```cmd
wget http://dev.mysql.com/get/mysql57-community-release-el7-10.noarch.rpm
```
## 1.2 安装MySQL的Yum源
```cmd
yum localinstall mysql57-community-release-el7-10.noarch.rpm
```

## 1.3 检查是否安装成功
```cmd
yum repolist enabled | grep "mysql.*-community.*"
```

# 2 安装MySQL
```cmd
yum install mysql-community-server
```

# 3 启动MySQL服务
```cmd
systemctl start mysqld
```
注：
- 重启MySQL:systemctl restart mysqld

# 4 设置开机启动MySQL
```cmd
systemctl enable mysqld
systemctl daemon-reload
```

# 5 登录MySQL
## 5.1 找到MySQL的默认密码
```cmd
cat /var/log/mysqld.log
```
查找root@localhost:
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200122195840568.png)
蓝色的地方为密码
## 5.2 登录MySQL
```cmd
mysql -uroot -p
>输入刚才找到的默认密码
```

# 6 重置MySQL的密码
```cmd
set password for 'root'@'localhost'=password('【密码】'); 
```
注：
- 初始密码有安全级别，太简单的不行

# 7 配置远程登录访问
## 7.1 修改配置文件
```cmd
vi /etc/my.cnf
```
看里面有没有bind-address=127.0.0.1，如果有这个配置的话，是只允许本地访问，所以把这行注释掉

## 7.2 配置远程用户权限
登录MySQL
```cmd
grant all on *.* to root@"%" identified by "kzlKNIGHT_123";
```
命令说明：

- all 表示所有的权限，例如可以仅仅设置查的权限：select
- *.* 第一个*表示任意数据库，第二个*表示任意表
- to 后面的为哪个用户设置权限
- @后写可以连接的IP地址，%表示任何IP
- identified by “密码”

## 7.3 重启服务
```cmd
systemctl restart mysqld
```

# 8 阿里云配置
## 8.1 配置白名单
注：
- 这一项应该在连接云ECS中端之前就配置好，否则连接不上终端
- 白名单的意思就是允许某些IP访问连接某个ECS服务器，不属于白名单的IP地址即使知道账号密码也不能登录

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200122200858593.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2t6bF9rbmlnaHQ=,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020012220115826.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2t6bF9rbmlnaHQ=,size_16,color_FFFFFF,t_70)
![](https://img-blog.csdnimg.cn/20200122201351851.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2t6bF9rbmlnaHQ=,size_16,color_FFFFFF,t_70)
## 8.2 配置MySQL端口访问
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200122201556946.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2t6bF9rbmlnaHQ=,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200122201814402.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2t6bF9rbmlnaHQ=,size_16,color_FFFFFF,t_70)
![](https://img-blog.csdnimg.cn/20200122201900566.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2t6bF9rbmlnaHQ=,size_16,color_FFFFFF,t_70)
## 8.3 重启服务器
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200122202453147.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2t6bF9rbmlnaHQ=,size_16,color_FFFFFF,t_70)
## 8.4 用PyCharm连接阿里云ECS的MySQL
![](https://img-blog.csdnimg.cn/20200122202038918.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200122202240527.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2t6bF9rbmlnaHQ=,size_16,color_FFFFFF,t_70)

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200122202330843.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2t6bF9rbmlnaHQ=,size_16,color_FFFFFF,t_70)
    """

    from appArticle.models import InsideArticle

    for article in InsideArticle.objects.all():
        article.content = content
        article.save()
