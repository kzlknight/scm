_复制代码_ 代码如下:

  
# -*- coding:utf-8 -*-  
import httplib  
import urllib  
import string  
import re  
def getContent(): #从网站中获取所有内容  
conn = httplib.HTTPConnection("tu.duowan.com")  
conn.request("GET", "/m/meinv/index.html")  
r = conn.getresponse()  
print r.status, r.reason  
data1 = r.read()#.decode('utf-8') #编码根据实际情况酌情处理  
return data1

def getImageUrl(data): #将获取到img链接写到sour.txt文件中国  
sour = open("test\\sour.txt", 'w')  
pplen =
len("http://s1.dwstatic.com/group1/M00/37/2A/e2c30e89184ea942a4be9c1f7ba217a5.jpg")  
for i in range(len(data) - 3):  
if data[i] == 'i' and data[i + 1] == 'm' and data[i + 2] == 'g':  
for j in xrange(i + 9, i + 9 + pplen):  
sour.write(data[j])  
sour.write('\n')  
sour.close()

  
def downImage(): #根据test\\sour.txt里面的url自动下载图片  
tt = 0 #name  
sour = open('test\\sour.txt')  
while 1:  
line = sour.readline()  
if line:  
Len = len(line)  
#print Len  
if line[Len - 2] == 'g' and line[Len - 3] == 'p' and line[Len - 4] == 'j':  
path = line  
data = urllib.urlopen(line).read()  
f = open('test\\' + str(tt) + '.jpg', 'wb')  
f.write(data)  
f.close()  
tt = tt + 1  
else:  
break  
sour.close()

content = getContent()  
getImageUrl(content)  
downImage()  

