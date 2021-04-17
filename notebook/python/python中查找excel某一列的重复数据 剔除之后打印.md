1.在python中excel的简单读写操作，推荐使用xlrd（特别是读操作）  
  
2.到 [ http://pypi.python.org/pypi/xlrd ](http://pypi.python.org/pypi/xlrd) 去下载
xlrd库；  
  
3.工程代码如下：  
  

_复制代码_ 代码如下:

  
import xlrd  
  
def open_excel(fileName="simple.xls"):  
try:  
fileHandler = xlrd.open_workbook(fileName)  
return fileHandler  
except Exception, e:  
print str(e)  
  
def scan_excel(sheet_name1=u'Sheet1'):  
handler = open_excel()  
page = handler.sheet_by_name(sheet_name1)  
return page  
  
def trim_cols(index=0):  
page = scan_excel()  
col1 = page.col_values(index)  
col2 = []  
  
for item in col1:  
if item not in col2:  
col2.append(item)  
print col1  
print col2  
  
def main():  
trim_cols()  
  
if __name__ == "__main__":  
main()  

  
  
打印结果：  
[1.0, 2.0, 3.0, 4.0, 1.0, 2.0, 3.0, 4.0]  
[1.0, 2.0, 3.0, 4.0]

