这篇博客对于考公人或者其他用华图或者粉笔做题的人比较友好，通过输入网址可以自动化获取华图以及粉笔练习的错题。

##  粉笔网站

我们从做过的题目组中获取错题

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010811020136.png)  
![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010811020137.png)

打开某一次做题组，我们首先进行抓包看看数据在哪里

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010811020138.png)

我们发现现在数据已经被隐藏，事实上数据在这两个包中：  
https://tiku.fenbi.com/api/xingce/questions  
https://tiku.fenbi.com/api/xingce/solutions  
一个为题目的一个为解析的。此url要通过传入一个题目组参数才能获取到当前题目数据，而题目组参数在这个包中

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010811020139.png)

以网址的倒数第二个数字串有关

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010811020140.png)

url的规则为 `
'https://tiku.fenbi.com/api/xingce/exercises/'+str(id_)+'?app=web&kav=12&version=3.0.0.0'
` ，id_即为下划线数字  
通过请求这个包获取到参数然后通过参数请求上面两个包（

```python

    https://tiku.fenbi.com/api/xingce/questions
    https://tiku.fenbi.com/api/xingce/solutions
```

）即可获取到题目数据，而且自己的答案在也在 ` [
https://tiku.fenbi.com/api/xingce/exercises/'+str(id_)+'?app=web&kav=12&version=3.0.0.0
](https://tiku.fenbi.com/api/xingce/exercises/'+str\(id_\)+'?app=web&kav=12&version=3.0.0.0)
` 这个包中。

不过粉笔的题目数据有些是图片，而且图片在题目中，选项中，这里以word文档存储操作docx库有些吃力，于是我想到了直接构造HTML代码，然后通过pdfkit转为pdf（具体如何下载可以参考百度，要下载wkhtmltopdf.exe）即可变为错题集在平板或者其他设备中看。  
（请求时一定要携带完整的headers，否则很可能获取不到数据）

具体操作看代码解析

```python

    ###此函数用于解析题目和每道题的答案
    def jiexi(liebiao):
     new = []
     timu_last = []
     for each in liebiao:
      new.append(re.sub(r'flag=\\"tex\\" ','',each))
     for each in new:
      timu_last.append(re.sub(r'\\','',each))
     return timu_last
    ###此函数用于解析选项
    def xuanxiang(liebiao):
     xuanxiang_v2 = []
     xuanxiang_v3 = []
     for each in liebiao:
      a = re.sub('<p>','',each)
      a = re.sub('</p>','',a)
      xuanxiang_v2.append(a)
     for each in xuanxiang_v2:
      each = each+'</p>'
      xuanxiang_v3.append(each)
     return xuanxiang_v3
    import requests
    import re
    import pdfkit
    import os
    url = str(input("请输入练习的网址："))
    ###获取本节练习id
    id_ = re.findall(r'https://www.fenbi.com/spa/tiku.*?/xingce/xingce/(.*?)/',url,re.S)[0]
    mid_url = 'https://tiku.fenbi.com/api/xingce/exercises/'+str(id_)+'?app=web&kav=12&version=3.0.0.0'
    headers = {
    #####完整的headers，自己添加
    }
    response = requests.get(url=mid_url,headers=headers)
    response.encoding = 'utf-8'
    page_text = response.text
    ###获取题目组参数
    id_list = re.findall('\"questionIds\"\:\[(.*?)\]\,',page_text,re.S)
    ###获取自己的答案
    your_answer = re.findall(r'"answer":{"choice":"(.*?)",',page_text,re.S)
    ###此练习名称
    name = re.findall(r'"name":"(.*?)",',page_text,re.S)[0]
    ###真正存储数据的包
    timu_url = 'https://tiku.fenbi.com/api/xingce/questions'
    params = {
     'ids': id_list
    }
    response = requests.get(url=timu_url,headers=headers,params=params)
    response.encoding = 'utf-8'
    page_text = response.text
    ###获取正确答案
    true_answer = re.findall('"correctAnswer":{"choice":"(.*?)"',page_text,re.S)
    ###真正存储数据的包
    solution_url = 'https://tiku.fenbi.com/api/xingce/solutions'
    response = requests.get(url=solution_url,headers=headers,params=params)
    response.encoding = 'utf-8'
    page_text = response.text
    ###获取解析
    solution_list = re.findall(r'"solution":"(.*?)","userAnswer"',page_text,re.S)
    solution_last = jiexi(solution_list)
    cailiao = []
    timu = []
    ###获取单选题题目和复合题的题目
    for each in response.json():
     timu.append(each['content'])
     try:
      cailiao.append(each['material']['content'])
     except:
      cailiao.append('none')
    ###获取选项信息
    A_option = re.findall('\"options\"\:\[\"(.*?)\"\,\".*?\"\,\".*?\"\,\".*?\"\]',page_text,re.S)
    B_option = re.findall('\"options\"\:\[\".*?\"\,\"(.*?)\"\,\".*?\"\,\".*?\"\]',page_text,re.S)
    C_option = re.findall('\"options\"\:\[\".*?\"\,\".*?\"\,\"(.*?)\"\,\".*?\"\]',page_text,re.S)
    D_option = re.findall('\"options\"\:\[\".*?\"\,\".*?\"\,\".*?\"\,\"(.*?)\"\]',page_text,re.S)
    A_option = xuanxiang(A_option)
    B_option = xuanxiang(B_option)
    C_option = xuanxiang(C_option)
    D_option = xuanxiang(D_option)
    A_option = jiexi(A_option)
    B_option = jiexi(B_option)
    C_option = jiexi(C_option)
    D_option = jiexi(D_option)
    ###构造HTML代码
    count = 0
    all_content = "<!DOCTYPE html>\n<meta charset='utf-8'>\n<html>"
    for each in true_answer:
     if each != your_answer[count]:
      ###处理复合题
      if cailiao[count] != 'none' and cailiao[count] not in all_content:
       all_content += cailiao[count]
      all_content += str(count+1)
      all_content += '、'
      all_content += timu[count][3:]
      all_content += 'A、'
      all_content += A_option[count]
      all_content += 'B、'
      all_content += B_option[count]
      all_content += 'C、'
      all_content += C_option[count]
      all_content += 'D、'
      all_content += D_option[count]
      all_content += '<br>'
     count += 1
    count = 0
    all_content += '<br><br><br><br><br><br><br><br><br>'
    for each in true_answer:
     if each != your_answer[count]:
      temp = '第'+str(count+1)+'题的正确答案为'
      all_content += temp
      if true_answer[count]=='0':
       all_content += 'A'
      elif true_answer[count]=='1':
       all_content += 'B'
      elif true_answer[count]=='2':
       all_content += 'C'
      elif true_answer[count]=='3':
       all_content += 'D'
      all_content += solution_last[count]
      all_content += '<br>'
     count += 1
    all_content += '</html>'
    path_name = name + '.html'
    ###保存为HTML文件
    with open(path_name,'w',encoding='utf-8') as fp:
     fp.write(all_content)
    confg = pdfkit.configuration(wkhtmltopdf=r'wkhtmltopdf.exe保存的路径')
    pdfkit.from_url(path_name, name+'.pdf',configuration=confg)###把HTML文件转为pdf
    print('错题PDF保存成功')
    ###删除HTML文件
    os.remove(path_name)
```

##  华图网站

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010811020141.png)

也是答题记录中自己做过的题目  
华图网站稍微不一样，他的数据直接抓包就可看到

![在这里插入图片描述](https://img.jbzj.com/file_images/article/202101/2021010811020142.png)

通过请求这个包即可获取到数据，接下来就是解析的事情了，这次我用word文档进行存储，如果觉得不方便也可以像上文一样构造HTML

```python

    ##导包
    import requests
    import lxml.etree
    import re
    import time
    import os
    from docx import Document
    from docx.shared import Inches
    from docx.shared import Pt
    from docx.shared import Inches
    from docx.oxml.ns import qn
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    url = str(input("请输入练习的网址："))
    headers={
    ###完整的headers，否则获取不到数据
    }
    response = requests.get(url = url,headers = headers)
    response.encoding='utf-8'
    reptext = response.text
    tree = lxml.etree.HTML(reptext) #解析网站获取源码
    
    dirName="考公图片"
    if not os.path.exists(dirName):
     os.mkdir(dirName) #网站图片保存路径
     
    jiexi = re.findall(r'<div class="jiexi-item-title">解析.*?。</div>.*?</div>', reptext,re.S) #获取题目解析
    
    imgg = []
    for each in jiexi:
     imgg.append(re.findall(r'<img src="(.*?)".*?>', each)) #获取解析里的图片URL
     
    imgt = []
    for each in imgg:
     if each == []:
      imgt.append([1])
     else:
      imgt.append(each) #把解析里图片URL美化整理一下
      
    jiexilast = []
    for qq in jiexi:
     jiexilast.append(re.sub(r'<[^>]+>', '', qq)) #美化题目解析
     
    corrected = re.findall(r'<span class="g-right-answer-color">[a-zA-Z]{1,4}</span>', reptext) #获取正确答案
    correct = []
    for ee in corrected:
     correct.append(re.sub(r'<[^>]+>', '', ee)) #美化正确答案
     
    yoursed = re.findall(r'<span class="yellowWord">[a-zA-Z]{1,4}</span>', reptext) #获取自己的答案
    yours = []
    for ee in yoursed:
     yours.append(re.sub(r'<[^>]+>', '', ee)) #美化自己的答案
     
    timuleixing = re.findall(r'<span class="greenWord">(.*?)</span>.*?</div>',reptext,re.S) #获取题目类型
    
    find1 = re.findall(r'<span class="greenWord">.*?</span>(.*?)</div>',reptext,re.S)
    for each in find1:
     re.sub(r'<.*?>','',each)
    find5 = [] #最终的题目
    for each in find1:
     find5.append(re.sub(r'<[^>]+>', '', each))
     
    img = []
    for each in find1:
     img.append(re.findall(r'<img src="(.*?)".*?>', each))
    imgx = []
    for each in img:
     if each == []:
      imgx.append([1])
     else:
      imgx.append(each) #最终版题目图片URL
      
    
    v = tree.xpath('//div[@class="exercise-main-title"]//text()') #本次题目类型
    
    try:
     ###这是既有复合题也有单选题的
     fuheti = re.findall(r'<!--复合题-->(.*?)<div class="exercise-main-topics"',reptext,re.S)[0].split('<!--复合题-->')
    except:
     try:
      ###这是只有复合题或者复合题在最后几题的
      fuheti = re.findall(r'<!--复合题-->(.*?)<!-- 纠错的弹窗 -->',reptext,re.S)[0].split('<!--复合题-->')
     except:
      pass
    count = 0
    
    ###导入标题
    document = Document()
    p = document.add_paragraph()
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(v[0][5:-3])
    run.font.size = Pt(14)
    run.font.name=u'宋体'
    r = run._element
    r.rPr.rFonts.set(qn('w:eastAsia'),u'宋体')
    choose = []
    
    ###处理题目选项
    axuanxiang = []
    bxuanxiang = []
    cxuanxiang = []
    dxuanxiang = []
    xuanxiang = re.findall(r'<div class="main-topic-choices">(.*?)<div class="main-topic-letters clearfix pl14">',reptext,re.S)
    for everything in xuanxiang:
     try: ##处理只有两个选项
      axuanxiang.append(re.sub("<.*?>","",re.findall(r'<div.*?class.*?main-topic-choice.*?>(A.*?)</div>',everything,re.S)[0]))
     except:
      axuanxiang.append('--')
     try:
      bxuanxiang.append(re.sub("<.*?>","",re.findall(r'<div.*?class.*?main-topic-choice.*?>(B.*?)</div>',everything,re.S)[0]))
     except:
      bxuanxiang.append('--')
     try:
      cxuanxiang.append(re.sub("<.*?>","",re.findall(r'<div.*?class.*?main-topic-choice.*?>(C.*?)</div>',everything,re.S)[0]))
     except:
      cxuanxiang.append('--')
     try:
      dxuanxiang.append(re.sub("<.*?>","",re.findall(r'<div.*?class.*?main-topic-choice.*?>(D.*?)</div>',everything,re.S)[0]))
     except:
      dxuanxiang.append('--')
      
    
     
    for every in correct:
     if every != yours[count]:
      ###处理复合题题目
      try:
       for eacy in fuheti:
        if find5[count] in eacy:
         fuheti_URL = re.findall(r'<img src="(.*?)".*?>',re.findall(r'.*?<p>(.*?)</p>',eacy,re.S)[0],re.S)
         fuheti_last = re.sub(r'<.*?>','',re.findall(r'.*?<p>(.*?)</p>',eacy,re.S)[0])
         fuheti_last = re.sub(r'\xa0\xa0\xa0\xa0\xa0\xa0\xa0','\n',fuheti_last)
         if fuheti_last not in choose:
          p = document.add_paragraph()
          run = p.add_run(fuheti_last)
          run.font.size = Pt(14)
          run.font.name=u'宋体'
          r = run._element
          r.rPr.rFonts.set(qn('w:eastAsia'),u'宋体')
          headers ={
         'Use-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
           }
          for eacu in fuheti_URL:
           img_data = requests.get(url = eacu,headers = headers).content
           img_path = dirName+'/'+'tupian'+'.jpg'
           with open(img_path,'wb') as fp:
            fp.write(img_data)
            print("保存成功")
           document.add_picture(img_path, width=Inches(5))
          choose.append(fuheti_last)
      except:
       pass
      
      ###导入单选题题目
      p = document.add_paragraph()
      run = p.add_run(str(count+1)+"、"+timuleixing[count]+find5[count][3:])
      run.font.size = Pt(14)
      run.font.name=u'宋体'
      r = run._element
      r.rPr.rFonts.set(qn('w:eastAsia'),u'宋体')
      url = imgx[count][0]
      headers ={
       'Use-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
      }
      try:
       img_data = requests.get(url = url,headers = headers).content
       img_path = dirName+'/'+'tupian'+'.jpg'
       with open(img_path,'wb') as fp:
        fp.write(img_data)
        print("保存成功")
       document.add_picture(img_path, width=Inches(5))
       count+=1
      except:
       count+=1
       
      ###导入选项
      p = document.add_paragraph()
      run = p.add_run(axuanxiang[count-1])
      run.font.size = Pt(14)
      run.font.name=u'宋体'
      r = run._element
      r.rPr.rFonts.set(qn('w:eastAsia'),u'宋体')
      p = document.add_paragraph()
      run = p.add_run(bxuanxiang[count-1])
      run.font.size = Pt(14)
      run.font.name=u'宋体'
      r = run._element
      r.rPr.rFonts.set(qn('w:eastAsia'),u'宋体')
      p = document.add_paragraph()
      run = p.add_run(cxuanxiang[count-1])
      run.font.size = Pt(14)
      run.font.name=u'宋体'
      r = run._element
      r.rPr.rFonts.set(qn('w:eastAsia'),u'宋体')
      p = document.add_paragraph()
      run = p.add_run(dxuanxiang[count-1])
      run.font.size = Pt(14)
      run.font.name=u'宋体'
      r = run._element
      r.rPr.rFonts.set(qn('w:eastAsia'),u'宋体')
      p = document.add_paragraph()
      run = p.add_run("\n")
      run.font.size = Pt(14)
      run.font.name=u'宋体'
      r = run._element
      r.rPr.rFonts.set(qn('w:eastAsia'),u'宋体')
      
     else:
      count+=1
    
    ###美化界面
    p = document.add_paragraph()
    run = p.add_run("\n\n\n\n\n")
    run.font.size = Pt(14)
    run.font.name=u'宋体'
    r = run._element
    r.rPr.rFonts.set(qn('w:eastAsia'),u'宋体')
    
    ###美化解析
    counting = 0
    jiexilast2 = []
    for ok in jiexilast:
     jiexilast2.append(re.sub(r'\n\t\t','：',ok))
    for every in correct:
     if every != yours[counting]:
      ###导入解析和答案
      p = document.add_paragraph()
      run = p.add_run(str(counting+1)+"、"+"正确答案为："+correct[counting]+"\n"+jiexilast2[counting])
      run.font.size = Pt(14)
      run.font.name=u'宋体'
      r = run._element
      r.rPr.rFonts.set(qn('w:eastAsia'),u'宋体')
      url = imgt[counting][0]
      headers ={
       'Use-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
      }
      try:
       img_data = requests.get(url = url,headers = headers).content
       img_path = dirName+'/'+'tupian'+'.jpg'
       with open(img_path,'wb') as fp:
        fp.write(img_data)
        print("保存成功")
       document.add_picture(img_path, width=Inches(5))
       print("写入成功")
       counting+=1
      except:
       counting+=1
     else:
      counting+=1
    ###保存文档
    document.save(v[0][5:-3]+'.docx')
    print(v[0][5:-3]+'保存成功！')
```

##  总结

粉笔和华图错题爬虫主要区别是华图获取数据简单，解析操作繁琐；粉笔的数据隐秘，解析起来可以用json，比较方便。

到此这篇关于Python爬虫自动化获取华图和粉笔网站的错题的文章就介绍到这了,更多相关Python爬虫获取网站错题内容请搜索脚本之家以前的文章或继续浏览下面的相关文章希望大家以后多多支持脚本之家！

