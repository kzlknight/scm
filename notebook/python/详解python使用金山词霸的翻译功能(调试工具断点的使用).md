今天试着用python获取金山词霸的翻译功能，链接在这里：  
[ ICIBA传送门 ](http://www.iciba.com/fy)  
打开之后，界面是这样的，还是比较干净的。

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010716333562.png)

按F12，打开调试工具，选择Network，找到XHR

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010716333563.png)

这里就是查看网络传输的内容。XHR就是不刷新页面的网络传输，就是常说的ajax（阿贾克斯，像是希腊神话里的名字……）。  
然后我们在翻译窗口写点儿内容，然后点翻译

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010716333564.png)

看，左边的页面出现了翻译结果，右边调试窗口出现了两条数据传输。  
两条？那我们选哪条呢？点开看看……  
哦，天哪~两条都是一样的，那我们随便选一条就可以了。  
点一下，看后面的内容

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010716333565.png)

好了，首先看到的是 **Request URL** 。嗯……就是我们要的URL了。  
先记下来……  
（你是用复制、粘贴，还是键盘上手打？难道是抄在本子上？）  
下面的 **Post** 也要记住，这是请求类型，别用成 **get** 了。  
再往下，

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010716333566.png)

上面那部分是不是很熟悉？对了，就是URL链接里的东西。不管他，URL里有了就好了。  
下面的部分，就是要提交的数据了。  
把这部分转成字典格式：

```python

    data = {
    	'from':'zh'
    	'to':'en'
    	'q':'风'
    }
```

**from** 和 **to** 这就好理解了，就是从中文到英文嘛。好，咱们不管他是中是英，都给成“ **auto** ”，让他自己去猜去……  
**q** 就是我们查的词语，那我们就用变量 **q** 表示吧，这样改后的字典就是：

```python

    data = {
    	'from':'auto'
    	'to':'auto'
    	'q':q
    }
```

提交的数据有了，那我们把请求头建立起来吧  
再让我们回到调试工具里去看下

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010716333567.png)

**headers** 就是请求头部，那里面这么多东西，我们要用什么呢？  
当然**User-Agent:**不能少了

```python

    headers = {
      'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER'
      }
```

好了，我们需要的东西都齐了，那就开始吧：  
首先是引入文件，

```python

    import requests
```

我们再到调试工具里看下返回值，看下获取的内容是什么格式的。一般返回值有json的，也有html的。

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010716333568.png)

这里把返回的结果给你了，这就是json的数据格式。  
我们用q来获取输入的文本

```python

    q = input('请输入要翻译的内容：')
```

整理后就是这样了：

```python

    import requests
    q = input('请输入要翻译的内容：')
    headers = {
     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
     }
    url = 'https://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_ciba&sign=c1b23d3ff9163427'
    data = {
     'from':'auto',
     'to':'auto',
     'q':q
      }
    
    res = requests.post(url=url,headers=headers,data=data).json()
    print(res)
```

好了，运行一遍试下

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010716333669.png)

我们输入要翻译的内容，

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010716333670.png)

不错，结果返回了，是json格式的数据，里面有我们需要的结果。  
再换个词试下……

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010716333671.png)

这是什么情况？为什么错了？  
好吧，我们在浏览器里试下

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010716333672.png)

点开看一下……

![](https://img.jbzj.com/file_images/article/202101/2021010716333673.png)

发现了吗？sign不一样……  
前一个是什么？

```python

    sign=c1b23d3ff9163427'
```

这个是

```python

    sign=4b733a5ea3f4dd5a
```

sign是动态生成的，怎么办？找生成方法！

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010716333674.png)

我们看这里……

这是运行的代码的位置，我们点进去……

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010716333675.png)

上面老长一行了，怎么办？  
看左下角的大括号了吗？点下就会有惊喜！

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010716333776.png)

好棒！已经排列整齐了……  
下面就是在这里查找sign的位置了，Ctrl+F，开始搜索

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010716333777.png)

23个结果，一个个看过去……找找哪个比较像加密的……

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010716333778.png)

看，这里是对URL进行拼接的。上面就是sign的加密方式  
sign后面拼接的是个 **r** , **r** 就是上面的一行算出来的，

```python

    r = c()("6key_cibaifanyicjbysdlove1".concat(t.q.replace(/(^\s*)|(\s*$)/g, ""))).toString().substring(0, 16);
```

你看，这个r就是用一系列字符串拼接起来的，都有什么呢？

```python

    1、"6key_cibaifanyicjbysdlove1"
    2、t.q.replace(/(^\s*)|(\s*$)/g, "")
```

第一个简单，就是一串固定的字符串  
第二个呢？t.q是什么鬼？我们来找一下……  
好，我们在这一行打个断点，就是在前面的行号上点一下。

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010716333779.png)

看见蓝色的标签了吧，这就是个断点。在运行的时候，运行到这里就会停止，然后把当前状态给你报出来。好了，断点有了，

咱们让点下翻译，让他运行下看看

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010716333880.png)

运行到断点时，停止了，并将当前的参数显示了出来。把鼠标放在q上……

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010716333881.png)

所得寺内！原来就是我们要查的词哦……  
然后就把他们拼在一起……

```python

    "6key_cibaifanyicjbysdlove1"+"云"
```

可是c()又是什么鬼？好吧，我们看下加密后的结果是什么

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010716333882.png)

这个字符串是不是很眼熟？很像md5不是吗？  
好的，那我们找一个md5加密工具试下，把加密前的字符串拼接起来

```python

    "6key_cibaifanyicjbysdlove1云"
```

然后我们放到md5加密工具里，看结果

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010716333883.png)

看这里……

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010716333884.png)

是不是这个？32位加密后的前16位！  
我们再验证一下，换一个词查下，我们查下“雨”

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010716333885.png)

我把字符串拼接好

```python

    "6key_cibaifanyicjbysdlove1雨"
```

放到md5工具里看下

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010716333886.png)

是不是一样的？好了，我们知道sign的加密规则了，那我们自己就把这个sign加密。  
要用到md5，我们就要引用新的文件了

```python

    import hashlib
```

至于md5的用法，可以看下：

```python

    import hashlib
     
     
    hash = hashlib.md5()#md5对象，md5不能反解，但是加密是固定的，就是关系是一一对应，所以有缺陷，可以被对撞出来
    hash.update(bytes('admin',encoding='utf-8'))#要对哪个字符串进行加密，就放这里
    print(hash.hexdigest())#拿到加密字符串
    # hash2=hashlib.sha384()#不同算法，hashlib很多加密算法
    # hash2.update(bytes('admin',encoding='utf-8'))
    # print(hash.hexdigest())
     
     
    hash3 = hashlib.md5(bytes('abd',encoding='utf-8'))
    ''' 如果没有参数，所有md5遵守一个规则，生成同一个对应关系，如果加了参数，
    就是在原先加密的基础上再加密一层，这样的话参数只有自己知道，防止被撞库，
    因为别人永远拿不到这个参数
    '''
    hash3.update(bytes('admin',encoding='utf-8'))
    print(hash3.hexdigest())
```

然后我们把sign的加密写一下

```python

    sign = (hashlib.md5(("6key_cibaifanyicjbysdlove1"+q).encode('utf-8')).hexdigest())[0:16]
```

再把sign拼接到url上

```python

    sign = (hashlib.md5(("6key_cibaifanyicjbysdlove1"+q).encode('utf-8')).hexdigest())[0:16]
    url = 'https://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_ciba'
    url = url+'&sign='+sign
```

然后我们运行下看看

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010716333887.png)

一切OK，没问题！  
最后我们从返回的json数据里提取出我们要的那部分

```python

    rt= res['content']['out']
    print('翻译完成：'+rt)
```

全部代码就是

```python

    import requests
    import hashlib
    
    q = input('请输入要翻译的内容：')
    
    headers = {
     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
     }
    
    
    url = 'https://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_ciba'
    sign = (hashlib.md5(("6key_cibaifanyicjbysdlove1"+q).encode('utf-8')).hexdigest())[0:16]
    url = url+'&sign='+sign
    
    data = {
     'from':'auto',
     'to':'auto',
     'q':q
      }
    
    res = requests.post(url=url,headers=headers,data=data).json()
    
    rt= res['content']['out']
    print('翻译完成：'+rt)
```

运行看下：

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010716333988.png)

OK，翻译完工！

**总结：**  
post请求的所有data都是已知的，只有url里有一个动态的sign。麻烦的地方就是查找sign的加密方式。  
一般情况下，大部分sign的加密都是使用的md5，你只要找到用来加密的字符串就可以了。  
使用断点来跟踪运行过程是比较常用的手段，但也不是全都能找到结果的。

到此这篇关于详解python使用金山词霸的翻译功能(调试工具断点的使用)的文章就介绍到这了,更多相关python金山词霸的翻译内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

