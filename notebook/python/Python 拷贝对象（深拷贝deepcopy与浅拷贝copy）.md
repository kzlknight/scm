1. copy.copy 浅拷贝 只拷贝父对象，不会拷贝对象的内部的子对象。   
2. copy.deepcopy 深拷贝 拷贝对象及其子对象   
一个很好的例子：  

![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) import  copy  
![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) a  =  [  1  ,
2  ,  3  ,  4  , [  '  a  '  ,  '  b  '  ]]  #  原始对象  
![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif)  
![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) b  =  a  #
赋值，传对象的引用  
![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) c  =
copy.copy(a)  #  对象拷贝，浅拷贝  
![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) d  =
copy.deepcopy(a)  #  对象拷贝，深拷贝  
![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif)  
![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) a.append(  5
)  #  修改对象a  
![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) a[  4
].append(  '  c  '  )  #  修改对象a中的['a', 'b']数组对象  
![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif)  
![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) print  '  a =
'  , a  
![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) print  '  b =
'  , b  
![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) print  '  c =
'  , c  
![](http://www.cnblogs.com/Images/OutliningIndicators/None.gif) print  '  d =
'  , d

  
输出结果：  
a = [1, 2, 3, 4, ['a', 'b', 'c'], 5]  
b = [1, 2, 3, 4, ['a', 'b', 'c'], 5]  
c = [1, 2, 3, 4, ['a', 'b', 'c']]  
d = [1, 2, 3, 4, ['a', 'b']]  

