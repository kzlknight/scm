因为Python是自带文档，可以通过help函数来查询每一个系统函数的用法解释说明。一般来说，关键的使用方法和注意点在这个系统的文档中都说的很清楚。我试图在网上找过系统文档的中文版的函数功能解释，但是都没有找到，所以我决定将就使用英文版的系统自带的函数解释来学习。

如果你想进行Tkinter和wxPython编程，想要知道一般的widget的使用方法和属性介绍，英文又不是太好的话，我推荐你，你可以去看看《Python与Tkinter编程》这本书，里面392页到538页的附录B和附录C选择了常用的函数和近乎所有的属性进行介绍，精彩不容错过。

我上面提到的这个工具很快做好了。可以把没有查询过的函数进行查询，并保存关键字key和查询结果info，便于下次直接从列表list中翻出来看；要是发现没有查过，则手动添加到列表list――就是这样一个简单的小工具。一切看上去都很顺利。但是问题也来了：英文的info打开后，解释里面有的单词不知道含义，查完单词之后想写在info里面，保存之后可以下次直接从硬盘打开看。但是在英文info中输入中文，保存过程中就出现了解码不了的问题，也就是解码到中文部分就弹出下面这个错误来：

UnicodeEncodeError: 'ascii' codec can't encode character u'\u6211' in position
61: ordinal not in range(128)  
  
其中的61这个位置是弹性的，就是info中加入了中文的那个位置。这个错误基本一直都存在，也就是当我想要把修改过后的info写入文件的时候：

_复制代码_ 代码如下:

  
fp = open('tt.txt','w')  
fp.write(info.encode("UTF-8")) # 此处错误  
fp.close()  

这三行本身看上去没有错误。但是就是在中间这行代码处出现了错误。难道是encode的方式不对？我有尝试了很多种编码，如ANSI、UTF-8、SHIFT_JIS、GB2312、GBK等编码，发现都不行。于是我就糊涂了。  
  
现在我已经知道为什么错误了。问题就在于修改之后的info这个字符串变量。info中的数据是我从系统中通过help函数查到的字串（也就是原始的纯英文的info）加上我手动输入的中文得到的一个综合的字符串。在我从系统中查询系统文档时，我对原始info进行了如下保存：  

_复制代码_ 代码如下:

  
fp = open('tt.txt','w')  
fp.write(info)  
fp.close()  

  
注意，错就错在直接将原始info直接写入到文件中。这样写之后的编码方式大家知道是什么吗？你打开tt.txt，查看编码方式将会知道，其编码方式是ANSI格式。于是错误就是这样产生的：我查询关键字key，将这个ANSI格式的字串info读到控件中显示，然后我有手动的添加了UTF-8格式的中文字符，于是通连起来形成的字符串info，就是一个混乱而具有多种编码方式的字符串info，系统怎么write都无法只使用一种编码方式将这个混合字串info再次写到tt.txt中去。  
  
所以，结论就是：当你在内存中操作时，你可以随意的不管编码方式是什么，系统会自动的按照具体情况进行判断。但是你如果要用到中文字符，并且还要通过文件的方式去暂时保存数据或者字串的话，请你一定要在第一次写文件的时候用utf-8的格式写进去，也就是如下的方式：

```python

    fp = open('tt.txt','w') 
    fp.write(info.encode("UTF-8")) 
    fp.close() 
```

这将会保证你下次读出来之后不用转换编码方式就可以直接打印和显示，即使是作为控件文本也没有问题。一定要注意这一点。

问题找到了，下面进行一些其他的讨论。

有的人说，只要使用了# -*- coding：utf-8 -*-不就行了吗？其实不然。

通过我的测试（我使用IDLE(Python2.5.4 GUI）编译器。【1】无论我开头用不用# -*- coding：utf-8
-*-，还是软件中是不是设置了使用默认的utf-8编码方式，中文在控件和文件之间的使用都是没有问题的。【2】info='中文';
这样的操作都是可以的。读的时候使用一般的读法就可以了。原因我想是因为编译器升级，解决了中文显示和使用的问题，早期中文语言不能够使用的情况现在已经不存在了。

```python

    #coding=utf-8 
    try: 
    JAP=open("jap.txt","r") 
    CHN=open("chn.txt","r") 
    UTF=open("utf.txt","w") 
    
    jap_text=JAP.readline() 
    chn_text=CHN.readline() 
    #先decode成UTF-16,再encode成UTF-8 
    jap_text_utf8=jap_text.decode("SHIFT_JIS").encode("UTF-8") 
    #不转成utf-8也可以 
    chn_text_utf8=chn_text.decode("GB2312").encode("UTF-8") 
    #编码方式大小写都行utf-8也一样 
    UTF.write(jap_text_utf8) 
    UTF.write(chn_text_utf8) 
    UTF.close() 
    except IOError,e: 
    print "open file error",e 
```

这是我从 [ //www.jb51.net/article/26542.htm ](//www.jb51.net/article/26542.htm)
中《学习python处理python编码》文章中摘录的代码。这里做一下解释，上面的jap_text_utf8和chn_text_utf8都要保证是机器默认的编码方式，或者utf-8编码方式，最重要的就是要保持一致。通过统一的编码为utf-8后，就可以写入一个文件中，再次读出使用都没有问题。读的时候使用下面的普通方式即可：  

_复制代码_ 代码如下:

  
filen = open('tt.txt')  
info = filen.read()  
print info  

  
另外。有人使用了下面这种方式来编码和转换：

```python

    import sys 
    reload(sys) 
    sys.setdefaultencoding('utf8') 
    
    def ConvertCN(s): 
    return s.encode('gb18030') 
    
    def PrintFile(filename): 
    f = file(filename, 'r') 
    for f_line in f.readlines(): 
    print ConvertCN(f_line) 
    f.close() 
    
    if __name__ == "__main__": 
    PrintFile('1.txt') 
    print ConvertCN("\n****** 按任意键退出! ******") 
    print sys.stdin.readline()
```

通过我的测试，这种方式是不可行的。第二行如果去掉，第三行的setdefaultencoding函数将会无效；如果保留第二行，第三行和以后的代码都得不到执行（虽然不报错）。这种方式是否可行请大家试试看。

另外，《python 中文乱码 问题深入分析》 [ //www.jb51.net/article/26543.htm
](//www.jb51.net/article/26543.htm)
一文中讲到了很多文本如何编码的问题，令我大开眼界。文本编码的原理：原来就是在文本开头处添加适当的注释符号来表示内部的编码方式，于是解释器就会以某种对应的规则去按照某种步长的字节或者灵活的方式去翻译字节，得到原文，翻译的步长和规则完全是开头的说明处对应的。所以，如果你正文是单个字节的编码方式，那么你就可以在你的编码最前头加上一个合适的规则，告诉别人如何翻译你的被编码文本即可。其中BOM_UTF_8等文本末尾的知识也是很有趣的，类似的还有BOM_UTF_16等等，不同的编码方式文末的符号不同，大家可以注意一下。

