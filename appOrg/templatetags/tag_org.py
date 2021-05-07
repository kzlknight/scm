from django.template import Library
from aaBase.search import table_to_datas as super_table_to_datas

register = Library()

@register.filter
def table_to_datas(md_text,num=10):
    return super_table_to_datas(md_text)[0:num]

