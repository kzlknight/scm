我就废话不多说了，大家还是直接看代码吧~

```python

    lt=client.fangjia.district_stat_all_0416
    dl = dt.find(query)
    
    bf=[]
    for m in dl:
      bf.append(m)
      if len(bf)==20000:
        lt.insert_many(bf)
        bf=[]
    lt.insert_many(bf)
    
```

**补充知识：** **Python操作Mongodb插入数据的两种方法：insert_one()与insert_many()**

代码说明：

将mysql中table的数据插入到mongodb里

```python

    sys.setdefaultencoding('utf8')
    import web
    from pymongo import MongoClient
    class getPltfList(object):
      def __init__(self):
        self.db1 = web.database(dbn='mysql', db = 'episode', user = 'root', pw= 'abc111--', host = '127.0.0.1')
        self.db1.printing = False
        self.db2 = web.database(dbn='mysql', db = 'episode_soc', user = 'root', pw= 'abc111--', host = '127.0.0.1')
        self.db2.printing = False
        self.db3 = web.database(dbn='mysql', db = 'cl_episode', user = 'root', pw= 'abc111--', host = '127.0.0.1')
        self.db3.printing = False
        self.db4 = web.database(dbn='mysql', db = 'cl_episode_soc', user = 'root', pw= 'abc111--', host = '127.0.0.1')
        self.db4.printing = False
      def __call__(self):
        return self.createPltfList()
    
      def createPltfList(self):
        self.ckpltfList = list(self.db1.query('select name, ip from EPISODE_PLTF_INFO order by id DESC'))
        self.ckpltfList += list(self.db2.query('select name, ip from EPISODE_PLTF_INFO order by id DESC'))
        self.clpltfList = list(self.db3.query('select name, ip from EPISODE_PLTF_INFO order by id DESC'))
        self.clpltfList += list(self.db4.query('select name, ip from EPISODE_PLTF_INFO order by id DESC'))
    
        return self.ckpltfList,self.clpltfList
    
    if __name__ == '__main__' :
      mpList = list()
      flag = 0
      tmp = 0
      sum1 = 0
      sum2 = 0
      pltfList = getPltfList()()
      client = MongoClient("127.0.0.1", 27017)
      mdb = client.episode
      collection = mdb.pltf_basic_info
      # print (type(pltfList[1])) #list
      result= list()
      for pltf_my in pltfList[0]:
        pltf_mog = collection.find()
        for record in pltf_mog:
          IP = record.get('Cfg').get('Debug_IP')
          Name = record.get('Cfg').get('Register_Name')
          # print IP, Name
          if IP == pltf_my['ip'] and Name == pltf_my['name'] :
            flag = 1
            # print IP, Name
            break
          else:
            flag = 0
    
        if flag == 0 :
          data1 = {"Cfg" : {"Debug_IP" : pltf_my['ip'],"Register_Name":pltf_my['name'], "Site":"SH-CK"} }
          # print data1
          result.append((data1))
          # collection.insert_one(data1)
          # collection.delete_one(data)
          sum1 = sum1+1
      # print len(result)
      # collection.insert_many(result)
      for pltf_my in pltfList[1]:
        pltf_mog = collection.find()
        for record in pltf_mog:
          IP = record.get('Cfg').get('Debug_IP')
          Name = record.get('Cfg').get('Register_Name')
          if pltf_my['ip'].encode("utf-8") == IP.encode("utf-8") and pltf_my['name'].encode("utf-8") == Name.encode("utf-8") :
            tmp = 1
            # print IP, Name
            break
          else:
            tmp = 0
    
        if tmp == 0 :
          data2 = {"Cfg" : {"Debug_IP":pltf_my['ip'],"Register_Name":pltf_my['name'], "Site":"SH-CL"} }
          # print data2
          result.append((data2))
    
          # collection.insert_one(data2)
          # collection.delete_one(data)
          sum2 = sum2+1
    
      collection.insert_many(result)
      print sum1,sum2
    
```

刚开始的时候我使用的是insert_one()方法，一条一条的插入到mongodb的集合里，但是计算出的sum有出入。

**在调试的过程中我发现：**

> 注释掉 # collection.insert_one(data1) # collection.insert_one(data2)

计算出来的sum1 = 193 sum2 = 222
这是合理的，因为ck_mysql里有193条记录，cl_mysql里有234条记录，mongod里有总共有15条，但是12条是与cl_mysql重复，所以正确。

但是当我去掉注释使用 collection.insert_one(data1)
collection.insert_one(data2)时，打印出的sum1=181 sum2 = 213

也就是说少了几个数据，我不知道去哪了。

想了好多办法，于是采用insert_many()的方法插入。先定义一个list(),将每个数据(数据的类型是dict)追加到list里：reslult.append(data1/data2),最后result里就会含有所有的数据，一起插入。

于是乎，问题解决了。

可是我还是很困惑insert_one()哪里出问题了！！！！！！

以上这篇pymongo insert_many 批量插入的实例就是小编分享给大家的全部内容了，希望能给大家一个参考，也希望大家多多支持脚本之家。

