每个公司在运维平台化过程中，如果以开始没有规划，免不了全面开花，会做成好多个平台，然后每个平台都有自己的认证体系，等平台多了，记录这些账号就变得非常烦人，如果用不同的密码，对人的记忆力是个挑战，所以基于此，大部分公司会有部署Ldap系统，来统一运维系统的账号管理，像我们常用的jenkins也可以做对接到ldap上，这样所有的系统就可以统一用ldap来认证，然后根据不同的人来设置不同的权限，那django怎么使用ldap来做后端验证呢，操作接入非常简单，整个过程可以几乎不改我们之前的代码任何逻辑。

我们先进行第一步，安装依赖，ldap和django-auth-ldap，django-auth-ldap这个安装没有任何问题，
我们不多说了，直接pip即可，但ldap这玩意儿在Linux系统上安装没啥问题，但如果你是windows系统，安装准报错，而且报的错能让你崩溃，你要是顺着报错的信息去搜去解决问题，会浪费大量的时间，但你又不能不安装，不然你本地怎么调试？（mac的忽略），不能每次改完代码提交到服务器上验证吧？不过大家别担心，我已把路给大家趟平了，按以下步骤去安装就绝对没问题，首先访问：

[ https://www.lfd.uci.edu/~gohlke/pythonlibs/#python-ldap
](https://www.lfd.uci.edu/~gohlke/pythonlibs/#python-ldap)

然后根据自己的版本需求下载对应的文件，以下是我下载的：

![](https://img.jbzj.com/file_images/article/202012/202012790011764.jpg?20201179030)

如果你用的虚拟环境，需要进入到你虚拟环境目录然后进行安装，进入windows虚拟环境下，执行: active.bat，进入虚拟环境：然后运行：

![](https://img.jbzj.com/file_images/article/202012/202012790047232.jpg?2020117912)

等安装完，就能正常使用了，下面我们来编辑settings.py文件，加入内容：

首先导入需要的模块：

```python

    import ldap
    from django_auth_ldap.config import LDAPSearch,GroupOfNamesType
    
```

指定后端验证为ldap:

```python

    AUTHENTICATION_BACKENDS = [
      'django_auth_ldap.backend.LDAPBackend',
      'django.contrib.auth.backends.ModelBackend',
    ]
    
```

然后设置ldap的ip地址连接配置：

```python

    # LDAP Setting
    AUTH_LDAP_SERVER_URI = "ldap://10.1.1.1:389"
    AUTH_LDAP_BIND_DN = "cn=admin,dc=xxx,dc=xxx,dc=xx"
    AUTH_LDAP_BIND_PASSWORD = "mypassword"
     
    AUTH_LDAP_USER_SEARCH = LDAPSearch(
    'ou=users,dc=xxx,dc=xxx,dc=xx',
    ldap.SCOPE_SUBTREE,
    '(uid=%(user)s)',
    )
     
    # 跟django中的auth_user对应
    AUTH_LDAP_USER_ATTR_MAP = {
      "first_name": "uid",
      "last_name": "sn",
      "email": "mail"
    }
    
```

完毕运行工程，这时候登录就是Ldap方式了，相对还是比较简单

到此这篇关于用ldap作为django后端用户登录验证的实现的文章就介绍到这了,更多相关django
登录验证内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

