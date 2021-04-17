_复制代码_ 代码如下:

  
def ReadOnlyObject(**args):  
dictBI = {}  
args_n = []  
for name, val in args.items():  
dictBI[name] = val  
args_n.append(name)  
dictBI['__slots__'] = args_n  
return type('ReadOnlyObject', (object,), dictBI)()  

