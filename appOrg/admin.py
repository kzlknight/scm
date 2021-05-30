from django.contrib import admin
from appOrg.models import Organization,Rule
from django import forms
from aaBase.search import table_to_datas,datas_to_table

# Register your models here.


@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    # 展示内容
    list_display = ['searchInterval','searchNum','title','content','brief','author','origin','keywords']
    # 修改
    list_editable = ['searchInterval','searchNum','title','content','brief','author','origin','keywords']

class OrganizationForm(forms.ModelForm):
    class Meta():
        model = Organization
        fields = '__all__'

    def clean(self):
        '''
        验证searchResult是否符合Markdown语法
        '''
        searchResult = self.cleaned_data.get('searchResult') # markdown语法的搜索结果
        try:
            table_to_datas(md_text=searchResult)
            return self.cleaned_data
        except:
            raise forms.ValidationError('搜索结果格式不正确')


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):

    # 验证字段
    form = OrganizationForm
    # 显示字段
    list_display = ['id','name','show_brief','position','url','autoAlter','createDatetime']
    # 分类
    list_filter = ['autoAlter','createDatetime']
    # 可编辑字段
    list_editable = ['position','autoAlter']
    # 不可编辑字段
    readonly_fields = ['url']
    # 页面数量
    list_per_page = 20
    # 搜索字段
    search_fields = ['name','brief']
    # 排序
    ordering = ['position']


    def show_brief(self,expert):
        brief = str(expert.brief)
        return brief[0:10]

    show_brief.short_description = '机构简介'

    # 通过Admin保存的机构，重置更新时间
    def save_model(self, request, organization, form, change):
        organization.searchDatetime = None
        organization.save()






