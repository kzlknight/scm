相信玩过爬虫的朋友都知道 ` selenium ` ，一个自动化测试的神器工具。写个 ` Python `
自动化脚本解放双手基本上是常规的操作了，爬虫爬不了的，就用自动化测试凑一凑。

虽然 ` selenium ` 有完备的文档，但也需要一定的学习成本，对于一个纯小白来讲还是有些门槛的。

最近，微软开源了一个项目叫「 ` playwright-python ` 」，简直碉堡了！这个项目是针对 ` Python `
语言的纯自动化工具，连代码都不用写，就能实现自动化功能。

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010514143860.gif)

可能你会觉得有点不可思议，但它就是这么厉害。下面我们一起看下这个神器。

###  1. Playwright介绍

` Playwright ` 是一个强大的Python库，仅用一个API即可自动执行 ` Chromium ` 、 ` Firefox ` 、 `
WebKit ` 等主流浏览器自动化操作，并同时支持以无头模式、有头模式运行。

Playwright提供的自动化技术是绿色的、功能强大、可靠且快速，支持 ` Linux ` 、 ` Mac ` 以及 ` Windows ` 操作系统。

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010514143861.jpg)

###  2. Playwright使用

安装

` Playwright ` 的安装非常简单，两步走。

```python

    # 安装playwright库
    pip install playwright
    
    # 安装浏览器驱动文件（安装过程稍微有点慢）
    python -m playwright install
```

上面两个pip操作分别安装：

  * 安装Playwright依赖库，需要Python3.7+ 
  * 安装Chromium、Firefox、WebKit等浏览器的驱动文件 

###  录制

使用 ` Playwright ` 无需写一行代码，我们只需手动操作浏览器，它会录制我们的操作，然后自动生成代码脚本。

下面就是录制的命令 ` codegen ` ，仅仅一行。

```python

    # 命令行键入 --help 可看到所有选项
    python -m playwright codegen
```

` codegen ` 的用法可以使用 ` \--help ` 查看，如果简单使用就是直接在命令后面加上url链接，如果有其他需要可以添加 `
options ` 。

```python

    python -m playwright codegen --help
    Usage: index codegen [options] [url]
    
    open page and generate code for user actions
    
    Options:
     -o, --output <file name> saves the generated script to a file
     --target <language>  language to use, one of javascript, python, python-async, csharp (default: "python")
     -h, --help    display help for command
    
    Examples:
    
     $ codegen
     $ codegen --target=python
     $ -b webkit codegen https://example.com
```

options含义：

  * -o：将录制的脚本保存到一个文件 
  * 

