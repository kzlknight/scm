from django.db import models
from django.utils.timezone import now

# Create your models here.


class User(models.Model):
    class Meta():
        verbose_name = verbose_name_plural = '1.用户'

    name = models.CharField(max_length=16,null=True,blank=True,verbose_name='用户名')
    account = models.CharField(max_length=16,unique=True,verbose_name='账号')
    password = models.CharField(max_length=32,verbose_name='密码')
    tel = models.CharField(max_length=11,null=True,blank=True,verbose_name='手机号')
    createDatetime = models.DateTimeField(auto_now_add=now(),verbose_name='创建时间')
    collectedActicles = models.ManyToManyField(to='appArticle.Article',related_name='collectedUsers',verbose_name='收藏文章')


    def __str__(self):
        return self.name


