题目：使用 Python 生成 200 个不重复的激活码

**编写思路**

# 激活码一般是由26个大写字母和10个数字任意组合而成  
# 长度为12位或者16位的居多激活码  
# 一个激活码里的字符是可以重复的，而且必须要保证激活码是不能重复的  

**测试用例**

# 1、随机生成字符：数字加字母  
# 2、生成200个  
# 3、去重  

**编码：**

第一步：随机生成16位字母跟数字的字符串

1.调用ramdom模块，使用了import random

2.choice() 方法返回一个列表，元组或字符串的随机项

使用了random.choice(seed)，从seed中随机获取字符串

3.join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串

join()方法语法：str.join(sequence)

使用"".join(sa)将随机生成的16个字符串连接在一起

```python

    import random
    
    # 生成16位字符串
    def random_str():
      seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
      sa = []
      for i in range(16):
        sa.append(random.choice(seed))
      salt = "".join(sa)
      print(salt)
      return salt
    
    
```

第二步：生成200个字符串

使用for循环，调用random_str()函数

```python

       for i in range(200):
         L.append(random_str()) 
    
```

第三部：删除重复的激活码

1.添加删除重复激活码函数

当两个激活码相同时，打印出重复激活码，并对该激活码进行标识

2.删除重复激活码

对标识过的激活码进行删除

```python

    def Removal():
      for i in range(200):
        for j in range(i+1,200):
          if L[i] == L[j]:
            print("重复的激活码：", L[i])
            L[i] = '-1'
    i = 0
    while i < len(L):
      if L[i] == '-1':
        print("删除重复元素", L[i])
        L.remove(L[i])
        i -= 1
      else:
        i +=1
    
```

完整代码如下：

```python

    import random
    
    # 生成16位字符串
    def random_str():
      seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
      sa = []
      for i in range(16):
        sa.append(random.choice(seed))
      salt = "".join(sa)
      print(salt)
      return salt
    
    # 去除重复激活码
    def Removal():
      for i in range(200):
        for j in range(i+1,200):
          if L[i] == L[j]:
            print("重复的激活码：", L[i])
            L[i] = '-1'
    
    
    if __name__ =="__main__":
      L = []
      for i in range(200):
        L.append(random_str()) #生成两百个激活码
      L[0] = L[1] #校验L[0]=L[1]时，是否删除重复
      Removal()
      i = 0
      while i < len(L):
        if L[i] == '-1':
          print("删除重复元素", L[i])
          L.remove(L[i])
          i -= 1
        else:
          i +=1
    
    
```

以上就是本文的全部内容，希望对大家的学习有所帮助，也希望大家多多支持脚本之家。

