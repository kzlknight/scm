from django.urls import path,re_path
from . import views


app_name = 'appExpert'

urlpatterns = [
    path('category/',views.CategoryModelView.as_view({'get':'list'})), # 专家种类
    path('categoryExpert/', views.CategoryExpertModelView.as_view({'get': 'list'})), # 1级页面的专家简介
    path('expert/',views.ExpertAPIView.as_view(),name='expert'),

]



