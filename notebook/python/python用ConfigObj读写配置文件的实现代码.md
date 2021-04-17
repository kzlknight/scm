发现一个简单而又强大的读写配置文件的lib， [ http://www.voidspace.org.uk/python/configobj.html
](http://www.voidspace.org.uk/python/configobj.html) 。  
个人觉得最大的亮点在于自带的格式校验功能，并且支持复杂的嵌套格式，而且使用起来也相当的简便。

来看例子吧。  
读文件  

_复制代码_ 代码如下:

  
from configobj import ConfigObj  
config = ConfigObj(filename)  
#  
value1 = config['keyword1']  
value2 = config['keyword2']  
#  
section1 = config['section1']  
value3 = section1['keyword3']  
value4 = section1['keyword4']  
#  
# you could also write  
value3 = config['section1']['keyword3']  
value4 = config['section1']['keyword4']  

写文件

_复制代码_ 代码如下:

  
from configobj import ConfigObj  
config = ConfigObj()  
config.filename = filename  
#  
config['keyword1'] = value1  
config['keyword2'] = value2  
#  
config['section1'] = {}  
config['section1']['keyword3'] = value3  
config['section1']['keyword4'] = value4  
#  
section2 = {  
'keyword5': value5,  
'keyword6': value6,  
'sub-section': {  
'keyword7': value7  
}  
}  
config['section2'] = section2  
#  
config['section3'] = {}  
config['section3']['keyword 8'] = [value8, value9, value10]  
config['section3']['keyword 9'] = [value11, value12, value13]  
#  
config.write()  

更多内容请参阅下官方doc文档。

