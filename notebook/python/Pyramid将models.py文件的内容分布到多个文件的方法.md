我们通过下面的文件结构，将models.py改成一个package.

_复制代码_ 代码如下:

  
myapp  
__init__.py  
scripts  
__init__.py  
initialize_db.py  
models  
__init__.py  
meta.py  
foo.py  
moo.py  

  
上面的 meta.py， 在代码中定义一个其它model文件共享Base和DBSession.

_复制代码_ 代码如下:

  
Base = declarative_base()  
DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension))  

foo.py和moo.py就是具体的model定义  
foo.py 和moo.py 使用meta.py中定义的base

为了保证定义的model能够在程序中被启用，在models/__init__.py中引入它们:

_复制代码_ 代码如下:

  
from .meta import DBSession  
from .foo import Foo  
from .moo import Moo  

