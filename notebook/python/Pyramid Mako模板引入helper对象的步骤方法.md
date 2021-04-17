原理是我们在pyramind的before render event 中插入我们的helper

1. 创建helper.py文件，在里面添加上我们常用的方法 

2. 在__init__.py文件中： 

加入这个函数:  

_复制代码_ 代码如下:

  
def add_renderer_globals(event):  
event['h'] = helpers  

  
  
在main函数中  

_复制代码_ 代码如下:

  
config.add_subscriber(add_renderer_globals, BeforeRender)  

  
  
3. 在模板中使用定义的方法，h.method() 

