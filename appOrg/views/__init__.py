from django.shortcuts import render,HttpResponse
from django.views import View
from appOrg.models import Organization
from appOrg.views.base import OrgListTool


class ORGListView(View):
    def get(self,request):
        # 1. 实例化
        ot = OrgListTool(request=request)
        # 2. 验证
        if not ot.clean():
            return HttpResponse('error')
        # 3. 页面数据内容
        orgs = ot.instance_page
        # 4. 分页数据
        page_data = ot.page_data()
        request.context['orgs'] = orgs[1:6]
        request.context['page_data'] = page_data
        return render(request, 'orgList.html', request.context)


class ORGDetailView(View):
    def get(self,request):
        return HttpResponse('detail')
