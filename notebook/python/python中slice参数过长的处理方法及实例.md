很多小伙伴对于slice参数的概念理解停留在概念上，切片的参数有三个，分别是step 、start 、stop
。因为参数的值也是多变的，所以我们需要对它们进行下一步的处理。在之前的slice讲解中我们提到列表数据过长的问题，其中在参数中也有这样的问题存在。下面我们就step
、start 、stop 三个参数的分别处理展开讲解，帮大家深入了解slice中的参数问题。

###  1.step 的处理

```python

    if (r->step == Py_None) {
         /* step 默认是 1，这不难理解 */
       *step = 1;
     } else {
       if (!_PyEval_SliceIndex(r->step, step)) return -1;
         /* step 不能为零，否则报 ValueError，要注意的是，这个异常是在执行 BINARY_SUBSCR 才报出来，
        * 在创建 slice 对象时如果 step 为 0 并不会报错 */
       if (*step == 0) {
         PyErr_SetString(PyExc_ValueError, "slice step cannot be zero");
         return -1;
       }
       /* step 的最小值，他是根据 size_t 来定义的
        * #define PY_SSIZE_T_MAX ((Py_ssize_t)(((size_t)-1)>>1))
        * 所以在 32 为系统上就是 -2147483647 */
       if (*step < -PY_SSIZE_T_MAX)
         *step = -PY_SSIZE_T_MAX;
     }
```

###  2.start 的处理

```python

    /* 当 start 未设置时的默认值，length 是序列的长度
      * 如果切片从序列头部开始（step > 0），start = 0
      * 如果切片从序列末尾开始（step < 0），start = length - 1 */
     defstart = *step < 0 ? length-1 : 0;
     if (r->start == Py_None) {
       *start = defstart;
     }
     else {
       if (!_PyEval_SliceIndex(r->start, start)) return -1;
       /* 如果 start 是负数，其实是通过加上序列长度转化成正数的 a[-1:] <=> a[4:] */
       if (*start < 0) *start += length;
       /* 如果加上 length 还是小于 0，也就是 -start 超出了序列长度，这时候会根据 step 的正负将start
        * 设置为序列的开始（0）或结束（-1）位置
        * a[-6:-1]  <=> a[0:-1]
        * a[-6:-1:-1] <=> a[-1:-1:-1] */
       if (*start < 0) *start = (*step < 0) ? -1 : 0;
        /* start 超出了序列长度，这时候会根据 step 的正负将start
        * 设置为序列的长度或序列长度减 1（最后一个元素）
        * a[6:-1]  <=> a[5:-1]
        * a[6:-1:-1] <=> a[4:-1:-1] */
       if (*start >= length)
         *start = (*step < 0) ? length - 1 : length;
     }
```

###  3.stop 的处理

```python

    /* 当 stop 未设置时的默认值，length 是序列的长度
      * 如果切片从序列头部开始（step > 0），stop = length，比最后一个元素的下标多 1
      * 如果切片从序列末尾开始（step < 0），start = -1，比第一个元素的下标少 1 */
     defstop = *step < 0 ? -1 : length;
     if (r->stop == Py_None) {
       *stop = defstop;
     } else {
       if (!_PyEval_SliceIndex(r->stop, stop)) return -1;
       /* 如果 stop 是负数，其实是通过加上序列长度转化成正数的 a[:-1] <=> a[:4] */
       if (*stop < 0) *stop += length;
       /* 如果加上 length 还是小于 0，也就是 -stop 超出了序列长度，这时候会根据 step 的正负将 stop
        * 设置为序列的开始（0）或结束（-1）位置
        * a[3:-6]  <=> a[3:0]
        * a[3:-6:-1] <=> a[3::-1] */
       if (*stop < 0) *stop = (*step < 0) ? -1 : 0;
       if (*stop >= length)
         *stop = (*step < 0) ? length - 1 : length;
     }
```

注意：

  * 指定的区间是左开右闭型 
  * 从头开始，开始索引数字可以省略，冒号不能省略 
  * 到末尾结束，结束索引数字可以省略，冒号不能省略。 
  * 步长默认为1，如果连续切片，数字和冒号都可以省略。 

####  关于Python中的slice操作扩展：

Python中slice操作的完整语法：

```python

    # i默认是0
    # j默认是len(S)
    # k的步长，默认为+1
    S[i:j:k]
```

其中i,j,k都可以是负数：

若i < 0或者k<0，等价于len(S) + i，或者len(S) + j；

若k < 0，则表示将[i,k)之间的字符按照步长k,从右往左数，而不是从左往右数

```python

    >>>S = 'abcdefg'
    >>>S[-3:-1]
    'ef'
    
    >>>S[-1:-3:-1]  # 将位于S[-1:-3]的字符子串，按照步长1，从右往左数，而不是从左往右数
    'gf'
    
    >>>S[4:2:-1]
    'ed'
    
    >>>S[2:4:-1]  # 输出空字符串
    ''
    
    >>>S[::-1]  # 逆序
    'gfedcba'
```

需要指出的是s[i:j:k]的形式，等价于下面的形式：

```python

    >>>S = 'abcdefg'
    >>>S[slice(None, None, -1)]  # 等价于使用slice对象进行数组元素的访问操作
    'gfedcba'
```

到此这篇关于python中slice参数过长的处理方法及实例的文章就介绍到这了,更多相关python中slice参数过长如何处理内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

