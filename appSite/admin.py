from django.contrib import admin
# from appSite.models import Nav,SignBoardHot,SignBoardNew,SignBoardRecommend
from appSite.models import Nav,SignBoard

admin.site.site_header = 'SCM后台管理'
admin.site.index_title = '后台系统'
admin.site.site_title = 'SCM后台管理'


@admin.register(Nav)
class NavAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name','position','url','level','show_subNavs']
    list_filter = ['level']
    list_editable = ['position','url']
    list_per_page = 20


    def show_subNavs(self,nav):
        names = []
        for n in nav.subNavs.all():
            n:Nav
            names.append(n.name)
        return ','.join(names)
    show_subNavs.short_description = '下级'



@admin.register(SignBoard)
class SignBoardAdmin(admin.ModelAdmin):
    list_display = ['name','position','autoAlter']
    list_editable = ['autoAlter']
    list_per_page = 10
    list_filter = ['autoAlter']

# @admin.register(SignBoardNew)
# class SignBoardNewAdmin(admin.ModelAdmin):
#     list_display = ['name','url','position','autoAlter']
#     list_editable = ['autoAlter']
#     list_per_page = 10
#     list_filter = ['autoAlter']
#
#
#
#
#
# @admin.register(SignBoardHot)
# class SignBoardHotAdmin(admin.ModelAdmin):
#     list_display = ['name','url','position','autoAlter']
#     list_editable = ['autoAlter']
#     list_per_page = 10
#     list_filter = ['autoAlter']
#
#
# @admin.register(SignBoardRecommend)
# class SignBoardRecommendAdmin(admin.ModelAdmin):
#     list_display = ['name','url','position','autoAlter']
#     list_editable = ['autoAlter']
#     list_per_page = 10
#     list_filter = ['autoAlter']