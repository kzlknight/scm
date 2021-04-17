from rest_framework.views import APIView
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from appArticle.models import Article, TagKeyword, Category
from rest_framework import viewsets
from appArticle.serializers import CategoryAricleSerializer  # 1级页面展示Article
from appArticle.serializers import CategoryTagKeywordSerializer  # 1级页面展示分类关键字
from appArticle.serializers import CategorySerializer  # 全部的文章分类
from appArticle.serializers import ArticleSerializer # 内部文章详细
from aaBase.base_view import MyBasePagination


class CategoryArticlePagination(MyBasePagination):
    page_size = 20


class CategoryAricleModelView(viewsets.ModelViewSet):
    queryset = Article.objects.all()  # 理解为默认
    serializer_class = CategoryAricleSerializer
    pagination_class = CategoryArticlePagination

    def get_queryset(self):
        """
        param:
            category_id:# int 种类ID
            keyword: # str 关键字
            year: # YYYY 创建年费
            order_bys:['click_num','collectNum','-createDatetime']
                order_by_click # 1|0 点击量排序
                order_by_collect # 1|0 收藏排序
                order_by_createDatetime # 1|0 创建时间排序


        """
        category_id = self.request.query_params.get('category_id', None)
        keyword = self.request.query_params.get('keyword', None)
        year = self.request.query_params.get('year', None)

        order_bys = self.request.query_params.getlist('order_bys')

        filter_dict = {}

        if category_id:
            filter_dict['category_id'] = category_id
        if keyword:
            filter_dict['keywords__contains'] = keyword
        if year:
            filter_dict['createDatetime__year'] = year

        return self.queryset.filter(**filter_dict).order_by(*order_bys).order_by('position','-createDatetime')


class CategoryTagKeywordModelView(viewsets.ModelViewSet):
    queryset = TagKeyword.objects.all()
    serializer_class = CategoryTagKeywordSerializer

    def get_queryset(self):
        """
        param:
            category_id: int 种类ID
        """

        category_id = self.request.query_params.get('category_id', None)

        filter_dict = {}
        if category_id:
            filter_dict['category_id'] = category_id

        return self.queryset.filter(**filter_dict)


class CategoryModelView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        """
        param:
            category_id: int 种类ID
        """
        category_id = self.request.query_params.get('category_id', None)

        filter_dict = {}
        if category_id:
            filter_dict['id'] = category_id

        return self.queryset.filter(**filter_dict).order_by('position')


class ArticleAPIView(APIView):
    def get(self,request):
        article_id = request.query_params.get('article_id',None)
        article = Article.objects.filter(id=article_id)
        article_serializer = ArticleSerializer(article,many=True)
        return Response(article_serializer.data)


