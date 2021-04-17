**如下所示：**

1、mongodb的日期时间格式是UTC时间，中国时间 = UTC时间 +8

2、可在pymongo客户端加入时区以解决此问题：

```python

    import pytz
    from pymongo import MongoClient
    from datetime import datetime
    tzinfo = pytz.timezone('Asia/Shanghai')
    
    client = MongoClient(
      host="127.0.0.1",
      port=27017,
      username="root",
      password="123456",
      authSource="admin", # 在哪个数据库进行身份验证，默认是admin
      tz_aware=True, # 设置为True
      tzinfo=tzinfo  # 加入时区信息
    )
    db = client["test"]
    collection = db["mytest"]
    
    datetime.now() # 2020-04-11 10:42:42.452433
    ret = collection.insert_one({
      "name": "测试5",
      "create_time": tzinfo.localize(datetime.now()) 
    })
    # create_time不能使用datetime.now()获取时间，
    # 应该使用 datetime.utcnow()或 tzinfo.localize(datetime.now())或 datetime.now(tz=tzinfo)
    # 这样读取数据时日期时间才是标准的中国时间
    res = collection.find_one({"name": "测试5"})
    print(res)
    # {'_id': ObjectId('5e912ea261d252f76350728a'), 'name': '测试5', 'create_time': datetime.datetime(2020, 4, 11, 10, 42, 42, 452000, tzinfo=<DstTzInfo 'Asia/Shanghai' CST+8:00:00 STD>)}
    
    # 下面测试直接使用datetime.now()的情形
    datetime.now() # 2020-04-11 10:49:41.899445
    collection.insert_one({
      "name": "测试6",
      "create_time": datetime.now()
    })
    res = collection.find_one({"name": "测试6"})
    # {'_id': ObjectId('5e913045143015041d776d08'), 'name': '测试6', 'create_time': datetime.datetime(2020, 4, 11, 18, 49, 41, 899000, tzinfo=<DstTzInfo 'Asia/Shanghai' CST+8:00:00 STD>)}
    # 可以看到时间+8小时
    
```

**补充知识：** **pymongo 按照时间查询**

我就废话不多说了，大家还是直接看代码吧~

```python

    from pymongo import MongoClient 
    client=MongoClient('localhost',27017)
    db=client.adv.message
    from datetime import datetime
    import pandas as pd
    #db.insert_one({'player_id':js2['player_id'],'message':js2['message'],
    #        'label':label,'predict_time':datetime.datetime.now()})
    
    #按照时间查询
    q1={"predict_time":{"$gte" :datetime(2019,9,25) ,"$lte": datetime(2019,9,28)}}  
    l1=list(db.find(q1))
    
    #l1=list(db.find({}))
    df=pd.DataFrame(l1)
    
```

以上这篇快速解决pymongo操作mongodb的时区问题就是小编分享给大家的全部内容了，希望能给大家一个参考，也希望大家多多支持脚本之家。

