from django.shortcuts import render
from aaBase.base_view import MyBasePagination
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from appExpert.models import Category,Expert
from appExpert.serializers import CategoryExpertSerializers,CategorySerializers,ExpertSerializers
# Create your views here.

class CategoryExpertPagination(MyBasePagination):
    page_size = 20


# 专家种类
class CategoryModelView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

    def get_queryset(self):
        """
        param:无
        """
        return self.queryset.all().order_by('position')

# 1级页面的专家详细
class CategoryExpertModelView(viewsets.ModelViewSet):
    queryset = Expert.objects.all()
    serializer_class = CategoryExpertSerializers
    pagination_class = CategoryExpertPagination


    def get_queryset(self):
        """
        param:category_id
        """
        category_id = self.request.query_params.get('category_id', None)

        filter_dict = {}
        if category_id:
            filter_dict['category_id'] = category_id

        print(category_id)
        return self.queryset.filter(**filter_dict).order_by('position','-createDatetime')

class ExpertAPIView(APIView):
    def get(self,request):
        expert_id = request.query_params.get('expert_id',None)
        expert = Expert.objects.filter(id=expert_id)
        expert_serializer = ExpertSerializers(expert,many=True)
        return Response(expert_serializer.data)



