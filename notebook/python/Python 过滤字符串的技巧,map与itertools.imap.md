具体的实例  
我们需要在目录中遍历，包括子目录（哈哈），找出所有后缀为：rmvb ，avi ，pmp 的文件。（天哪？！你要干什么？这可是我的隐私啊～～）  

_复制代码_ 代码如下:

  
import os  
  
def anyTrue(predicate, sequence):  
return True in map(predicate, sequence)  
  
def filterFiles(folder, exts):  
for fileName in os.listdir(folder):  
if os.path.isdir(folder + '/' + fileName):  
filterFiles(folder + '/' + fileName, exts)  
elif anyTrue(fileName.endswith, exts):  
print fileName  
  
exts = ['.rmvb', '.avi', '.pmp']  
filterFiles('/media/Personal/Movie', exts)  

  
输出结果  
来看看有什么好东东：  
[66影视www.66ys.cn]迷失第四季04.rmvb  
[迷失.第4季].Lost.S04E00.rmvb  
[迷失Lost第四季][第02集][中文字幕].rmvb  
《迷失Lost第四季》第05集[中文字幕].rmvb  
《迷失Lost第四季》第06集[中文字幕].rmvb  
《迷失Lost第四季》第07集[中文字幕].rmvb  
天赐第2季01.rmvb  
天赐第2季02.rmvb  
天赐第2季03.rmvb  
天赐第2季04.rmvb  
天赐第2季05.rmvb  
影视帝国(bbs.cnxp.com).美丽心灵.A.Beautiful.Mind.2001.CD1.rmvb  
( ... 太多了，不要全输出来吧～～)  
  
  
扩展  
CookBook一书中，提供的是itertools.imap来实现对字符串的过滤。imap和map不同的是，imap返回的是一个iteration对象，而map返回的是一个list对象。代码如下：  
import itertools  
def anyTrue(predicate, sequence):  
return True in itertools.imap(predicate, sequence)  
def endsWith(s, *endings):  
return anyTrue(s.endswith, endings)  
imap 等价于：  
def imap(function, *iterables):  
iterables = map(iter, iterables)  
while True:  
args = [i.next() for i in iterables]  
if function is None:  
yield tuple(args)  
else:  
yield function(*args)

