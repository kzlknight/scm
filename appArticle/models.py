import os
from django.db import models
from django.utils import timezone
from mdeditor.fields import MDTextField
from django.utils.timezone import now
import urllib.parse as up
from aaBase.urlsmapping import UrlMapping as UM
from aaBase.random_filename import random_filename


# 抽象类
class CategoryAbstract(models.Model):
    class Meta():
        abstract = True
        ordering = ['position']


    name = models.CharField(max_length=255, verbose_name='文章种类')
    url = models.CharField(null=True, blank=True, max_length=255, verbose_name='URL', help_text='管理系统自行维护',
                           editable=False)
    position = models.PositiveSmallIntegerField(default=1, verbose_name='位置')
    createDatetime = models.DateTimeField(auto_now_add=now(), verbose_name='创建时间')
    keywordsAll = models.TextField(default='', blank=True, verbose_name='全部关键字', help_text='用于批量上传接口，英文逗号分隔')
    keywordsTag = models.TextField(default='', blank=True, verbose_name='行业分类', help_text='英文逗号分隔')

    def __str__(self):
        return self.name




# 抽象类

class ArticleAbstract(models.Model):
    class Meta():
        abstract = True

    title = models.CharField(max_length=255, verbose_name='标题')
    url = models.CharField(max_length=255, null=True, blank=True, verbose_name='文章地址', help_text='系统维护')
    content = MDTextField(null=True, blank=True, verbose_name='正文')
    brief = models.CharField(null=True, blank=True, max_length=255, verbose_name='简介')  # 所有种类的文章都应该有简介
    author = models.CharField(max_length=255, null=True, blank=True, verbose_name='作者')
    origin = models.CharField(max_length=255, null=True, blank=True, verbose_name='来源')
    createDatetime = models.DateTimeField(auto_now_add=timezone.now(), verbose_name='创建时间')
    publishDatetime = models.DateTimeField(auto_now_add=timezone.now(), verbose_name='发布时间')
    clickNum = models.IntegerField(default=0, verbose_name='点击数量')
    collectNum = models.IntegerField(default=0, verbose_name='收藏数量')
    position = models.PositiveIntegerField(default=1, verbose_name='文章位置')
    keywords = models.CharField(max_length=255, null=True, blank=True, verbose_name='关键字')

    def __str__(self):
        return self.title


class OutsideCategory(CategoryAbstract):
    class Meta():
        verbose_name = verbose_name_plural = '1.1 外部文章种类'

    def save(self, *args, **kwargs):
        '''
        维护URL
        '''
        if not self.id:
            models.Model.save(self, *args, **kwargs)
        url = up.urljoin(
            UM.OUTSIDE_CATEGORY, '?category_id={id}'.format(id=self.id)
        )
        self.url = url
        models.Model.save(self, *args, **kwargs)


class PDFCategory(CategoryAbstract):
    class Meta():
        verbose_name = verbose_name_plural = '2.1 PDF文章种类'

    def save(self, *args, **kwargs):
        '''
        维护URL
        '''
        if not self.id:
            models.Model.save(self, *args, **kwargs)
        url = up.urljoin(
            UM.PDF_CATEGORY, '?category_id={id}'.format(id=self.id)
        )
        self.url = url
        models.Model.save(self, *args, **kwargs)


class InsideCategory(CategoryAbstract):
    class Meta():
        verbose_name = verbose_name_plural = '3.1 内部文章种类'

    def save(self, *args, **kwargs):
        '''
        维护URL
        '''
        if not self.id:
            models.Model.save(self, *args, **kwargs)
        url = up.urljoin(
            UM.INSIDE_CATEGORY, '?category_id={id}'.format(id=self.id)
        )
        self.url = url
        models.Model.save(self, *args, **kwargs)


# 上传PDF文件
def upload_pdflink(instance, filename):
    filename_new = random_filename(filename)
    return os.path.join('article_pdf', filename_new)


# 上传文章头图
def upload_ppicture(instance, filename):
    filename_new = random_filename(filename)
    return os.path.join('article_ppicture', filename_new)


# 上传文章视频
def upload_video(instance, filename):
    filename_new = random_filename(filename)
    return os.path.join('article_video', filename_new)


class OutsideArticle(ArticleAbstract):
    class Meta():
        verbose_name = verbose_name_plural = '1.2 外部文章详细'

    outlink = models.CharField(max_length=255, verbose_name='外部链接地址')
    category = models.ForeignKey(to='appArticle.OutsideCategory',related_name='articles',on_delete=models.CASCADE,verbose_name='种类')

    def save(self, *args,**kwargs):
        if not self.id:
            models.Model.save(self,*args,**kwargs)
        self.url = self.outlink
        models.Model.save(self,*args,**kwargs)



class PDFArticle(ArticleAbstract):
    class Meta():
        verbose_name = verbose_name_plural = '2.2 PDF文章详细'

    pdflink = models.FileField(upload_to=upload_pdflink, null=True, blank=True, verbose_name='PDF地址')
    category = models.ForeignKey(to='appArticle.PDFCategory',related_name='articles',on_delete=models.CASCADE,verbose_name='种类')

    def save(self,*args,**kwargs):
        if not self.id:
            models.Model.save(self,*args,**kwargs)
        self.url = up.urljoin(
            UM.ARTICLE_PDF,'?id={id}'.format(id=self.id)
        )
        models.Model.save(self, *args, **kwargs)


class InsideArticle(ArticleAbstract):
    class Meta():
        verbose_name = verbose_name_plural = '3.2 内部文章详细'

    content = MDTextField(verbose_name='正文')
    category = models.ForeignKey(to='appArticle.InsideCategory',related_name='articles',on_delete=models.CASCADE,verbose_name='种类')

    def save(self,*args,**kwargs):
        if not self.id:
            models.Model.save(self,*args,**kwargs)
        self.url = up.urljoin(
            UM.ARTICLE_INSIDE,'?id={id}'.format(id=self.id)
        )
        models.Model.save(self, *args, **kwargs)
