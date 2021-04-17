_复制代码_ 代码如下:

  
#coding=utf8  
__author__ = 'Administrator'

# 当函数的参数不确定时，可以使用*args和**kwargs。*args没有key值，**kwargs有key值

def fun_var_args(farg, *args):  
print 'args:', farg  
for value in args:  
print 'another arg:',value

# *args可以当作可容纳多个变量组成的list或tuple  
fun_var_args(1, 'two', 3, None)

#args: 1  
#another arg: two  
#another arg: 3  
#another arg: None

  
def fun_var_kwargs(farg, **kwargs):  
print 'args:',farg  
for key in kwargs:  
print 'another keyword arg:%s:%s' % (key, kwargs[key])

# myarg1,myarg2和myarg3被视为key， 感觉**kwargs可以当作容纳多个key和value的dictionary  
fun_var_kwargs(1, myarg1='two', myarg2=3, myarg3=None)  
# 输出：  
#args: 1  
#another keyword arg:myarg1:two  
#another keyword arg:myarg2:3  
#another keyword arg:myarg3:None

def fun_args(arg1, arg2, arg3):  
print 'arg1:', arg1  
print 'arg2:', arg2  
print 'arg3:', arg3

myargs = ['1', 'two', None] # 定义列表  
fun_args(*myargs)

# 输出：  
#arg1: 1  
#arg2: two  
#arg3: None

mykwargs = {'arg1': '1', 'arg2': 'two', 'arg3': None} # 定义字典类型  
fun_args(**mykwargs)

# 输出：  
#arg1: 1  
#arg2: two  
#arg3: None

# 两者都有  
def fun_args_kwargs(*args, **kwargs):  
print 'args:', args  
print 'kwargs:', kwargs

  
args = [1, 2, 3, 4]  
kwargs = {'name': 'BeginMan', 'age': 22}  
fun_args_kwargs(args,kwargs)  
# args: ([1, 2, 3, 4], {'age': 22, 'name': 'BeginMan'})  
# kwargs: {}

fun_args_kwargs(1,2,3,a=100)  
#args: (1, 2, 3)  
#kwargs: {'a': 100}

fun_args_kwargs(*(1,2,3,4),**{'a':None})  
#args: (1, 2, 3, 4)  
#kwargs: {'a': None}  

  
  
![](https://img.jbzj.com/file_images/article/201312/20131204103902.png?2013114103950)  
---

