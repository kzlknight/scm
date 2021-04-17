在操作数据库时，需要将字符串转换成decimal类型。

**代码如下：**  

```python

    select cast('0.12' as decimal(18,2));
    select convert(decimal(18,2), '0.12');
    
```

当需要将科学计数法的数字字符串转换成decimal时，这2种写法都报错：

```python

    msg 8114, level 16, state 5, line 1
    error converting data type varchar to numeric.
     
    select cast('0.12e+006' as decimal(18,2));
    select convert(decimal(18,2), '0.12e+006');
    
```

网上查了很多资料都没有找到答案。最后无意中发现float类型转换成字符串时就会产生科学计数法的数值字符串：

```python

    select cast(cast(1234400000 as float) as varchar)
    1.2344e+009
    
```

反向思维，那科学计数法的数值字符串应该可以转换成float类型，再转换float到decimal。

以上这篇转换科学计数法的数值字符串为decimal类型的方法就是小编分享给大家的全部内容了，希望能给大家一个参考，也希望大家多多支持脚本之家。

