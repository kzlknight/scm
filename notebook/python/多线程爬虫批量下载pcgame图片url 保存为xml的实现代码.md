_复制代码_ 代码如下:

  
#coding=gbk  
from xml.dom import minidom,Node  
import urllib2,re,os  
def readsrc(src):  
try:  
url = urllib2.urlopen(src)  
content = url.read()#.decode('utf-8')  
return content  
except:  
print 'error'  
return None  
def pictype(content):  
'''  
通过抓取网站导航栏，获得网站的图片类型  
返回列表，每个列表元素为一个字典，addr代表图片类型对于的链接，name代表图片类型的名称  
错误会返回None  
'''  
p = re.compile(r'<ul>(.*)</ul>',re.S)  
r=p.search(content)  
if r:  
content=r.group()  
else:  
print None  
p = re.compile(r'<li\s*.*?>\s*<a href *=
*"(?P<addr>.*?)">(?P<name>.*?)\s*</a>\s*</li>')

l = [i.groupdict() for i in p.finditer(content)]  
l=l[1:]  
if len(l):return l  
else:return None  
def pageinfo(src):  
'''  
获取一个页面的详细信息  
返回对于的字典列表  
name:图片的名字  
cutaddr：缩小的浏览图  
picaddr：实际图片的地址  
'''  
d=os.path.split(src)[0]  
try:  
url = urllib2.urlopen(src)  
content = url.read()#.decode('utf-8')  
except:  
print 'error'  
return None  
#find all the pictures info in a page  
p = re.compile(r'<ul.*?>(.*?)</ul>',re.S)  
r = p.findall(content)  
if not r: return None  
r = r[1]  
p = re.compile(r'<li><a href="(?P<picaddr>.*?)".*?><img.*?alt="(?P<name>.*?)"
*src="(?P<cutaddr>.*?)" */></a>.*?</li>')  
l = [ i.groupdict() for i in p.finditer(r)]  
for i in l:  
i['picaddr']=d+'/'+i['picaddr']  
if len(l): return l  
else: return None

def nextpageaddr(src):  
'''  
从页面的html源码中获取下一个页面地址的名称，最后一页返回None  
'''  
content=readsrc(src)  
p = re.compile(r'<a class="next" href="(.*?)">.*?</a>')  
r = p.search(content)  
if r:  
return os.path.dirname(src)+"/"+r.group(1)  
else:  
return None  
def picinfoaddr(src):  
'''  
参数相册图集的html代码  
返回全部图片的相对地址  
'''  
content=readsrc(src)  
p = re.compile(r'<div class="picinfo">.*?<a
href="(?P<addr>.*?)".*?>.*?</div>',re.S)  
r = p.search(content)  
if r:  
return os.path.dirname(src)+"/"+r.group(1)  
else:  
return None  
def parseinfo(content):  
'''  
读取全部图片html代码，获得一个相册的详细信息  
kw：关键字  
title：标题  
type：类型  
pic：各个图片的地址列表，末尾加上_220x165，_medium,_small 可以得到不同大小的图片  
'''  
info={}  
temp=str()

#title  
temp=''  
r=re.search('<h1>(.*?)</h1>',content)#get the pic title  
if r:  
temp = r.group(1)  
info['title']=temp

#keyword  
temp=''  
r=re.search('<meta name="keywords" content="(.*?)" />',content)  
if r:  
temp = r.group(1)  
info['kw']=temp

#type  
r=re.findall('<i><a.*?>(.*?)</a></i>.*?&gt',content)  
if r:  
info['type']=':'.join(r)  
else:  
info['type']=''  
r=re.search('<ul class=".*?">(.*?)</ul>',content,re.S)  
if not r:return None  
content=r.group(1)#filter content  
# print content  
r=re.findall('<a href=".*?<img.*?src="(.*?)".*?</a>',content)

for index,i in enumerate(r):  
r[index]=i[0:i.rfind('_')]  
# print r[index]  
info['pic']=r  
return info  
import threading  
class mthread(threading.Thread):  
def __init__(self,tp,addr,lock):  
threading.Thread.__init__(self)  
# self.doc = minidom.Document()  
self.doc=minidom.Document()  
self.tp=tp  
self.lock=lock  
self.addr=addr  
self.thread_stop=False  
self.picdoc=None  
def run(self):  
self.picdoc = self.doc.createElement('urlclass')  
# print self.tp  
self.picdoc.setAttribute('type',self.tp)  
# self.doc.appendChild(self.picdoc)  
m=pageinfo(self.addr)  
while self.addr:  
for i in m:  
# print i['picaddr']  
picaddr=picinfoaddr(i['picaddr'])  
# print picaddr  
info=parseinfo(readsrc(picaddr))  
name=info['title']

  
picture=doc.createElement('picture')

title = doc.createElement('title')  
title.appendChild(doc.createTextNode(info['title']))  
picture.appendChild(title)

keyword = doc.createElement('keywords')  
keyword.appendChild(doc.createTextNode(info['kw']))  
picture.appendChild(keyword)

tp = doc.createElement('pictype')  
tp.appendChild(doc.createTextNode(info['type']))  
picture.appendChild(tp)

cuturl = doc.createElement('piccut')  
cuturl.appendChild(doc.createTextNode(i['cutaddr']))  
picture.appendChild(cuturl)

urls = doc.createElement('urls')  
self.lock.acquire()  
print 'downloading ',name  
self.lock.release()  
for picurl in info['pic']:  
singleurl=doc.createElement('url')  
singleurl.appendChild(doc.createTextNode(picurl+'.jpg'))  
urls.appendChild(singleurl)

picture.appendChild(urls)  
self.picdoc.appendChild(picture)  
m=pageinfo(self.addr)  
self.addr=nextpageaddr(self.addr)  
# f = open('c:\\'+self.tp+'.xml','w')  
# f.write(doc.toprettyxml(indent = ''))  
# f.close()  
def stop(self):  
self.thread_stop=True

  
path='C:\\pict\\'#下载的路径  
#import sys  
sys.exit(12)  
content=readsrc('http://photos.pcgames.com.cn/cate/3/1.html')  
r=pictype(content)  
lt=[]  
doc = minidom.Document()  
root=doc.createElement('url_resource')  
root.setAttribute('type','url')  
root.setAttribute('urltype','image')  
root.setAttribute('imgfmt','jpg')  
doc.appendChild(root)  
lock=threading.RLock()  
for iaddr in r:  
print 'downloading type: ',iaddr['name']  
addr=iaddr['addr']  
th=mthread(iaddr['name'],addr,lock)  
lt.append(th)  
th.start()  
for t in lt:  
t.join()  
root.appendChild(t.picdoc)

print 'write'  
f = open('c:\\'+'urls'+'.xml','w')  
f.write(doc.toprettyxml(indent = ''))  
f.close()  
print doc.toprettyxml()  
print 'end'  

