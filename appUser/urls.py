from django.urls import path,re_path
from . import views


app_name = 'appUser'

urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('logout',views.LogoutView.as_view(),name='logout'),
    path('user/info',views.InfoView.as_view(),name='info'),
    path('user/collect/<slug:category>', views.CollectView.as_view(), name='collect'),
]