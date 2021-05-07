from django.contrib import admin
from django import forms
import urllib.parse as up

from appArticle.models import Category, Article, TagKeyword
from aaBase.urlsmapping import UrlMapping as UM


# 种类管理
@admin.register(Category)
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

    # def save_model(self, request, category, form, change):
    #     '''
    #     维护url
    #     '''
    #     category.save()
    #     url = up.urljoin(
    #         UM.ARTICLE_CATEGORY, '?id={id}'.format(id=category.id)
    #     )
    #     category.url = url
    #     category.save()



# 文章Admin的表单验证
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

    def clean(self):
        '''
        # 站内文章 content不能为空
        # 站外文章 outlink不能为空
        # PDF文章 pdflink不能为空
        '''

        articleType = self.cleaned_data.get('articleType') # 文章种类
        # 站内文章 content不能为空
        if articleType == Article.ARTICLETYPE_INSIDE:
            content = self.cleaned_data.get('content')
            if not content: raise forms.ValidationError('站内文章 正文不能为空')
        # 站外文章 outlink不能为空
        elif articleType == Article.ARTICLETYPE_OUTSIDE:
            outlink = self.cleaned_data.get('outlink')
            if not outlink: raise forms.ValidationError('站外文章 外部链接地址不能为空')
        # PDF文章 pdflink不能为空
        elif articleType == Article.ARTICLETYPE_PDF:
            pdflink = self.cleaned_data.get('pdflink')
            if not pdflink: raise forms.ValidationError('PDF文章 PDF地址不能为空')
        return self.cleaned_data


# 文章管理
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # 表单验证
    form = ArticleForm
    # 展示字段
    list_display = ['id', 'title', 'position', 'articleType', 'author', 'origin', 'category', 'clickNum', 'collectNum','url']
    # 不可编辑字段
    readonly_fields = ['url']
    # 搜索字段
    search_fields = ['title', 'content', 'brief', 'origin', 'author']
    # 分类字段
    list_filter = ['category', 'articleType','createDatetime']
    # 可编辑字段
    list_editable = ['position', ]
    # 排序
    ordering = ['position', 'id']
    # 页面数量
    list_per_page = 50

    # def save_model(self, request, article, form, change):
    #     '''
    #     维护url
    #     '''
    #     # 保存数据库，以获得id
    #     article.save()
    #     # 站内文章
    #     if article.articleType == Article.ARTICLETYPE_INSIDE:
    #         article.url = up.urljoin(
    #             UM.ARTICLE_INSIDE, '?id={id}'.format(id=article.id)
    #         )
    #     # PDF
    #     elif article.articleType == Article.ARTICLETYPE_PDF:
    #         pdf_filename = article.pdflink.split('/')[-1]
    #         article.url = up.urljoin(
    #             UM.ARTICLE_pdf, '?pdf={pdf}'.format(pdf=pdf_filename)
    #         )
    #     # 站外链接
    #     elif article.articleType == Article.ARTICLETYPE_OUTSIDE:
    #         article.url = article.outlink
    #     # 再次保存
    #     article.save()

# 种类下属关键字管理
@admin.register(TagKeyword)
class TagKeywordAdmin(admin.ModelAdmin):
    # 展示字段
    list_display = ['category', 'keywords']
    # 页面数量
    list_per_page = 20
