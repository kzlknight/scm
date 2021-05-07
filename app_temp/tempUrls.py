from django.urls import path, re_path
from django.urls import include
from . import views
from aaBase.urlsmapping import UrlMapping as UM

app_name = 'app_temp'

sub_urlpatterns = [
    path('tag/header.html', views.sub_header,),
    path('tag/nav-left.html', views.sub_nav_left,),
    path('tag/nav-top.html', views.sub_nav_top,),
    path('tag/content.html', views.sub_content,),
]

urlpatterns = [
    path('',include(sub_urlpatterns)),
    path('',views.article_list,name='index'),
]
