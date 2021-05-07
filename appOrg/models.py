from django.db import models
from mdeditor.fields import MDTextField
from django.utils.timezone import now
import urllib.parse as up
from aaBase.urlsmapping import UrlMapping as UM
from aaBase.search import search_article,table_to_datas,datas_to_table
import datetime
# Create your models here.

class Rule(models.Model):
    class Meta():
        verbose_name = verbose_name_plural = '1.匹配规则'

    SEARCH_TRUE = True
    SEARCH_FALSE = False

    SEARCH_CHOICES = (
        (SEARCH_TRUE,'使用'),
        (SEARCH_FALSE, '禁用'),

    )

    searchInterval = models.IntegerField(default=24, verbose_name='更新间隔（小时）')
    searchNum = models.IntegerField(default=50, verbose_name='搜索数量')  # 优先级低于Org
    name = models.CharField(max_length=255,verbose_name='规则名称')
    title = models.BooleanField(default=SEARCH_TRUE,choices=SEARCH_CHOICES,verbose_name='是否搜索标题')
    content = models.BooleanField(default=SEARCH_TRUE,choices=SEARCH_CHOICES,verbose_name='是否搜索正文')
    brief = models.BooleanField(default=SEARCH_TRUE,choices=SEARCH_CHOICES,verbose_name='是否搜索简介')
    author = models.BooleanField(default=SEARCH_TRUE,choices=SEARCH_CHOICES,verbose_name='是否搜索作者')
    origin = models.BooleanField(default=SEARCH_TRUE,choices=SEARCH_CHOICES,verbose_name='是否搜索来源')
    keywords = models.BooleanField(default=SEARCH_TRUE,choices=SEARCH_CHOICES,verbose_name='是否搜索关键字')

    def __str__(self):
        return self.name


class Organization(models.Model):
    class Meta():
        verbose_name = verbose_name_plural = '2.机构详细'

    SEARCH_TRUE = True
    SEARCH_FALSE = False

    SEARCH_CHOICES = (
        (SEARCH_TRUE,'使用'),
        (SEARCH_FALSE, '禁用'),

    )

    AUTOALTER_TRUE = True
    AUTOALTER_FALSE = False

    AUTOALTER_CHOICES = (
        (AUTOALTER_TRUE, '允许更新'),
        (AUTOALTER_FALSE, '禁止更新'),
    )

    SEARCHRESULT_DEFAULT = """| 序号 | 标题 | 地址 |\n| :------------ | :------------ | :------------ |\n|  |  |  |"""
    url = models.CharField(max_length=255, null=True, blank=True, verbose_name='地址', help_text='系统维护')
    name = models.CharField(max_length=255, verbose_name='机构名称')
    searchKeywords = models.CharField(max_length=255,null=True,blank=True,verbose_name='搜索关键字')
    brief = models.CharField(null=True,blank=True,max_length=255, verbose_name='机构简介')
    position = models.PositiveSmallIntegerField(default=1, verbose_name='位置')
    searchResult = MDTextField(null=True, blank=True, verbose_name='检索结果',default=SEARCHRESULT_DEFAULT)
    searchNum = models.IntegerField(null=True,blank=True,verbose_name='搜索数量')
    searchDatetime = models.DateTimeField(null=True, blank=True, verbose_name='搜索更新时间')
    createDatetime = models.DateTimeField(auto_now_add=now(), verbose_name='创建时间')
    autoAlter = models.BooleanField(choices=AUTOALTER_CHOICES,default=AUTOALTER_TRUE,verbose_name='自动更新')

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        '''
        URL和检索内容
        '''
        if not self.id:
            models.Model.save(self,*args,**kwargs)
        # 维护URL
        self.url = up.urljoin(
            UM.ORG_DETAIL,'?id={id}'.format(id=self.id)
        )
        # 维护检索
        if self.autoAlter:  # 需要更新
            rule = Rule.objects.all().first()  # 规则
            searchInterval = rule.searchInterval  # 更新时间间隔
            # 无更新时间或者应该被更新
            if not self.searchDatetime or self.searchDatetime + datetime.timedelta(
                    hours=searchInterval) <= now():  # 超时时间未更新
                # 处理search_texts
                if not self.searchKeywords:
                    search_texts = []
                else:
                    search_texts = self.searchKeywords.split(',')
                searchDatas: str = search_article(
                    search_texts=search_texts,
                    rule=rule,
                    searchNum=self.searchNum or rule.searchNum,
                ) # [{index:"",title:"",url:""},]
                self.searchResult = datas_to_table(searchDatas) # 把搜索的结果变成markdown的table
                self.searchDatetime = now()
            else: pass # 需要更新但为到更新时间
        else: pass # 不需要更新
        models.Model.save(self,*args,**kwargs)



