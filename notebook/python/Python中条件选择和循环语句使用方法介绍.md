同C语言、Java一样，Python中也存在条件选择和循环语句，其风格和C语言、java的很类似，但是在写法和用法上还是有一些区别。今天就让我们一起来了解一下。  
**一.条件选择语句**  
Python中条件选择语句的关键字为：if 、elif 、else这三个。其基本形式如下：  

_复制代码_ 代码如下:

  
if condition:  
block  
elif condition:  
block  
...  
else  
block  

  
其中elif和else语句块是可选的。对于if和elif只有condition为True时，该分支语句才执行，只有当if和所有的elif的condition都为False时，才执行else分支。注意Python中条件选择语句和C中的区别，C语言中condition必须要用括号括起来，在Python中不用，但是要注意condition后面有个冒号。  
**下面这个是成绩划分等级的一个例子** ：  

_复制代码_ 代码如下:

  
score=input()  
if score<60:  
print "D"  
elif score<80:  
print "C"  
elif score<90:  
print "B"  
else:  
print "A"  

  
**二.循环语句**  
和C语言一样，Python也提供了for循环和while循环（在Python中没有do..while循环）两种。但是Python中的for循环用法和C语言中的大不一样（和Java、C#中的for循环用法类似），while循环用法大致和C语言中的类似。  
for循环的基本形式如下：  

_复制代码_ 代码如下:

  
for variable in list:  
block  

  
举个例子，求算从1加到100的和：  

_复制代码_ 代码如下:

  
sum=0  
for var in range(1,101):  
sum+=var  
print sum  

  
range()是一个内置函数，它可以生成某个范围内的数字列表。比如说range(1,6)就会生成[1,2,3,4,5]这样一个列表，而range(8)会生成[0,1,2,3,4,5,6,7]这样一个列表。  
当然可以有嵌套循环，比如说有一个列表list=['China','England','America']，要遍历输出每个字母。  

_复制代码_ 代码如下:

  
list=['China','England','America']  
for i in range(len(list)):  
word=list[i]  
for j in range(len(word)):  
print word[j]  

  
内置的函数len()不仅可以用来求算字符串的长度也可以用来求列表或者集合中成员的个数。  
下面来看一下while循环的基本形式：  

_复制代码_ 代码如下:

  
while condition:  
block  

  
只有当condition为True时，才执行循环。一旦condition为False，循环就终止了。  
举个例子：  

_复制代码_ 代码如下:

  
count=2  
while count>0:  
print "i love python!"  
count=count-1  

  
如果想要在语句块过程中终止循环，可以用break或者continue。break是跳出整个循环，而continue是跳出该次循环。  

_复制代码_ 代码如下:

  
count=5  
while True:  
print "i love python!"  
count=count-1  
if count==2:  
break  

  

_复制代码_ 代码如下:

  
count=5  
while count>0:  
count=count-1  
if count==3:  
continue  
print "i love python!"  

  
关于条件语句和循环语句暂时就讲这么多了，它的基本用法基本就这些。有兴趣的话最好自己动手上机练练。

