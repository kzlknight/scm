本文实例讲述了Python实现的简单读写csv文件操作。分享给大家供大家参考，具体如下：

python中有一个读写csv文件的包，直接 ` import csv ` 即可

新建test.csv

**1.写**

```python

    import csv
    with open("test.csv","w",encoding='utf8') as csvfile:
      writer=csv.writer(csvfile)
      writer.writerow(["index","a_name","b_name"])
      writer.writerows([[0,'a1','b1'],[1,'a2','b2'],[2,'a3','b3']])
    
    
```

直接使用这种写法会导致文件每一行后面会多一个空行

**解决的方法**

用python3来写wirterow时，打开文件时使用w模式，然后带上newline=''

```python

    import csv
    with open("test.csv","w",encoding='utf8',newline='') as csvfile:
      writer=csv.writer(csvfile)
      writer.writerow(["index","a_name","b_name"])
      writer.writerows([[0,'a1','b1'],[1,'a2','b2'],[2,'a3','b3']])
    
    
```

**2.读**

```python

    import csv
    with open("test.csv","r") as csvfile:
      reader=csv.reader(csvfile)
      for line in reader:
        print(line)
    
    
```

![](https://img.jbzj.com/file_images/article/201807/2018712100907952.png?201861210938)

更多Python相关内容感兴趣的读者可查看本站专题：《 [ Python操作Excel表格技巧总结
](//www.jb51.net/Special/961.htm) 》、《 [ Python编码操作技巧总结
](//www.jb51.net/Special/788.htm) 》、《 [ Python数据结构与算法教程
](//www.jb51.net/Special/663.htm) 》、《 [ Python函数使用技巧总结
](//www.jb51.net/Special/642.htm) 》、《 [ Python字符串操作技巧汇总
](//www.jb51.net/Special/636.htm) 》、《 [ Python入门与进阶经典教程
](//www.jb51.net/Special/520.htm) 》及《 [ Python文件与目录操作技巧汇总
](//www.jb51.net/Special/516.htm) 》

希望本文所述对大家Python程序设计有所帮助。

