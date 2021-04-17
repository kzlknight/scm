今天搞了一天的文本处理，发现python真的太适合做数据处理了。废话不多说，一起学习吧！

**1.我的原始数据是这样的，如图**

![](https://img.jbzj.com/file_images/article/202012/202012091017195.png)

**2.如果要提取每行含有pass的字符串，代码如下：**

```python

    import re
    
    filepath = "E:/untitled1/analyze_log/test.log"
    txt = open(filepath, "r").read()
    
    result=""
    test_text = re.findall("..............+pass", txt)#取出每行含有pass的文本
    result = result +'\n'.join(test_text)#换行输出
    print(result)
    
```

**3.执行上面代码，可以取出每行含有pass的文本，如图：**

![](https://img.jbzj.com/file_images/article/202012/202012091017196.png)

**4.其实我真正要提取的是每行类似上图红色框内的字符串，代码实现如下：**

```python

    import re
    
    filepath = "E:/untitled1/analyze_log/test.log"
    txt = open(filepath, "r").read()
    
    result=""
    test_text = re.findall("..............+pass", txt)#取出每行含有pass的文本
    result = result +'\n'.join(test_text)#换行输出
    del_num = re.sub("\d+ ", "", result)#去掉每行行首的数字
    del_awake = del_num.replace("awake", "")#去掉awake
    del_commd = del_awake.replace("commd", "")#去掉commd
    del_string1 = re.sub("-a+\d\d\d\d-\d.wav", "", del_commd)#去掉-a0023-1.wav类型的字符串
    del_string2 = re.sub("-a+\d\d\d\d.wav", "", del_string1)#去掉-a0016.wav类型的字符串
    print(del_string2)
    
```

**5.执行上面代码，可以取出最后我需要的文本，如图：**

![](https://img.jbzj.com/file_images/article/202012/202012091017197.png)

**6.拓展**

![](https://img.jbzj.com/file_images/article/202012/202012091017208.png)

**7.示例代码**

```python

    import re
    
    str = 'Hello123/World 45_?6bye'
    result1 = re.findall('\d',str)#\d匹配任何十进制数
    result2 = re.findall('\d+',str)#\d+可匹配一位或多位数字使用
    result3 = re.findall('\D',str)#\d匹配非数字字符任何十进制数
    result4 = re.findall('\w',str)#\w匹配任何字母数字字符，包括下划线在内
    result5 = re.findall('\W',str)#\W匹配非任何字母数字字符，包括下划线在内
    result6 = re.findall('\s',str)#\s匹配任何空白字符
    result7 = re.findall('\S',str)#\S匹配非任何空白字符
    result8 = re.findall('\AHello',str)#\A仅匹配字符串开头
    result9 = re.findall('bye\Z',str)#\Z仅匹配字符串结尾
    print(result1)
    print(result2)
    print(result3)
    print(result4)
    print(result5)
    print(result6)
    print(result7)
    print(result8)
    print(result9)
    
```

接下来会更几篇关于文本处理的博客，一边学习一边记笔记。加油！

到此这篇关于使用Python提取文本中含有特定字符串的文章就介绍到这了,更多相关Python提取文本特定字符串内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

