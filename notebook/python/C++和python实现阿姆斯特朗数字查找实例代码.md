##  1.题目解释

如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。 例如 **1^3 + 5^3 + 3^3 = 153** 。

1000以内的阿姆斯特朗数： 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407

##  2.判断一个数是否为阿姆斯特朗数

**1.先来一个简单的代码，判断一个数是否为阿姆斯特朗数** ；

来看看C++写的

```python

    #include <iostream>
    using namespace std;
    int main()
    {
    	int n, r, sum=0, temp; 
    	cout<<"Enter the Number= "; 
    	cin>>n; 
    	temp=n; 
    	while(n>0) 
    	{ 
    		r=n%10; 
    		sum=sum+(r*r*r); 
    		n=n/10; 
    	} 
    	if(temp==sum) 
    		cout<<"Armstrong Number."<<endl; 
    	else 
    		cout<<"Not Armstrong Number."<<endl; 
    	return 0;
    }
    
```

运行结果：

![](https://img.jbzj.com/file_images/article/202012/2020120714124725.png)

接下来看看Python

```python

    num = int(input("请输入一个数字："))
    sum= 0
    n = len(str(num))
    temp = num
    while temp >0:
     digit = temp %10 # 获取个位数字
     sum += digit**n # 对计算结果进行累加
     temp //= 10
    if num == sum :
     print("太棒了！",num,"是阿姆斯特朗数")
    else:
     print("很遗憾！",num,"不是阿姆斯特朗数")
    
```

运行结果：

![](https://img.jbzj.com/file_images/article/202012/2020120714124726.png)

##  2.写一个查找固定范围内的阿姆斯特朗数

python实现：

```python

    lower = int(input("最小值："))
    upper = int(input("最大值："))
    print("下面是你想要从{}到{}之间的阿姆斯特朗数\n".format(lower,upper))
    for num in range(lower,upper+1):
     sum = 0
     n = len(str(num))
     temp = num
     while temp >0:
      digit = temp %10 # 获取个位数字
      sum+= digit**n # 对计算结果进行累加
    
      temp //= 10
     if num == sum:
      print(num)
    
```

运行结果：

![](https://img.jbzj.com/file_images/article/202012/2020120714124727.png)

C++实现：

```python

    #include <iostream>
    using namespace std;
    
    int test(int a,int b,int c,int d)
    {
    	if(a)return a*a*a*a+b*b*b*b*b+c*c*c*c+d*d*d*d*d;
    	if(b)return b*b*b+c*c*c+d*d*d;
    	if(c)return c*c+d*d;
    	if(d)return d;
    }
    void func(int min, int max)
    {
    	if(min<=0||min>=max||max<0||max>9999)
    	{
    		cout << "error!" << endl;
    	}
    	int a,b,c,d;
    	for(int i=min;i<=max;i++)
    	{
    		a = i/1000;
    		b = (i%1000)/100;
    		c = (i%100)/10;
    		d = i%10;
    		if(i==test(a,b,c,d))
    			cout << i << endl;
    	}
    }
    
    int main()
    {
    	int min,max;
    	cin >> min;
    	cin >> max;
    
    	func(min,max);
    
    	system("pause");
    	return 0;
    }
    
```

运行结果展示：

![](https://img.jbzj.com/file_images/article/202012/2020120714124828.png)

C++太复杂了，就不能向python学学，多友好的语言，学C++心态炸裂的第二天，如果有帮助到你点个关注呗！

到此这篇关于C++和python实现阿姆斯特朗数字查找的文章就介绍到这了,更多相关C++和python阿姆斯特朗数字查找内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

