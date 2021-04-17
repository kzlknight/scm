看下面的例子就会明白了：  

_复制代码_ 代码如下:

  
print '|','*'.ljust(10),'|'  
print '|','*'.ljust(10,'-'),'|'  
print '|','*'.rjust(10,'-'),'|'  
print '|','*'.center(10,'-'),'|'  
  
  
for a in range(1, 6):  
print 'a = '.ljust(5), repr(a).ljust(10), 'b = '.ljust(5), repr(a * 2)  

  
输出结果:  
| * |  
| *--------- |  
| ---------* |  
| ----*----- |  
a = 1 b = 2  
a = 2 b = 4  
a = 3 b = 6  
a = 4 b = 8  
a = 5 b = 10

