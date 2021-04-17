###  介绍  

我编写了一个快速且带有斑点的python脚本，以可视化nmap和masscan的结果。它通过解析来自扫描的XML日志并生成所扫描IP范围的直观表示来工作。以下屏幕截图是输出示例：

![](https://img.jbzj.com/file_images/article/202012/2020122914043439.jpg)

由于缺少更好的词，我将从现在开始将输出称为地图。每个主机由一个彩色正方形表示。覆盖地图大部分内容的浅蓝色方块表示主机处于脱机状态（或仅未响应masscan的SYN。）其他彩色方块表示处于联机状态且具有开放端口的主机。正方形的颜色从蓝色到红色。正方形越红，表示主机上打开的端口越多。将鼠标悬停在每个方块上，将在工具提示中显示IP地址和打开的端口。

该工具非常有用，因为它使您可以大致了解IP范围，而不必在日志文件中拖网。它使您可以轻松查看扫描中的主机块。该工具可以从github下载，但是我将在下面描述代码的工作方式。

###  如何使用

首先，我要说这段代码没有经过优化。我已经针对/ 21的日志运行了代码，并花费了大约40秒钟来生成输出映射。

第一步是查找运行扫描的IP地址范围。由于扫描命令未保存在日志文件中，因此这真是一个痛苦。因此，我们必须根据最低和最高IP结果来计算范围。我们从扫描中解析XML文件，并将扫描到的每个IP地址附加到名为ipList的列表中

```python

    ipList = []
    for event, element in etree.iterparse('output.xml', tag="host"):
     for child in element:
      if child.tag == 'address':
      ipList.append(child.attrib['addr'])
```

然后，我们遍历ipList并将每个八位位组分成单独的列表，分别称为firstOctetRange，secondOctetRange，thirdOctetRang和forwardOctetRange。

```python

    firstOctetRange = []
    secondOctetRange = []
    thirdOctetRange = []
    forthOctetRange = []
    bitDelimeter = 0
    startingIP = 0
    endingIP = 0
    for ip in ipList:
     binaryOctet = ''
     octets = ip.split('.')
     firstOctetRange.append(int(octets[0]))
     secondOctetRange.append(int(octets[1]))
     thirdOctetRange.append(int(octets[2]))
     forthOctetRange.append(int(octets[3]))
```

然后，我们将每个结果的每个八位位组与另一个结果的相同八位位组进行比较，以确定值发生变化的八位位组。例如。如果前两个八位位组始终相同。我们知道扫描的CIDR表示法将大于/
16。我使用了变量bitDelimeter来存储CIDR表示法截取的八位字节的值。

```python

    if min(firstOctetRange) != max(firstOctetRange):
     bitDelimeter = 0
    elif min(secondOctetRange) != max(secondOctetRange):
     bitDelimeter = 1
    elif min(thirdOctetRange) != max(thirdOctetRange):
     bitDelimeter = 2
    elif min(forthOctetRange) != max(forthOctetRange):
     bitDelimeter = 3
```

