1. 列表可包含任何数据类型的元素，单个列表中的元素无须全为同一类型。   
2. append() 方法向列表的尾部添加一个新的元素。只接受一个参数。   
3. extend()方法只接受一个列表作为参数，并将该参数的每个元素都添加到原有的列表中。 

**append()用法示例：**

>>> mylist = [1,2,0,'abc']

>>> mylist

[1, 2, 0, 'abc']

>>> mylist.append(4)

>>> mylist

[1, 2, 0, 'abc', 4]

>>> mylist.append('haha')

>>> mylist

[1, 2, 0, 'abc', 4, 'haha']

>>>

**extend()用法示例：**

>>> mylist

[1, 2, 0, 'abc', 4, 'haha']

>>> mylist.extend(['lulu'])

>>> mylist

[1, 2, 0, 'abc', 4, 'haha', 'lulu']

>>> mylist.extend([aaa,'lalalala'])

Traceback (most recent call last):

File "<stdin>", line 1, in <module>

NameError: name 'aaa' is not defined

>>> mylist.extend(['123123','lalalala'])

>>> mylist

[1, 2, 0, 'abc', 4, 'haha', 'lulu', '123123', 'lalalala']

>>> mylist.extend([111111,222])

>>> mylist

[1, 2, 0, 'abc', 4, 'haha', 'lulu', '123123', 'lalalala', 111111, 222]

>>>

OVER!

