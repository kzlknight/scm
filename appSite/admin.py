from django.contrib import admin
# from appSite.models import Nav,SignBoardHot,SignBoardNew,SignBoardRecommend
# from appSite.models import Nav,SignBoard
from appSite.models import Nav, NavLeft

admin.site.site_header = 'SCM后台管理'
admin.site.index_title = '后台系统'
admin.site.site_title = 'SCM后台管理'


@admin.register(Nav)
class NavAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id', 'name', 'position', 'url', 'level', 'show_subNavs', 'superNav']
    list_filter = ['level']
    list_editable = ['name', 'position', 'url', 'level', 'superNav']
    list_per_page = 20

    ordering = ['level', 'position', 'id']

    def show_subNavs(self, nav):
        names = []
        for n in nav.subNavs.all():
            n: Nav
            names.append(n.name)
        return ','.join(names)

    show_subNavs.short_description = '下级'


@admin.register(NavLeft)
class NavLeftAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['id', 'name', 'position', 'url', 'level', 'show_subNavs', 'superNav']
    list_filter = ['level']
    list_editable = ['name', 'position', 'url', 'level', 'superNav']
    list_per_page = 20

    ordering = ['level', 'position', 'id']

    def show_subNavs(self, nav):
        names = []
        for n in nav.subNavs.all():
            n: Nav
            names.append(n.name)
        return ','.join(names)

    show_subNavs.short_description = '下级'

# @admin.register(SignBoard)
# class SignBoardAdmin(admin.ModelAdmin):
#     list_display = ['name','position','autoAlter']
#     list_editable = ['autoAlter']
#     list_per_page = 10
#     list_filter = ['autoAlter']

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
