from django.urls import path
from . import views
from aaBase.urlsmapping import UrlMapping as UM

app_name = 'appArticle'

urlpatterns = [
    path('', views.OutArticleListView.as_view(), name='index'),
    path(UM.OUTSIDE_CATEGORY[1:], views.OutArticleListView.as_view(), name='outsideArticleList'),
    path(UM.PDF_CATEGORY[1:], views.PDFArticleListView.as_view(), name='pdfArticleList'),
    path(UM.INSIDE_CATEGORY[1:], views.InsideArticleListView.as_view(), name='insideArticleList'),

    path(UM.ARTICLE_PDF[1:], views.PDFArticleDetailView.as_view(), name='pdfArticleDetail'),
    path(UM.ARTICLE_INSIDE[1:], views.InsideArticleDetailView.as_view(), name='insideArticleDetail'),
    path(UM.ARTICLE_OUTSIDE[1:], views.OutsideArticleDetailView.as_view(), name='outsideArticleDetail'),

    path(UM.ARTICLE_COLLECT[1:],views.ArticleCollect.as_view(),name='articleCollect'), # category: /ourside /inside /pdf

    path(UM.ARTICLE_SEARCH[1:], views.ArticleSearch.as_view(), name='articleSearch'),

]
