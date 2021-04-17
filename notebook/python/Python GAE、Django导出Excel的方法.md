但GAE、Django并没有直接将pyExcelerator导出为Excel的方法。我的思路是先用把数据导入到Workbook和Worksheet中，如果存为文件可以直接调用Workbook的save方法，但GAE不支持本地文件操作，即使图片也只能存放在DataStore中，但我们可以类似于返回图片的方法，直接将Excel的二进制流返回给浏览器。这就需要修改一下Workbook的代码，加入返回二进制流的方法，我给他取的名字是savestream，在savestream中再次调用CompoundDoc.XlsDoc的savestream方法，也是自己增加的。代码如下：  
Workbook的savestream：  

_复制代码_ 代码如下:

  
def savestream(self):  
import CompoundDoc  
doc = CompoundDoc.XlsDoc()  
return doc.savestream(self.get_biff_data())  

  
**CompoundDoc.XlsDoc的savestream方法：  
**

_复制代码_ 代码如下:

  
def savestream(self, stream):  
# 1. Align stream on 0x1000 boundary (and therefore on sector boundary)  
padding = '\x00' * (0x1000 - (len(stream) % 0x1000))  
self.book_stream_len = len(stream) + len(padding)  
self.__build_directory()  
self.__build_sat()  
self.__build_header()  
s = ""  
s = s + str(self.header)  
s = s + str(self.packed_MSAT_1st)  
s = s + str(stream)  
s = s + str(padding)  
s = s + str(self.packed_MSAT_2nd)  
s = s + str(self.packed_SAT)  
s = s + str(self.dir_stream)  
return s  

  
这样就可以返回Excel文件的二进制流了，下面就是如何在用户请求的时候将Excel文件返回，我借鉴了PHP的实现方法，代码如下：  

_复制代码_ 代码如下:

  
class Main(webapp.RequestHandler):  
def get(self):  
self.sess = session.Session()  
t_values['user_id'] = self.sess['userid']  
if self.request.get('export') == 'excel':  
wb = Workbook()  
ws = wb.add_sheet(u'统计报表')  
#表头  
font0 = Font()  
font0.bold = True  
font0.height = 12*20;  
styletitle = XFStyle()  
styletitle.font = font0  
ws.write(0, 0, u"日期："+begintime.strftime('%Y-%m-%d') + " - " +
endtime.strftime('%Y-%m-%d'), styletitle)  
#返回Excel文件  
self.response.headers['Content-Type'] = "application/vnd.ms-execl"  
self.response.headers['Content-Disposition'] = str("attachment;
filename=%s.xls"%t_values['user_id'])  
self.response.headers['Pragma'] = "no-cache"  
self.response.headers['Expires'] = "0"  
self.response.out.write(wb.savestream())  
return  

  
效果可以参见我爱记账网的excel报表。

