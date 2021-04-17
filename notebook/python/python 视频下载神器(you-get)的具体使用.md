you-get是github上python的一个开源库( [ https://github.com/soimort/you-get
](https://github.com/soimort/you-get) )，使用you-
get你只需要取得视频所在网页链接地址就可以很轻松的下载下来，目前you-
get所支持的网站包含国内外几十个网站(youtube、twitter、腾讯、爱奇艺、优酷、bilibili等)，基本上可以满足你的需求。

1.you-get可以直接通过命令行使用

前提是你要先安装you-get： ` pip install you-get `

下载命令： ` **you-get** your-url `

l例如：

```python

    you-get https://www.bilibili.com/bangumi/play/ep118488?from=search&seid=5050973611974373611
```

效果如下：（我直接在pycharm的终端命令行执行）

![](https://img.jbzj.com/file_images/article/202101/2021010610283973.png)

2.通过python 简单调用you-get库

```python

    # ！/usr/bin/env python
    # -*-coding:utf-8-*-
    """
    @Author : xiaofeng
    @Time : 2018/12/25 10:26
    @Desc : Less interests,More interest.
    @Project : python_appliction
    @FileName: you-get.py
    @Software: PyCharm
    @Blog ：https://blog.csdn.net/zwx19921215
    """
    import sys
    import you_get
     
     
    def download(url, path):
     sys.argv = ['you-get', '-o', path, url]
     you_get.main()
     
     
    if __name__ == '__main__':
     # 视频网站的地址
     url = 'https://www.bilibili.com/bangumi/play/ep118488?from=search&seid=5050973611974373611'
     # 视频输出的位置
     path = 'G:/test'
     download(url, path)
```

![](https://img.jbzj.com/file_images/article/202101/2021010610284074.png)

3.python 简单集成 tkinter，通过GUI的形式展现（单线程，未做优化，后续做优化处理）

```python

    # ！/usr/bin/env python
    # -*-coding:utf-8-*-
    """
    @Author  : xiaofeng
    @Time    : 2018/12/25 11:50
    @Desc : Less interests,More interest.
    @Project : python_appliction
    @FileName: you-get2.py
    @Software: PyCharm
    @Blog    ：https://blog.csdn.net/zwx19921215
    """
     
    import re
    import sys
    import tkinter as tk
    import tkinter.messagebox as msgbox
    import webbrowser
     
    import you_get
     
    """
    视频下载类
    """
     
     
    class DownloadApp:
     # construct
     def __init__(self, width=800, height=200):
      self.w = width
      self.h = height
      self.title = '视频下载助手'
      self.root = tk.Tk(className=self.title)
      self.url = tk.StringVar()
      self.start = tk.IntVar()
      self.end = tk.IntVar()
      self.path = tk.StringVar()
      self.path.set('D:/DownloadApp')
     
      # define frame
      frame_1 = tk.Frame(self.root)
      frame_2 = tk.Frame(self.root)
      frame_3 = tk.Frame(self.root)
      frame_4 = tk.Frame(self.root)
     
      # menu
      menu = tk.Menu(self.root)
      self.root.config(menu=menu)
      menu1 = tk.Menu(menu, tearoff=0)
      menu.add_cascade(label='Menu', menu=menu1)
      menu1.add_command(label='about me', command=lambda: webbrowser.open('https://blog.csdn.net/zwx19921215'))
      menu1.add_command(label='exit', command=lambda: self.root.quit())
     
      # set frame_1
      label1 = tk.Label(frame_1, text='请输入视频链接：')
      entry_url = tk.Entry(frame_1, textvariable=self.url, highlightcolor='Fuchsia', highlightthickness=1, width=35)
     
      # set frame_2
      s_lable = tk.Label(frame_2, text='起始值：')
      e_lable = tk.Label(frame_2, text='结束值：')
      start = tk.Entry(frame_2, textvariable=self.start, highlightcolor='Fuchsia', highlightthickness=1, width=10)
      end = tk.Entry(frame_2, textvariable=self.end, highlightcolor='Fuchsia', highlightthickness=1, width=10)
     
      # set frame_3
      label2 = tk.Label(frame_3, text='请输入视频输出地址：')
      entry_path = tk.Entry(frame_3, textvariable=self.path, highlightcolor='Fuchsia', highlightthickness=1, width=35)
      down = tk.Button(frame_3, text='下载', font=('楷体', 12), fg='green', width=3, height=-1,
           command=self.video_download)
      # set frame_4
      label_desc = tk.Label(frame_4, fg='black', font=('楷体', 12),
            text='\n注意：支持youtube、twitter、腾讯、爱奇艺、优酷、bilibili等大部分主流网站视频下载、图片下载！')
      label_warning = tk.Label(frame_4, fg='blue', font=('楷体', 12), text='\nauthor:xiaofeng')
     
      # layout
      frame_1.pack()
      frame_2.pack()
      frame_3.pack()
      frame_4.pack()
     
      label1.grid(row=0, column=0)
      entry_url.grid(row=0, column=1)
     
      s_lable.grid(row=1, column=0)
      start.grid(row=1, column=1)
      e_lable.grid(row=1, column=2)
      end.grid(row=1, column=3)
     
      label2.grid(row=2, column=0)
      entry_path.grid(row=2, column=1)
      down.grid(row=2, column=2, ipadx=20)
     
      label_desc.grid(row=3, column=0)
      label_warning.grid(row=4, column=0)
     
     """
     视频下载
     """
     
     def video_download(self):
      # 正则表达是判定是否为合法链接
      url = self.url.get()
      path = self.path.get()
      if re.match(r'^https?:/{2}\w.+$', url):
       if path != '':
        msgbox.showwarning(title='警告', message='下载过程中窗口如果出现短暂卡顿说明文件正在下载中！')
        try:
         sys.argv = ['you-get', '-o', path, url]
         you_get.main()
        except Exception as e:
         print(e)
         msgbox.showerror(title='error', message=e)
        msgbox.showinfo(title='info', message='下载完成！')
       else:
        msgbox.showerror(title='error', message='输出地址错误！')
      else:
       msgbox.showerror(title='error', message='视频地址错误！')
     
     def center(self):
      ws = self.root.winfo_screenwidth()
      hs = self.root.winfo_screenheight()
      x = int((ws / 2) - (self.w / 2))
      y = int((hs / 2) - (self.h / 2))
      self.root.geometry('{}x{}+{}+{}'.format(self.w, self.h, x, y))
     
     def event(self):
      self.root.resizable(False, False)
      self.center()
      self.root.mainloop()
     
     
    if __name__ == '__main__':
     app = DownloadApp()
     app.event()
```

![](https://img.jbzj.com/file_images/article/202101/2021010610284075.png)

注： **由于视频窗口是单线程，所以下载过程会一直卡顿（是正常的，因为处于下载中，下载完后会恢复），后续将会优化**

到此这篇关于python 视频下载神器(you-get)的具体使用的文章就介绍到这了,更多相关python
视频下载内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

