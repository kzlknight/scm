from django.db import models
from mdeditor.fields import MDTextField
from aaBase.search import table_to_datas, datas_to_table
import datetime
from django.utils.timezone import now


# Create your models here.

class Nav(models.Model):
    class Meta():
        verbose_name = verbose_name_plural = '1.导航'
        ordering = ['position', 'level']

    LEVEL_1 = 1  # 1级分类
    LEVEL_2 = 2  # 2级分类

    LEVEL_CHOICES = (
        (LEVEL_1, '1级标题'),
        (LEVEL_2, '2级标题')

    )

    name = models.CharField(max_length=255, verbose_name='名称')
    position = models.PositiveSmallIntegerField(default=1, verbose_name='位置')
    url = models.CharField(max_length=255, verbose_name='URL地址', null=True, blank=True)
    level = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES, default=LEVEL_1, verbose_name='标题级别')
    superNav = models.ForeignKey(to='appSite.Nav', related_name='subNavs', verbose_name='父标题', null=True, blank=True,
                                 on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class NavLeft(models.Model):
    class Meta():
        verbose_name = verbose_name_plural = '2. 左侧导航'
        ordering = ['level', 'position', ]

    LEVEL_1 = 1  # 1级分类
    LEVEL_2 = 2  # 2级分类

    LEVEL_CHOICES = (
        (LEVEL_1, '1级标题'),
        (LEVEL_2, '2级标题')

    )
    name = models.CharField(max_length=255, verbose_name='名称')
    position = models.PositiveSmallIntegerField(default=1, verbose_name='位置')
    url = models.CharField(max_length=255, verbose_name='URL地址', null=True, blank=True)
    level = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES, default=LEVEL_1, verbose_name='标题级别')
    superNav = models.ForeignKey(to='appSite.NavLeft', related_name='subNavs', verbose_name='父标题', null=True, blank=True,
                                 on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# class SignBoard(models.Model):
#     class Meta():
#         verbose_name = verbose_name_plural = '2 布告板'
#
#     AUTOALTER_TRUE = True
#     AUTOALTER_FALSE = False
#
#     AUTOALTER_CHOICES = (
#         (AUTOALTER_TRUE, '允许更新'),
#         (AUTOALTER_FALSE, '禁止更新'),
#     )
#     SEARCHRESULT_DEFAULT = """| 序号 | 标题 | 地址 |\n| :------------ | :------------ | :------------ |\n|  |  |  |"""
#     name = models.CharField(max_length=255,verbose_name='标题')
#     searchAdd = MDTextField(null=True,blank=True,verbose_name='置顶内容',default=SEARCHRESULT_DEFAULT)
#     searchInterval = models.IntegerField(default=24, verbose_name='更新间隔（小时）')
#     searchNum = models.IntegerField(default=10, null=True, blank=True, verbose_name='搜索数量')
#     searchResult = MDTextField(null=True, blank=True, verbose_name='检索结果', default=SEARCHRESULT_DEFAULT)
#     searchDatetime = models.DateTimeField(null=True, blank=True, verbose_name='搜索更新时间')
#     position = models.PositiveSmallIntegerField(default=1, verbose_name='位置')
#     autoAlter = models.BooleanField(choices=AUTOALTER_CHOICES,default=AUTOALTER_TRUE,verbose_name='自动更新')
#
#
#     def save(self,*args,**kwargs):
#         # 非三类关键字，不进行处理
#         if self.name not in ['最新更新','热门文章','本站推荐']:
#             pass
#         else:
#             # 如果不需要自动更新
#             if not self.autoAlter:
#                 pass
#             # 需要自动更新
#             else:
#                 # 满足更新条件
#                 if not self.searchDatetime or self.searchDatetime + datetime.timedelta(
#                         hours=self.searchInterval) >= now():  # 超时时间未更新
#                     if self.name == '最新更新':
#                         searchDatas = search_article_new(searchNum=self.searchNum) # [index:'',title:'',url:'']
#                         self.searchResult = datas_to_table(datas=searchDatas)
#                     elif self.name == '热门文章':
#                         searchDatas = search_article_hot(searchNum=self.searchNum) # [index:'',title:'',url:'']
#                         self.searchResult = datas_to_table(datas=searchDatas)
#                     elif self.name == '本站推荐':
#                         pass
#                 # 不满足更新条件
#                 else:pass
#             models.Model.save(self,*args,**kwargs)


#
#
# class SignBoardHot(models.Model):
#     class Meta():
#         verbose_name = verbose_name_plural = '2.2 布告板-热门文章'
#     AUTOALTER_TRUE = True
#     AUTOALTER_FALSE = False
#
#     AUTOALTER_CHOICES = (
#         (AUTOALTER_TRUE, '允许更新'),
#         (AUTOALTER_TRUE, '禁止更新'),
#     )
#
#     name = models.CharField(max_length=255,verbose_name='标题')
#     url = models.CharField(max_length=255,verbose_name='地址')
#     position = models.PositiveSmallIntegerField(default=1, verbose_name='位置')
#     autoAlter = models.BooleanField(choices=AUTOALTER_CHOICES,default=AUTOALTER_TRUE,verbose_name='自动更新')
#
# class SignBoardRecommend(models.Model):
#     class Meta():
#         verbose_name = verbose_name_plural = '2.3 布告板-本站推荐'
#
#     AUTOALTER_TRUE = True
#     AUTOALTER_FALSE = False
#
#     AUTOALTER_CHOICES = (
#         (AUTOALTER_TRUE, '允许更新'),
#         (AUTOALTER_TRUE, '禁止更新'),
#     )
#
#     name = models.CharField(max_length=255,verbose_name='标题')
#     url = models.CharField(max_length=255,verbose_name='地址')
#     position = models.PositiveSmallIntegerField(default=1, verbose_name='位置')
#     autoAlter = models.BooleanField(choices=AUTOALTER_CHOICES,default=AUTOALTER_TRUE,verbose_name='自动更新')
