##  02条件语句和while循环

三目运算

```python

    a = 6
    #原判断语句
    if a > 5:
    	print(True)
    else:
    	print(False)
    #三目运算
    print(True if a >5 else False)
```

##  逻辑运算

1. 三种逻辑运算 

与逻辑 and

两边为真则为真

或逻辑 or

一边为真则为真

非逻辑

not 逻辑值取反

优先级: not > and > or

2.逻辑短路

```python

    # and 逻辑短路
    a = 3 #没有对b赋值，但程序不会报错能够正常运行
    #左边布尔值为假，右边布尔值的真假性不影响整体布尔值为假
    print(a > 4 and b > 4) #输出布尔值为False
    
    # or 逻辑短路
    a = 3 #没有对b赋值，但程序不会报错能够正常运行
    #左边布尔值为真，右边布尔值的真假性不影响整体布尔值为真
    print(a > 2 and b > 2) #输出布尔值为True
    
    # not 没有逻辑短路
```

3.连续判断

```python

    #python底层会把连续判断转换成 and 连接的形式
    print(1 > 2 > 3) #相当于 1>2 and 2>3, 其值为False
    
    #连续判断的逻辑短路
    #由于and存在逻辑短路，所以连续判断也存在逻辑短路
    #整数2和字符串'3'类型不同无法比较大小
    #左边1>2布尔值为假，右边无需进行判断，所以不会报错
    print(1 > 2 > '3') #输出布尔值为False
```

while循环

```python

    #循环条件可以为True，但内部必须要有break保证循环能够被终止，否则将陷入死循环
    #使用break终止的循环属于非正常结束循环，不会执行else部分
    a = 1
    while True:
    	if a % 5 == 0:
    		break
    	print(a)
    	a += 1
    else:
    	print('循环结束')
```

练习

利用while 写出九九乘法表

```python

    #使用continue终止的循环不属于非正常结束循环，循环结束后会执行else部分
    a = 1
    while a < 4:
    	if a % 2 == 0:
    		a += 1
    		continue
    	print(a)
    	a += 1
    else: 
    	print('循环结束')
```

利用random 的randint 方法写一个猜数字的小游戏

```python

    i = 1
    while i < 10:
    	j = 1
    	while j <= i:
    		result = '%-3d'%(i*j)
    		print(f'{j}×{i}={result}', end='')
    		j += 1
    	print('\n')
    	i += 1
```

```python

    print('1～100以内整数的猜数字游戏，总共7次机会哦！')
    import random
    Min = 1
    Max = 100
    mynumber = random.randint(Min, Max)
    i = 1
    while i <= 7:
    	yournumber = int(input('请输入你猜的数字：'))
    	if yournumber == mynumber:
    		print('恭喜你，猜对了！你真聪明！')
    		break
    	elif yournumber > mynumber:
    		Max = yournumber
    		print(f'你猜的太大了，在{Min}~{Max}之间哦！你还有{7-i}次机会！')
    		i += 1
    	else:
    		Min = yournumber
    		print(f'你猜的太小了，在{Min}~{Max}之间哦！你还有{7-i}次机会！')
    		i += 1
    else:
    	print('机会已经用完了！很遗憾，你没有猜对！')
```

到此这篇关于详解python 条件语句和while循环的文章就介绍到这了,更多相关python
条件语句和while循环内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

