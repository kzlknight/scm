使用了Python的 xml.etree.ElementTree 库

##  xml.etree.ElementTree 库简介  

xml.etree.ElementTree模块实现了一个简单而高效的API用于解析和创建XML数据。xml.etree.ElementTree模块对于恶意构造的数据是不安全的。如果您需要解析不受信任或未经验证的数据，请参阅XML漏洞。  
参考文献： [ https://docs.python.org/3.6/library/xml.etree.elementtree.html
](https://docs.python.org/3.6/library/xml.etree.elementtree.html)

```python

    from xml.etree import ElementTree
    import json
    
    LISTTYPE = 1
    DICTTYPE = 0
    
    def getDictResults(res_dicts, iters):
      result_dicts = {}
      for iter in iters.getchildren():
        iterxml(iter, result_dicts)
    
      if result_dicts:
        res_dicts[iters.tag].update(result_dicts)
    
    def getListResults(res_dicts, iters):
      result_lists = []
      for iter in iters.getchildren():
        result_dicts = {}
        iterxml(iter, result_dicts)
        result_lists.append(result_dicts.copy())
        del(result_dicts)
      
      if result_lists:
        if len(res_dicts[iters.tag].items()) == 0:
          res_dicts[iters.tag] = result_lists.copy()
        else:
          for resobj in result_lists:
            resobjkey = list(resobj.keys())[0]
            if res_dicts[iters.tag].get(resobjkey) == None:
              res_dicts[iters.tag].update(resobj)
            else:
              if type(res_dicts[iters.tag][resobjkey]) == list:
                res_dicts[iters.tag][resobjkey].append(resobj[resobjkey].copy())
              else:
                old_value = res_dicts[iters.tag][resobjkey]
                res_dicts[iters.tag][resobjkey] = []
                res_dicts[iters.tag][resobjkey].append(old_value)
                res_dicts[iters.tag][resobjkey].append(resobj[resobjkey].copy())
    
        del(result_lists)
    
    def checkxmlchildrentype(iters):
      taglist = []
      for iter in iters.getchildren():
        taglist.append(iter.tag)
    
      if len(set(taglist)) == len(taglist):
        return DICTTYPE
      else:
        return LISTTYPE
    
    def getResults(res_dicts, iters):
      if checkxmlchildrentype(iters):
        return getListResults(res_dicts, iters)
      else:
        return getDictResults(res_dicts, iters)
    
    #@res_dicts  {}
    def iterxml(iter, res_dicts):
      res_dicts[iter.tag] = {}
    
      if iter.attrib:
        for k,v in dict(iter.attrib).items():
          res_dicts[iter.tag].update({k : v})
      
      if iter.text is not None and iter.text.strip() != "":
        res_dicts[iter.tag].update({"__XmlTagText__" : iter.text.strip()})
      
      if iter.getchildren():
        getResults(res_dicts, iter)
    
    def parserxmltojson(file_path):
      try:
        tree = ElementTree.parse(file_path)
      except Exception as e:
        #multi-byte encodings are not supported  把字符集改成utf-8就可以
        #encoding specified in XML declaration is incorrect  xml encoding标识和文件的字符集不同
        #syntax error  语法错误，乱码等
        #not well-formed (invalid token)  编辑器点击后字符集被修改成ASCII等，或者文件本身字符集和xml encoding不相同
        print("Parser {} Error, Errmsg: {}".format(file_path, e))
        return ""
    
      if tree is None:
        print("{} is None.".format(file_path))
        return ""
    
      root = tree.getroot()
    
      report = {}
      iterxml(root, report)
      #return getDictResults(root)
    
      return report
    
    if __name__ == "__main__":
      jsonret = parserxmltojson("test.xml")
      with open("test.json", "w", encoding="utf-8") as fd:
        fd.write(json.dumps(jsonret, ensure_ascii=False, indent=4))
      print(json.dumps(jsonret, ensure_ascii=False, indent=4))
```

以上就是python实现xml转json文件的示例代码的详细内容，更多关于python实现xml转json文件的资料请关注脚本之家其它相关文章！

