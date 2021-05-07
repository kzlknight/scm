from django.urls import path,re_path
from . import views
from aaBase.urlsmapping import UrlMapping as UM

app_name = 'appOrg'

urlpatterns = [
    path(UM.ORG_CATEGORY[1:],views.ORGListView.as_view(),name='orgList'),
    path(UM.ORG_DETAIL[1:],views.ORGDetailView.as_view(),name='orgDetail'),
]