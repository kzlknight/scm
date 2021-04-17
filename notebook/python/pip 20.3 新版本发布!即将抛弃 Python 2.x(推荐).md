![](https://img.jbzj.com/file_images/article/202012/2020121611155352.png)

据 Python 软件基金会消息，Python Packaging Authority 和 pip 团队于北美时间11月30日宣布发布 pip
20.3版本，开发者可以通过运行 ` python -m pip install --upgrade pip ` 进行升级安装。

由于改变了默认的依赖解析器，这个版本可能具有颠覆性。pip 项目已经发布了如何测试和迁移到新解析器的用户指南。除了新的解析器，其它变化包括 Python
3.5 将在 pip 21.0 中移除，不再建议使用；pip 21.0 将在 2021 年 1 月释出，这个版本也将停止支持 Python 2.7，不再支持
Python 2.x 系列。

这是一个重要且具有颠覆性的版本，视频中的开发者们解释了这个原因：

**重点提要**

  * 颠覆项：默认情况下切换到新的依赖项解析器。注意处理可编辑安装，约束文件等方面的更改，更多内容请查阅： ` https://pip.pypa.io/en/latest/user_guide/#changes-to-the-pip-dependency-resolver-in-20-3-2020 `
  * 弃用项：抛弃对Python 3.5的支持（将在pip 21.0中移除）。 
  * 弃用项：在将来的版本中， ` pip freeze ` 命令将停止在 ` pip freeze ` 结果输出中抽取 ` pip ` 、 ` setuptools ` 、 ` distribute ` 、 ` wheel packages ` 。如果要保持之前的习惯操作，需要在命令中添加 ` \--exclude ` 选项。 
  * 新解析程序在性能，输出和报错消息方面进行了重大改进，避免了无限循环，并支持约束文件。 
  * 支持PEP 600：为支持多版本Linux发行版，兼容 ` manylinux ` 平台。 
  * 文档改进：解析程序迁移指南，快速入门指南和新的文档主题。 
  * 添加对 ` MacOS Big Sur ` 兼容性的支持 

默认情况下，新的解析器现在处于打开状态。当它接收到不兼容的指令时，它会变得更加严格且更加一致，并且会减少对某些约束文件的支持，因此某些解决方法和工作流程可能会中断。请参阅有关如何测试和迁移以及如何报告问题的指南。您可以使用已弃用的（旧）解析器，并使用
` \--use-deprecated = legacy-resolver ` 标志，直到我们在2021年1月的pip
21.0版本中将其删除。您可以在变更日志中找到更多详细信息。

**即将不再支持 Python 2.7版本**

根据计划，pip团队将在在2021年1月发布 ` pip 21.0 ` 。届时，pip将停止支持Python 2.7，并将完全停止支持 Python
2版本系列。

**更多信息请参阅**

  * GitHub issues ： ` https://github.com/pypa/pip/projects/6 `
  * pip新版本官方讨论区： ` https://discuss.python.org/t/an-update-on-pip-and-dependency-resolution/1898 `
  * 会议纪要： ` https://wiki.python.org/psf/PackagingWG#Dependency_resolver_and_user_experience_improvements_for_pip `

到此这篇关于pip 20.3 新版本发布!即将抛弃 Python 2.x的文章就介绍到这了,更多相关pip 20.3
新版本发布内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

