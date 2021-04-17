Problem:

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/20201204155438104.png)

Solution：

参考stackoverflow给出的解决方案：https://stackoverflow.com/questions/65085956/pycharm-
venv-failed-no-such-option-build-dir

①

确定自己pycharm里面python解释器的路径：

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/20201204155439105.png)

②

在cmd里面输入：自己解释器的路径 + -m pip install pip==20.2.4

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/20201204155439106.png)

(其中可能会有网络问题提示Retry，要多尝试几次)

_这里做法的主要原因是：pycharm依赖于 --build-
dir来安装包，但是这在最新版的pip中被移除了，所以解决办法就是先将pip的版本回退到20.2.4之后再升级回来就好了_

③

导入Flask包成功：

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/20201204155439107.png)

到此这篇关于pycharm 2020.2.4 pip install Flask 报错 Error：Non-zero exit
code的文章就介绍到这了,更多相关pycharm 2020.2.4 pip install Flask
报错内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

