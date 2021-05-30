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


