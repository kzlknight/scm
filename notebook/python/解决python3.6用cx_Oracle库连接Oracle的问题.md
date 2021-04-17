1.Python代码

```python

    import cx_Oracle
    
    tns=cx_Oracle.makedsn('127.0.0.1','1521','mytest')
    db=cx_Oracle.connect('system','123456',tns)
    print('成功连接上oracle数据库')
    db.close();
```

2.报错信息及解决 错误1：cx_Oracle.DatabaseError: DPI-1047: Cannot locate a 64-bit Oracle
Client library

解决办法：下载对应版本的 instant client 工具包，我这里下载的是win64 12.2版本的  
https://download.oracle.com/otn/nt/instantclient/122010/instantclient-basic-
nt-12.2.0.1.0.zip  
然后，解压zip，把该文件下的所有dll文件拷贝到Python安装目录即可

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020120715014083.png)  
![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020120715014184.png)

错误2：cx_Oracle.DatabaseError: DPI-1072:…

这个错误是因为 instant client 的版本不对应，所以下载其他版本的来试试即可解决

到此这篇关于python3.6用cx_Oracle库连接Oracle的文章就介绍到这了,更多相关python3.6用cx_Oracle库连接Oracle内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

