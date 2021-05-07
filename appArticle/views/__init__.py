from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
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

from appArticle.views.base import ArticleListTool


def index_handler(request):
    request.get_full_path()
    return HttpResponse('ok')





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
            return render(request, 'articleList404.html')
        # 3. 上方分类
        nav_top_data = at.nav_top_data()
        # 4. 页面内容数据
        articles = at.instance_page
        # 5. 分页数据
        page_data = at.page_data()

        request.context['articles'] = articles
        request.context['page_data'] = page_data
        request.context['nav_top_data'] = nav_top_data

        return render(request, 'articleList.html', request.context)


class OutArticleListView(ArticleListView):
    Category = OutsideCategory
    Article = OutsideArticle

    def get(self, request):
        return self.my_get(request)



class PDFArticleListView(ArticleListView):
    Category = PDFCategory
    Article = PDFArticle

    def get(self, request):
        return self.my_get(request)


class InsideArticleListView(ArticleListView):
    Category = InsideCategory
    Article = InsideArticle

    def get(self, request):
        return self.my_get(request)




class PDFArticleDetailView(View):
    def get(self,request):
        id = request.GET.get('id',None)
        article = get_object_or_404(PDFArticle,id=id)
        pdflink = article.pdflink
        request.context['pdflink'] = pdflink
        return render(request,'pdfDetail.html',request.context)


class InsideArticleDetailView(View):
    Article = InsideArticle
    def get(self,request):
        id = request.GET.get('id',None)
        article = self.Article.objects.get(id=id)
        request.context['article'] = article
        return render(request,'articleDetail.html',request.context)

