###  需求问题

在日常工作中，对于前端发送过来的请求，后端django大部分都是采用json格式返回，也有采用模板返回视图的方式。

在模板返回视图的方式的确很方便，但是如果涉及到动静分离、ajax请求这类，django就只能返回json格式的数据了。

那么这里就带来了一个问题，如何将django从数据库模型类中查询的数据以json格式放回前端。

然后前端如果获取读取返回过来的数据呢？

###  环境说明

  * 前端采用jquery发送ajax请求 
  * python 3.7.2 
  * django 2.1.7 

###  示例说明

这次示例首先写一个简单的页面发送ajax请求，然后后端分 **如何返回多行数据** ， **如果返回查询对象** 进行示例说明。

###  前端代码

首先编写一个简单的前端页面 ` test_ajax.html ` 如下：

```python

    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Title</title>
      <script src="/static/js/jquery-3.0.0.min.js"></script>
      <script>
        $(function () {
          $('#search_server').click(function () {
            // 获取服务器名称
            var server_name = $('#server_name').val();
            console.log('server_name = ' + server_name);
     
            // 发送ajax post请求
            $.ajax({
              url: "/assetinfo/test_ajax",
              type: 'POST',
              data: {
                "tag": "search_project",
                "server_name": server_name,
              },
              dataType: "json",
              async: false,
              // 请求成功调用的函数
              success: function (data) {
                console.log(data);
              },
              // 请求出错时调用的函数
              error: function () {
                alert("查询项目数据发送失败");
              }
     
            })
          })
        })
      </script>
    </head>
    <body>
     
    <input type="text" id="server_name">
    <button id="search_server">提交</button>
     
     
    </body>
    </html>
```

实现的功能很简单，只是获取输入框的内容，然后点击提交按钮发送一个ajax的post请求即可。

**后台直接查询服务器信息，然后返回多条json数据**

实现类视图代码如下：

```python

    from django.core import serializers
    from django.http import HttpResponse
    from assetinfo.models import ServerInfo
     
    # ex: /assetinfo/test_ajax
    class TestAjax(View):
     
      def get(self,request):
        """显示html页面"""
        return render(request,'assetinfo/test_ajax.html')
     
      def post(self,request):
        """接收处理ajax的post请求"""
        servers = ServerInfo.objects.all() # 查询服务器信息
        json_data = serializers.serialize('json', servers) # 将查询结果进行json序列化
        return HttpResponse(json_data, content_type="application/json") # 返回json数据
```

在后台代码我没有做获取post请求的参数，再进行的参数查询的操作，这样只演示如何返回json格式数据。

其中获取post请求参数的方式很简单，依然是 ` request.POST.get('参数名') ` 即可。

浏览器测试功能如下：

![](https://img.jbzj.com/file_images/article/202012/202012290936289.png)

可以从浏览器的控制台看到后端返回过来的结果数据。

但是这样直接返回跟前端没有任务约束是不好的，那么下面来增加一下与前端交互的格式约束。

###  前后端约束返回数据格式

```python

     {"resCode": '0', "message": 'success',"data": []}
```

按照这个约束格式，那么查询的结果应该放在 ` data ` 的数组中。下面来改后端视图代码。

###  后端按照约束格式返回json数据

```python

    from django.core import serializers
    from django.http.response import JsonResponse
    from assetinfo.models import ServerInfo
     
    # ex: /assetinfo/test_ajax
    class TestAjax(View):
     
      def get(self,request):
        """显示html页面"""
        return render(request,'assetinfo/test_ajax.html')
     
      def post(self,request):
        """接收处理ajax的post请求"""
     
        # 和前端约定的返回格式
        result = {"resCode": '0', "message": 'success',"data": []}
     
        # 查询服务器信息
        servers = ServerInfo.objects.all()
     
        # 序列化为 Python 对象
        result["data"] = serializers.serialize('python', servers)
     
        return JsonResponse(result)
```

浏览器测试如下：

![](https://img.jbzj.com/file_images/article/202012/2020122909362910.png)

这样子返回前端的话，每条数据对象包含 fields，model，pk三个对象，分别代表字段、模型、主键，我更想要一个只包含所有字段的字典对象。

###  后端修改每个model对象转化为dict字典对象

```python

    from django.core import serializers
    from django.http.response import JsonResponse
    from django.forms.models import model_to_dict
     
    # ex: /assetinfo/test_ajax
    class TestAjax(View):
     
      def get(self,request):
        """显示html页面"""
        return render(request,'assetinfo/test_ajax.html')
     
      def post(self,request):
        """接收处理ajax的post请求"""
     
        # 和前端约定的返回格式
        result = {"resCode": '0', "message": 'success',"data": []}
        # 查询服务器信息
        servers = ServerInfo.objects.all()
     
        # 将model对象逐个转为dict字典，然后设置到data的list中
        for server in servers:
          server = model_to_dict(server) # model对象转dict字典
          server['server_used_type_id'] = serializers.serialize('python', server['server_used_type_id']) # 外键模型对象需要序列化，或者去除不传递
          result["data"].append(server)
     
        return JsonResponse(result)
```

浏览器测试如下：

![](https://img.jbzj.com/file_images/article/202012/2020122909362911.png)

可以看到，这样传递给前端就是字典对象了。

最后，再给出前端js遍历json格式数据的示例。

###  前端遍历返回的json格式数据示例

```python

    <script>
        $(function () {
          $('#search_server').click(function () {
            ....
     
            // 发送ajax post请求
            $.ajax({
              url: "/assetinfo/test_ajax",
              type: 'POST',
              data: {
                "tag": "search_project",
                "server_name": server_name,
              },
              dataType: "json",
              async: false,
              // 请求成功调用的函数
              success: function (res) {
                {#console.log(res.data);#}
                // 遍历data信息
                for(var i=0;i<res.data.length;i++){
                  console.log(res.data[i]);
                  console.log(res.data[i]['server_hostname']);
                  console.log(res.data[i]['server_internet_ip']);
                  console.log(res.data[i]['server_intranet_ip']);
                }
              },
              // 请求出错时调用的函数
              error: function () {
                alert("查询项目数据发送失败");
              }
     
            })
          })
        })
      </script>
```

浏览器显示如下：

![](https://img.jbzj.com/file_images/article/202012/2020122909362912.png)

到此这篇关于Django2.1.7
查询数据返回json格式的实现的文章就介绍到这了,更多相关Django返回json格式内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

