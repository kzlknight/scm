import os
from django.db import models
from django.utils import timezone
from mdeditor.fields import MDTextField
from django.utils.timezone import now
import urllib.parse as up
from aaBase.urlsmapping import UrlMapping as UM
from aaBase.random_filename import random_filename


class Category(models.Model):
    class Meta():
        verbose_name = verbose_name_plural = '1.文章种类'

    name = models.CharField(max_length=255,verbose_name='文章种类')
    url = models.CharField(null=True,blank=True,max_length=255,verbose_name='URL',help_text='管理系统自行维护',editable=False) # todo Admin维护
    position = models.PositiveSmallIntegerField(default=1,verbose_name='位置')
    createDatetime = models.DateTimeField(auto_now_add=now(),verbose_name='创建时间')


    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        '''
        维护URL
        '''
        if not self.id:
            models.Model.save(self,*args,**kwargs)
        url = up.urljoin(
            UM.ARTICLE_CATEGORY, '?id={id}'.format(id=self.id)
        )
        self.url = url
        models.Model.save(self,*args,**kwargs)


# 上传PDF文件
def upload_pdflink(instance,filename):
    filename_new = random_filename(filename)
    return os.path.join('article_pdf', filename_new)

# 上传文章头图
def upload_ppicture(instance,filename):
    filename_new = random_filename(filename)
    return os.path.join('article_ppicture',filename_new)

# 上传文章视频
def upload_video(instance,filename):
    filename_new = random_filename(filename)
    return os.path.join('article_video',filename_new)


class TagKeyword(models.Model):
    class Meta():
        verbose_name = verbose_name_plural = '2.关键字'


    keywords = models.TextField(null=True,blank=True,verbose_name='分类标签',help_text='关键字使用英文逗号隔开","')
    category = models.ForeignKey(to='appArticle.Category',on_delete=models.CASCADE,related_name='keywords',verbose_name='文章种类')


class Article(models.Model):

    class Meta():
        verbose_name = verbose_name_plural = '3.文章详细'

    ARTICLETYPE_INSIDE = 1 # 站内文章
    ARTICLETYPE_OUTSIDE = 2 # 站外文章
    ARTICLETYPE_PDF = 3 # PDF
    ARTICLETYPE_CHOICES = (
        (ARTICLETYPE_INSIDE, '站内文章'),
        (ARTICLETYPE_OUTSIDE,'站外文章'),
        (ARTICLETYPE_PDF, 'PDF'),
    )


    title = models.CharField(max_length=255,verbose_name='标题')
    articleType = models.PositiveSmallIntegerField(default=ARTICLETYPE_INSIDE,choices=ARTICLETYPE_CHOICES,verbose_name='文章种类')
    outlink = models.CharField(max_length=255,null=True,blank=True,verbose_name='外部链接地址')
    url = models.CharField(max_length=255,null=True,blank=True,verbose_name='文章地址',help_text='站内文章或PDF的地址，管理系统自行维护')
    pdflink = models.FileField(upload_to=upload_pdflink,null=True,blank=True,verbose_name='PDF地址')
    ppicture = models.FileField(upload_to=upload_ppicture,null=True,blank=True,verbose_name='配图')
    content = MDTextField(null=True,blank=True,verbose_name='正文')
    brief = models.CharField(null=True,blank=True,max_length=255,verbose_name='简介') # 所有种类的文章都应该有简介
    author = models.CharField(max_length=255,null=True,blank=True,verbose_name='作者')
    origin = models.CharField(max_length=255,null=True,blank=True,verbose_name='来源')
    createDatetime = models.DateTimeField(auto_now_add=timezone.now(),verbose_name='创建时间')
    category = models.ForeignKey(to='appArticle.Category', on_delete=models.CASCADE, verbose_name='文章种类',related_name='articles')
    clickNum = models.IntegerField(default=0,verbose_name='点击数量')
    collectNum = models.IntegerField(default=0,verbose_name='收藏数量')
    video = models.FileField(upload_to=upload_video,null=True,blank=True,verbose_name='视频')
    position = models.PositiveIntegerField(default=1,verbose_name='文章位置')
    keywords = models.CharField(max_length=255,null=True,blank=True,verbose_name='关键字')


    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        '''
        save方法之前需要验证
        重写save方法的目的在于维护url
        '''
        # 新对象，需要先保存以获得ID
        if not self.id:
            models.Model.save(self,*args,**kwargs)
        print(self.articleType)
        # 维护文章
        # 1.站内文章
        if self.articleType == Article.ARTICLETYPE_INSIDE:
            self.url = up.urljoin(
                UM.ARTICLE_INSIDE, '?id={id}'.format(id=self.id)
            )
        # 2.PDF
        elif self.articleType == Article.ARTICLETYPE_PDF:
            self.url = up.urljoin(
                UM.ARTICLE_PDF, '?id={id}'.format(id=self.id)
            )
        # 3.站外链接
        elif self.articleType == Article.ARTICLETYPE_OUTSIDE:
            self.url = self.outlink
        # 再次保存
        models.Model.save(self,*args,**kwargs)




# 当前版本选择在appSite中维护
# class SignBoard(models.Model):
#
#     class Meta():
#         verbose_name = verbose_name_plural = '布告牌'
#
#     title = models.CharField(max_length=255,verbose_name='标题')
#     url = models.CharField(max_length=255,verbose_name='网址')
#     position = models.PositiveSmallIntegerField(default=0,verbose_name='位置')
#
#     def __str__(self):
#         return self.title









