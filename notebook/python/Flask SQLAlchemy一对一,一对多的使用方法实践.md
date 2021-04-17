Flask-SQLAlchemy安装和建表操作请 [ 参考这里 ](https://www.jb51.net/article/34000.htm) 。  
  

_复制代码_ 代码如下:

  
# Role表  
class Role(db.Model):  
id=db.Column(db.Integer,primary_key=True)  
name=db.Column(db.String(80))  
  
# RoleType表  
class Role_type(db.Model):  
query_class=Common_list_name_Query  
id=db.Column(db.Integer,primary_key=True)  
name=db.Column(db.String(120))  

一对一  
只需要在属性里改变下定义

_复制代码_ 代码如下:

  
# Role表  
class Role(db.Model):  
role_type_id=db.Column(db.Integer,db.ForeignKey('role_type.id'))  
  
role=db.relationship('Role',backref='role_type',lazy='dynamic', uselist=False)  

一对多

_复制代码_ 代码如下:

  
# 一对多需要在两个表内斗填上相互的关系  
class Role(db.Model):  
role_type_id=db.Column(db.Integer,db.ForeignKey('role_type.id'))  
  
class Role_type(db.Model):  
roles=db.relationship('Role',backref='role_type',lazy='dynamic')  

具体参数可以参考如下的文档：  
[ http://flask.pocoo.org/docs/patterns/sqlalchemy/
](http://flask.pocoo.org/docs/patterns/sqlalchemy/)  
[ http://packages.python.org/Flask-SQLAlchemy/
](http://packages.python.org/Flask-SQLAlchemy/)

