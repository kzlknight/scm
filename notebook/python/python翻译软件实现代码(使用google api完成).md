_复制代码_ 代码如下:

  
# -*- coding: utf-8 -*-  
import httplib  
from urllib import urlencode  
import re

def out(text):  
p = re.compile(r'","')  
m = p.split(text)  
print m[0][4:].decode('UTF-8').encode('GBK')

if __name__=='__main__':  
while True:  
word=raw_input('Input the word you want to search:')  
text=urlencode({'text':word})  
h=httplib.HTTP('translate.google.cn')  
h.putrequest('GET', '/translate_a/t?client=t&hl=zh-CN&sl=en&tl=zh-
CN&ie=UTF-8&oe=UTF-8&'+text)  
h.endheaders()  
h.getreply()  
f = h.getfile()  
lines = f.readlines()  
out(lines[0])  
f.close()  

haskell版

_复制代码_ 代码如下:

  
module Main where

import Network.HTTP  
import Text.Regex.Posix

main = do  
putStrLn "Input the word you want to search:"  
word <- getLine  
handle <- simpleHTTP (getRequest $
"http://translate.google.cn/translate_a/t?client=t&hl=zh-CN&sl=en&tl=zh-
CN&ie=UTF-8&oe=UTF-8&" ++ (text word))  
content <- getResponseBody handle  
let match = (content =~ "\",\""::(String,String,String))  
putStrLn $ drop 4 $ first match  
main

text word = urlEncodeVars [("text",word)]

first::(String,String,String)->String  
first (x,_,_) = x  

  
  
作者：Hevienz

