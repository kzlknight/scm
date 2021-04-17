###  什么是运行时配置（Runtime Configuration，rc）  

Matplotlib使用matplotlibrc配置文件来自定义图形的各种属性，称之为rc配置或rc参数(rcParams)。通过rc参数可以修改matplotlib绝大多数属性的默认值，包括窗体大小、每英寸的点数、线条宽度、颜色、样式、坐标轴、坐标和网络属性、文本、字体等。

###  运行时配置的默认值  

运行时配置的默认值存放在默认的matplotlibrc文件中。

**matplotlibrc文件与rcParams的关系**  

rcParams是RcParams类的实例，结构类似于字典，用于处理matplotlib的默认运行时配置，它是matplotlib模块的全局变量。当导入matplotlib模块时，matplotlibrc文件中的所有rc
参数存储在matplotlib.rcParams中。

源码如下：

```python

    rcParamsDefault = _rc_params_in_file(
      cbook._get_data_path("matplotlibrc"),
      # Strip leading comment.
      transform=lambda line: line[1:] if line.startswith("#") else line,
      fail_on_error=True)
    dict.update(rcParamsDefault, rcsetup._hardcoded_defaults)
    rcParams = RcParams() # The global instance.
    dict.update(rcParams, dict.items(rcParamsDefault))
    dict.update(rcParams, _rc_params_in_file(matplotlib_fname()))
    
```

###  修改运行时配置参数的方法  

通过rc文件：修改默认 matplotlibrc文件或者指定自定义rc文件。  

修改默认 matplotlibrc文件。  

指定自定义的rc文件。  

```python

    matplotlib.rc_file(fname, *, use_default_template=True)
    
```

通过rcParams对象：直接修改rcParams对象。这种方法比较灵活，修改的方法有以下三种：

  * matplotlib.rc(group, **kwargs) 
  * rcParams[group.params] 
  * rcParams.update() 

第一、二种方法是等价的，第三种方法不支持缩写和分组。  

```python

      #第一种方法1
      rc('lines', linewidth=2, color='r')
      #第一种方法2
      font = {'linewidth' : 2,
        'color'  : 'r'}
      rc('lines', **font) 
      #第二种方法
      rcParams['lines.linewidth'] = 2
      rcParams['lines.color'] = 'r'
      #第三种方法
      rcParams.update({"lines.linewidth": 2,'lines.color': 'r'})
    
```

还原修改运行时配置默认值的方法

  * matplotlib.rcdefaults()：根据matplotlib内置的默认样式还原rcParams对象。 
  * matplotlib.rc_file_defaults()：根据matplotlib加载的rc文件的源文件还原rcParams对象。 
  * matplotlib.style.use(default)：加载默认样式。 

到此这篇关于matplotlib运行时配置(Runtime
Configuration，rc)参数rcParams解析的文章就介绍到这了,更多相关matplotlib配置rcParams内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

