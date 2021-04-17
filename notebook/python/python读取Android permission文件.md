今天用python解析一个文本文件，格式如下：  

_复制代码_ 代码如下:

  
[  
{  
"Key":"android.permission.ACCESS_CHECKIN_PROPERTIES",  
"Title":"访问检入属性",  
"Memo":"允许对检入服务上传的属性进行读/写访问。普通应用程序不能使用此权限。",  
"Level":0  
},  
{  
"Key":"android.permission.ACCESS_COARSE_LOCATION",  
"Title":"大概位置",  
"Memo":"访问大概的位置源(例如蜂窝网络数据库)以确定手机的大概位置(如果可以)。恶意应用程序可借此确定您所处的大概位置。",  
"Level":1  
},  
{  
"Key":"android.permission.ACCESS_COARSE_LOCATION",  
"Title":"大概位置",  
"Memo":"访问大概的位置源(例如蜂窝网络数据库)以确定手机的大概位置(如果可以)。恶意应用程序可借此确定您所处的大概位置。",  
"Level":1  
}  
]  

  
开始采用open('filepath').readlines()的方法读取，这样读取的内容都存取到一个列表中，但是我要取每一个{}中的内容取不到，于是考虑用split(',')的方法分离开来，结果把每一个{}里面的内容也根据","分开了。后来请教了网友，说用json方式读取。于是采用以下方式：  

_复制代码_ 代码如下:

  
#-*-encoding:utf-8-*-  
import json  
f = file(r'C:\Users\Tim\Desktop\test.json')  
jsonobj = json.load(f)  
#列表用序号来查询  
print jsonobj[0]['Memo']  
f.close  

  
运行之后报以下错误：  
ValueError: No JSON object could be decoded  
重新将json文件以UTF8无BOM方式保存了一下，运行成功了。另外，对于读取json string可以用以下方式：  

_复制代码_ 代码如下:

  
s = json.loads('{"name":"test", "type":{"name":"seq", "parameter":["1",
"2"]}}')  
print s  
print s.keys()  
print s["name"]  
print s["type"]["name"]  
print s["type"]["parameter"][1]  

  
下面给出完整的读取permission文件的代码：  

_复制代码_ 代码如下:

  
#-*-coding:utf8-*-  
import json  
import codecs

def getperinfo(inputper):  
f = file(r'C:\Users\Tim\Desktop\test.json')  
jsonobj = json.load(f)  
#print jsonobj[0]['Memo']  
for permission in jsonobj:  
#permission.values()获取词典的值  
if permission.values()[2] == inputper:  
print "permission name:%s\npermission info:%s"
%(permission.values()[3],permission.values()[0])  
f.close

if __name__ == '__main__':  
#optparse采用预先定义好的选项来解析命令行参数，optparse默认就是解析命令行参数的。  
from optparse import OptionParser  
parser = OptionParser()  
parser.add_option("-p", "--permission", dest="permission",help="input
permission")  
(options, args) = parser.parse_args()  
#options.permission为输入的permission  
getperinfo(options.permission)  

  
执行示例如下：  
![](https://img.jbzj.com/file_images/article/201311/20131101103549.jpg?2013101103627)

