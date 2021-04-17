from django.urls import path,re_path,include
from rest_framework import routers
from . import views



app_name = 'appArticle'
urlpatterns = [
    # 某类别下的文章s
    path('categoryArticle/',views.CategoryAricleModelView.as_view({'get':'list'}),name='categoryArticle'),
    # 类别下的关键字
    path('categoryTagKeyword/', views.CategoryTagKeywordModelView.as_view({'get': 'list'}), name='categoryTagKeyword'),
    # 搜索的文章类别
    path('category/',views.CategoryModelView.as_view({'get':'list'}),name='cateogry'),
    # 文章详细
    path('article/', views.ArticleAPIView.as_view(), name='article'),
]