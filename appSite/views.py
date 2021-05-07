from django.shortcuts import HttpResponse
from appSite.models import Nav
from appSite.serializers import NavSerializer
from rest_framework import viewsets


from rest_framework.permissions import BasePermission


class IsLogin(BasePermission):
    message = '未登录'

    def has_permission(self, request, view):
        return True

class NavModelView(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = [IsLogin]
    queryset = Nav.objects.all() # 理解为默认
    serializer_class = NavSerializer

    def get_queryset(self):
        return self.queryset


def page_not_found(request,exception):
    return HttpResponse('aaa')


