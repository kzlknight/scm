from django.urls import path, re_path
from . import views
from aaBase.urlsmapping import UrlMapping as UM

app_name = 'app_temp'

urlpatterns = [
    path('',views.index_handler,name='index')
]
