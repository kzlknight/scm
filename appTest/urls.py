from django.urls import path,re_path
from . import views

urlpatterns = [
    path('',views.V1.as_view()),
    path('1', views.some_view,),
]