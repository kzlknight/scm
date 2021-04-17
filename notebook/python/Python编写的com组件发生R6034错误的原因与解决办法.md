解决该问题的方法可以为调用本程序的exe文件建立一个合适的manifest文件，指定正确的msvcr90.dll版本即可，具体可参照 [
https://www.jb51.net/article/35219.htm
](https://www.jb51.net/article/35219.htm)  
  
**ps:可以使用mt.exe进行导出或合并manifest资源到exe或者dll文件。  
**  
查看manifest的方法：mt -inputresource:pythoncom27.dll;#2 -out:sss.txt  
  
**合并manifest到dll的方法：  
  
**

