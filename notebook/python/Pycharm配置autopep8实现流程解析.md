关于PEP 8

PEP 8，Style Guide forPythonCode，是Python官方推出编码约定，主要是为了保证 Python
编码的风格一致，提高代码的可读性。

官网地址： [ https://www.python.org/dev/peps/pep-0008/
](https://www.python.org/dev/peps/pep-0008/)

关于Autopep8

Autopep8是自动将Python代码格式化为符合PEP
8风格的工具。它使用pycodestyle工具来确定代码的哪些部分需要被格式化。Autopep8能够修复大部分pycodestyle检测的格式问题。

github地址： [ https://github.com/hhatto/autopep8
](https://github.com/hhatto/autopep8)

下载安装Autopep8

pip install autopep8

使用Autopep8

命令行使用方式如下

$ autopep8 --in-place --aggressive --aggressive <filename>  
$ autopep8 --in-place --aggressive --aggressive Student.py  

Pycharm配置Autopep8方法

