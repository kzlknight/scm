` kivy BoxLayout布局 `

创建 ` main.py ` ，文件内添加具体的布局，代码如下：

```python

    from kivy.app import App 					 # 导入kivy的App类， 它是所有kivy应用的基础
    from kivy.uix.boxlayout import BoxLayout 	 # 引入布局
    
    class BoxLayoutWidget(BoxLayout):     	 # 布局类
      def __init__(self, **kwargs):			 # 初始化
        super().__init__(**kwargs)
    
    class BoxApp(App):
      # 实现App类的build()方法（继承自类App类）
      def build(self):
    
        return BoxLayoutWidget() 			# 返回根控制
    
    if __name__ == '__main__':					# 程序入口
      BoxApp().run()							# 启动程序
```

然后创建 ` box.kv ` ，文件内添加一些按钮，由于未指定位置，所以按钮会按默认的方式排列， 具体代码如下：

```python

    <BoxLayoutWidget>:
      Button:
        text: "Btn0"
        background_color: 0, 0, 0, 0
        font_size: 35
    
      Button:
        text: "Btn1"
        background_color: 0, 1, 1, 1
        font_size: 35
    
      Button:
        text: "Btn2"
        background_color: 0, 1, 0, 1
        font_size: 35
    
      Button:
        text: "Btn3"
        background_color: 0, 0, 1, 1
        font_size: 35
    
      Button:
        text: "Btn4"
        background_color: 1, 0, 1, 1
        font_size: 35
    
      Button:
        text: "Btn5"
        background_color: 1, 0, 0, 1
        font_size: 35
    
      Button:
        text: "Btn6"
        background_color: 1, 1, 1, 1
        font_size: 35
```

` main.py ` 运行会加载 ` box.kv ` 文件样式，运行程序如下所示：

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202012/2020122814452867.png)

到此这篇关于Python+kivy BoxLayout布局的文章就介绍到这了,更多相关Python kivy
BoxLayout布局内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

