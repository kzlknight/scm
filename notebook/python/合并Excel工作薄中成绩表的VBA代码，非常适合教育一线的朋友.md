这时候还需要把各个工作表合并到一起来形成一个汇总表。这时候比较麻烦也比较容易出错，因为各个表的学号不一定都是一致的、对齐的。因为可能会有人缺考，有人会考号涂错等等。特奉献以下代码，用于合并学生成绩表或者其它类似的表都可以。本代码特点在于不需要使用SQL或者Access等大头软件，只需要Excel就可以执行，非常方便，速度也不慢。转载请勿清除广告。  
没有合适的局域网管理软件吗？你的网管工具够灵活够高效吗？看看这个network management software。  
' =============================================  
' 合并总表时，不参加计算的表格数目  
' 因为一般合并的总表放在最后一个工作表，要排除掉这个表。  
Const ExcludeSheetCount = 1  
' 主函数，因为用到了ADO，必须作如下引用才能运行本代码。  
' 工具>引用， 引用ADO(Microsoft ActiveX Data Objects 2.X Library)  
' 链接所有sheet到一个总表  
' 要合并的表的第一行必须是字段名称，不能是合并单元格  
Sub SQL_ADO_EXCEL_JOIN_ALL()  
Dim cnn As New ADODB.Connection  
Dim rs As New ADODB.Recordset  
Dim i, k, shCount As Integer  
Dim SQL, SQL2 As String, cnnStr As String  
Dim s1, s2, s3, tmp As String  
Dim ws As Worksheet  
Const IDIdx = 1  
Const ScoreIdx = 3  
shCount = ActiveWorkbook.Sheets.Count  
' 获取所有考号  
' EXCEL 会自动去除重复数据  
' SQL = "(select ID from [语文$]) union (select ID from [英语$]) union (select ID
from [物理$]) order by ID"  
SQL = ""  
For i = 1 To shCount - ExcludeSheetCount  
s1 = "(SELECT ID FROM [" & Sheets(i).Name & "$])"  
If i = 1 Then  
SQL = s1  
Else  
SQL = SQL & " UNION " & s1  
End If  
Next  
'MsgBox SQL  
Set ws = ActiveWorkbook.Sheets(shCount)  
cnnStr = "provider = microsoft.jet.oledb.4.0;Extended Properties='Excel
8.0;HDR=yes;IMEX=1';data source=" & ThisWorkbook.FullName  
cnn.CursorLocation = adUseClient  
cnn.ConnectionString = cnnStr  
cnn.Open  
rs.Open SQL, cnn, adOpenKeyset, adLockOptimistic  
ws.Activate  
ws.Cells.Clear  
For i = 1 To rs.Fields.Count  
ws.Cells(1, i) = rs.Fields(i - 1).Name  
Next  
ws.Range("A2").CopyFromRecordset rs  
For i = 1 To shCount - ExcludeSheetCount  
Sheets(shCount).Cells(1, i + 1) = Sheets(i).Name  
Next  
'EXCEL 不支持 UPDATE  
'SQL = "update [合并$] set 语文 = '1'"  
' 相当于内联接  
'SQL = "select tt.ID,ta.score as 语文,tb.score as 英语 from [合并$] AS tt, [语文$] as
ta, [英语$] as tb "  
'SQL = SQL & "where (tt.ID = ta.ID) and (tt.ID = tb.ID)"  
' 左联接所有表格  
' 通过测试的语句  
'SQL = "select tt.ID,ta.score AS 语文,tb.score as 英语 from ([合并$] AS tt left join
[语文$] as ta on tt.ID = ta.ID) "  
'SQL = SQL & "left join [英语$] as tb on tt.ID = tb.ID"  
SQL2 = "([" & Sheets(shCount).Name & "$] AS tt LEFT JOIN [" & Sheets(1).Name &
"$] AS t1 ON tt.id=t1.id) "  
SQL = "SELECT tt.ID,"  
For i = 1 To shCount - ExcludeSheetCount  
tmp = "t" & i  
SQL = SQL & tmp & ".score AS " & Sheets(i).Name  
If i < shCount - ExcludeSheetCount Then SQL = SQL & ", "  
If i > 1 Then  
SQL2 = "(" & SQL2 & " LEFT JOIN [" & Sheets(i).Name & "$] AS " & tmp & " ON
tt.id=" & tmp & ".id)"  
End If  
Next  
s1 = SQL & " FROM " & SQL2 & " ORDER BY tt.ID"  
MsgBox s1  
rs.Close  
rs.Open s1, cnn, adOpenKeyset, adLockOptimistic  
' 清除表格  
ws.Activate  
Cells.Select  
Selection.Delete Shift:=xlUp  
For i = 1 To rs.Fields.Count  
ws.Cells(1, i) = rs.Fields(i - 1).Name  
Next  
ws.Range("A2").CopyFromRecordset rs  
rs.Close  
cnn.Close  
Set rs = Nothing  
Set cnn = Nothing  
Call AddHeader  
Call FindBlankCells  
Call TableBorderSet  
ws.Columns(1).AutoFit  
ws.Cells(2, 1).Select  
MsgBox "Finished."  
End Sub  
' 在表格第一行插入行，然后合并单元格，加上说明文字  
Sub AddHeader()  
Dim ws As Worksheet  
Dim s1, s2 As String  
shCount = ActiveWorkbook.Sheets.Count  
Set ws = Sheets(shCount)  
Column = ws.UsedRange.Columns.Count  
ws.Rows(1).Insert  
s1 = Chr(Asc("A") + Column - 1)  
s2 = "A1:" & s1 & "1"  
ws.Range(s2).Merge  
ws.Rows(1).RowHeight = 100  
s1 = "说明" & Chr(13) & Chr(10) & _  
"本总表为计算生成，把几个单科的客观题成绩合并在一起，避免手工处理时因考号不对齐而导致错位。" & Chr(13) & Chr(10) & _  
"注意：如果某单科成绩表中存在相同考号，则总表中该考号的该科成绩是不准确的。" & Chr(13) & Chr(10) & _  
"填涂错误的考号，一般出现在表里顶端或底端"  
ws.Cells(1, 1) = s1  
ActiveSheet.Rows(1).RowHeight = 80  
' 冻结窗格  
ActiveSheet.Rows(3).Select  
ActiveWindow.FreezePanes = True  
ActiveWindow.SmallScroll Down:=0  
End Sub  
' 设置表格边框  
Sub TableBorderSet()  
ActiveSheet.UsedRange.Select  
Selection.Borders(xlDiagonalDown).LineStyle = xlNone  
Selection.Borders(xlDiagonalUp).LineStyle = xlNone  
With Selection.Borders(xlEdgeLeft)  
.LineStyle = xlContinuous  
.Weight = xlThin  
.ColorIndex = xlAutomatic  
End With  
With Selection.Borders(xlEdgeTop)  
.LineStyle = xlContinuous  
.Weight = xlThin  
.ColorIndex = xlAutomatic  
End With  
With Selection.Borders(xlEdgeBottom)  
.LineStyle = xlContinuous  
.Weight = xlThin  
.ColorIndex = xlAutomatic  
End With  
With Selection.Borders(xlEdgeRight)  
.LineStyle = xlContinuous  
.Weight = xlThin  
.ColorIndex = xlAutomatic  
End With  
With Selection.Borders(xlInsideVertical)  
.LineStyle = xlContinuous  
.Weight = xlThin  
.ColorIndex = xlAutomatic  
End With  
With Selection.Borders(xlInsideHorizontal)  
.LineStyle = xlContinuous  
.Weight = xlThin  
.ColorIndex = xlAutomatic  
End With  
End Sub  
' 标记无分数的单元格，方便找出答题卡没有分数的学生  
Sub FindBlankCells()  
Dim i, j, row, col As Integer  
'ActiveSheet.Cells(2, 1).Interior.ColorIndex = 15  
row = ActiveSheet.UsedRange.Rows.Count  
col = ActiveSheet.UsedRange.Columns.Count  
For i = 2 To row  
For j = 2 To col  
If IsEmpty(ActiveSheet.Cells(i, j).Value) Then  
ActiveSheet.Cells(i, j).Interior.ColorIndex = 15  
End If  
Next  
Next  
End Sub

