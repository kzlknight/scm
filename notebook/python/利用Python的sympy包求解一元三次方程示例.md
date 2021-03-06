环境说明：Python3.7.2+Jupyter Notebook

**示例1（求解一元三次方程）：**

```python

    import sympy as sp  # 导入sympy包
    x = sp.Symbol('x')  # 定义符号变量
    f = x**3 - 3*x**2 + 3*x - 9/16  # 定义要求解的一元三次方程
    x = sp.solve(f)    # 调用solve函数求解方程
    x           # solve函数的返回结果是一个列表
     
    # x的值为[0.240852757031084,1.37957362148446-0.657440797623999*I,1.37957362148446+ 0.657440797623999*I]
```

**示例2（求解一元二次方程）：**

```python

    import sympy as sp
    x = sp.Symbol('x')
    f = x**2 - x + 3/16
    x = sp.solve(f)
    x
     
    # x的值为[0.250000000000000, 0.750000000000000]
```

以上这篇利用Python的sympy包求解一元三次方程示例就是小编分享给大家的全部内容了，希望能给大家一个参考，也希望大家多多支持脚本之家。

