**如何解决pycharm配置跨域不提示？**

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/202012061011151.png)

正常我们需在在如上中间件内配置跨域，但是 **2019之前的版本** 配置中间件可能需要全部自己敲出来，不会有提示，那我们不妨换个位置试试

在 **TEMPLATES** 模板的最后一行（如上图位置所示）编写跨域的中间件会出现完整提示，如若提示不准确，可多打几个单词，以更准确的提示全部中间件配置

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/202012061011153.png)

然后按住Ctrl 鼠标左键单击 **CorsMiddleware** ，就会跳转到底层文件

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/202012061011164.png)

然后就可以找到如上图所示的配置允许所有源访问的代码，只需复制以后放在文件的最下方（个人习惯）然后后面加上=True

即 **CORS_ORIGIN_ALLOW_ALL = True** 即可。

最后只需要将我们编写在TEMPLATES中的跨域中间件剪切后粘贴到MIDDLEWARE中间件的
**django.middleware.common.CommonMiddleware** 之前就可以啦！（如下图所示）

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/202012061011165.png)

到此这篇关于pycharm +
django跨域无提示解决的文章就介绍到这了,更多相关pycharm+django跨域无提示内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

