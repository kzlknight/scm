from django.contrib import admin
from django import forms
import urllib.parse as up

from appArticle.models import OutsideCategory,PDFCategory,InsideCategory
from appArticle.models import OutsideArticle,PDFArticle,InsideArticle

from aaBase.urlsmapping import UrlMapping as UM




# 种类管理
# @admin.register(OutsideArticle)
class CategoryAdmin(admin.ModelAdmin):
    # 搜索
    search_fields = ['name']
    # 不可编辑字段
    readonly_fields = ['url']
    # 展示字段
    list_display = ['id', 'name', 'url', 'position', 'createDatetime']
    # 可编辑字段
    list_editable = ['name', 'position']
    # 显示数量
    list_per_page = 10
    # 排序
    ordering = ['position', 'id']


@admin.register(OutsideCategory)
class OutsideCategoryAdmin(CategoryAdmin):
    pass

@admin.register(PDFCategory)
class PDFCategoryAdmin(CategoryAdmin):
    pass

@admin.register(InsideCategory)
class InsideCategoryAdmin(CategoryAdmin):
    pass



# 文章管理
# @admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # 表单验证
    # pass
    # 展示字段
    list_display = ['id', 'title', 'position', 'author', 'origin', 'category', 'clickNum', 'collectNum','url','createDatetime','publishDatetime']
    # 不可编辑字段
    readonly_fields = ['url']
    # 搜索字段
    search_fields = ['title', 'content', 'brief', 'origin', 'author']
    # 分类字段
    list_filter = ['category', 'createDatetime','publishDatetime']
    # 可编辑字段
    list_editable = ['position', ]
    # 排序
    ordering = ['position', 'id']
    # 页面数量
    list_per_page = 50


@admin.register(OutsideArticle)
class OutsideArticleAdmin(ArticleAdmin):
    pass

@admin.register(PDFArticle)
class PDFArticleAdmin(ArticleAdmin):
    pass

@admin.register(InsideArticle)
class InsideArticleAdmin(ArticleAdmin):
    pass
