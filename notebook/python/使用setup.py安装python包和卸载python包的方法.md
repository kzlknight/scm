我们使用 python setup.py install 来安 **装python包** ，但是如何卸载呢?

只能 **手动删除** 安装的文件

可以使用如下命令  

_复制代码_ 代码如下:

  
python setup.py install --record files.txt 记录安装后文件的路径

cat files.txt | xargs rm -rf 删除这些文件  

