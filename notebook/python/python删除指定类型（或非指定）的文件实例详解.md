本文实例分析了python删除指定类型（或非指定）的文件用法。分享给大家供大家参考。具体如下：  
如下，删除目录下非源码文件  

```python

    import os 
    import string 
    def del_files(dir,topdown=True): 
      for root, dirs, files in os.walk(dir, topdown): 
        for name in files: 
          pathname = os.path.splitext(os.path.join(root, name)) 
          if (pathname[1] != ".cpp" and pathname[1] != ".hpp" and pathname[1] != ".h"): 
            os.remove(os.path.join(root, name)) 
            print(os.path.join(root,name)) 
    dir = os.getcwd() 
    print(dir) 
    del_files(dir)
    #will delete the self .py file after run !!!-_- 
    os.removedirs(dir)
    #delete the empty directory recursively 
    
```

以上功能，遍历文件夹 也可以用函数 os.listdir (dirname) 。只不过其与os.walk（dir, topdown） 的方式还是略有差异。  
listdir 是按命名规则，对文件夹和文件、统一采用深度优先搜索的方式，进行列举  
而os.walk的标准例程一般是先遍历文件，后遍历文件夹。

**学习要点：**

**os类的函数：**

os.getenv()和os.putenv()函数分别用来读取和设置环境变量。  
os.system()函数用来运行shell命令。  
os.linesep字符串给出当前平台使用的行终止符。例如，Windows使用'\r\n'，Linux使用'\n'而Mac使用'\r'。

**与路径相关的os函数**

os.listdir(dirname)：列出dirname下的目录和文件  
os.getcwd()：获得当前工作目录，即当前Python脚本工作的目录路径。  
os.curdir:返回当前目录（'.')  
os.chdir(dirname):改变工作目录到dirname

os.path.isdir(name):判断name是不是一个目录，name不是目录就返回false  
os.path.isfile(name):判断name是不是一个文件，不存在name也返回false  
os.path.exists(name):判断是否存在文件或目录name

os.path.getsize(name):获得文件大小，如果name是目录返回0  
os.path.abspath(name):获得绝对路径  
os.path.normpath(path):规范path字符串形式

os.path.split(name):分割文件名与目录（事实上，如果你完全使用目录，它也会将最后一个目录作为文件名而分离，同时它不会判断文件或目录是否存在）  
>>> os.path.split('/home/swaroop/byte/code/poem.txt')  
('/home/swaroop/byte/code', 'poem.txt')  
os.path.splitext():分离文件名与扩展名

os.rename(name1, name2) 重命名文件  
如修改文件类型，os.rename(os.path.join(root, name), pathname[0]+".cpp")
pathname[0]为文件名，pathname[1]为扩展名

os.path.join(path,name):连接目录与文件名或目录  
os.path.basename(path):返回文件名  
os.path.dirname(path):返回文件路径

os.walk返回三元组形式，相当于三元组列表，遍历path，返回一个对象，他的每个部分都是一个三元组,('目录x'，[目录x下的目录list]，目录x下面的文件)

string类型的数据，可以使用==, !=等运算符

多参考python帮助文档，很强大。

希望本文所述对大家的Python程序设计有所帮助。

