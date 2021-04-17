写入Excel中后有显示第一列客户款号总库存这些，开始写在第12行第一列开始写入，一行写入5个，然后再隔12行，再写入下边的数据，图片需要对应客户款号在Excel写入图片，类似下面的格式

![](https://img.jbzj.com/file_images/article/202101/20210101135540.jpg)

![](https://img.jbzj.com/file_images/article/202101/20210101135548.jpg)

```python

    import xlsxwriter
    import os
    #以空字符填充缺失值，不然写入数据会报错
    data.fillna('',inplace=True)
    #创建一个新Excel文件并添加一个工作表。
    workbook = xlsxwriter.Workbook('images.xlsx')
    worksheet = workbook.add_worksheet()
    # # 加宽第2列，,根据图片缩放大小进行调整。
    worksheet.set_column('B:B', 20)
    worksheet.set_column('D:D', 20)
    worksheet.set_column('F:F', 20)
    worksheet.set_column('H:H', 20)
    ##写入数据和图片
    for i in range(len(data)):
      for j in range(4):
        worksheet.write(i//5*16+j+12,i%5*2 ,['客户款号','总库存','零售数量','前一周'][j])
        worksheet.write(i//5*16+j+12,i%5*2+1 ,data.iloc[i,0::].values[j])
        #插入图片，insert_image(位置行，位置列,文件名,缩放比例)
      if data.iloc[i,0::].values[0]+'.jpg' not in os.listdir('.\img\\'):
        print(i,'找不到',data.iloc[i,0::].values[0]+'.jpg')
      else:
        worksheet.insert_image(i//5*16,i%5*2+1,'img/'+data.iloc[i,0::].values[0]+'.jpg',{'x_scale': 0.1, 'y_scale': 0.12}) 
        print(i,'写入成功!')
      i+=1
    workbook.close()
    
```

```python

    0 写入成功!
    1 写入成功!
    2 找不到 N038400237.jpg
    3 找不到 N038400301.jpg
    4 找不到 N039400310.jpg
    5 找不到 N038400552.jpg
    6 写入成功!
    7 找不到 N038401101.jpg
    8 找不到 N039400105.jpg
    9 找不到 N039400219.jpg
```

效果如下：

![](https://img.jbzj.com/file_images/article/202101/20210101135600.jpg)

当然还有合并单元格，设置单元格格式，以及处理图片的操作没写，有时间再来补充！

**补充：python对excel表格处理需要导入相关的库：**

###  （1）、操作xls格式的表格文件：

读取：xlrd

写入：xlwt

修改（追加写入）：xlutils

###  （2）、操作xlsx格式的表格文件：

读取/写入：openpyxl

*如果用操作xls的方法去写入xlsx文件，会导致文件损坏无法打开；反之一样。 

###  （一）、操作xls格式表格

1、读取excel表格数据

```python

    import xlrd  #从excle里读数据
    import xlwt  #创建新的表格写入数据
    import xlutils #往已有表格中追加数据
     
    class IOExcel(object):
      def __init__(self,file):
        self.file = file
     
      def get_sheet(self,sheetname):
        excelfile=xlrd.open_workbook(self.file)
        self.sheet = excelfile.sheet_by_name(sheetname)
        return self.sheet
      #获取第*行的数据
      def get_rowData(self,row):
        cols = self.sheet.ncols  #获取sheet页有多少列
        Cells = []
        for i in range(0,cols):
          Cells.append(self.sheet.cell(row,i).value)
        return Cells
```

2、创建表格写入数据

```python

    def write_excel(self,sheet_name, value):
      index = len(value) # 获取需要写入数据的行数
      workbook = xlwt.Workbook() # 新建一个工作簿
      sheet = workbook.add_sheet(sheet_name) # 在工作簿中新建一个表格
      for i in range(0, index):
        for j in range(0, len(value[i])):
          sheet.write(i, j, value[i][j])   #向表格中写入数据（对应的行和列）
      workbook.save(self.file)   # 保存工作簿
```

3、向已存在表格中追加数据

```python

    def write_excel_xls_append(self,value):
      index = len(value) # 获取需要写入数据的行数
      workbook = xlrd.open_workbook(self.file) # 打开工作簿
      sheets = workbook.sheet_names() # 获取工作簿中的所有表格
      worksheet = workbook.sheet_by_name(sheets[0]) # 获取工作簿中所有表格中的的第一个表格
      rows_old = worksheet.nrows # 获取表格中已存在的数据的行数
      new_workbook = copy(workbook) # 将xlrd对象拷贝转化为xlwt对象
      new_worksheet = new_workbook.get_sheet(0) # 获取转化后工作簿中的第一个表格
      for i in range(0, index):
        for j in range(0, len(value[i])):
          new_worksheet.write(i+rows_old, j, value[i][j]) # 追加写入数据，注意是从i+rows_old行开始写入
      new_workbook.save(self.file) # 保存工作簿
```

###  （二）、操作xlsx格式表格

```python

    wb = openpyxl.Workbook()  #创建一个新的excel
    we = wb.create_sheet('第二页',0) #修改sheet页的名字；设置插入sheet页的位置，默认在上一页后面（ 初始创建的excel是只有一个默认sheet页的，所以设置位置的值大于1效果都一样，都是在默认sheet页的后面接着）
    # we.title = '你好' # 修改sheet页的名字
    #操作单元格
    we['A1']=123124
    we['B2']='你好'
    print(we.cell(1,2,'123123').value)  #设置cell的行号和列号和值，返回cell的值
    wb.save('C:\\Users\\t_ful\\PycharmProjects\\test\\element\\t.xlsx')  #保存表格
    
```

以上为个人经验，希望能给大家一个参考，也希望大家多多支持脚本之家。如有错误或未考虑完全的地方，望不吝赐教。

