from django.shortcuts import HttpResponse
from appSite.models import Nav
from appSite.serializers import NavSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class NavAPIView(APIView):
    def get(self,request,format=None):
        id = self.request.query_params.get('id',1)

        navs = Nav.objects.filter(id = id)
        nav_serializer = NavSerializer(navs,many=True)
        return Response(nav_serializer.data)



from rest_framework import mixins
from rest_framework import generics
# class NavMixinView(mixins.ListModelMixin,generics.GenericAPIView):
#     queryset = Nav.objects.all() # 理解为默认
#     serializer_class = NavSerializer
    # def get(self,request,*args,**kwargs):
    #     id = self.request.query_params.get('id',1)
    #     navs = Nav.objects.filter(id=id)
    #     self.queryset = navs
    #     return self.list(request,*args,**kwargs)

class NavMixinView(generics.ListAPIView):
    queryset = Nav.objects.all() # 理解为默认
    serializer_class = NavSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)



from rest_framework.permissions import BasePermission


class IsLogin(BasePermission):
    message = '未登录'

    def has_permission(self, request, view):
        return True



from rest_framework import viewsets
class NavPerimissionView(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = [IsLogin]
    queryset = Nav.objects.all() # 理解为默认
    serializer_class = NavSerializer

    def get_queryset(self):
        return self.queryset



def test_handler(request):
    return HttpResponse('ok')