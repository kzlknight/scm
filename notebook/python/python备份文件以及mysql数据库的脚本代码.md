_复制代码_ 代码如下:

  
#!/usr/local/python  
import os  
import time  
import string  
  
source=['/var/www/html/xxx1/','/var/www/html/xxx2/']  
target_dir='/backup/'  
target=target_dir+time.strftime('%Y%m%d')  
zip_comm='zip -r %s %s'%(target," ".join(source))  
  
target_database=['DB_name1','DB_name2']  
sql_user='root'  
sql_pwd='xxx'  
  
if os.system(zip_comm) == 0:  
print 'file backup Success is:',target  
#if python version is 3.x ,print('file backup Success is:',target)  
else:  
print 'file backup failed!'  
  
for database_name in target_database:  
target_sql=target_dir+database_name+time.strftime('%Y%m%d')+'.sql'  
sql_comm='/usr/local/mysql/bin/mysqldump -u %s -p%s %s >
%s'%(sql_user,sql_pwd,database_name,target_sql)  
if os.system(sql_comm) == 0:  
print database_name,'is backup seccess!'  
else:  
print database_name,'is backup Failed!!'  

