实现代码如下:  

_复制代码_ 代码如下:

  
import json  
from datetime import date, datetime  
  
  
def __default(obj):  
if isinstance(obj, datetime):  
return obj.strftime('%Y-%m-%dT%H:%M:%S')  
elif isinstance(obj, date):  
return obj.strftime('%Y-%m-%d')  
else:  
raise TypeError('%r is not JSON serializable' % obj)  
  
print json.dumps({'d': datetime.now(), 'today': date.today(), 'x': 111},  
default=__default)  

