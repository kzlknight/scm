代码实现如下:

```python

    import win32com.client,os,time
     
    def word_encryption(path, password):
      # 若加密保存.docx时，覆盖原文件，则无法成功添加密码。但是保存为另一个文件名，则可以添加密码。
      # 因此将A存为B，删A，再将B改为A。
      dirname, tempname = os.path.split(path)
      path_temp = os.path.join(dirname, tempname)
      while os.path.exists(path_temp):
        tempname = f'{len(tempname)}' + tempname
        path_temp = os.path.join(dirname, tempname)
      def encryption(fp, pt, pw):
        word_app = win32com.client.Dispatch('Word.Application')
        word_app.Visible = 0
        word_app.DisplayAlerts = 0
        doc = word_app.Documents.Open(fp, False, False, False, '')
        doc.SaveAs2(pt, None, False, pw)
        doc.Close()
        word_app.Quit()
     
      encryption(path, path_temp, password)
      os.remove(path) # 删除原文件
      os.rename(path_temp, path) # 改临时文件名称为原文件名称
      time.sleep(0.5) # 不要删除,不要删除
    def word_decryption(path, password):
      # 若加密保存.docx时，覆盖原文件，则无法成功添加密码。但是保存为另一个文件名，则可以添加密码。
      # 因此将A存为B，删A，再将B改为A。
      dirname, tempname = os.path.split(path)
      path_temp = os.path.join(dirname, tempname)
      while os.path.exists(path_temp):
        tempname = f'{len(tempname)}' + tempname
        path_temp = os.path.join(dirname, tempname)
      def decryption(fp, pt, pw):
        word_app = win32com.client.Dispatch('Word.Application')
        word_app.Visible = 0
        word_app.DisplayAlerts = 0
        doc = word_app.Documents.Open(fp, False, False, False, key)
        doc.SaveAs2(pt, None, False, pw)
        doc.Close()
        word_app.Quit()
     
      decryption(path, path_temp, password)
      os.remove(path) # 删除原文件
      os.rename(path_temp, path) # 改临时文件名称为原文件名称
      time.sleep(0.5) # 不用删除
     
    def elistdir(path):
      for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path) and file_path==path:#排除子路径
          elistdir(file_path)
          #print(file_path)
        elif os.path.splitext(file_path)[1]=='.docx':
          #list_name.append(file_path)
          
          if file_path != '':
            print(file_path)
            try:
              word_encryption(file_path, key)
            except:
              pass
     
    def dlistdir(path):
      for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path) and file_path==path:#排除子路径
          dlistdir(file_path)
          #print(file_path)
        elif os.path.splitext(file_path)[1]=='.docx':
          #list_name.append(file_path)
          
          if file_path != '':
            print(file_path)
            try:
              word_decryption(file_path, '')
            except:
              pass
     
    if __name__ == '__main__':
      key='12345'                 #加密解密密匙
      filedir=r"C:\Users\Administrator\Desktop"# 指定路径不包含子路径
      elistdir(filedir) #遍历word
      print('encrytion sucess\n Waiting...')
      time.sleep(2)#设置时间随意操作
      dlistdir(filedir) #遍历word
      print('decrytion Done')
```

实现:

![](https://img.jbzj.com/file_images/article/202012/2020122914541240.png)

到此这篇关于Python实现对word文档添加密码去除密码的示例代码的文章就介绍到这了,更多相关Python
word文档添加密码去除密码内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

