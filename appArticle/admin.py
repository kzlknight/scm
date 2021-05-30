from django.contrib import admin
from django import forms
import urllib.parse as up

from appArticle.models import OutsideCategory,PDFCategory,InsideCategory
from appArticle.models import OutsideArticle,PDFArticle,InsideArticle
from appArticle.models import NavLeft

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


class NavLeftForm(forms.ModelForm):
    class Meta():
        model = NavLeft
        fields = '__all__'

    def clean(self):
        '''

        '''
        superNav = self.cleaned_data.get('superNav')
        level = self.cleaned_data.get('level')

        if superNav and level != NavLeft.LEVEL_2:
            raise forms.ValidationError('存在父级导航，需要为二级标题')
        return self.cleaned_data


@admin.register(NavLeft)
class NavLeftAdmin(admin.ModelAdmin):
    form = NavLeftForm
    search_fields = ['name']
    list_display = ['id', 'name', 'position', 'url', 'level', 'show_subNavs', 'superNav']
    list_filter = ['level']
    list_editable = ['name', 'position', 'url', 'level', 'superNav']
    list_per_page = 20


    ordering = ['level', 'position', 'id']

    def show_subNavs(self, nav):
        names = []
        for n in nav.subNavs.all():
            names.append(n.name)
        return ','.join(names)




    show_subNavs.short_description = '下级'