from django.contrib import admin
from appExpert.models import Category, Expert, Rule
from aaBase.urlsmapping import UrlMapping as UM
import urllib.parse as up
from django import forms
from aaBase.search import datas_to_table,table_to_datas


# 专家检索规则 注：专家检索规则有一个即可
@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    # 显示内容
    list_display = ['id', 'name']


# 专家种类
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # 显示内容
    list_display = ['id', 'name', 'position',
                    'show_brief',  # 仅显示前10个字
                    'url',
                    'show_expert_num', # 包含专家的人数
                    ]
    # 页面数量
    list_per_page = 20
    # 可编辑字段
    list_editable = ['position']
    # 不可编辑字段
    readonly_fields = ['url']
    ordering = ['position','-id']
    # 简介的显示
    def show_brief(self, category):
        brief = category.brief

        if not brief:
            return ''
        else:
            brief = str(brief)
            sufffix = '...' if len(brief) > 10 else ''  # 超过10个长度后缀...
            return brief[0:10] + sufffix

    show_brief.short_description = '简介'


    def show_expert_num(self,category):
        count = category.experts.count()
        return count

    show_expert_num.short_description = '专家人数'

    # # 维护URL
    # def save_model(self, request, category, form, change):
    #     category.save()
    #     category.url = up.urljoin(
    #         UM.EXPERT_CATEGORY, '?id={id}'.format(id=category.id)
    #     )
    #     category.save()


class ExpertForm(forms.ModelForm):
    class Meta():
        model = Expert
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
            raise forms.ValidationError('专家搜索结果格式不正确')



# 专家详细
@admin.register(Expert)
class ExpertAdmin(admin.ModelAdmin):
    # 验证字段
    form = ExpertForm
    # 显示字段
    list_display = ['id', 'name', 'show_brief', 'position', 'url','autoAlter','createDatetime']
    # 分类
    list_filter = ['category', 'autoAlter','createDatetime']
    # 可编辑字段
    list_editable = ['position','autoAlter']
    # 不可编辑字段
    readonly_fields = ['url']
    # 页面数量
    list_per_page = 50
    # 搜索字段
    search_fields = ['name','brief','content']
    # 排序
    ordering = ['position']

    def show_brief(self, expert):
        brief = str(expert.brief)
        return brief[0:10]

    show_brief.short_description = '专家简介'

