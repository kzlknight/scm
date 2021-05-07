from django.shortcuts import render,HttpResponse,get_object_or_404
from django.views import View
from appExpert.views.base import ExpertListTool
from appExpert.models import Expert
from aaBase.search import table_to_datas




class ExpertListView(View):
    def get(self,request):
        # 1. 实例化
        xt = ExpertListTool(request=request)
        # 2. 验证数据
        if not xt.clean():
            print(xt.error_message)
            # return render(request,'')
            return HttpResponse('error')
        # 3. 页面内容数据
        experts = xt.instance_page
        # 4. 分页数据
        page_data = xt.page_data()
        # end:context
        request.context['this_category'] = xt.this_category
        request.context['categorys'] = xt.categorys
        request.context['experts'] = experts
        request.context['page_data'] = page_data
        return render(request,'expertList.html',request.context)


class ExpertDetailView(View):
    def get(self,request):
        # 根据上次检索时间，出发检索更新
        expert = get_object_or_404(Expert,id=request.GET.get('id',None))
        request.context['expert'] = expert
        searchResultDatas = table_to_datas(expert.searchResult)
        request.context['searchResultDatas'] = searchResultDatas
        print(searchResultDatas)
        return render(request,'expertDetail.html',request.context)

