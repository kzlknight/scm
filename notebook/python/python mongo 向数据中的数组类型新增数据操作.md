我就废话不多说了，大家还是直接看图吧~

![](https://img.jbzj.com/file_images/article/202012/20201205102557.jpg)

**补充知识：** **pymongo插入数据时更新和不更新的使用**

**（1）update的setOnInsert**

当该key不存在的时候执行插入操作，当存在的时候则不管，可以使用setOnInsert

> db.test.update({'_id': 'id'}, {'$setOnInsert': {'a': 'a'}, true)

当id存在的时候，忽略setOnInsert。

**（2）update的set**

当key不存在的时候执行插入操作，当存在的时候更新除key以外的set内的值

> db.test.update({'_id': 'id'}, {'$set': {'b': 'b'}}, true)

当id存在的时候，如果要插入，则插入{'a': 'a'}

最后的参数true，则是指明，当update不存在的_id时，执行插入操作。默认是false，只更新，不插入。

**（3）insert**

insert是直接将内容插入数据库，这样会造成重复插入数据。

以上这篇python mongo 向数据中的数组类型新增数据操作就是小编分享给大家的全部内容了，希望能给大家一个参考，也希望大家多多支持脚本之家。

