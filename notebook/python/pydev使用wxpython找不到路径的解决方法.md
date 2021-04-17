问题：  
pydev使用wx库开发的过程中，import时碰到wx可以识别，但是其它很多函数和变量上面全部是红叉，即无法识别。  
  
**解决方法：**  
  
1、window->preferences->PyDev->Interpreter--Python>Libraries;  
2、加入"C:\Python27\Lib\site-packages\wx-2.8-msw-unicode"和"C:\Python27\Lib\site-
packages\wx-2.8-msw-unicode\wx";  
3、重启eclipse

