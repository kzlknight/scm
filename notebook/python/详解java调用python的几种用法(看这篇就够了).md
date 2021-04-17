##  java调用python的几种用法如下：

  * 在java类中直接执行python语句 
  * 在java类中直接调用本地python脚本 
  * 使用Runtime.getRuntime()执行python脚本文件（推荐） 
  * 调用python脚本中的函数 

###  准备工作:

创建maven工程，结构如下：

![](https://img.jbzj.com/file_images/article/202012/20201210142950105.png)

到官网 [ https://www.jython.org/download.html
](https://www.jython.org/downloads.html)
下载Jython的jar包或者在maven的pom.xml文件中加入如下代码：

```python

    <dependency>
      <groupId>org.python</groupId>
      <artifactId>jython-standalone</artifactId>
      <version>2.7.0</version>
    </dependency>
```

###  1.在java类中直接执行python语句

创建JavaRunPython.java类：

```python

    package com.test;
    
    import org.python.util.PythonInterpreter;
    
    public class JavaRunPython {
      
      public static void main(String[] args) {
        PythonInterpreter interpreter = new PythonInterpreter();
        interpreter.exec("a='hello world'; ");
        interpreter.exec("print a;");
      }
    
    }
```

输出结果如下：

![](https://img.jbzj.com/file_images/article/202012/20201210142950106.png)

出现的console: Failed to install '':
java.nio.charset.UnsupportedCharsetException: cp0.并不是错误，而是兼容所导致，解决方法如下：

![](https://img.jbzj.com/file_images/article/202012/20201210142950107.png)

![](https://img.jbzj.com/file_images/article/202012/20201210142951108.png)

![](https://img.jbzj.com/file_images/article/202012/20201210142951109.png)

###  2.在java中直接调用python脚本

在本地的D盘创建一个python脚本，文件名字为javaPythonFile.py，文件内容如下：

```python

    a = 1
    b = 2
    print (a + b)
```

创建JavaPythonFile.java类，内容如下：

```python

    package com.test;
    
    import org.python.util.PythonInterpreter;
    
    public class JavaPythonFile {
    
      public static void main(String[] args) {
        PythonInterpreter interpreter = new PythonInterpreter();
        interpreter.execfile("D:\\javaPythonFile.py");
      }
    }
```

输出结果如下：

![](https://img.jbzj.com/file_images/article/202012/20201210142951110.png)

###  3.使用Runtime.getRuntime()执行python脚本文件，推荐使用

在本地的D盘创建一个python脚本，文件名字为Runtime.py，文件内容如下：

```python

    print('RuntimeDemo')
```

创建RuntimeFunction.java类，内容如下：

```python

    package com.test;
    
    import java.io.BufferedReader;
    import java.io.IOException;
    import java.io.InputStreamReader;
    
    public class RuntimeFunction {
      public static void main(String[] args) {
        Process proc;
        try {
          proc = Runtime.getRuntime().exec("python D:\\Runtime.py");
          BufferedReader in = new BufferedReader(new InputStreamReader(proc.getInputStream()));
          String line = null;
          while ((line = in.readLine()) != null) {
            System.out.println(line);
          }
          in.close();
          proc.waitFor();
        } catch (IOException e) {
          e.printStackTrace();
        } catch (InterruptedException e) {
          e.printStackTrace();
        } 
      }
    }
```

运行结果如下：

![](https://img.jbzj.com/file_images/article/202012/20201210142951111.png)

###  4.调用python脚本中的函数

在本地的D盘创建一个python脚本，文件名字为add.py，文件内容如下：

```python

    def add(a,b):
      return a + b
```

创建Function.java类，内容如下：

```python

    package com.test;
    
    import org.python.core.PyFunction;
    import org.python.core.PyInteger;
    import org.python.core.PyObject;
    import org.python.util.PythonInterpreter;
    
    public class Function {
      
      public static void main(String[] args) {
        PythonInterpreter interpreter = new PythonInterpreter();
        interpreter.execfile("D:\\add.py");
            
        // 第一个参数为期望获得的函数（变量）的名字，第二个参数为期望返回的对象类型
        PyFunction pyFunction = interpreter.get("add", PyFunction.class);
        int a = 5, b = 10;
        //调用函数，如果函数需要参数，在Java中必须先将参数转化为对应的“Python类型”
        PyObject pyobj = pyFunction.__call__(new PyInteger(a), new PyInteger(b)); 
        System.out.println("the anwser is: " + pyobj);
      }
    
    }
```

运行结果如下：

![](https://img.jbzj.com/file_images/article/202012/20201210142951112.png)

到此这篇关于详解java调用python的几种用法(看这篇就够了)的文章就介绍到这了,更多相关java调用python内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

