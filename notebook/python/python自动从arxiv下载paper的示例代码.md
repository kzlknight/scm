
```python

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    # @Time  : 2020/02/11 21:44
    # @Author : dangxusheng
    # @Email  : dangxusheng163@163.com
    # @File  : download_by_href.py
    '''
    自动从arxiv.org 下载文献
    '''
    
    import os
    import os.path as osp
    import requests
    from lxml import etree
    from pprint import pprint
    import re
    import time
    import glob
    
    headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36",
      "Host": 'arxiv.org'
    }
    
    HREF_CN = 'http://cn.arxiv.org/pdf/'
    HREF_SRC = 'http://cn.arxiv.org/pdf/'
    SAVE_PATH = '/media/dangxs/E/Paper/download_at_20200730'
    os.makedirs(SAVE_PATH, exist_ok=True)
    
    FAIL_URLS = []
    FAIL_URLS_TXT = f'{SAVE_PATH}/fail_urls.txt'
    
    
    def download(url, title):
      pattern = r'[\\/:*?"\'<>|\r\n]+'
      new_title = re.sub(pattern, " ", title)
      print(f'new title: {new_title}')
      save_filepath = '%s/%s.pdf' % (SAVE_PATH, new_title)
      if osp.exists(save_filepath) and osp.getsize(save_filepath) > 50 * 1024:
        print(f'this pdf is be existed.')
        return True
      try:
        with open(save_filepath, 'wb') as file:
          # 分字节下载
          r = requests.get(url, stream=True, timeout=None)
          for i in r.iter_content(2048):
            file.write(i)
        if osp.getsize(save_filepath) >= 10 * 1024:
          print('%s 下载成功.' % title)
          return True
      except Exception as e:
        print(e)
      return False
    
    
    # 从arxiv.org 去下载
    def search(start_size=0, title_keywords='Facial Expression'):
      # 访问地址: https://arxiv.org/find/grp_eess,grp_stat,grp_cs,grp_econ,grp_math/1/ti:+Face/0/1/0/past,2018,2019/0/1?skip=200&query_id=1c582e6c8afc6146&
```

