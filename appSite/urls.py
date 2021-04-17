from django.urls import path,re_path
from . import views
from rest_framework.routers import DefaultRouter
from django.conf.urls import include

app_name = 'appSite'

from django.urls import path,re_path
from . import views

urlpatterns = [
    path('nav',views.NavModelView.as_view({'get':'list'}),name='nav')
]
