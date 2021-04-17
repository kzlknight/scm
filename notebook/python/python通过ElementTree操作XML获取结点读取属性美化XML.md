1.引入库  
需要用到3个类，ElementTree，Element以及建立子类的包装类SubElement  
from xml.etree.ElementTree import ElementTree  
from xml.etree.ElementTree import Element  
from xml.etree.ElementTree import SubElement as SE

2.读入并解析  
tree = ElementTree(file=xmlfile)  
root = tree.getroot()  
读入后，tree是ElementTree的类型，获取xml根结点使用getroot()方法；

XML示例文件：  

_复制代码_ 代码如下:

  
<item sid='1712' name = '大CC' >  
<a id=1></a>  
<a id=2></a>  
</item>  

3.获取儿子结点  
查找Element的所有子结点:  

_复制代码_ 代码如下:

  
AArry = item.findall('a')  
也可使用getchildren()：  
childs = item.getchildren()  
for subItem in childs:  
print subItem.get('id')  

4.插入儿子结点  
方法一：  

_复制代码_ 代码如下:

  
item = Element("item", {'sid' : '1713', 'name' : 'ityouhui'})  
root.append(item)  

  
方法二：  

_复制代码_ 代码如下:

  
SE(root,'item',{'sid':'1713','name':'ityouhui'})  

  
法一的好处是插入之后可以对item继续操作。法二是写法上简单，其中SE就是SubElement,在引入处做了声明；

5.操作属性  
获取Element的某个属性值（eg：获取item的 name）  

_复制代码_ 代码如下:

  
print root.find('item/name').text  
print item.get('name')  

  
获取Element所有属性  

_复制代码_ 代码如下:

  
print item.items() # [('sid', '1712'), ('name', '大CC')]  
print item.attrib # {'sid': '1712', 'name': '大CC'}  

6.美化XML  
在写入之前，传入root调用此函数，写入的XML文件格式整齐美观：  

_复制代码_ 代码如下:

  
indent(root)  
book.write(xmlfile,'utf-8')  

_复制代码_ 代码如下:

  
## Get pretty look  
def indent( elem, level=0):  
i = "\n" + level*" "  
if len(elem):  
if not elem.text or not elem.text.strip():  
elem.text = i + " "  
for e in elem:  
indent(e, level+1)  
if not e.tail or not e.tail.strip():  
e.tail = i  
if level and (not elem.tail or not elem.tail.strip()):  
elem.tail = i  
return elem  

