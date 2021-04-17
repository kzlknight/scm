安装显示目录功能：

```python

    pip install jupyter_contrib_nbextensions
```

配置：安装完之后需要配置 nbextension，注意配置的时候要确保已关闭 Jupyter Notebook

```python

    jupyter contrib nbextension install --user --skip-running-check
```

启动 Jupyter Notebook，勾选设置  

上面两个步骤都没报错后，启动 Jupyter Notebook，上面选项栏会出现 Nbextensions 的选项  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010711032829.png)  

点开 Nbextensions 的选项，并勾选 Hinterland  

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010711032930.png)  

自动补全功能  
按 Tab 键即可使用

到此这篇关于Jupyter Notebook添加代码自动补全功能的实现的文章就介绍到这了,更多相关Jupyter
Notebook自动补全内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

