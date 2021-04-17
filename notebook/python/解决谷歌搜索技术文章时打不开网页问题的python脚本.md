注意：Win7或者WIn8用户要用管理员权限执行。  
  
项目地址： [ http://code.google.com/p/my-hosts-file/downloads
](http://code.google.com/p/my-hosts-file/downloads)  
  

_复制代码_ 代码如下:

  
import urllib  
import os  
import shutil  
  
hostspath = "C:\\Windows\\System32\\drivers\\etc"  
savepath = hostspath + "\\hostsave"  
  
def download_hosts(url = "http://my-hosts-
file.googlecode.com/svn/trunk/hosts"):  
os.chdir(hostspath)  
if os.getcwd() != hostspath:  
print("Switch Dir to System32 Error,check permission!\npwd:"+os.getcwd())  
exit()  
try:  
urllib.urlretrieve(url, "hostsave")  
except:  
print '\t Error when retrieveing hosts file from url: ', url  
  
def backup_hosts():  
shutil.copy("hosts","hosts.bak")  
  
def replace_hosts():  
shutil.copy("hostsave", "hosts")  
print("Replace original hosts file finished, then flush dns...")  
os.remove(savepath)  
os.system("ipconfig /flushdns")  
  
def main():  
download_hosts()  
backup_hosts()  
replace_hosts()  
if __name__ == '__main__':  
main()  

