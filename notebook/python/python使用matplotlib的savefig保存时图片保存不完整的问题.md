python使用matplotlib的savefig保存时图片保存不完整的问题

使用如下形式的代码进行图片保存时，保存的图片出现不完整的情况，如图1所示。

```python

    plt.colorbar()
    plt.savefig(title)
    plt.show()
```

![](https://img.jbzj.com/file_images/article/202101/2021010809400910.png)

一开始我以为是图片大小比例不对，因而通过以下代码进行修改：

```python

    plt.figure(figsize=(10,8))
```

但是无论怎么修改，始终会出现这种情况，要么是下面显示不完全，要么就是左边显示不完全。这是为什么呢？

这是因为 ` colorbar ` 会占据右边位置，导致输出的图片偏左。

摸索了半天，最终解决方法是，在 ` savefig（） ` 的参数中添加 ` bbox_inches = 'tight' ` 。

```python

    plt.colorbar()
    plt.savefig(title, dpi=300, bbox_inches = 'tight')
    plt.show()
```

![](https://img.jbzj.com/file_images/article/202101/2021010809400911.png)

完美解决！！！

到此这篇关于python使用matplotlib的savefig保存时图片保存不完整的问题的文章就介绍到这了,更多相关matplotlib
savefig保存图片内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

