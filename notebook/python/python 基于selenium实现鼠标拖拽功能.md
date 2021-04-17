##  1、准备html文件

首先我们需要准备一个鼠标滑动的html文件，用来演示鼠标滑动的效果，注意需要将我们的html文件放在自己的服务器上，

这样我们才能够通过selenium来进行验证。html文件如下：

```python

    <html>
    <head>
      <meta charset="utf-8" />
      <style>
        body {
      margin: 0;
      padding: 0;
    }
    
    input{
      appearance:none;
      -moz-appearance:none;
      -webkit-appearance:none;
      background: none;
      border:none;
    }
    
    .wrap{
      margin: 200px 0 0 200px;
    }
    
    .box {
      position: relative;
      width: 200px;
      height: 30px;
      border-radius: 20px;
      background: #686B69;
      line-height: 30px;
      overflow: hidden;
      margin-bottom: 40px;
      color: #fff;
      font-size: 12px;
    }
    
    .btn {
      position: absolute;
      top: 0;
      left: 0;
      height: 30px;
      width: 30px;
      background: #0c7;
      border-radius: 20px;
      text-align: center;
    }
    
    .tips {
      text-align: center;
    }
    
    #submit{
      line-height: 28px;
      border-radius: 3px;
      background: #0c7;
      width: 200px;
      text-align: center;
      color: #fff;
    }
      </style>
    </head>
    <body>
    <div class="wrap">
    　　<div class="box">
    　　　　<div class="btn" id="dragEle"></div>
    　　　　<div class="tips">>>拖动滑块验证<<</div>
    　　</div>
    　<input type="button" value="提交验证" id="submit" />
    </div>
    <script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
    <script type="text/javascript">
      function DragValidate (dargEle,msgEle){
        var dragging = false;//滑块拖动标识
        var iX;
        dargEle.mousedown(function(e) {
          msgEle.text("");
          dragging = true;
          iX = e.clientX; //获取初始坐标
        });
        $(document).mousemove(function(e) {
          if (dragging) {
            var e = e || window.event;
            var oX = e.clientX - iX;
            if(oX < 30){
              return false;
            };
            if(oX >= 210){//容器宽度+10
              oX = 200;
              return false;
            };
            dargEle.width(oX + "px");
            //console.log(oX);
            return false;
          };
        });
        $(document).mouseup(function(e) {
          var width = dargEle.width();
          if(width < 200){
            //console.log(width);
            dargEle.width("30px");
            msgEle.text(">>拖动滑块验证<<");
          }else{
            dargEle.attr("validate","true").text("验证成功！").unbind("mousedown");
          };
          dragging = false;
        });
      };
    
      DragValidate($("#dragEle"),$(".tips"));
      $("#submit").click(function(){
        if(!$("#dragEle").attr("validate")){
          alert("请先拖动滑块验证！");
        }else{
          alert("验证成功！");
        }
      });
    </script>
    </body>
    </html>
```

##  2、使用selenium进行鼠标拖拽操作，具体代码如下：

```python

    from selenium import webdriver
    import unittest
    from selenium.webdriver import ActionChains
    import time
     
     
    url = 'http://192.168.62.9:1234/easytest/tt'
    driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
    driver.get(url)
    driver.maximize_window()
     # 获取第一，二，三能拖拽的元素
    drag1 = driver.find_element_by_id('dragEle')
     
    # 创建一个新的ActionChains，将webdriver实例对driver作为参数值传入，然后通过WenDriver实例执行用户动作
    action_chains = ActionChains(driver)
    # 将页面上的第一个能被拖拽的元素拖拽到第二个元素位置
    # 将页面上的第三个能拖拽的元素，向右下拖动10个像素，共拖动5次
    action_chains.drag_and_drop_by_offset(drag1, 208, 0).perform()
    time.sleep(5)
    driver.quit()
```

以上就是python 基于selenium实现鼠标拖拽功能的详细内容，更多关于python 鼠标拖拽的资料请关注脚本之家其它相关文章！

