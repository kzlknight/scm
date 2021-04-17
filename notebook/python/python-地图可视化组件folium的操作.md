folium是python的一个用来绘制地图，并在地图上打点，画圈，做颜色标记的工具类。简单易学，和pandas可以很好的融合，是居家必备良品。

**一 基本功能演示**

```python

    import folium
    import webbrowser
    m=folium.Map(location=[40.009867,116.485994],zoom_start=10) # 绘制地图，确定聚焦点
    folium.Marker([40.2,116.7],popup='<b>浮标上面的那个文字</b>').add_to(m) # 定一个点，放到地图m上
    folium.Marker([40.22,116.72],popup='<b>浮标上面的那个文字</b>',icon=folium.Icon(color='red')).add_to(m)
    # 把浮标变成红色
    folium.Marker([40.24,116.74],popup='<b>浮标上面的那个文字</b>',icon=folium.Icon(color='green',icon='info-sign')).add_to(m)
    # 浮标改图样
    #标记一个空心的圈
    folium.Circle(
     location=[40.2,117.7],
     radius=10000,
     color='crimson',
     popup='popup',
     fill=False
    ).add_to(m)
    #标记一个实心圆
    folium.CircleMarker(
     location=[39.2,117.7],
     radius=100,
     popup='popup',
     color='#DC143C',#圈的颜色
     fill=True,
     fill_color='#6495ED' #填充颜色
    ).add_to(m)
    m.save('f1.html')
    webbrowser.open('f1.html')
    
```

另外，folium还支持交互，比如鼠标点击的地方显示经纬度，或者直接在点击过的地方标记一个icon

```python

    import folium
    import webbrowser as wb
    # 地图上悬浮显示经纬度
    m = folium.Map(
     location=[36.68159, 117.103565],
     zoom_start=10
    )
    m.add_child(folium.LatLngPopup())
    # 手动打点功能
    m.add_child(
     folium.ClickForMarker(popup='Waypoint')
    )
    m.save('f2.html')
    wb.open('f2.html')
    
```

**二 使用folium绘制散点图，热力图**

热力图 ,现实中数据的量级不好控制，有时候用folium画出的热力图，效果往往不是太好。

```python

    import numpy as np
    import pandas as pd
    import seaborn as sns
    import folium
    import webbrowser
    from folium.plugins import HeatMap
    #导入数据集：
    posi = pd.read_excel("D:/Python/File/Cities2015.xlsx")
    posi = posi.dropna()
    #生成所需要的数组格式数据：
    lat = np.array(posi["lat"][0:len(posi)])
    lon = np.array(posi["lon"][0:len(posi)])
    pop = np.array(posi["pop"][0:len(posi)],dtype=float)
    gdp = np.array(posi["GDP"][0:len(posi)],dtype=float)
    data1 = [[lat[i],lon[i],pop[i]] for i in range(len(posi))]
    #创建以高德地图为底图的密度图：
    map_osm = folium.Map(
     location=[35,110],
     zoom_start=5,
     tiles='http://webrd02.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x={x}&y={y}&z={z}',
     attr="&copy; <a href="http://ditu.amap.com/" rel="external nofollow" >高德地图</a>"
     )
    #创建以腾讯地图为底图的密度图：
    map_osm = folium.Map(
     location=[35,110],
     zoom_start=5,
     tiles='http://rt{s}.map.gtimg.com/realtimerender?z={z}&x={x}&y={y}&type=vector&style=0',
     attr="&copy; <a href="http://map.qq.com/" rel="external nofollow" >腾讯地图</a>"
     )
    #生成交互式地图：
    HeatMap(data1).add_to(map_osm)
    file_path = r"D:/Python/Image/People.html"
    map_osm.save(file_path)
    webbrowser.open(file_path)
    
```

folium的散点图更适合作展示，考虑到加载的顺畅性，不建议读取太大的数据，另外其组件可能会读一些外网的js，如果所在的网络不能访问google可能效果无法展示。解决办法是把里面的js地址替换成国内的镜像。

```python

    import pandas as pd
    import numpy as np
    import os
    import folium
    from folium import plugins
    import webbrowser
    import geopandas as gp
    #数据导入：
    full = pd.read_excel("D:/Python/File/Cities2015.xlsx")
    full = full.dropna()
    #创建地图对象：
    schools_map = folium.Map(location=[full['lat'].mean(), full['lon'].mean()], zoom_start=10)
    marker_cluster = plugins.MarkerCluster().add_to(schools_map) 
    #标注数据点：
    for name,row in full.iterrows():
     folium.Marker([row["lat"], row["lon"]], popup="{0}:{1}".format(row["cities"], row["GDP"])).add_to(marker_cluster) 
    #逐行读取经纬度，数值，并且打点
    #folium.RegularPolygonMarker([row["lat"], row["lon"]], popup="{0}:{1}".format(row["cities"], row["GDP"]),number_of_sides=10,radius=5).add_to(marker_cluster)
    schools_map.save('schools_map.html') #保存到本地
    webbrowser.open('schools_map.html') #在浏览器中打开
    
```

除此之外folium还可以绘制填充图，填充图比较素颜，如下图

![](https://img.jbzj.com/file_images/article/202012/20201214083826.jpg)

这里有一些官方示例，感兴趣可以看下 ：

[ https://nbviewer.jupyter.org/github/python-
visualization/folium/tree/master/examples/
](https://nbviewer.jupyter.org/github/python-
visualization/folium/tree/master/examples/)

**补充：Python遥感可视化 ― folium模块展示热力图**

“本节通过folium模块来绘制全国PM2.5热力分布图，并生成对应的html文件。”

今天的遥感之美―歌曲《欧若拉》中的阿拉斯加。阿拉斯加州位于北美大陆西北端，东与加拿大接壤，另三面环北冰洋、白令海和北太平洋。卫星俯瞰神秘北极圈，阿拉斯加的山巅，谁的脸出现海角的天边（盗用歌词捂脸）。

![](https://img.jbzj.com/file_images/article/202012/20201214084257.jpg)

哥伦比亚冰川位于美国阿拉斯加州，从海拔3,050米的冰原开始下降，沿着楚加奇山脉的侧翼下降，进入一个狭窄的入口，通往阿拉斯加东南部的威廉王子湾，它是世界上变化最快的冰川之一。科学家使用Landsat
4,5,7和8跟踪哥伦比亚冰川的变化已超过30年。哥伦比亚冰川是一个大型的潮水冰川，最终流入大海。

由Landsat系列卫星捕获的假彩色图像显示了自1986年以来冰川及其周围景观的变化。图像由以下传感器收集―专题制图仪（TM），增强型专题制图仪（ETM
+）和陆地成像仪（OLI）―来自四种不同的Landsat卫星（4,5,7和8）。

Landsat图像结合了电磁波谱的短波红外，近红外和绿光波段。通过这种波长组合，雪和冰呈现明亮的青色，植被为绿色，云为白色或浅橙色，水体为深蓝色。暴露的基岩呈棕色，而冰川表面的岩石碎片呈灰色。

在过去三十年里，终点站向北退缩了20公里。在某些年份，终点站退缩了一公里以上，但速度不均匀。例如，终点站的运动在2000年至2006年之间停滞不前，因为大努纳塔克峰和卡丁峰（直接向西）限制了冰川的运动并将冰块固定。自20世纪80年代以来，冰川已经失去了其总厚度和体积的一半左右（译自Landsat官网）。

folium是Python中一个绘制地图的模块，并可以在地图（底图）上打点，画圈，做颜色标记的工具类。简单易学，和pandas可以很好的融合，是地图可视化的一款神器。

在命令行中直接在线安装即可，快速、简洁、方便、高效。

> pip install folium

这个开源库中有许多来自OpenStreetMap、MapQuest Open、MapQuestOpen
Aerial、Mapbox和Stamen的内建地图组件，而且支持使用Mapbox或Cloudmade的API密钥来定制个性化的地图组件。Folium支持GeoJSON和TopoJSON两种文件格式的叠加，也可以将数据连接到这两种文件格式的叠加层，最后可使用color-
brewer配色方案创建分布图。

本节先来展示一下它的简单应用，主要以2018年1月全国1000多个PM2.5地面观测站点为例，将这些数据以热力图（heat
map）的形式展现给大家，并生成相应的html文件。

代码实现：

```python

    # _*_ coding: utf-8 _*_
    __author__ = 'xbr'
    __date__ = '2019/1/9 15:47'
     
    import numpy as np
    import pandas as pd
    import folium
    import webbrowser
    from folium.plugins import HeatMap
     
     
    # 读取csv文件,以Dataframe形式保存
    df = pd.read_csv(r"D:\data\PM25-20180101.csv")
    # 获取数据个数
    num = df.shape[0]
    # 获取纬度
    lat = np.array(df["lat"][0:num])
    # 获取经度
    lon = np.array(df["lon"][0:num])
    # 获取PM2.5，转化为numpy浮点型
    pm25 = np.array(df["PM25"][0:num], dtype=float)
    # 将数据制作成[lats, lons, weights]的形式
    data1 = [[lat[i], lon[i], pm25[i]] for i in range(num)]
    # 绘制Map，中心经纬度[32, 120],开始缩放程度是5倍
    map_osm = folium.Map(location=[32, 120], zoom_start=5)
    # 将热力图添加到前面建立的map里
    HeatMap(data1).add_to(map_osm)
     
    file_path = r"D:\AirQualityMap.html"
    # 保存为html文件
    map_osm.save(file_path)
    # 默认浏览器打开
    webbrowser.open(file_path)
```

结果图：

![](https://img.jbzj.com/file_images/article/202012/20201214084307.jpg)

对结果图局部放大：

![](https://img.jbzj.com/file_images/article/202012/20201214084314.jpg)

对结果图局部放大：

![](https://img.jbzj.com/file_images/article/202012/20201214084322.jpg)

缩小后全景图：

![](https://img.jbzj.com/file_images/article/202012/20201214084336.jpg)

以上为个人经验，希望能给大家一个参考，也希望大家多多支持脚本之家。如有错误或未考虑完全的地方，望不吝赐教。

