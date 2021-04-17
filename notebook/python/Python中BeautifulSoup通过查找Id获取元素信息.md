比如如下的html

![](https://img.jbzj.com/file_images/article/202012/2020120710151720.png)

他是在span标签下的class为name，id为is-like-span

这样就可以通过这样的代码进行方法：

![](https://img.jbzj.com/file_images/article/202012/2020120710151721.png)

```python

    isCliked = soup.find('span', id = 'is-like-span'
```

通过这种方式去获取即可，如果里面的为字符串则调用get_text()即可

到此这篇关于Python中BeautifulSoup通过查找Id获取元素信息的文章就介绍到这了,更多相关BeautifulSoup
Id获取元素信息内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

