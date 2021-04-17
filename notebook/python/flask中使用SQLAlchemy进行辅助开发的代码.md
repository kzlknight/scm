安装方法

1）、apt-ge安装  

_复制代码_ 代码如下:

  
sudo apt-get install Flask-SQLAlchemy  

2)、下载安装包进行安装  

_复制代码_ 代码如下:

  
# 安装后可直接在py中使用  
import flask  
from flask.ext.sqlalchemy import SQLAlchemy  
  
app = flask.Flask(__name__)  
# - Settings里配置了SqlAlchemy的数据库地址  
# sqlite ex: "sqlite:///dbname.db"  
app.config.from_object("Settings")  
db = SQLAlchemy(app)  
db.init_app(app)  
# - create_all() 调用时将会创建所有继承db.Model的模版  
# Model ex: 见 Class AdminInfo  
db.create_all()  
  
class AdminInfo(db.Model):  
id = db.Column(db.Integer, primary_key = True)  
name = db.Column(db.String(16))  
password = db.Column(db.String(32))  
kidname = db.Column(db.String(16))  
diy_show = db.Column(db.Text)  
  
def __init__(self, name, password, kidname, diy_show):  
self.name = name  
self.password = password  
self.kidname = kidname  
self.diy_show = diy_show  
  
def __repr__(self):  
return "<name: %s pw: %s>"%(self.name, '*'*len(self.password))  

这样就是就可以在render 模版时使用SQLAlchemy了。  

_复制代码_ 代码如下:

  
# 对AdminInfo进行操作  
ai = AdminInfo("gaoyiping", "gaoyiping", u"我叫高一平", u"大家好，我叫高一平，你叫什么？我们交个朋友啊。")  
# 这样就已经实例了一个SQL Data  
# 对db进行插入  
db.session.add(ai)  
# 对db commit  
db.session.commit()  
  
# 如果进行查询  
AdminInfo.query.all()  
# >>> [<name: gaoyiping pw: *********>, ]  
AdminInfo.query.get(1) # 查询刚插入的第一条记录  
# >>> <name: gaoyiping pw: *********>  
AdminInfo.query.filter_by(name = "gaoyiping")  
# >>> <name: gaoyiping pw: *********>  

