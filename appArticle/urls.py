from django.urls import path,re_path,include
from rest_framework import routers
from . import views
#
#
#
app_name = 'appArticle'
# urlpatterns = [
#     # 某类别下的文章s
#     path('categoryArticle/',views.CategoryAricleModelView.as_view({'get':'list'}),name='categoryArticle'),
#     # 类别下的关键字
#     path('categoryTagKeyword/', views.CategoryTagKeywordModelView.as_view({'get': 'list'}), name='categoryTagKeyword'),
#     # 搜索的文章类别
#     path('category/',views.CategoryModelView.as_view({'get':'list'}),name='cateogry'),
#     # 文章详细
#     path('article/', views.ArticleAPIView.as_view(), name='article'),
# ]

from aaBase.urlsmapping import UrlMapping as UM

urlpatterns = [
    path('',views.OutArticleListView.as_view(),name='index'),
    path(UM.OUTSIDE_CATEGORY[1:],views.OutArticleListView.as_view(),name='outsideArticleList'),
    path(UM.PDF_CATEGORY[1:], views.PDFArticleListView.as_view(), name='pdfArticleList'),
    path(UM.INSIDE_CATEGORY[1:], views.InsideArticleListView.as_view(), name='insideArticleList'),
    path(UM.ARTICLE_PDF[1:],views.PDFArticleDetailView.as_view(),name='pdfArticleDetail'),
    path(UM.ARTICLE_INSIDE[1:], views.InsideArticleDetailView.as_view(), name='insideArticleDetail'),
]
