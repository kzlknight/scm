通过第三方库exifread读取照片信息。  
exifread官网： [ https://pypi.org/project/ExifRead/
](https://pypi.org/project/ExifRead/)

##  一、安装exifread

```python

    pip install exifread
```

##  二、读取照片信息，以及根据经纬度通过百度地图API获取位置

```python

    import exifread
    import json
    import urllib.request
    
    # Open image file for reading (binary mode)
    f = open('001.jpg', 'rb')
    
    # Return Exif tags
    tags = exifread.process_file(f)
    
    '''
    #打印所有照片信息
    for tag in tags.keys():  
      print("Key: {}, value {}".format(tag, tags[tag]))
    '''
    
    #打印照片其中一些信息
    print('拍摄时间：', tags['EXIF DateTimeOriginal'])
    print('照相机制造商：', tags['Image Make'])
    print('照相机型号：', tags['Image Model'])
    print('照片尺寸：', tags['EXIF ExifImageWidth'], tags['EXIF ExifImageLength'])
    
    #获取经度或纬度
    def getLatOrLng(refKey, tudeKey):
      if refKey not in tags:
        return None
      ref=tags[refKey].printable
      LatOrLng=tags[tudeKey].printable[1:-1].replace(" ","").replace("/",",").split(",")
      LatOrLng=float(LatOrLng[0])+float(LatOrLng[1])/60+float(LatOrLng[2])/float(LatOrLng[3])/3600
      if refKey == 'GPS GPSLatitudeRef' and tags[refKey].printable != "N":
        LatOrLng=LatOrLng*(-1)
      if refKey == 'GPS GPSLongitudeRef' and tags[refKey].printable != "E":
        LatOrLng=LatOrLng*(-1)
      return LatOrLng
    
    #调用百度地图API通过经纬度获取位置
    def getlocation(lat,lng):  
      url = 'http://api.map.baidu.com/geocoder/v2/?location=' + lat + ',' + lng + '&output=json&pois=1&ak=申请的百度地图KEY'
      req = urllib.request.urlopen(url)
      res = req.read().decode("utf-8") 
      str = json.loads(res)
      #print(str)
      jsonResult = str.get('result')
      formatted_address = jsonResult.get('formatted_address')
      return formatted_address
    
    lat = getLatOrLng('GPS GPSLatitudeRef','GPS GPSLatitude') #纬度
    lng = getLatOrLng('GPS GPSLongitudeRef','GPS GPSLongitude') #经度
    print('纬度:{} 经度：{}'.format(lat, lng))
    
    location = getlocation(str(lat), str(lng))
    print('位置：{}'.format(location))
```

以上就是python 通过exifread读取照片信息的详细内容，更多关于python 读取照片信息的资料请关注脚本之家其它相关文章！

