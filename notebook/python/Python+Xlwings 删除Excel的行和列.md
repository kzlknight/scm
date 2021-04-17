##  一、需求：

某公司管理的多个资管计划每天生成A表，业务人员需手工打开每个A表，将某些行、列删除后方可打印上报。

现拟采用程序代替手工操作。

##  二、分析：

1、应在原始文件的副本上操作，因此需拷贝文件夹内所有Excel至目标目录；

解答：使用shutil.copy()

2、需打开excel并删除指定的行和列；

解答：openpyxl不支持xls格式，xlwt无法删除行和列，最终选择xlwings；

##  三、代码实现：

```python

    #!/usr/bin/env python
    # _*_ coding:utf-8 _*_
     
    """
     
    @Time    : 2019-12-27 17:16
    @Author  : Peanut_C
    @FileName: excel_converter.py
     
    """
     
     
    import os
    import shutil
    import xlwings as xw
     
    current_dir = os.getcwd()
    src_dir = os.path.join(current_dir, 'src_dir')
    dst_dir = os.path.join(current_dir, 'dst_dir')
    exist_list = ['YYYY', 'XXXX']  # 要保留行的A列关键字
     
     
    def file_copy(source_dir, destination_dir):
        os.chdir(source_dir)
        for file in os.listdir(source_dir):
            shutil.copy(file, destination_dir)
        print('INFO ===>>> 文件拷贝完成！')
     
     
    def excel_modifier(wk_dir):
        os.chdir(wk_dir)
        for file in os.listdir(wk_dir):
            # 检查文件格式是否为xls
            # print(type(os.path.splitext(file)[1]))
            if os.path.splitext(file)[1] != '.xls':
                print(file, '===>>>文件格式不正确，请检查！')
            else:
                print('开始处理===>>>', file)
                # 创建app，打开工作表
                app = xw.App(visible=False, add_book=False)
                app.screen_updating = False
                app.display_alerts = False
                load_wb = app.books.open(file)
                load_ws = load_wb.sheets.active
                print('\t已打开工作表……')
     
                # 获取总行数（列数固定不需要获取）
                rows = load_ws.api.UsedRange.Rows.count
                # cols = load_ws.api.UsedRange.Columns.count
     
                # 获取需要处理的A列范围
                a_range = load_ws.range('A1:A'+str(rows-4))  # 得到range对象
     
                # 将range中每行对象存放到列表中并倒序
                print('\t开始获取标志列……')
                cell_list = []
                for cell in a_range:
                    cell_list.append(cell)
                cell_list.reverse()
                # print(cell_list)
     
                # 将表头拆分、重新合并，为插入的值腾地方
                print('\t开始调整合并单元格……')
                load_ws.range('H3:J3').api.unmerge()  # 拆分单元格
                load_ws.range('H3:I3').api.merge()  # 合并单元格
                load_ws.range('J3').value = 'xxx'  # 插入值
     
                # 设定将A列每个值与要保留列表比对，比对不上则删除整行
                print('\t开始调整行和列……')
                for cell in cell_list:
                    if cell.value is not None:  # 单元格不为空则开始比对
                        find_flag = 0  # 匹配标志
                        for exist_value in exist_list:
                            if cell.value.find(exist_value) != -1:
                                find_flag = 1  # 匹配则将标志置为1
                                break  # 一个单元格只要匹配就不再比对保留列表剩下的值
                            else:
                                continue  # 匹配不上则继续
                        if find_flag == 0:  # 没匹配上的删除整行
                            cell_to_del = cell.address
                            # print(cell_to_del)
                            load_ws.range(cell_to_del).api.EntireRow.Delete()
                    else:  # 单元格为空直接删除
                        cell_to_del = cell.address
                        # print(cell_to_del)
                        load_ws.range(cell_to_del).api.EntireRow.Delete()
     
                # 处理列，将指定列从大到小删除（避免先删除小列导致后续列号变动）
                load_ws.api.columns('K').delete
                load_ws.api.columns('G').delete
                load_ws.api.columns('B').delete
                # 美化处理后的Excel
                print('\t开始美化表格……')
                load_ws.range('A1:H24').columns.autofit()
                # 处理完毕，保存、关闭、退出Excel
                load_wb.save()
                load_wb.close()
                app.quit()
                print('处理完毕===>>>', file, '\n\n')
     
     
    if __name__ == '__main__':
        file_copy(src_dir, dst_dir)
        excel_modifier(dst_dir)
        print('任务结束，请至dst_dir目录查看文件！\n\n')
        os.system('pause')
```

##  四、运行情况：

脚本测试完毕后，使用pyinstaller -F excel_converter.py -i icon.ico打包成为exe文件。

将可执行程序拷贝至业务人员电脑可直接执行，原始文件拖入src_dir，处理后文件输出至dst_dir。

经测试excel2013使用正常，excel2007无法连接。

![](https://img.jbzj.com/file_images/article/202012/20201219102905715.png?20201119102914)

以上就是Python+Xlwings 删除Excel的行和列的详细内容，更多关于python 删除Excel的行和列的资料请关注脚本之家其它相关文章！

