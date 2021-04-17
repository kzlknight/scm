1. 安装python虚拟环境   

_复制代码_ 代码如下:

  
virtualenv --no-site-packages env  

2. 安装pyramid   

_复制代码_ 代码如下:

  
$ env/bin/easy_install pyramid  

3. 使用alchemy模板，创建一个项目   

_复制代码_ 代码如下:

  
pcreate -s alchemy MyProject  

4. 安装项目的依赖   

_复制代码_ 代码如下:

  
python setup.py develop  

5. 运行单元测试   

_复制代码_ 代码如下:

  

