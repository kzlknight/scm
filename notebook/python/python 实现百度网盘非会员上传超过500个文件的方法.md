##  案例故事:  

百度网盘非会员大量上传文件，会弹出：“上传文件数量超出500个现在，开通超级会员后可继续上传”，其实是限制拖入500张相片，并非限制上传500张。

![](https://img.jbzj.com/file_images/article/202101/202117115437384.jpg?202107115448)

非会员如何将众多文件，分割成500一个的文件夹，不受拖入数量限制呢？

##  准备阶段  

  * os.walk()函数，可以树形遍历整个路径下的文件夹列表和文件列表 
  * Path(路径).parent属性，可以获取该“路径”的父路径 
  * os.path.relpath("D:\aaa\bbb\ccc"，start="D:\aaa")函数，可以返回“bbb\ccc”字符串， 实现路径裁剪。 
  * os.sep 可以代表任何路径分隔符 
  * os.rename()函数，可以实现移动功能 
  * sys.argv[1] 通过接收“待分割的路径”参数的输入 

##  Python面向对象类形式

```python

    # python3.8
    # coding=utf-8
     
    import os
    import sys
    from pathlib import Path
     
     
    class BaiduPanCutter(object):
      '''百度网盘500个文件分割器'''
     
      def __init__(self, root_path, count=500):
        self.root_path = root_path
        self.count = count
        self.folder_file_dict = {} # 文件夹与其文件列表的映射字典
        self.get_folders_files() # 获取该根路径下的所有文件夹列表和文件列表
     
      def get_folders_files(self):
        '''获取该根路径下的所有文件夹列表和文件列表'''
        for folders, _, files in os.walk(self.root_path):
          self.folder_file_dict[folders] = files
     
      def _split(self, arr, count):
        '''分割文件列表，每500算一份'''
        arrs = []
        while len(arr) > count:
          piece = arr[:count]
          arrs.append(piece)
          arr = arr[count:]
        arrs.append(arr)
        return arrs
     
      # 分割文件并放到新的文件去
      def cut_file(self):
        '''分割并移动到新的文件夹'''
        for each_folder in self.folder_file_dict.keys():
          num = 1 # 以500为倍数，这是1倍
     
          # 将文件路径(摒弃当前路径）转成字符串，用_隔开
          temp_path = os.path.relpath(each_folder, Path(self.root_path).parent)
          temp_path = temp_path.replace(os.sep, "_")
          print(temp_path)
     
          files_list = self.folder_file_dict[each_folder]
          file_group = self._split(files_list, self.count) # 按500来分割
     
          if len(file_group) > 1: # 有超过500个的文件列表
            for each_group in file_group: # 遍历每500份的文件列表
              new_folder = os.path.join(self.root_path, temp_path + "_" + str(num)) # 新路径
              if not os.path.exists(new_folder):
                os.mkdir(new_folder)
              for each_file in each_group:
                old_file = os.path.join(each_folder, each_file)
                new_file = os.path.join(new_folder, each_file)
                print("正在将%s 移动到 %s" % (old_file, new_file))
                os.rename(old_file, new_file)
              num = num + 1
          else: # 无超过500个的文件列表
            new_folder = os.path.join(self.root_path, temp_path) # 新路径
            if not os.path.exists(new_folder):
              os.mkdir(new_folder)
            for each_file in file_group[0]: #
              old_file = os.path.join(each_folder, each_file)
              new_file = os.path.join(new_folder, each_file)
              print("正在将%s 移动到 %s" % (old_file, new_file))
              os.rename(old_file, new_file)
     
     
    if __name__ == '__main__':
      try:
        arg1 = sys.argv[1]
        if os.path.isdir(arg1):
          b_obj = BaiduPanCutter(arg1, 500)
          b_obj.cut_file()
        else:
          print("非文件夹，运行方法：python %s 路径文件夹" % sys.argv[0])
      except IndexError:
        print("未输入待分割的路径文件夹， 运行方法：python %s 路径文件夹" % sys.argv[0])
      os.system("pause")
```

##  运行方式与效果  

运行方式：将以上代码命名为：baidu_pan_500_cutter.py  
通过命令：python baidu_pan_500_cutter.py D:\DCIM\Photos 运行

![](https://img.jbzj.com/file_images/article/202101/202117115625717.jpg?202107115632)

每个文件夹都不会超过500个文件，后续将一个一个的文件夹拖入百度网盘（电脑客户端）即可了。

##  备注信息  

  * 本脚本不涉及任何的删除文件或文件夹的操作，不会出现文件丢失情况。 
  * 兼容非英文的文件夹或文件分割操作。 

以上就是python 实现百度网盘非会员上传超过500个文件的详细内容，更多关于python 百度网盘上传超过500个文件的资料请关注脚本之家其它相关文章！

