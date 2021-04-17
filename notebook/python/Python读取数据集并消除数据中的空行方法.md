**如下所示：**

```python

    # -*- coding: utf-8 -*-
    # @ author hulei 2016-5-3
    from numpy import *
    import operator
    from os import listdir
     
    import sys
    reload(sys)
    sys.setdefaultencoding('utf8')
     
    # x,y=getDataSet_dz('iris.data.txt',4)
     
    def getDataSet(filename,numberOfFeature):  #将数据集读入内存 
     fr = open(filename)
     numberOfLines = len(fr.readlines())   #get the number of lines in the file file.readlines()是把文件的全部内容读到内存，并解析成一个list
     returnMat = zeros((numberOfLines,numberOfFeature))  #prepare matrix to return 3代表数据集中特征数目###
     classLabelVector = []      #prepare labels return 
     fr = open(filename)
     index = 0
     for line in fr.readlines():
      line = line.strip()     #strip() 参数为空时，默认删除空白符（包括'\n', '\r', '\t', ' ')
      listFromLine = line.split(',')   #split 以什么为标准分割一次 分成数组中的每个元素
      returnMat[index,:] = listFromLine[0:numberOfFeature] 
      #classLabelVector.append(int(listFromLine[-1])) #append() 方法向列表的尾部添加一个新的元素
      if listFromLine[-1] == 'Iris-setosa' :
       classLabelVector.append(1)
      elif listFromLine[-1] == 'Iris-versicolor' :
       classLabelVector.append(2)
      else:
      #elif listFromLine[-1] == 'Iris-virginica' :
       classLabelVector.append(3)
      index += 1
     return returnMat,classLabelVector
     
    def getDataSet_dz(filename,numberOfFeature): #改进版，可以消除数据中的空白行
     numberOfLines = 0
     mx = []  #将数据集 去除空行后存入
     fr = open(filename)
     for line in fr.readlines():  
      line = line.strip() 
      if line != '' : #去除空白行 
       numberOfLines+=1
       mx.append( line.split(',') )
     returnMat = zeros((numberOfLines,numberOfFeature))
     classLabelVector = [] 
     for index in range(numberOfLines) :
      returnMat[index,:] = mx[index][0:numberOfFeature] 
      if mx[index][-1] == 'Iris-setosa' :
       classLabelVector.append(1)
      elif mx[index][-1] == 'Iris-versicolor' :
       classLabelVector.append(2)
      else:
      #elif listFromLine[-1] == 'Iris-virginica' :
       classLabelVector.append(3)
     return returnMat,classLabelVector
    
```

以上这篇Python读取数据集并消除数据中的空行方法就是小编分享给大家的全部内容了，希望能给大家一个参考，也希望大家多多支持脚本之家。

