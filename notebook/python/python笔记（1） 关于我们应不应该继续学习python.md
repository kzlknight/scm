以前面试的时候会被问到，linux熟不熟呀？对于这种问题：我总会尴尬地回答，“额..了解一点”。  
  
然而，我大学毕业的时候，连linux的虚拟机都没装过，更别提系统熟不熟悉了。虽然我了解一点这个系统可以完全通过命令来操作。后来工作了，有时候写点代码，svn提交上去，服务器是Linux的，自己也是在windows上跑跑客户端。记得有个项目，要求用shell来启动java程序，你知道那时候我是怎么做的吗？把他们的shell拿来，问哪几个地方要改的，然后改下要启动java类的路径。ok了，完全不去理解里面的意思。到最后又一次面试的时候，不得不坦白：不是太了解Linux命令。  
  
有人可能会说：Linux命令没什么难啊。花几天时间就好了。现在的我也会这么和完全不懂Linux的朋友这么说。可是如果我不跨出学习命令的第一步。我未来的很长一段时间都不得不在面试的时候再一次尴尬。  
回到正题，我们到底该不该去学习现在看来没什么用而确实是不错的东西呢？  
我的回答是：如果你的确是有余力，并愿意向自己投资的话，我觉得是有必要的。  
1，这种额外的学习会让你的周末变得充实。  
2，当学习到一定程度的时候，会对事物有新的看法。  
3，面试的时候，你多了一块筹码。  
4，有一个理论：学习的越多，知道自己不知道的越多。（知识面越广，你所看到的世界就越大！）  
  
就像情歌里唱的那样：”我们一直都忘了要到一座桥，到对方心里瞧一瞧“，我想我们是不是也忘了去到一座桥，去别的地方瞧一瞧呢！呵呵  
  
所以让我们一起进入PYTHON世界吧！  
  
python笔记（1）  
  
关于Python，如果你要学习，建议大家查看一下网站：（因为本人也是刚刚决定收集点零碎时间来学习下它，推荐可能并不是最好的）  
  
[ http://book.huihoo.com/dive-into-python/5.4_zh-cn/html/toc/index.html
](http://book.huihoo.com/dive-into-python/5.4_zh-cn/html/toc/index.html) 《Dive
to python》  
[ http://docs.python.org/ ](http://docs.python.org/)  
[ http://woodpecker.org.cn/ ](http://woodpecker.org.cn/)  
[ http://code.google.com/intl/zh-CN/edu/languages/google-python-
class/introduction.html ](http://code.google.com/intl/zh-
CN/edu/languages/google-python-class/introduction.html)  
  
刚接触python我觉得很棒，因为安装个软件，马上就能来个HelloWorld！  
也许我们早就过了兴奋的年纪，事实上，我是想说python绝对是让你放轻松学习的语言。  
  
**1，函数声明用 def**  
  

_复制代码_ 代码如下:

  
def buildConnectionString(params):  

  
  
**2，导入模块：import  
  
**

_复制代码_ 代码如下:

  
import odbchelper  

  
  
在导入模块时是python编译器去自己的环境变量制定的路径路去找这个模块，如果要导入的模块是自定义的路径下，就必须把这个路径先放进环境变量中去。  

_复制代码_ 代码如下:

  
import sys  
sys.path.append('/my/new/path')  

  
**3，if_else语句** ：（python通过缩进来控制代码块，代替了java中的“{}”）  

_复制代码_ 代码如下:

  
if n > 1:  
return n * fib(n - 1)  
else:  
print 'end of the line'  
return 1  

  
**4，内置数据类型List：**  
List li = ["a", "b", "mpilgrim", "z", "example"]  
  
用“[]”包起来。  
  
A.用for var in list，可以遍历一个list。在遍历的时候不要试着增加和删除元素哦！  

_复制代码_ 代码如下:

  
squares = [1, 4, 9, 16]  
sum = 0  
for num in squares:  
sum += num  
print sum ## 30  

  
B.用in来判断一个元素是否在list中：  

_复制代码_ 代码如下:

  
list = ['larry', 'curly', 'moe']  
if 'curly' in list:  
print 'yay  

  
C.list其他的方法：  

_复制代码_ 代码如下:

  
list.append(elem) -- adds a single element to the end of the list. Common
error: does not return the new list, just modifies the original.  
list.insert(index, elem) -- inserts the element at the given index, shifting
elements to the right.  
list.extend(list2) adds the elements in list2 to the end of the list. Using +
or += on a list is similar to using extend().  
list.index(elem) -- searches for the given element from the start of the list
and returns its index. Throws a ValueError if the element does not appear (use
"in" to check without a ValueError).  
list.remove(elem) -- searches for the first instance of the given element and
removes it (throws ValueError if not present)  
list.sort() -- sorts the list in place (does not return it). (The sorted()
function shown below is preferred.)  
list.reverse() -- reverses the list in place (does not return it)  
list.pop(index) -- removes and returns the element at the given index. Returns
the rightmost element if index is omitted (roughly the opposite of append()).  

  
D.其他关于list的例子：  

_复制代码_ 代码如下:

  
list = ['larry', 'curly', 'moe']  
list.append('shemp') ## append elem at end  
list.insert(0, 'xxx') ## insert elem at index 0  
list.extend(['yyy', 'zzz']) ## add list of elems at end  
print list ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']  
print list.index('curly') ## 2  
  
list.remove('curly') ## search and remove that element  
list.pop(1) ## removes and returns 'larry'  
print list ## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']  

  
本文纯粹的目的是想让更多的人去学习他们可能因各种借口拒绝学习的东西。  
希望你能被我我的鼓动，而有所行动哦！

