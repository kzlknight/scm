但是，当一本书学过之后，对一般的技术和函数都有了印象，突然想要查找某个函数的实例代码时，却感到很困难，因为一本书的源代码目录很长，往往有几十甚至上百个源代码文件，想要找到自己想要的函数实例谈何容易？  
  
所以这里就是要将所有源代码按照目录和文件名作为标签，全部合并到一处，这样便于快速的搜索。查找，不是，那么查找下一个……于是很快便可以找到自己想要的实例，非常方便。当然，分开的源代码文件依然很有用，同样可以保留。合并之后的源代码文件并不大，n*100KB而已，打开和搜索都是很快速的。大家可以将同一种编程语言的所有实例通过这种方法全部合并为一个文件，搜索的效率就会大大提高。  
  
注意：保存代码之后，将源文件复制到目录下，同一目录下的所有目录和其子目录都会被搜索；你可以加上后缀限定，只获取某种格式的文件的内容即可；源代码如下，请复制后保存：  

_复制代码_ 代码如下:

  
# -*- coding: utf-8 -*-  
  
import os,sys  
info = os.getcwd()  
fout = open('note.tpy', 'w') # 合并内容到该文件  
  
def writeintofile(info):  
fin = open(info)  
strinfo = fin.read()  
# 利用##作为标签的点缀，你也可以使用其他的  
fout.write('\n##\n')  
fout.write('## '+info[-30:].encode('utf-8'))  
fout.write('\n##\n\n')  
fout.write(strinfo)  
fin.close()  
  
  
for root, dirs, files in os.walk(info):  
if len(dirs)==0:  
for fl in files:  
info = "%s\%s" % (root,fl)  
if info[-2:] == 'py': # 只将后缀名为py的文件内容合并  
writeintofile(info)  
  
fout.close()  

  
如果你不想合并内容，只想获得一个文件名的清单文件，也可以。这里给你代码。例如，有的作者就会使用这个功能为自己生成一个源代码文件清单，很实用。  
  
源代码为：  

_复制代码_ 代码如下:

  
# -*- coding: utf-8 -*-  
'''  
本程序自动搜索指定的目录,  
打印所有文件的完整文件名到指定的文件中  
'''  
import os,sys  
export = ""  
i=1  
for root, dirs, files in os.walk(r'..'):  
#r'.'表示当前目录中的所有清单  
#..表示平行的其他目录,多出很多内容  
export += "--%s--\n%s\n\n%s\n\n" % (i,root,'\n'.join(files))  
i=i+1  
fp = open('cdcfile-4.txt', 'w')  
fp.write(export)  
fp.close()  

