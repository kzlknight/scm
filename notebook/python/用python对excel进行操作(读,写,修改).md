##  一、对excel的写操作实例：

将一个列表的数据写入excel, 第一行是标题，下面行数具体的数据

```python

    import xlwt
    #只能写不能读
    stus = [['姓名', '年龄', '性别', '分数'],
        ['mary', 20, '女', 89.9],
        ['mary', 20, '女', 89.9],
        ['mary', 20, '女', 89.9],
        ['mary', 20, '女', 89.9]
        ]
    book = xlwt.Workbook()#新建一个excel
    sheet = book.add_sheet('case1_sheet')#添加一个sheet页
    row = 0#控制行
    for stu in stus:
      col = 0#控制列
      for s in stu:#再循环里面list的值，每一列
        sheet.write(row,col,s)
        col+=1
      row+=1
    book.save('stu_1.xls')#保存到当前目录下
```

##  二、对excel 的读操作：

```python

    import xlrd
    #只能读不能写
    book = xlrd.open_workbook('stu.xls')#打开一个excel
    sheet = book.sheet_by_index(0)#根据顺序获取sheet
    sheet2 = book.sheet_by_name('case1_sheet')#根据sheet页名字获取sheet
    print(sheet.cell(0,0).value)#指定行和列获取数据
    print(sheet.cell(0,1).value)
    print(sheet.cell(0,2).value)
    print(sheet.cell(0,3).value)
    print(sheet.ncols)#获取excel里面有多少列
    print(sheet.nrows)#获取excel里面有多少行
    print(sheet.get_rows())#
    for i in sheet.get_rows():
      print(i)#获取每一行的数据
    print(sheet.row_values(0))#获取第一行
    for i in range(sheet.nrows):#0 1 2 3 4 5
      print(sheet.row_values(i))#获取第几行的数据
    
    print(sheet.col_values(1))#取第一列的数据
    for i in range(sheet.ncols):
      print(sheet.col_values(i))#获取第几列的数据
```

##  三、对excel的修改操作：

将excel中的某个值修改并重新保存

```python

    from xlutils.copy import copy
    import xlrd
    #xlutils:修改excel
    book1 = xlrd.open_workbook('stu.xls')
    book2 = copy(book1)#拷贝一份原来的excel
    # print(dir(book2))
    sheet = book2.get_sheet(0)#获取第几个sheet页，book2现在的是xlutils里的方法，不是xlrd的
    sheet.write(1,3,0)
    sheet.write(1,0,'hello')
    book2.save('stu.xls')
```

以上就是用python对excel进行操作(读,写,修改)的详细内容，更多关于python对excel进行操作的资料请关注脚本之家其它相关文章！

