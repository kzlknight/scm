##  1 简介  

kepler.gl作为开源地理空间数据可视化神器，也一直处于活跃的迭代开发状态下。而在前不久，kepler.gl正式发布了其2.4.0版本，下面我们就来对其重要的新特性进行介绍：

![](https://img.jbzj.com/file_images/article/202012/2020122294459060.png?202011229457)

##  2 kepler.gl 2.4.0重要新特性  

###  2.1 增量时间窗口  

在这次更新中，为时间序列数据的可视化新增了增量时间窗口功能，在上一个版本2.3.2中，当我们的数据集带有时间类型字段时，在添加对应的Filters之后，显示出的时间窗口是这个样子的：

![](https://img.jbzj.com/file_images/article/202012/2020122294539579.png?2020112294547)

而在2.4.0版本中，时间窗口如图所示：

![](https://img.jbzj.com/file_images/article/202012/2020122294624046.png?2020112294633)

在如下图一样从默认的Moving Time Window模式切换到Incremental Time
Window模式之后，就可以使用增量时间窗口模式，画面中的数据会从起点开始持续叠加：

![](https://img.jbzj.com/file_images/article/202012/2020122294701858.gif?2020112294712)

###  2.2 Python接口新增_repr_html_()方法  

而这个更新不仅针对原生的kepler.gl，还针对其面向Python的接口keplergl新增_repr_html_()方法，使得将kepler.gl与flask等进行结合更加方面，就像folium中的_repr_html_()方法一样：

结合flask

```python

    from flask import Flask
    from keplergl import KeplerGl
    
    app = Flask(__name__)
    
    @app.route('/')
    def index():
      
      map_1 = KeplerGl()
      
      return map_1._repr_html_()
    
    if __name__ == '__main__':
      app.run(debug=True)
```

而如果你对 ` dash ` 有所了解，那么纯 ` Python ` 快速开发出一个嵌入 ` kepler.gl ` 的交互式 ` web `
应用将会变得非常容易，就像下面这个简单的例子一样：

![](https://img.jbzj.com/file_images/article/202012/2020122294838477.gif?2020112294849)

```python

    import dash
    from keplergl import KeplerGl
    import dash_html_components as html
    import dash_core_components as dcc
    from dash.dependencies import Input, Output
    import requests
    
    app = dash.Dash(__name__)
    
    app.layout = html.Div(
      [
        html.H1("Dash结合Kepler.gl："),
        dcc.Dropdown(
          id='demo-dropdown',
          options=[
            {'label': '重庆', 'value': '重庆'}
          ],
          style={'width': '300px'}
        ),
        html.Iframe(id='iframe',
              style={'height': '800px', 'width': '1900px'})
      ]
    )
    
    @app.callback(
      Output('iframe', 'srcDoc'),
      [Input('demo-dropdown', 'value')]
    )
    def switch_area(selected_area):
    
      if selected_area == '重庆':
        map_1 = KeplerGl(data={
                   selected_area: requests.get('https://geo.datav.aliyun.com/areas_v2/bound/500000_full.json').json()
                 },
                 config={
                   "mapState": {
                     "bearing": 0,
                     "dragRotate": False,
                     "latitude": 29.751819,
                     "longitude": 107.441431,
                     "pitch": 0,
                     "zoom": 6,
                     "isSplit": False
                   }
                 })
    
        return map_1._repr_html_().decode()
    
      else:
        map_1 = KeplerGl(data={
                   selected_area: requests.get('https://geo.datav.aliyun.com/areas_v2/bound/100000_full.json').json()
                 },
                 config={
                   "mapState": {
                     "bearing": 0,
                     "dragRotate": False,
                     "latitude": 29.751819,
                     "longitude": 107.441431,
                     "pitch": 0,
                     "zoom": 3,
                     "isSplit": False
                   }
                 })
    
        return map_1._repr_html_().decode()
    
    if __name__ == '__main__':
      app.run_server()
```

以上就是地图可视化神器kepler.gl python接口的使用方法的详细内容，更多关于python
地图可视化神器kepler.gl的资料请关注脚本之家其它相关文章！

