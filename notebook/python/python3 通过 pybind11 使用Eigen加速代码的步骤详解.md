python是很容易上手的编程语言，但是有些时候使用python编写的程序并不能保证其运行速度（例如：while 和
for），这个时候我们就需要借助c++等为我们的代码提速。下面是我使用pybind11调用c++的Eigen库的简单介绍:

第一步：准备系统和IDE：

  * Windows 10 
  * vs2015 (用于调试c++代码) 
  * vscode (调试python代码) 

第二步：python虚拟环境：

1.创建虚拟python虚拟环境： 在vscode的terminal中执行

```python

    python -m venv env
```

2.下载 Eigen : 将Eigen解压到当前目录命名为 eigen-3.3.8

3.在vscode的terminal中激活虚拟环境：

```python

    ./env/Scripts/Activate.ps1
```

4.安装pybind11:

```python

    pip install pybind11
```

安装numpy==1.19.3（使用1.19.4可能会有问题） :

```python

     pip install numpy==1.19.3 
```

第三步：使用vs2015编写cpp_python.cpp, 并保证没有bug

```python

    #include <Eigen/Dense>
    using namespace std
    using namespace Eigen
    MatrixXd add_mat(MatrixXd A_mat, MatrixXd B_mat)
    {
      return A_mat + B_mat;
    }
```

第四步：使用pybind11为cpp_python.cpp添加python接口

```python

    // cpp_python.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
    //
    #include <pybind11/pybind11.h>
    #include <pybind11/eigen.h>
    #include<pybind11/numpy.h>
    #include<fstream>
    #include<iostream>
    #include <Eigen/Dense>
    using namespace std;
    using namespace Eigen;
    
    MatrixXd add_mat(MatrixXd A_mat, MatrixXd B_mat)
    {
    	return A_mat + B_mat;
    }
    
    namespace py = pybind11;
    PYBIND11_MODULE(add_mat_moudle, m)
    {
    	m.doc() = "Matrix add";//解释说明
    	m.def("mat_add_py"/*在pyhon中使用的函数名*/, &add_mat);
    }
```

第五步：设置setup.py用来编译c++代码

```python

    from setuptools import setup
    from setuptools import Extension
    
    add_mat_module = Extension(name='add_mat_moudle', # 模块名称
                  sources=['cpp_python.cpp'],  # 源码
                  include_dirs=[r'.\eigen-3.3.8',
                        r'.\env\Scripts',   # 依赖的第三方库的头文件
                         r'.\env\Lib\site-packages\pybind11\include']
                  )
    
    setup(ext_modules=[add_mat_module])
```

第六步：编译测试

这是我当前的工作目录

![](https://img.jbzj.com/file_images/article/202012/2020120710154646.png)

注意：我的cpp_python.cpp和setup.py是在同一个文件夹下。

```python

    执行: "python .\setup.py build_ext --inplace"就会得下面的结果，生成.pyd文件表明我们已经编译成功。
```

![](https://img.jbzj.com/file_images/article/202012/2020120710154647.png)

运行测试：

![](https://img.jbzj.com/file_images/article/202012/2020120710154748.png)

到此这篇关于python3 通过 pybind11 使用Eigen加速代码的步骤详解的文章就介绍到这了,更多相关python3 pybind11
Eigen加速代码内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

