直接上代码：

_复制代码_ 代码如下:

  
#!/usr/bin/python  
# -*- coding: utf-8 -*-

import urllib

import os,datetime,string

import sys

from bs4 import BeautifulSoup

reload(sys)

sys.setdefaultencoding('utf-8')

__BASEURL__ = 'http://bj.58.com/'

__INITURL__ = "http://bj.58.com/shoujiweixiu/"

soup = BeautifulSoup(urllib.urlopen(__INITURL__))

lvlELements =
soup.html.body.find('div','selectbarTable').find('tr').find_next_sibling('tr')('a',href=True)

f = open('data1.txt','a')

for element in lvlELements[1:]:

f.write((element.get_text()+'\n\r' ))

url = __BASEURL__ + element.get('href')

print url

soup = BeautifulSoup(urllib.urlopen(url))

lv2ELements = soup.html.body.find('table','tblist').find_all('tr')

for item in lv2ELements:  
addr = item.find('td','t').find('a').get_text()  
phone = item.find('td','tdl').find('b','tele').get_text()  
f.write('地址：'+addr +' 电话:'+ phone + '\r\n\r')

f.close()  

直接执行后，存在 data1.txt中就会有商家的地址和电话等信息。  
BeautifulSoup api 的地址为： http://www.crummy.com/software/BeautifulSoup/bs4/doc/

