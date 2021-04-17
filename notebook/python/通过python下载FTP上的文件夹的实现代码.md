_复制代码_ 代码如下:

  
# -*- encoding: utf8 -*-  
import os  
import sys  
import ftplib  
class FTPSync(object):  
def __init__(self):  
self.conn = ftplib.FTP('10.22.33.46', 'user', 'pass')  
self.conn.cwd('/') # 远端FTP目录  
os.chdir('/data/') # 本地下载目录  
def get_dirs_files(self):  
u''' 得到当前目录和文件, 放入dir_res列表 '''  
dir_res = []  
self.conn.dir('.', dir_res.append)  
files = [f.split(None, 8)[-1] for f in dir_res if f.startswith('-')]  
dirs = [f.split(None, 8)[-1] for f in dir_res if f.startswith('d')]  
return (files, dirs)  
def walk(self, next_dir):  
print 'Walking to', next_dir  
self.conn.cwd(next_dir)  
try:  
os.mkdir(next_dir)  
except OSError:  
pass  
os.chdir(next_dir)  
ftp_curr_dir = self.conn.pwd()  
local_curr_dir = os.getcwd()  
files, dirs = self.get_dirs_files()  
print "FILES: ", files  
print "DIRS: ", dirs  
for f in files:  
print next_dir, ':', f  
outf = open(f, 'wb')  
try:  
self.conn.retrbinary('RETR %s' % f, outf.write)  
finally:  
outf.close()  
for d in dirs:  
os.chdir(local_curr_dir)  
self.conn.cwd(ftp_curr_dir)  
self.walk(d)  
def run(self):  
self.walk('.')  
def main():  
f = FTPSync()  
f.run()  
if __name__ == '__main__':  
main()  

