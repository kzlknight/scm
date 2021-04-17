工欲善其事,必先利其器.python是解释型的语言,但是在windows下如果要执行程序的话还得加个python
shell的话,未免也太麻烦了.而这里所说的东西就是将python程序转换为exe文件.下面是一些常用的工具,不过似乎py2exe应用的更加广泛一些.  
py2exe http://py2exe.sf.net  
只支持windows平台，应该是大家听到最多的一个名字了，用户不少，所以有问题的话在它的mail
list里面很容易找到答案。文档中提到了"无法找到某某code"、使用opengl等模块的问题  
  
  
PyPackage http://codereactor.net/projects/pypack/index.html  
我觉得py2exe等等工具还是罗嗦得像唐僧，需要在配置文件中写上需要的数据文件。作者完全无视这样一个事实：我需要发布可执行文件的时候，程序已经完工了，所有的数据文件就在主程序所在目录下，所以多数情况下，根本不用到别的地方搜索。现在终于有人站了出来，PyPackage实际上并不是一个程序打包的工具，而只是简化py2exe的操作，甚至可以自动调用InnoSetup
5制作安装文件――不过这个软件并不智能，会打包很多不需要的文件  
  
  
Installer http://www.mcmillan-inc.com/installer_dnld.html  
可以产生windows、linux平台的可执行文件，现在作者主页连不上去了，但是搜索一下可以在其它地方下载  
自带一个小程序写配置文件，如果程序较复杂，还是需要手工修改这个配置文件。支持从py15以来的所有Python版本  
2005年9月，冰冻牡蛎更新：Giovanni Bajo获得Gordon McMillan's
Installer的授权、版权改变为GPL，并在http://pyinstaller.hpcf.upr.edu/继续开发PYinstaller。2006年9月更新：这里可以看到Gordon
McMillan's的原始网站的镜像  
  
  
Python自带的freeze.py（不过windows版本不带这个，你可以自己下载Python的源程序再找）。这个是我最不推荐的一种方法（为什么？自己看），不过如果你的Python程序要发布到其它工具不支持的平台上，可以考虑这个方法  
  
  
新出来的Pyco http://www.pythonapocrypha.com/projects/pyco/  
还没用过  
  
  
Squeeze http://starship.python.net/crew/fredrik/ipa/squeeze.htm  
还没用过，只支持Python 1.4  
  
  
cx_Freeze http://starship.python.net/crew/atuining/cx_Freeze/  
winodws、linux平台。简单的程序甚至都不需要写配置文件  
  
  
Stand alone Python for Windows http://arctrix.com/nas/python/standalone.html  
如果你不介意源程序太过"暴露"的话，用这个吧  
会不会觉得Updated: Sun, 09 Apr 2000 18:39:54 -0600
扎眼？如果你看一看它的VC源代码，就不会这么想了――其实这是普遍适用于ｗｉｎ系统的方法，无论是９８、２０００或者ｘｐ。也许也可以用到ｌｉｎｕｘ上――我不懂ｌｉｎｕｘ，如果真的可以这么做，还请告诉我。  
  
  
py2app http://undefined.org/python/  
支持linux平台的工具可能也支持mac os，或者直接使用这个py2app。具体就不知道了，只吃过苹果，还没玩过苹果呢  
  
  
Movable Python http://www.voidspace.org.uk/python/movpy/  
这个其实是使用py2exe制作的、可以放在U盘上的绿色Python。有使用py2app制作苹果版movpy和用cx_Freeze制作Linux版movpy的计划。懒到都不愿意学习py2exe、py2app或者cx_Freeze的人可以看看。  
  
  
Shed Skin - A Python-to-C++ Compiler： 试验项目，windows上，连他的例子我都没有编译成功 :(。  
  
  
Psyco： 给Python程序加速的东西，看不出对发布Python程序的直接好处，并且作者以后将致力于PyPy。  
  
  
PyPy： 项目目标是纯Python实现的Python、速度比CPython快，将来可以帮助实现编译Python。  
  
  
pyc： Python compiler in
Python，一个用纯Python写的Python的bytecode编译器，可以优化输出的pyc文件。和PyPy一样，现在还看不出对发布Python程序的直接好处。只有py24的bytecode。pyc是pyvm这个新的python虚拟机的一部分。  
  
  
Jungle：
使用GNU工具（as、ld和winres）把Python程序编译到windows的exe可执行文件。该可执行文件只使用基于python24的的pythonic.dll。猜测它支持的模块仅限于内部模块以及jungle.jgl列出的模块。只有可执行文件下载，而这个可执行文件也是用Jungle自己编译的。目前版本号都到1.10了，经常看0.xx的版本号，这个数字好大啊，娃哈哈。  
  
  
另类的方法，对Python语言特性都还不是100％支持，众多的CPython模块也不可以使用，还有，我也没有试过：  
  
  
for .NET的Python编译器（如Visual Python、IronPython），不过我可不喜欢为了一个芝麻大的软件安装.NET
framework  
  
用jython，然后用jbuilder、jsmooth、NativeJ之类的包裹一下，或者用gcj编译成本地代码  
在最后,给一个人学习py2exe的文章,帮助学习:  
  
最近学了一点PYTHON，想把PYTHON写的程序转换成EXE文件，在网上查到了资料后发现了这个东东  
写下来做一下记录。  
  
英文教程：  
http://www.py2exe.org/index.cgi/Tutorial  
  
  
Python 2.5 + Py2exe  
  
工作目录：c:\python25  
  
  
首先随便写一个程序  
hello.py  
  
print "Hello World!"  
  
  
测试一下是否能运行  
python hello.py  
结果：Hello World  
  
到www.py2exe.org下载 PY2exe ,或者在SF上下载  
http://sourceforge.net/project/showfiles.php?group_id=15583  
  
接下来直接安装PY2EXE包。。它是一个安装文件。。直接装就行了。  
  
下在编写一个设置的PY文件 setup.py  
  
from distutils.core import setup  
import py2exe  
setup(console=['hello.py'])  
  
  
运行：python setup.py py2exe  
出现以下信息后，在DIST目录里，就会有一个hello.exe  
即成功。  
  
running py2exe  
*** searching for required modules ***  
*** parsing results ***  
creating python loader for extension 'zlib'  
creating python loader for extension 'unicodedata'  
creating python loader for extension 'bz2'  
*** finding dlls needed ***  
*** create binaries ***  
*** byte compile python files ***  
byte-compiling C:\Tutorial\build\bdist.win32\winexe\temp\bz2.py to bz2.pyc  
byte-compiling C:\Tutorial\build\bdist.win32\winexe\temp\unicodedata.py to
unicodedata.pyc  
byte-compiling C:\Tutorial\build\bdist.win32\winexe\temp\zlib.py to zlib.pyc  
skipping byte-compilation of c:\Python24\lib\StringIO.py to StringIO.pyc  
  
[skipping many lines for brevity]  
  
skipping byte-compilation of c:\Python24\lib\warnings.py to warnings.pyc  
*** copy extensions ***  
*** copy dlls ***  
copying c:\Python24\lib\site-packages\py2exe\run.exe ->
C:\Tutorial\dist\hello.exe  
  
*** binary dependencies ***  
Your executable(s) also depend on these dlls which are not included,  
you may or may not need to distribute them.  
  
Make sure you have the license if you distribute any of them, and  
make sure you don't distribute files belonging to the operating system.  
  
ADVAPI32.dll - C:\WINDOWS\system32\ADVAPI32.dll  
USER32.dll - C:\WINDOWS\system32\USER32.dll  
SHELL32.dll - C:\WINDOWS\system32\SHELL32.dll  
KERNEL32.dll - C:\WINDOWS\system32\KERNEL32.dll  
  

