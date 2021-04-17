from django.contrib import admin
from appUser.models import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # 显示字段
    list_display = ['name','account','tel','createDatetime']
    # 分类
    list_filter = ['createDatetime']
    # 可编辑字段 无
    # 不可编辑字段 无
    # 页面数量
    list_per_page = 50
    # 搜索字段
    search_fields = ['name','account','tel']
    # 排序
    ordering = ['id']
