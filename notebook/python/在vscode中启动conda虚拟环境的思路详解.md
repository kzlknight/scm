问题：cudatoolkit cudnn 通过conda 虚拟环境安装，先前已经使用virtualenv安装tf，
**需要在conda虚拟环境中启动外部python虚拟环境**

思路：conda prompt

![](https://img.jbzj.com/file_images/article/202012/2020122510474522.png)

即将 [虚拟环境位置] 以参数形式传入 [activate.bat]

**VSOCDE中的设置**

![](https://img.jbzj.com/file_images/article/202012/2020122510474523.png)

添加以下语句

```python

    {
      "terminal.integrated.shell.windows": "C:\\Windows\\System32\\cmd.exe", #选用cmd作为命令行窗口
      "terminal.integrated.shellArgs.windows": [
        "/k",
        "C:\\Users\\PC\\miniconda3\\Scripts\\activate.bat C:\\Users\\PC\\miniconda3\\envs\\tfcuda101" #此处修改为你conda虚拟环境文件夹位置
      ],
      "python.pythonPath": "c:\\Users\\PC\\tensorflow2\\Scripts\\python.exe", #选择virtualenv下的python路径
    }
```

搞定，下次进入相关项目自动加载conda环境与virtualenv环境

![](https://img.jbzj.com/file_images/article/202012/2020122510474524.png)

验证成功加载cuda库：

```python

    python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
```

![](https://img.jbzj.com/file_images/article/202012/2020122510474525.png)

到此这篇关于在vscode中启动conda虚拟环境的思路详解的文章就介绍到这了,更多相关vscode中启动conda虚拟环境内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

