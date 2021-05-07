from django.urls import path,re_path
from . import views
from aaBase.urlsmapping import UrlMapping as UM


app_name = 'appExpert'

urlpatterns = [
    path(UM.EXPERT_CATEGORY[1:],views.ExpertListView.as_view(),name='expertList'),
    path(UM.EXPERT_DETAIL[1:],views.ExpertDetailView.as_view(),name='expertDetail'),
    # path('category/',views.CategoryModelView.as_view({'get':'list'})), # 专家种类
    # path('categoryExpert/', views.CategoryExpertModelView.as_view({'get': 'list'})), # 1级页面的专家简介
    # path('expert/',views.ExpertAPIView.as_view(),name='expert'),

]



