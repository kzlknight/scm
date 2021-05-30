from django.template import Library
from aaBase.search import table_to_datas as super_table_to_datas
from appOrg.models import Organization

register = Library()

@register.filter
def table_to_datas(md_text,num=10):
    return super_table_to_datas(md_text)[0:num]


@register.filter
def brief(text,length=10):
    if text:
        if len(text)> length:
            return text[0:length] + '...'
        else:
            return text
    else:
        return ''

@register.inclusion_tag('appOrg/tags/org-nav-left.html')
def org_nav_left(request):
    orgs = Organization.objects.all()
    full_path = request.get_full_path()
    return {'orgs':orgs,'full_path':full_path}
