from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.views import View
from django.db.models import Q, F
# 分页
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
# model:
from appSite.models import Nav
from appUser.models import WebUser
from appArticle.models import OutsideCategory, InsideCategory, PDFCategory
from appArticle.models import OutsideArticle, InsideArticle, PDFArticle
# sys
import traceback
# up
import urllib.parse as up
# tool
# from aaBase.build_url import get_url
from copy import deepcopy
import datetime

from typing import Union

from appArticle.views.base import ArticleListTool,SearchTool

from django.views.generic import DetailView, ListView


def index_handler(request):
    request.get_full_path()


class ArticleListView(View):
    Article: OutsideArticle
    Category: OutsideCategory

    def my_get(self, request):
        # 1. 实例化
        at = ArticleListTool(request)
        at.Category = self.Category
        at.Article = self.Article
        # 2. 验证数据
        if not at.clean():
            print(at.error_message)
            raise Http404('')
        # 3. 上方分类
        nav_top_data = at.nav_top_data()
        # 4. 页面内容数据
        articles = at.instance_page
        # 5. 分页数据
        page_data = at.page_data()

        request.context['articles'] = articles
        request.context['page_data'] = page_data
        request.context['nav_top_data'] = nav_top_data
        return request


class OutArticleListView(ArticleListView):
    Category = OutsideCategory
    Article = OutsideArticle

    def get(self, request):
        request = self.my_get(request)
        # 6 User
        webUserDict = request.session.get('webUser', None)
        ids = []
        if webUserDict:
            webUser = get_object_or_404(WebUser, id=webUserDict['id'])
            for id_tup in webUser.collectedOutsideActicles.values_list('id'):
                ids.append(id_tup[0])
        else:
            pass
        request.context['collect_ids'] = ids
        request.context['category'] = 'outside'


        return render(request, 'appArticle/articleList.html', request.context)


class PDFArticleListView(ArticleListView):
    Category = PDFCategory
    Article = PDFArticle

    def get(self, request):
        request = self.my_get(request)
        # 6 User
        webUserDict = request.session.get('webUser', None)
        ids = []
        if webUserDict:
            webUser = get_object_or_404(WebUser, id=webUserDict['id'])
            for id_tup in webUser.collectedOutsideActicles.values_list('id'):
                ids.append(id_tup[0])
        else:
            pass
        request.context['collect_ids'] = ids
        request.context['category'] = 'pdf'
        return render(request, 'appArticle/articleList.html', request.context)


class InsideArticleListView(ArticleListView):
    Category = InsideCategory
    Article = InsideArticle

    def get(self, request):
        request = self.my_get(request)
        # 6 User
        webUserDict = request.session.get('webUser', None)
        ids = []
        if webUserDict:
            webUser = get_object_or_404(WebUser, id=webUserDict['id'])
            for id_tup in webUser.collectedOutsideActicles.values_list('id'):
                ids.append(id_tup[0])
        else:
            pass
        request.context['collect_ids'] = ids
        request.context['category'] = 'inside'
        return render(request, 'appArticle/articleList.html', request.context)


class PDFArticleDetailView(View):
    def get(self, request):
        article = get_object_or_404(PDFArticle, id=request.GET.get('id', None))
        article.clickNum += 1
        article.save()
        request.context['pdflink'] = article.pdflink
        request.context['title'] = article.title

        return render(request, 'appArticle/pdfDetail.html', request.context)


class InsideArticleDetailView(View):
    def get(self, request):
        article: InsideArticle = get_object_or_404(InsideArticle, id=request.GET.get('id', None))
        article.clickNum += 1
        article.save()
        request.context['article'] = article
        return render(request, 'appArticle/insideArticleDetail.html', request.context)


class OutsideArticleDetailView(View):

    def get(self, request):
        article: OutsideArticle = get_object_or_404(OutsideArticle, id=request.GET.get('id', None))
        article.clickNum += 1
        article.save()
        request.context['article'] = article
        return render(request, 'appArticle/outsideArticleDetail.html', request.context)


class ArticleCollect(View):
    category_dict = {
        'outside': OutsideArticle,
        'inside': InsideArticle,
        'pdf': PDFArticle,
    }

    def post(self, request):
        # webUser
        webUserDict = self.request.session.get('webUser', None)
        if not webUserDict:
            return JsonResponse({'code': False, 'msg': '请先登录'})
        webUser = get_object_or_404(WebUser, id=webUserDict.get('id', None))
        category = self.request.POST.get('category', None)
        # category
        if not category in self.category_dict.keys():
            return JsonResponse({'code': False, 'msg': '文章类型id有误'})
        # article
        Article = self.category_dict[category]
        article_id = self.request.POST.get('id', None)
        try:
            article = Article.objects.get(id=article_id)
        except:

            return JsonResponse({'code': False, 'msg': '文章id有误'})
        # add or delete
        way = self.request.POST.get('way')  # add | delete
        if way == 'add':
            if category == 'outside':
                webUser.collectedOutsideActicles.add(article)
            if category == 'inside':
                webUser.collectedInsideActicles.add(article)
            if category == 'pdf':
                webUser.collectedPDFActicles.add(article)
            try:
                webUser.save()
                return JsonResponse({'code': True, 'msg': '添加成功', 'ret': 'add'})
            except:
                return JsonResponse({'code': False, 'msg': '添加失败'})
        elif way == 'delete':
            if category == 'outside':
                webUser.collectedOutsideActicles.remove(article)
            if category == 'inside':
                webUser.collectedInsideActicles.remove(article)
            if category == 'pdf':
                webUser.collectedPDFActicles.remove(article)
            try:
                webUser.save()
                return JsonResponse({'code': True, 'msg': '添加成功', 'ret': 'delete'})
            except:
                return JsonResponse({'code': False, 'msg': '添加失败'})
        return JsonResponse({'code': False, 'msg': '未知错误'})


class ArticleSearch(View):

    def get(self, request):
        st = SearchTool(request=request)
        if not st.clean():
            print(st.error_message)
            raise Http404('error')


        # 4. 页面内容数据
        articles = st.instance_page
        nav_left = st.get_nav_left()
        # 5. 分页数据
        page_data = st.page_data()
        request.context['articles'] = articles
        request.context['page_data'] = page_data
        request.context['nav_left'] = nav_left
        request.context['category'] = st.instance_category
        request.context['way'] = st.way
        request.context['keyword'] = st.keyword

        return render(request,'appArticle/articleSearchList.html',request.context)





        




