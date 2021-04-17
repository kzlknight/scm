相对之前版本更新内容：

※ 根据UP主分类存放导出的视频。

※ 新增一种标题格式

注意：需要安装ffmpeg才可使用  
ffmpeg下载地址： [ https://ffmpeg.zeranoe.com/builds/
](https://ffmpeg.zeranoe.com/builds/)  
ffmpeg安装方法：  
解压好下载的压缩包后，再将bin目录加入Path环境变量中 按Win+R 运行 输入cmd 在弹出的框框中输入 ffmpeg
，如果没有出现"既不是内部或外部命令"之类的话就是安装成功了  
参考链接： [ https://www.jb51.net/article/153806.htm
](https://www.jb51.net/article/153806.htm)  
运行截图

![](https://img.jbzj.com/file_images/article/202012/202012010810371.png)

工具源码

```python

    import os
    import json
    import random
    import time
    import requests
    
    # 清除所有空格
    def clearSpace(str):
     return str.replace(" ", "").replace("　", "");
    
    
    # 获取指定Uid的Up主名
    def getUpNameByUid(uid):
     try:
     url = 'https://space.bilibili.com/' + str(uid)
     html = requests.get(url)
     html.encoding = 'UTF-8'
     html = html.text
     index1 = html.find("<title>") + len("<title>")
     index2 = html.find("的个人空间", index1)
     result = html[index1:index2]
     if (result != ""):
      return result
     else:
      return uid
     except Exception:
     return uid
    
    # 获取时间戳
    def getTimeStamp():
     t = time.localtime(time.time())
     return str(t.tm_year) + '_' + str(t.tm_mon) + '_' + str(t.tm_mday) + '_' + str(t.tm_hour) + \
      str(t.tm_min) + str(t.tm_sec) + str(random.randint(10, 99))
    
    
    # 更正文件名
    def correctFileName(name):
     n_list = list(name)
     for i in range(0, len(n_list)):
     index = 0
     for i in n_list:
      if (
       i == '\\' or i == '/' or i == ':' or i == '*' or i == '?' or i == '\"' or i == '<' or i == '>' or i == '|'):
      n_list.pop(index)
      index = index + 1
     return ''.join(n_list)
    
    # 读取json文件
    def getVideoName(path):
     f = open(path, encoding='utf-8')
     setting = json.load(f)
     try:
     result = setting['page_data']['download_subtitle'] # 注意多重结构的读取语法
     except KeyError:
     try:
      result = setting['title'] + ' 第' + setting['ep']['index'] + '话 ' + setting['ep']['index_title']
     except KeyError:
      try:
      result = setting['title']
      except KeyError:
      result = getTimeStamp()
     return result
    
    
    def getVideoOwner(path):
     try:
     f = open(path, encoding='utf-8')
     setting = json.load(f)
     return clearSpace(getUpNameByUid(setting['owner_id']))
     except Exception:
     return ""
    
    # 获取文件列表
    def getFileList(file_dir):
     # 定义四个列表
     title = []
     owner = []
     videoPath = []
     audioPath = []
     # 遍历文件目录
     for root, dirs, files in os.walk(file_dir):
     if ('entry.json' in files):
      title.append(getVideoName(str(root) + '\\entry.json'))
      owner.append(getVideoOwner(str(root) + '\\entry.json'))
     if ('video.m4s' in files and 'audio.m4s' in files):
      videoPath.append(str(root) + '\\video.m4s')
      audioPath.append(str(root) + '\\audio.m4s')
     if (len(title) < len(videoPath)):
      title.append(getTimeStamp())
     if ('0.blv' in files):
      title.pop()
     return [title, owner, videoPath, audioPath]
    
    
    # 输出mp4文件
    def getMP4(title, owner, video_path, audio_path):
     # 生成输出目录
     if not os.path.exists("./output"):
     os.mkdir("./output")
     # 循环生成MP4文件
     for i in title:
     reName = correctFileName(i)
     # 开始生成MP4文件
     if not os.path.exists("./output/" + reName + ".mp4"):
      # 获取临时文件时间戳
      t_stamp = getTimeStamp()
      # 开始合成
      os.system(
      "ffmpeg -i " + video_path[title.index(i)] + " -i " + audio_path[
       title.index(i)] + " -codec copy ./output/" + t_stamp + ".mp4")
      # 设置所属Up主
      curOwner = owner[title.index(i)]
      if curOwner != "":
      if not os.path.exists("./output/" + curOwner):
       os.mkdir("./output/" + curOwner)
      os.rename("./output/" + t_stamp + ".mp4", "./output/" + curOwner + "/" + reName + ".mp4")
      else:
      # 将临时文件时间戳改为标题名
      os.rename("./output/" + t_stamp + ".mp4", "./output/" + reName + ".mp4")
      print("正在合成...")
      print("标题：" + reName)
      print("UP主：" + curOwner)
      print("视频源：" + video_path[title.index(i)])
      print("音频源：" + audio_path[title.index(i)])
      time.sleep(1)
    
    print("欢迎使用批量合成M4S工具 ver2.5")
    fileDir = str(input("请输入含M4S文件的目录:"))
    f = getFileList(fileDir)
    getMP4(f[0], f[1], f[2], f[3])
    print("合成完毕")
```

已编译好的可执行文件(EXE)：

链接: [ https://pan.baidu.com/s/1bLOg6GGJ5Wp7gcW73sXzvg
](https://pan.baidu.com/s/1bLOg6GGJ5Wp7gcW73sXzvg)

提取码: yqvm

到此这篇关于python批量合成bilibili的m4s缓存文件为MP4格式
ver2.5的文章就介绍到这了,更多相关python批量合成bilibili缓存文件内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

