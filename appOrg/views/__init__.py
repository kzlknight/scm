from django.shortcuts import render,HttpResponse,get_object_or_404
from django.views import View
from appOrg.models import Organization,Rule
from appOrg.views.base import OrgListTool
import datetime
from django.utils.timezone import now


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
        request.context['orgs'] = orgs
        request.context['page_data'] = page_data
        return render(request, 'appOrg/orgList.html', request.context)


class ORGDetailView(View):
    def get(self, request):
        org = get_object_or_404(Organization,id=request.GET.get('id',None))
        if org.autoAlter:  # 需要更新
            rule = Rule.objects.all().first()  # 规则
            searchInterval = rule.searchInterval  # 更新时间间隔
            # 无更新时间或者应该被更新
            if not org.searchDatetime or org.searchDatetime + datetime.timedelta( hours=searchInterval) <= now():  # 超时时间未更新
                org.save()

        request.context['org'] = org
        return render(request, 'appOrg/orgDetail.html', request.context)


