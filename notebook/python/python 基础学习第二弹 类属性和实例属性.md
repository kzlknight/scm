_复制代码_ 代码如下:

  
#!/usr/bin/env python  
class Foo(object):  
x=1  
if __name__=='__main__':  
foo = Foo()  
print 'foo.x=',foo.x  
print 'Foo.x=',Foo.x  
foo.x = 2  
print 'foo.x=',foo.x  
print 'Foo.x=',Foo.x  

