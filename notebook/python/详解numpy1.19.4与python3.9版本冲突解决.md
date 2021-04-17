###  一、问题分析

runtimeError: package fails to pass a sanity check解决方法如下：  
解决一：使用python3.9和numpy1.19.4时会发生此错误，卸载numpy1.19.4并安装1.19.3, 即可解决此问题  
使用 ` pip uninstall numpy `  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020121515583392.png)  

再安装numpy1.19.3版本即可，使用如下命令  

卸载命令： ` pip uninstall numpy `

一般命令： ` pip install numpy == 1.19.3 `

我用的命令： ` pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-
host pypi.tuna.tsinghua.edu.cn numpy==1.19.3 `

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020121515583393.png)  

注：我在这儿使用的镜像下载，但是由于我之前可能没有把python32位卸载干净，所以可能导致了版本冲突，使用这个命令就可以下载库。但是这个命令就是万能的。

###  二、查看你下载的库，用如下命令  

```python

    pip list
```

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020121515583394.png)

到此这篇关于详解numpy1.19.4与python3.9版本冲突解决的文章就介绍到这了,更多相关numpy1.19.4与python3.9版本冲突内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

