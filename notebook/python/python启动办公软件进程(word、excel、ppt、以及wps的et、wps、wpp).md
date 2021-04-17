_复制代码_ 代码如下:

  
#-*- coding:utf-8 -*-  
from win32com.client import Dispatch  
import time  
def start_office_application(app_name):  
# 在这里获取到app后，其它的操作和通过VBA操作办公软件类似  
app = Dispatch(app_name)  
app.Visible = True  
time.sleep(0.5)  
app.Quit()  
if __name__ == '__main__':  
'''''  
通过python启动办公软件的应用进程，  
其中wpp、et、wpp对应的是金山文件、表格和演示  
word、excel、powerpoint对应的是微软的文字、表格和演示  
'''  
lst_app_name = [  
"wps.Application",  
'et.Application',  
'wpp.Application',  
'word.Application',  
'excel.Application',  
'powerpoint.Application'  
]  
for app_name in lst_app_name:  
print "app_name:%s" % app_name  
start_office_application(app_name)  

