Pylons 经过漫长的开发，终于放出了 1.0 版本。对于正规的产品开发来说，1.0 版本的意义很大，这表明 Pylons 的 API 终于稳定下来了。

Pylons 虽是山寨 Rails 而生，但作为一个纯 Python 的 Web
框架，它有一个鲜明的特点：可定制性强。框架每一层都没重新发明轮子，而是尽量整合现有的 Python 库。在 MVC 的 Model 层，Pylons
默认支持 SQLAlchemy。现在 NoSQL 很火 MongoDB 很热。在 Pylons 中应用 MongoDB 也很简单。下面是一个简单的示例。

在 PROJECT/model/__init__.py 中定义 MongoDB 初始化函数和映射对象：

_复制代码_ 代码如下:

  
from ming import Session

from ming import schema  
from ming.orm import MappedClass  
from ming.orm import FieldProperty, ForeignIdProperty, RelationProperty  
from ming.orm import ThreadLocalORMSession

session = None

def init_single_model(model_class):  
model_class.__mongometa__.session = session

class Page(MappedClass):  
class __mongometa__:  
session = session  
name = 'pages'

_id = FieldProperty(schema.ObjectId)  
title = FieldProperty(str)  
content = FieldProperty(str)

def init_model(engine):  
global session  
session = ThreadLocalORMSession(doc_session=Session(engine))  
init_single_model(Page)  
MappedClass.compile_all()  

在 PROJECT/config/environment.py 中进行初始化：

_复制代码_ 代码如下:

  
from ..model import init_model  
from ming.datastore import DataStore

def load_environment(global_conf, app_conf):

...

# Create the Mako TemplateLookup, with the default auto-escaping  
config['pylons.app_globals'].mako_lookup = TemplateLookup(  
directories=paths['templates'],  
error_handler=handle_mako_error,  
module_directory=os.path.join(app_conf['cache_dir'], 'templates'),  
input_encoding='utf-8', default_filters=['escape'],  
imports=['from webhelpers.html import escape'])

# Setup the mongodb database engine  
init_model(DataStore(config['database.uri']))

# CONFIGURATION OPTIONS HERE (note: all config options will override  
# any Pylons config options)

return config  

最后在 development.ini 中加入 MongoDB 的配置项：

_复制代码_ 代码如下:

  
[app:main]  
database.uri = mongodb://localhost:27017/test  

如果需要在程序安装时初始化一些数据, 可以在 PROJECT/websetup.py 中加入

_复制代码_ 代码如下:

  
"""Setup the wukong application"""  
import logging

import pylons.test

from .config.environment import load_environment  
from . import model

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):  
"""Place any commands to setup wukong here"""  
# Don't reload the app if it was loaded under the testing environment  
if not pylons.test.pylonsapp:  
load_environment(conf.global_conf, conf.local_conf)

log.info("Adding demo data.")  
page = model.Page(title='demo', content='This is for demo.')  
model.session.flush()  
log.info("Successfully set up.")  

这里使用了 Ming 库来连接 MongoDB 并做简单的 ORM。Ming 库是对 PyMongo 的 ORM 包装库。它是 SourceForge 用
TurboGears 和 MongoDB 对网站进行重构的副产物。使用起来有点象 SQLAlchemy ORM 。在上面的示例中，也可以把 Ming 替换成
MongoKit 或其它 MongoDB 的 ORM 库，甚至直接用 PyMongo 也无不可。  
有种感觉，MongoDB 会火。

