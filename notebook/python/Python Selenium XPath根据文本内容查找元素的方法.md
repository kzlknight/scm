**问题现象**  

元素的属性中没有id、name；虽然有class，但比较大众化，且位置也不固定；例如：页码中的下一页；那该如何找到该元素？

```python

    <a class="paging">上一页</div>
    <a class="paging">1</div>
    <a class="paging">2</div>
    <a class="paging">下一页</div>
    
```

**解决办法  
**

**text()**  

text() 函数文本定位

```python

    page_next = driver.find_element(By.XPATH, '//a[text()="下一页")]')
    
```

**contain()**  

