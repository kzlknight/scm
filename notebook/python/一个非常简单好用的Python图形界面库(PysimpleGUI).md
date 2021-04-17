前一阵，我在为朋友编写一个源代码监控程序的时候，发现了一个 Python 领域非常简单好用的图形界面库。

说起图形界面库，你可能会想到 TkInter、PyQt、PyGUI
等流行的图形界面库，我也曾经尝试使用，一个很直观的感受就是，这太难用了。就去网上搜搜，看看有没有一些
demo，拿来改改，结果很少有，当时我就放弃了这些图形库的学习，转而使用了 vue+flask
的形式以浏览器网页作为程序界面，因为我会这个，即使实现起来稍微麻烦，但是也快。

那有朋友可能问了：一定要学习图形界面吗？

其实不一定，如果你写的程序都是自己用，或者配合其他程序员使用，那么直接命令行调用即可，完全不用学习图形界面？那什么时候要学呢？如果你要做游戏，或者你要为他人（非技术人员）编写软件工具，那么你就需要学习图形界面了。我是后者，偶尔受邀帮别人写点小工具，因此有个图形界面体验会好很多。

今天要说的这个库就是 PySimpleGUI，在 GitHub 仓库[1]有 5.1K 个 star，20 天前还有人提交代码，可以说非常火热了。

我看了官方文档，找了个 demo，花了 2 个小时的时间，写了 56 行代码，就搞定了一个具有图形界面的监控工具，如下：

要说 PysimpleGUI 最吸引我的地方，在于它有 200 多个示例程序，几乎覆盖了日常的开发需求，拿来稍作修改就可以用，着实方便。  

PysimpleGUI 内部封装了 tkinter，Qt（pyside2），wxPython和 Remi，Remi
用于浏览器支持，因此你很容易将你的界面搬到浏览器中而无需修改代码。如下图：

![](https://img.jbzj.com/file_images/article/202012/202012280907438.jpg)

还有最吸引我的一点，就是足够简单，在几分钟内用几行代码就可以构建自定义 GUI 布局，对于初学者来说足够容易，对于高级用户来说足够强大。广泛的文档。有
100 多种内置颜色主题，200 多个示例程序[2]，还经常更新。如果你玩 Raspberry Pi，也可以用这个库写界面，你说好用不好用。

通常一个 PySimpleGUI 程序包含 5 个部分，见下面代码的注释：

```python

    import PySimpleGUI as sg            # Part 1 - 导入库
     
    # 定义窗口的内容
    layout = [ [sg.Text("What's your name?")],   # Part 2 - 排版
          [sg.Input()],
          [sg.Button('Ok')] ]
     
    # 创建窗口
    window = sg.Window('Window Title', layout)   # Part 3 - 窗口定义
                            
    # Display and interact with the Window
    event, values = window.read()          # Part 4 - 开启主循环 window.read()
     
    # Do something with the information gathered
    print('Hello', values[0], "! Thanks for trying PySimpleGUI")
     
    # Finish up by removing from the screen
    window.close() # Part 5 - 关闭窗口
```

执行上述代码，会得到一个如下图所示的程序：

![](https://img.jbzj.com/file_images/article/202012/202012280907439.jpg)

这仅仅是一个类似 hello world 的程序，PySimpleGUI 还可以做出更加强大的图形界面和游戏界面，

**多个窗口  
**

我看到许多新程序员都在挣扎的一件事是在他们选择的GUI工具包中打开多个窗口。 幸运的是，PySimpleGUI明确标明了如何执行此操作的说明。
实际上，他们有两种不同的“设计模式”来做这种事情。

为简便起见，我将仅展示如何执行两个活动窗口：

```python

    # -*- coding: utf-8 -*-
    # https://www.jianshu.com/u/69f40328d4f0
    # https://github.com/china-testing/python-api-tesing
    # https://china-testing.github.io/
    # support q group: 630011153 144081101
    import PySimpleGUI as sg
     
    # Create some widgets
    ok_btn = sg.Button('Open Second Window')
    cancel_btn = sg.Button('Cancel')
    layout = [[ok_btn, cancel_btn]]
     
    # Create the first Window
    window = sg.Window('Window 1', layout)
     
    win2_active = False
     
    # Create the event loop
    while True:
      event1, values1 = window.read(timeout=100)
     
      if event1 in (None, 'Cancel'):
        # User closed the Window or hit the Cancel button
        break
     
      if not win2_active and event1 == 'Open Second Window':
        win2_active = True
        layout2 = [[sg.Text('Window 2')],
              [sg.Button('Exit')]]
     
        window2 = sg.Window('Window 2', layout2)
     
      if win2_active:
        events2, values2 = window2.Read(timeout=100)
        if events2 is None or events2 == 'Exit':
          win2_active = False
          window2.close()
     
    window.close()
```

###  参考资料

[1] GitHub 仓库: [ https://github.com/PySimpleGUI/PySimpleGUI
](https://github.com/PySimpleGUI/PySimpleGUI)

[2] 200 多个示例程序: [
https://github.com/PySimpleGUI/PySimpleGUI/tree/master/DemoPrograms
](https://github.com/PySimpleGUI/PySimpleGUI/tree/master/DemoPrograms)

到此这篇关于一个非常简单好用的Python图形界面库的文章就介绍到这了,更多相关Python
图形界面库内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

