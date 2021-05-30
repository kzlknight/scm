from django.db import models
from django.utils.timezone import now

# Create your models here.


class WebUser(models.Model):
    class Meta():
        verbose_name = verbose_name_plural = '1.用户'

    GENDER_MALE = 1
    GENDER_FAMALE = 0
    GENDER_CHOICES = (
        (GENDER_MALE,'男'),
        (GENDER_FAMALE, '女'),
    )
    name = models.CharField(max_length=16,null=True,blank=True,verbose_name='用户名')
    account = models.CharField(max_length=16,unique=True,verbose_name='账号')
    password = models.CharField(max_length=32,verbose_name='密码')
    tel = models.CharField(max_length=11,null=True,blank=True,verbose_name='手机号')
    gender = models.BooleanField(choices=GENDER_CHOICES,default=GENDER_MALE,blank=True,verbose_name='性别')
    introduction = models.TextField(default='',blank=True,verbose_name='个人简介')
    location = models.CharField(max_length=100,default='',verbose_name='所在地区')
    createDatetime = models.DateTimeField(auto_now_add=now(),verbose_name='创建时间')
    collectedOutsideActicles = models.ManyToManyField(to='appArticle.OutsideArticle',related_name='collectedUsers',verbose_name='收藏文章',blank=True)
    collectedPDFActicles = models.ManyToManyField(to='appArticle.PDFArticle',related_name='collectedUsers',verbose_name='收藏文章',blank=True)
    collectedInsideActicles = models.ManyToManyField(to='appArticle.InsideArticle',related_name='collectedUsers',verbose_name='收藏文章',blank=True)


    def __str__(self):
        return self.account

    def toDict(self):
        return {
            'id':self.id,
            'account':self.account,
            'name':self.name,
            'password':self.password,
            'tel':self.tel,
            'gender':self.gender,
            'introduction':self.introduction,
            'location':self.location,
        }


