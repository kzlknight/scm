本文实例讲述了python清除指定目录内所有文件中script的方法。分享给大家供大家参考。具体如下：

将脚本存储为stripscripts.py  
调用语法 : python stripscripts.py <directory>  
使用范例 : python stripscripts.py d:\myfiles

```python

    # Hello, this is a script written in Python. See http://www.pyhon.org
    import os,sys,string,re
    message = """
     stripscripts 1.1p - Script stripper
     This script will walk a directory (and its subdirectories) and disable
     all scripts (javascript, vbscript...) from .html and .htm files.
     (The scripts will not be deleted, but simply deactivated, so that
     you can review them if you like.)
     Can be usefull for sites you have downloaded with HTTrack or similar tools.
     No more nosey or buggy scripts in your local html files.
     Syntax : python %s <directory>
     Example : python %s d:\myfiles
     This script is public domain. You can freely reuse it.
     The author is
        Sebastien SAUVAGE
        <sebsauvage at sebsauvage dot net>
        http://sebsauvage.net
     More quick & dirty scripts are available at http://sebsauvage.net/python/
    """ % ((sys.argv[0], )*2)
    def stripscripts ( directoryStart ) :
      os.path.walk( directoryStart, callback, '' )
    def callback ( args, directory, files ) :
      print 'Scanning',directory
      for fileName in files:
        if os.path.isfile( os.path.join(directory,fileName) ) :
          if string.lower(os.path.splitext(fileName)[1]) in ['.html','.htm'] :
            stripScriptFromHtml ( os.path.join(directory,fileName) )
    def stripScriptFromHtml ( filepath ) :
      print ' Processing',os.path.split(filepath)[1]
      file = open(filepath, 'rb')
      html = file.read()
      file.close()
      regexp = re.compile(r'<script.*?>', re.IGNORECASE)
      html = regexp.sub('<script language="MonthyPythonsScript">',html)
      file = open(filepath, 'w+')
      file.write(html)
      file.close()
    if len(sys.argv) > 1 :
      stripscripts( sys.argv[1] )
    else:
      print message
```

希望本文所述对大家的Python程序设计有所帮助。

