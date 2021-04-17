标题用pycharm导入numpy包的和使用时报错：RuntimeError: The current Numpy installation
('D:\python3.6\lib\site-packages\numpy\ **init** .py

1.file→settings→project interpreter→+（建议用pychon3.6版本，我之前用3.8版本安装不上numpy），

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020120810171719.png)

2.搜索numpy,注意把下面对号点上

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020120810171720.png)

3.现在简单用numpy还是会报错：RuntimeError: The current Numpy installation
('D:\python3.6\lib\site-packages\numpy\ **init** .py  
这时pycharm的命令框输入pip install numpy==1.19.3，之后就可以用了

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020120810171721.png)

到此这篇关于解决pycharm导入numpy包的和使用时报错：RuntimeError: The current Numpy installation
(‘D:\\python3.6\\lib\\site-
packa的问题的文章就介绍到这了,更多相关pycharm导入numpy包报错内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

