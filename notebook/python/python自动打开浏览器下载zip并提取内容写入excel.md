##  前言

佬们轻喷，里面有些代码都是现学现写的，一些细节没处理好的地方还请指出来~~~

首先贴上效果图：有些部分我没有放进来，比如浏览器的启动，但我详细聪明的你们那个玩意肯定一学就会。有些东西我没放进来

![](https://img.jbzj.com/file_images/article/202101/202114115701939.gif?20210411579)

##  下载  

###  使用到的库和总体思路  

这部分用到time，selenium，urllib，re，requests，os这几个库。

###  代码  

```python

    #!/usr/bin/python3
    # coding=utf-8
    import time
    from selenium import webdriver
    from urllib.parse import quote,unquote
    import re
    import requests
    import os
    # 下面两个参数是防止反爬的，别的文章也是这么写的，但我这里没用到
    headers = {
     'Accept': '*/*',
     'Accept-Language': 'en-US,en;q=0.5',
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
    }
    params = {
     'from': 'search',
     'seid': '9698329271136034665'
    }
    
    
    class Download_file():
     def __init__(self,url,order_number,file_path):
     self.url=url
     self.order_number=order_number
     self.file_path=file_path
    
     # 拿到文件对应的下载链接
     def _get_files_url(self):
     # 用谷歌浏览器打开
     driver=webdriver.Chrome()
     # 拿到url
     driver.get(self.url)
     print(driver.title)
     time.sleep(5)
     # 通过标签id拿到对应操作对象
     driver.switch_to.frame(0)
     driver.find_element_by_id('search_id').send_keys(self.order_number)
     # 具体页面有具体的操作，这里我需要找的button没有id，他是用ng-click="queryCheckRecordByTid(queryInfo.queryTid)"
     driver.find_element_by_class_name('btn').click()
     # driver.find_element_by_id('su').click()
     time.sleep(3)
     # AngularJS语法写的标签很烦。。。我这里先找到目标标签的父标签
     # 然后通过父标签拿到目标标签
     dd=driver.find_elements_by_class_name('col-xs-2')
     # 我这个父标签下有两个<a></a>标签，只能要第一个
     url_list=[]
     for i in dd:
     # 因为下载的url正好是第一个，然后这里取得是element，所以正好取到正确的url
     a=i.find_element_by_xpath('.//a')
     # print(a.get_attribute('href'))
     url_list.append(a.get_attribute('href'))
     # download_btn[0].click()
     time.sleep(3)
     driver.close()
     return url_list
    
     # 下载文件
     def download_save(self):
     # 匹配出来的可能有None，所以要做一下处理
     url_list=self._get_files_url()
     url_list=list(filter(lambda x:x!=None,url_list))
     if len(url_list)==0:
     return False
     # 创建一个保存zip的文件夹
     # 更改执行路径的原因是这样可以灵活的在用户指定的目录下创建文件
     os.chdir(self.file_path)
     if os.path.exists(self.file_path+'/'+'Download_Files') == False:
     os.mkdir('Download_Files')
     # 更改执行路径
     os.chdir(self.file_path + '/'+'Download_Files/')
     for url in url_list:
     # 链接中附带了作者和文件名，但是需要解码，所以先用正则语言提取目标串，然后转换成中文
     ret = re.search(r'_.*\.zip$',url)
     file_info=unquote(ret.group())
     file_author=file_info.split('_')[1]
     file_title=file_info.split('_')[2]
     file_object=requests.get(url)
     file_name=file_author+'_'+file_title
     print('正在下载:%s'%file_name)
     with open(file_name,'wb') as f:
     f.write(file_object.content)
    
    
     # def auto_fill(self):
    
    if __name__ == '__main__':
     url='http://***'
     order_id='***'
     file_path='D:/For discipline/Get_excel'
     test=Download_file(url,order_id,file_path)
     test.download_save()
    
    
```

###  解释  

用selenium库访问目标页面，我这里通过_get_files_url方法定位输入框和超链接地址，然后返回超链接地址。之后在download_save方法内通过request.get拿到文件，然后存在本地，里面的一些存放目录、文件名处理等细节看代码就可以了。  
注意，这只是一个案例，不具备普适性，因为每个页面的前端编写方法不尽相同，具体页面需要具体分析，我这里不贴我的网站是涉及到女朋友的业务，所以不适合贴。

##  提取内容并填写  

###  使用到的库  

这部分用到time，xlwt，urllib，re，pickle，os，zipfile，BeautifulSoup这几个库。

###  代码  

```python

    #!/usr/bin/python3
    # coding=utf-8
    import os
    import time
    import xlwt
    import zipfile
    import re
    import pickle
    from bs4 import BeautifulSoup
    from Download_files import Download_file
    class get_excel():
     def __init__(self,file_path):
     self.file_path=file_path
    
    
     # 解压出目标文件
     def _unzip_files(self):
     '''
     这个函数具备解压目标文件的功能并且返回需要处理的文件列表
     :return:
     '''
     files_list=os.listdir(self.file_path)
     # 文件名存放在列表中，为了防止处理了别的文件，先用正则匹配一下
     files_list=list(filter(lambda x:re.search(r'\.zip$',x)!=None,files_list))
     title_list=[]
     for file in files_list:
     title=file.split('.')[0].split('_')[1]
     with zipfile.ZipFile(self.file_path+'/'+file,'r') as z:
     # 代码有点长，主要是用于筛选出目标文件
     target_file=list(filter(lambda x:re.search(r'比对报告.html$',x)!=None,z.namelist()))
     # 下面的方法就是比较灵活的
     contentb=z.read(target_file[0])
     # 这里很头痛的一点是返回值是二进制的，就算decode了也没办法正则匹配
     # 所以我想把它存一下再用utf8格式读取
     # 当然我也尝试了decode，但网页内的有些东西还是没办法转换，也会导致正则无法匹配
     if os.path.exists(self.file_path+'/'+title+'_'+'比对报告.html')==False:
     with open(self.file_path+'/'+title+'_'+'比对报告.html','wb') as fb:
     pickle.dump(contentb,fb)
     # with open(self.file_path+'/'+target_file[0],'r',encoding='utf-8') as fa:
     # contenta=fa.read()
     # print(contenta)
     # sentence=str(re.search(r'<b [^"]*red tahoma.*</b>$',contenta))
     # value=re.search(r'\d.*%', sentence)
     # info=[author,title,value]
     # repetition_rate.append(info)
     title_list.append(target_file[0])
     return files_list,title_list
    
    
     # 读取html文件内容
     def read_html(self):
     '''
     之前的函数已经把目标文件解压出来了，但html文件的读取比较麻烦，
     所以这里用到了BeautifulSoup库来读取我想要的信息，
     然后把想要的东西存在列表里面返回回来。
     :return:
     '''
     files_list,title_list=self._unzip_files()
     repetition_rate=[]
     for file in files_list:
     # 取出作者和标题，这两个数据要写到excel里面
     file=file.split('.')
     file=file[0].split('_')
     author=file[0]
     title=file[1]
     # 比对报告已经解压出来了，直接读取就可以
     with open(self.file_path+'/'+title+'_比对报告.html','rb') as f:
     # 下面是BeautifulSoup的用法，看不懂的话可以去官网
     content=f.read()
     content=BeautifulSoup(content,"html.parser")
     # print(type(content))
     # 网上搜了很多，终于可以找到我想要的重复率了
     value=content.find('b',{"class":"red tahoma"}).string
     repetition_rate.append([author,title,value])
     return repetition_rate
    
    
     def write_excel(self):
     '''
     生成xls表格
     :return:
     '''
     workbook=xlwt.Workbook(encoding='utf-8')
     booksheet=workbook.add_sheet('Sheet1')
     # 设置边框
     borders = xlwt.Borders() # Create Borders
     borders.left = xlwt.Borders.THIN #DASHED虚线，NO_LINE没有，THIN实线
     borders.right = xlwt.Borders.THIN #borders.right=1 表示实线
     borders.top = xlwt.Borders.THIN
     borders.bottom = xlwt.Borders.THIN
     borders.left_colour=0x40
     borders.right_colour = 0x40
     borders.top_colour = 0x40
     borders.bottom_colour = 0x40
     style1=xlwt.XFStyle()
     style1.borders=borders
     # 设置背景颜色，这些操作搞得很像js和css
     pattern = xlwt.Pattern()
     pattern.pattern = xlwt.Pattern.SOLID_PATTERN
     pattern.pattern_fore_colour = 44
     style = xlwt.XFStyle() # Create the Pattern
     style.pattern = pattern
     repetition_rate=self.read_html()
     # 写一个标题
     booksheet.write(0,0,'作者',style)
     booksheet.write(0,1,'标题',style)
     booksheet.write(0,2,'重复率',style)
     for item in repetition_rate:
     booksheet.write(repetition_rate.index(item)+1,0,item[0],style1)
     booksheet.write(repetition_rate.index(item)+1,1,item[1],style1)
     booksheet.write(repetition_rate.index(item)+1,2,item[2],style1)
     s='重复率.xls'
     workbook.save(self.file_path+'/'+s)
    
    
    if __name__ == '__main__':
     # 判断一下Download_files文件夹
     file_path='D:/For discipline/Get_excel'
     url='http://***'
     order_number='***'
     if os.path.exists('./Download_Files')==False:
     get_file=Download_file(url,order_number,file_path)
     get_file.download_save()
     os.chdir(file_path+'/Download_Files')
     test=get_excel('D:/For discipline/Get_excel/Download_Files')
     test.write_excel()
    
```

###  解释  

由于我下载的zip文件，这就需要先解压，解压的库是zipfile，当然这种解压只是在执行的时候解开，不是实际解压到目录下面的。解压出来的文件比较冗杂，所以我用正则匹配了一个最合适（能够减少编写工作量）的文件，这部分代码中的大部分工作都是为了拿到我的目标值（其中包括字节流和字符串的转换工作，我就是失败了才会选择保存html文件并重新读取信息的多余过程），也就是（作者,标题,repetition
rate），信息写入excel的过程倒不是很复杂。我基本上没有解释方法是因为这些百度一下或者看官网就行了，主要还是阐述一下我的编写思路

**附：Python使用beautifulSoup获取标签内数据**

```python

    from bs4 import BeautifulSoup
    
    for k in soup.find_all('a'):
     print(k)
     print(k['class'])#查a标签的class属性
     print(k['id'])#查a标签的id值
     print(k['href'])#查a标签的href值
     print(k.string)#查a标签的string
     #tag.get('calss')，也可以达到这个效果
```

到此这篇关于python自动打开浏览器下载zip并提取内容写入excel的文章就介绍到这了,更多相关python自动浏览器下载zip并提取内容内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

##  参考文章  

  * Excel的操作： [ Python3读取和写入excel表格数据 ](https://www.jb51.net/article/188317.htm) . 
  * selenium的操作: [ selenium之 定位以及切换frame（iframe） ](https://www.jb51.net/article/203425.htm) . [ Python Selenium库的使用 ](https://www.jb51.net/article/203427.htm) . 
  * zip文件的解压和读取： [ Python读写zip压缩文件 ](https://www.jb51.net/article/146469.htm) . 

