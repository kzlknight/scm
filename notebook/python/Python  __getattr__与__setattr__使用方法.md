比如下面的例子：

class  Book  (  object  ):  
def  __setattr__  (  self  ,  name  ,  value  ):  
if  name  ==  'value'  :  
object  .  __setattr__  (  self  ,  name  ,  value  -  100  )  
else  :  
object  .  __setattr__  (  self  ,  name  ,  value  )  
def  __getattr__  (  self  ,  name  ):  
try  :  
return  object  .  __getattribute__  (  name  )  
except  :  
return  name  +  ' is not found!'  
def  __str__  (  self  ):  
return  self  .  name  +  ' cost : '  +  str  (  self  .  value  )  
  
c  =  Book  ()  
c  .  name  =  'Python'  
c  .  value  =  100  
print  c  .  name  
print  c  .  value  
print  c  
print  c  .  Type

  
上面的例子中，在赋值书的value属性时，偷偷的将value减去了１００，呵。输出结果：

Python  
0  
Python cost : 0  
Type is not found!

