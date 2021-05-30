"""scm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.views import static as view_static
from django.conf import settings

urlpatterns = [
    path(r'mdeditor/', include('mdeditor.urls')),
    path('admin/', admin.site.urls),
    path('', include('appArticle.urls', namespace='appArticle'), ),
    path('', include('appExpert.urls', namespace='appExpert'), ),
    path('', include('appOrg.urls', namespace='appOrg'), ),
    path('', include('appSite.urls', namespace='appSite'), ),
    path('', include('appUser.urls', namespace='appUser'), ),

    # path('api/appArticle/', include('appArticle.urls', namespace='appArticle'), ),
    # path('api/appExpert/', include('appExpert.urls', namespace='appExpert'), ),
    # path('api/appOrg/', include('appOrg.urls', namespace='appOrg'), ),
    # path('api/appSite/', include('appSite.urls', namespace='appSite'), ),
    # path('api/appUser/', include('appUser.urls', namespace='appUser'), ),
    # path('t/', include('appTest.urls', )), # 测试接口
    # path('', include('app_temp.tempUrls', namespace='app_temp')),
    re_path(r'^static/(?P<path>.*)$', view_static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    re_path(r'^media/(?P<path>.*)$', view_static.serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
]

from appSite.views import page404
handler404 = page404

# mdeditor
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                          document_root=settings.STATIC_ROOT)
