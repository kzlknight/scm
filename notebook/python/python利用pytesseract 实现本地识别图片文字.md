
```python

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    import glob
    from os import path
    import os
    import pytesseract
    from PIL import Image
    from queue import Queue
    import threading
    import datetime
    import cv2
    
    def convertimg(picfile, outdir):
      '''调整图片大小，对于过大的图片进行压缩
      picfile:  图片路径
      outdir：  图片输出路径
      '''
      img = Image.open(picfile)
      width, height = img.size
      while (width * height > 4000000): # 该数值压缩后的图片大约 两百多k
        width = width // 2
        height = height // 2
      new_img = img.resize((width, height), Image.BILINEAR)
      new_img.save(path.join(outdir, os.path.basename(picfile)))
    
    
    def baiduOCR(ts_queue):
      while not ts_queue.empty():
        picfile = ts_queue.get()
        filename = path.basename(picfile)
        outfile = 'D:\Study\pythonProject\scrapy\IpProxy\port_zidian.txt'
        img = cv2.imread(picfile, cv2.IMREAD_COLOR)
        print("正在识别图片：\t" + filename)
        message = pytesseract.image_to_string(img,lang = 'eng')
        message = message.replace('', '')
        message = message.replace('\n', '')
        # message = client.basicAccurate(img)  # 通用文字高精度识别，每天 800 次免费
        #print("识别成功！"))
        try:
          filename1 = filename.split('.')[0]
          filename1 = ''.join(filename1)
          with open(outfile, 'a+') as fo:
            fo.writelines('\'' + filename1 + '\'' + ':' + message + ',')
            fo.writelines('\n')
            # fo.writelines("+" * 60 + '\n')
            # fo.writelines("识别图片：\t" + filename + "\n" * 2)
            # fo.writelines("文本内容：\n")
            # # 输出文本内容
            # for text in message.get('words_result'):
            #   fo.writelines(text.get('words') + '\n')
            # fo.writelines('\n' * 2)
          os.remove(filename)
          print("识别成功！")
        except:
          print('识别失败')
    
    
    
        print("文本导出成功！")
        print()
    def duqu_tupian(dir):
      ts_queue = Queue(10000)
    
      outdir = dir
      # if path.exists(outfile):
      #   os.remove(outfile)
      if not path.exists(outdir):
        os.mkdir(outdir)
      print("压缩过大的图片...")
      # 首先对过大的图片进行压缩，以提高识别速度，将压缩的图片保存与临时文件夹中
      try:
        for picfile in glob.glob(r"D:\Study\pythonProject\scrapy\IpProxy\tmp\*"):
          convertimg(picfile, outdir)
        print("图片识别...")
        for picfile in glob.glob("tmp1/*"):
          ts_queue.put(picfile)
          #baiduOCR(picfile, outfile)
          #os.remove(picfile)
        print('图片文本提取结束！文本输出结果位于文件中。' )
        #os.removedirs(outdir)
        return ts_queue
      except:
        print('失败')
    
    if __name__ == "__main__":
    
      start = datetime.datetime.now().replace(microsecond=0)
      t = 'tmp1'
      s = duqu_tupian(t)
      threads = []
      try:
        for i in range(100):
          t = threading.Thread(target=baiduOCR, name='th-' + str(i), kwargs={'ts_queue': s})
          threads.append(t)
        for t in threads:
          t.start()
        for t in threads:
          t.join()
        end = datetime.datetime.now().replace(microsecond=0)
        print('删除耗时：' + str(end - start))
      except:
        print('识别失败')
```

实测速度慢，但用了多线程明显提高了速度，但准确度稍低，同样高清图片，90百分识别率。还时不时出现乱码文字，乱空格，这里展现不了，自己实践吧，重点免费的，随便识别，通向100张图片，用时快6分钟了，速度慢了一倍，但是是免费的，挺不错的了。

以上就是python利用pytesseract 实现本地识别图片文字的详细内容，更多关于python 识别图片文字的资料请关注脚本之家其它相关文章！

