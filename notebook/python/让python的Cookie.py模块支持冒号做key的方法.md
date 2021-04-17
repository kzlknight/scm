为了做好兼容性，只能选择兼容:冒号。  
  
很简单，修改一下Cookie.Morsel  

_复制代码_ 代码如下:

  
#!/usr/bin/python  
# -*- coding: utf-8 -*-  
"""MorselHook, fix Cookie.CookieError: Illegal key value: ys-tab:entrance:e  
"""  
  
import Cookie  
import string  
  
_Morsel = Cookie.Morsel  
  
class MorselHook(_Morsel):  
"""  
>>> import inspect  
>>> (inspect.getargspec(MorselHook.set)[3])[0]  
"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'*+-.^_`|~:"  
>>> cookie = Cookie.SimpleCookie()  
>>> cookie.load("ys-tab:entrance:e=abc;
webpy_session_id=75eb60dcc83e2d902146af0bb7f47afe61fbd2b2")  
>>> print cookie  
Set-Cookie: webpy_session_id=75eb60dcc83e2d902146af0bb7f47afe61fbd2b2;  
Set-Cookie: ys-tab:entrance:e=abc;  
"""  
def set(self, key, val, coded_val, LegalChars=Cookie._LegalChars+':',
idmap=string._idmap, translate=string.translate):  
return super(MorselHook, self).set(key, val, coded_val, LegalChars, idmap,
translate)  
  
Cookie.Morsel = MorselHook  
  
# 在你需要使用到Cookie的地方先让上面的代码执行一遍  
  
  
if __name__ == '__main__':  
import doctest  
doctest.testmod()  

