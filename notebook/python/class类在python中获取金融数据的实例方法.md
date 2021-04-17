我们搜集金融数据，通常想要的是利用爬虫的方法。其实我们最近所学的class不仅可以进行类调用，在获取数据方面同样是可行的，很多小伙伴都比较关注理财方面的情况，对金融数据的需要也是比较多的。下面就class类在python中获取金融数据的方法为大家带来讲解。

使用tushare获取所有A股每日交易数据，保存到本地数据库，同时每日更新数据库；根据行情数据进行可视化和简单的策略分析与回测。由于篇幅有限，本文着重介绍股票数据管理（下载、数据更新）的面向对象编程应用实例。

```python

    #导入需要用到的模块
    import numpy as np
    import pandas as pd
    from dateutil.parser import parse
    from datetime import datetime,timedelta
    #操作数据库的第三方包，使用前先安装pip install sqlalchemy
    from sqlalchemy import create_engine
    #tushare包设置
    import tushare as ts
    token='输入你在tushare上获得的token'
    pro=ts.pro_api(token)
    #使用python3自带的sqlite数据库
    #本人创建的数据库地址为c:\zjy\db_stock\
    file='sqlite:///c:\\zjy\\db_stock\\'
    #数据库名称
    db_name='stock_data.db'
    engine = create_engine(file+db_name)
    class Data(object):
      def __init__(self,
             start='20050101',
             end='20191115',
             table_name='daily_data'):
        self.start=start
        self.end=end
        self.table_name=table_name
        self.codes=self.get_code()
        self.cals=self.get_cals()    
      #获取股票代码列表  
      def get_code(self):
        codes = pro.stock_basic(list_status='L').ts_code.values
        return codes
      #获取股票交易日历
      def get_cals(self):
        #获取交易日历
        cals=pro.trade_cal(exchange='')
        cals=cals[cals.is_open==1].cal_date.values
        return cals
      #每日行情数据
      def daily_data(self,code):
        try:
          df0=pro.daily(ts_code=code,start_date=self.start,
            end_date=self.end)      
          df1=pro.adj_factor(ts_code=code,trade_date='') 
          #复权因子
          df=pd.merge(df0,df1) #合并数据
        except Exception as e:
          print(code)
          print(e)
        return df
      #保存数据到数据库
      def save_sql(self):
        for code in self.codes:
          data=self.daily_data(code)
          data.to_sql(self.table_name,engine,
             index=False,if_exists='append')
      #获取最新交易日期
      def get_trade_date(self):
        #获取当天日期时间
        pass
      #更新数据库数据
      def update_sql(self):
        pass #代码省略
      #查询数据库信息      
      def info_sql(self):
```

**代码运行**

```python

    #假设你将上述代码封装成class Data
    #保存在'C:\zjy\db_stock'目录下的down_data.py中
    import sys
    #添加到当前工作路径
    sys.path.append(r'C:\zjy\db_stock')
    #导入py文件中的Data类
    from download_data import Data
    #实例类
    data=Data()
    #data.save_sql() #只需运行一次即可
    data.update_sql()   
    data.info_sql()
```

实例扩展：

Python下，pandas_datareader模块可以用于获取研究数据。例子如下：

```python

    >>> from pandas_datareader.data import DataReader
    >>>
    >>> datas = DataReader(name='AAPL', data_source='yahoo', start='2018-01-01')
    >>>
    >>> type(datas)
    <class 'pandas.core.frame.DataFrame'>
    >>> datas
             Open    High     Low    Close  Adj Close \
    Date
    2018-01-02 170.160004 172.300003 169.259995 172.259995 172.259995
    2018-01-03 172.529999 174.550003 171.960007 172.229996 172.229996
    2018-01-04 172.539993 173.470001 172.080002 173.029999 173.029999
    2018-01-05 173.440002 175.369995 173.050003 175.000000 175.000000
    2018-01-08 174.350006 175.610001 173.929993 174.350006 174.350006
    2018-01-09 174.550003 175.059998 173.410004 174.330002 174.330002
    2018-01-10 173.160004 174.300003 173.000000 174.289993 174.289993
    2018-01-11 174.589996 175.490005 174.490005 175.279999 175.279999
    2018-01-12 176.179993 177.360001 175.649994 177.089996 177.089996
    
           Volume
    Date
    2018-01-02 25555900
    2018-01-03 29517900
    2018-01-04 22434600
    2018-01-05 23660000
    2018-01-08 20567800
    2018-01-09 21584000
    2018-01-10 23959900
    2018-01-11 18667700
    2018-01-12 25226000
    >>>
    >>> print(datas.to_csv())
    Date,Open,High,Low,Close,Adj Close,Volume
    2018-01-02,170.160004,172.300003,169.259995,172.259995,172.259995,25555900
    2018-01-03,172.529999,174.550003,171.960007,172.229996,172.229996,29517900
    2018-01-04,172.539993,173.470001,172.080002,173.029999,173.029999,22434600
    2018-01-05,173.440002,175.369995,173.050003,175.0,175.0,23660000
    2018-01-08,174.350006,175.610001,173.929993,174.350006,174.350006,20567800
    2018-01-09,174.550003,175.059998,173.410004,174.330002,174.330002,21584000
    2018-01-10,173.160004,174.300003,173.0,174.289993,174.289993,23959900
    2018-01-11,174.589996,175.490005,174.490005,175.279999,175.279999,18667700
    2018-01-12,176.179993,177.360001,175.649994,177.089996,177.089996,25226000
    
    >>>
```

到此这篇关于class类在python中获取金融数据的实例方法的文章就介绍到这了,更多相关class类怎样在python中获取金融数据内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

