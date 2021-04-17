比如代码  
  
binfo = {'name':'jay','age':20,'python':'haha'}  
  
print binfo.pop('name')#pop方法删除键，并且返回键对应的值  
  
print binfo##输出结果：{'python': 'haha', 'age': 20}  
  
del binfo['python']##内置方法删除元素  
  
print binfo##输出结果：{'age': 20}

