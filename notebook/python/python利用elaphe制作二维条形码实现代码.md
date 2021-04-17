手机上的二维码识别程序已经做的很好了，“我查查”用起来很不错的  
  
我搜集了几个二维条码生成网站：  
  
http://www.morovia.com/free-online-barcode-generator/qrcode-maker.php  
  
http://qrencode.sinaapp.com/  
  
http://www.mayacode.com/  
  
作为一个程序猿，我们也要懂得如何制作二维条形码  
  
python的elaphe模块帮我们解决了问题  

_复制代码_ 代码如下:

  
from elaphe import barcode  
def get_barcode(info):  
a = barcode('qrcode',info,options=dict(version=9, eclevel='M'), margin=10,
data_mode='8bits')  
a.show()  
if __name__=='__main__':  
info = raw_input("input a string: ")  
get_barcode(info)  

  
用python，一切变得那么简单！

