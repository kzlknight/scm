###  前言  

为了往我们写好的Python代码传入参数，有很多种方法，比如使用input获取从DOS 输入的参数，又或者读取txt
文件中的字符作为参数。但为了比较规范，在windows 上我们常常用ini的配置文件进行工具配置。因此，今天我们说明下如果使用python 读取ini
文件。

###  一、后缀 ini 配置文件介绍  

我们新建一个txt 文件，将后缀改为.ini形式，在ini文件中按照分组写入需要的参数。

ini示例:

```python

    # 定义arnold分组
    [arnold]    # 分组名称
    platformName=Android #键值对，platformName为用于获取的键，Android 为可以被获取的值
    appPackage=com.romwe
    appActivity=com.romwe.SplashActivity
    
    
```

###  二、python 文件  

代码如下（示例）：

```python

    import configparser
    
    # 实例化configParser对象
    config = configparser.ConfigParser()
    # read读取ini文件,设定编解码方式
    config.read('config2.ini', encoding='GB18030')
    
    # options(section)得到该section的所有option,(option 表示分组中的**键-key**)
    print('options:', ' ', config.options('arnold'))
    # items（section）得到该section的所有键值对,(item 返回**键值对**)
    print('items:', ' ', config.items('arnold'))
    
    # get(section,option)得到section中option的值，返回为string类型 
    #(get带上分组名和对应的键，获取对应的值为str类型)
    print('get:', ' ', config.get('arnold', 'platformName'))
    
    one_string_vlaue = config.get('arnold', 'platformName')
    print("验证1：" + one_string_vlaue)
    
```

###  三、执行结果  

options: [‘platformname', ‘apppackage', ‘appactivity']

items: [(‘platformname', ‘Android'), (‘apppackage', ‘com.romwe'),
(‘appactivity', ‘com.romwe.SplashActivity')]

get: Android

验证1：Android

###  总结

到此这篇关于Python读取ini配置文件传参的文章就介绍到这了,更多相关Python读取ini配置文件传参内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

