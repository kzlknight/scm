用清理软件清理电脑垃圾的时候，发现微信存了很多图片，进入路径一看，全是以.dat为格式的文件：

![微信图片储存的格式](https://img.jbzj.com/file_images/article/202011/202011300837231.png)

尝试了直接把后缀名的.dat 改 .jpg和.png，都打不开，感觉事情没那么简单，随后立刻度娘了一下，并找到了代码。下面一步一步的来看一下。

微信客户端保存的路径一般是这样的，相信你能找到。  
F:\Users\Tencent Files\WeChat Files\wxid_\FileStorage\Image\2020-11

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202011/202011300837232.png)

就可以发现里面保存了一堆.dat格式的东西，微信保存的这个格式是16进制存储的，所以需要一个可以查看16进制的软件，如果你有就更好了，没有的话推荐一个：微软出的文本编辑器，官方链接：https://www.ultraedit.com/

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202011/202011300837233.png)

用它就可以打开我们的.dat文件。打开后就可以看到是这个样子的，注意图中标红的位置，就是这个文件的开头部分，你会发现你不管打开哪个.dat文件，开头的四个数都是一样的（你的4个数可能和我的不一样，很正常，就像微信号一样，但是你的.dat文件都是以特定的4位数字开头）。这四个数相当于一把解锁的钥匙。

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202011/202011300837244.png)

我们用能打开16进制的软件打开.jpg时，会发现.jpg的格式都是以FFD8为开头的，同样.png的也是FFD8。

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202011/202011300837245.png)

用你的4位数钥匙与FFD8做异或运算，就能得到你的解锁密码：

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202011/202011300837246.jpg)  
![在这里插入图片描述](https://img.jbzj.com/file_images/article/202011/202011300837247.jpg)  
![在这里插入图片描述](https://img.jbzj.com/file_images/article/202011/202011300837248.jpg)

异或运算的结果是一个16进制的4位数，但是我们只需要最后两位。所以最终你得到的是一个16进制的两位数。记住它，后面要用的。

准备工作到这里就结束了，接下来就是代码，用的python语言。  
需要你改的地方有三个（代码中有相应的注释）：  
两个路径：将.dat的路径、你要保存解密后文件的路径都改为你自己的；  
一个值：用你自己的密码（两位数）代替我的密码。

```python

    import os
    
    def imageDecode(dat_dir,dat_file_name):
     dat_read = open(dat_dir, "rb")
     if not os.path.exists(target_path):
     os.makedirs(target_path)
     out=target_path+"\\"+dat_file_name+".png"
     png_write = open(out, "wb")
     for now in dat_read:
     for nowByte in now:
     newByte = nowByte ^ xor_value
     png_write.write(bytes([newByte]))
     dat_read.close()
     png_write.close()
    
    def findFile(dat_path):
     fsinfo = os.listdir(dat_path)
     for dat_file_name in fsinfo:
     temp_path = os.path.join(dat_path, dat_file_name)
     if not os.path.isdir(temp_path):
     #print('文件路径: {}' .format(temp_path))
     imageDecode(temp_path,dat_file_name)
     else:
     pass
      
    if __name__=='__main__':
    
     # 修改.dat文件的存放路径
     dat_path = r'F:\Users\Tencent Files\WeChat Files\wxid\FileStorage\Image\2020-04'
     
     # 修改转换成png图片后的存放路径
     target_path = r'F:\Users\Tencent Files\WeChat Files\image'
     
     # 修改加密的异或值,比如说我的异或值最后两位是B2，则xor_value = 0xB2，0x表示16进制
     xor_value = 0xB2
     
     findFile(dat_path)
     print("end")
```

运行后，可以看到输出都是一个有一个图片，直观明了，就可以保存自己想要的图片，清理不需要的：

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202011/202011300837259.png)

最后，我对比了一下解密前后的空间占用情况，占用空间的完全相同，不知道为啥腾讯要以.dat文件存储。

![左图为.dat,右图为.png](https://img.jbzj.com/file_images/article/202011/2020113008372510.png)

参考： [ https://www.jb51.net/article/200924.htm
](https://www.jb51.net/article/200924.htm)

到此这篇关于使用python将微信image下.dat文件解密为.png的方法的文章就介绍到这了,更多相关python 微信image
.dat文件解密为.png内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

