其他语言中，比如C＃，我们通常遍历数组是的方法是：  

![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) for  (  int  i
=  0  ; i  < list.Length; i  ++  )  
![](http://www.cnblogs.com/Images/OutliningIndicators/ExpandedBlockStart.gif)
![](http://www.cnblogs.com/Images/OutliningIndicators/ContractedBlock.gif)
![](http://www.cnblogs.com/Images/dot.gif) {  
![](http://www.cnblogs.com/Images/OutliningIndicators/InBlock.gif) //  todo
with list[i]  
![](http://www.cnblogs.com/Images/OutliningIndicators/ExpandedBlockEnd.gif) }

  
在Python中，我们习惯这样遍历：  

![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) for  item  in
sequence:  
![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) process(item)

  
这样遍历取不到item的序号i，所有就有了下面的遍历方法：  

![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) for  index  in
range(len(sequence)):  
![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif)
process(sequence[index])

  
其实，如果你了解内置的enumerate函数，还可以这样写：  

![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) for  index,
item  in  enumerate(sequence):  
![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) process(index,
item)

