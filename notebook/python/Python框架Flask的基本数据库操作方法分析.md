本文实例讲述了Python框架Flask的基本数据库操作方法。分享给大家供大家参考，具体如下：

数据库操作在web开发中扮演着一个很重要的角色，网站中很多重要的信息都需要保存到数据库中。如用户名、密码等等其他信息。Django框架是一个基于MVT思想的框架，也就是说他本身就已经封装了Model类，可以在文件中直接继承过来。但是在Flask中，并没有把Model类封装好，需要使用一个扩展包，Flask-
SQLAlchemy。它是一个对数据库的抽象，让开发者不用这些编写SQL语句，而是使用其提供的接口去操作数据库，这其中涉及到一个非常重要的思想：ORM什么是ORM呢？下面我们就来详细讲解一下。

##  一、ORM

**1. ORM** 的全称是：Object Relationship Map：对象-
关系映射。主要的功能是实现模型对象到关系型数据库数据的映射。说白了就是使用通过对象去操作数据库。

**2. 操作过程图：**

![](https://img.jbzj.com/file_images/article/201807/2018713121936591.png?201861312209)

**3. 优点：**

(1). 不需要编写SQL代码，这样可以把精力放在业务逻辑处理上。

(2). 使用对象的方式去操作数据库。实现数据模型与数据库的解耦，利于开发。

**4. 缺点：**

性能较低。

##  二、Flask-SQLAlchemy的介绍

**1. 设置配置信息**

在开发中，一般是把一些配置信息都写在一个单独的文件中，如settings.py。这样一些安全信息就可以得到保存！

重点字段有：

数据库的指定是使用URL的方式来指定的：'mysql://用户名:密码@服务器地址:端口号/数据库名'，但是连接SQLite是使用这用格式：sqlite:////absolute/path/to/foo.db，使用////开头

SQLALCHEMY_DATABASE_URI = 'myslq://root:meiyou@127.0.0.1:3306/test'  
SQLALCHEMY_POOL_RECYCLE  ：设置多少秒后自动回收连接，对MySQL来说，默认是2小时  
SQLALCHEMY_ECHO  ：设置True的话，查询时会显示原始SQL语句。  
SQLALCHEMY_TRACK_MODIFICATIONS  ：动态追踪修改设置。

**2. 常用的SQLAlchemy字段类型：**

Integer  
String  
Numberic  
Boolean  
Date

**3. 常用的SQLAlchemy列选项**

primary_key  ：如果为True，表示主键。Flask中没有自动生成主键，需要自定义。  
unique  ：为True，设置该列不能有重复值，如用户名、邮箱、手机号  
nullable  ：为True的话可以为null  
default  ：设置默认值  
index  ：为True，设置该列为索引，默认索引是主键。

**4. 关系选项**

backref  ：在关系的另一模型中添加的反向引用，查询时起很大作用。  
secondary  ：用于多对多关系中表的名字  
primary join  ：

##  三、Flask-SQLAlchemy的基本操作

在Flask-
SQLAlchemy中的增、删、改操作是由数据库会话(db.session)管理的。也就是说，在准备把数据写入数据库前，要先将数据添加(add())到会话中，然后使用commit()提交会话。

在Flask-SQLAlchemy中的查询操作都是通过query对象操作数据库。基本的查询是返回表中的所有数据，还可以使用过滤器进行更精确的数据库查询。

**1. 常用查询过滤器：**

过滤器得到的还只是一些对象，需要使用执行器来获取真正的数据。

` filter() ` ： 把过滤器添加到原查询上，返回一个新查询，需要使用模型类名去获取字段来进行比较。  
` filter_by() ` ：把等值(只能使用=比较操作)过滤器添加到查询上，返回一个新查询。  
` order_by() ` ：根据指定条件对查询结果进行排序，返回一个新查询。  
` group_by() ` ：根据指定条件对原查询结果进行分组，返回一个新查询。

**2. 常用查询执行器**

` all() ` ：以列表的形式返回查询的所有结果  
` first() ` ：返回查询的第一个结果，  
` first_or_404() ` ：同first(), 只不过如果没有找到的话，返回404错误  
` get() ` ：返回指定主键对应的行，  
` get_or_404() ` ：返回指定主键对应的行，如不存在，返回404错误  
` count() ` ：返回查询结果的数量  
` paginate() ` ：返回一个Paginate对象，包含指定范围内的结果。

**3. 查询条件**

` startswith('xx') ` ：查询以xx开头的所有数据  
` endswith('xx') ` ：查询以xx结尾的所有数据  
` not_() ` ：取反  
` and_() ` ：返回and()条件满足的所有数据  
` or_() ` ：返回or()条件满足的所有数据

**示例：**

```python

    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy
    from settings import Config
    app = Flask(__name__)
    app.config.from_object(Config)
    # 创建数据库实例对象
    db = SQLAlchemy(app)
    class Role(db.Model):
      """创建角色模型类"""
      __tablename__ = 'roles'
      id = db.Column(db.Integer, primary_key=True)
      name = db.Column(db.String(64), unique=True)
      # 描述roles表和users表的关系,
      # 第一个参数为多那端的模型类名
      # 第二个参数backref:为模型类名声明新属性,这样就可以实现反向查询
      # 第三个参数决定了什么时候从数据库中查询数据
      us = db.relationship('User', backref='role', lazy='dynamic')
      def __repr__(self):
        return 'Role:%s' % self.name
    class User(db.Model):
      """创建用户模型类"""
      # 设置表名
      __tablename__ = 'users'
      # 添加主键
      id = db.Column(db.Integer, primary_key=True)
      # 用户名
      name = db.Column(db.String(30), unique=True)
      email = db.Column(db.String(64), unique=True)
      password = db.Column(db.String(64))
      # 定义一个外键
      role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
      def __repr__(self):
        return 'User:%s' % self.name
    if __name__ == '__main__':
      # 先删除表
      db.drop_all()
      # 创建表
      db.create_all()
      # 添加数据
      app.run()
```

更多关于Python相关内容感兴趣的读者可查看本站专题：《 [ Python+MySQL数据库程序设计入门教程
](//www.jb51.net/Special/864.htm) 》、《 [ Python常见数据库操作技巧汇总
](//www.jb51.net/Special/681.htm) 》、《 [ Python数据结构与算法教程
](//www.jb51.net/Special/663.htm) 》、《 [ Python函数使用技巧总结
](//www.jb51.net/Special/642.htm) 》、《 [ Python字符串操作技巧汇总
](//www.jb51.net/Special/636.htm) 》、《 [ Python入门与进阶经典教程
](//www.jb51.net/Special/520.htm) 》及《 [ Python文件与目录操作技巧汇总
](//www.jb51.net/Special/516.htm) 》

希望本文所述对大家Python程序设计有所帮助。

