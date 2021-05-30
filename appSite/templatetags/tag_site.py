from django.template import Library
from appSite.models import Nav

register = Library()


@register.inclusion_tag('tags/header.html')
def tag_header(request):
    # 用户
    webUser = request.session.get('webUser', None)
    #
    navLevels = Nav.objects.filter(level=Nav.LEVEL_1)
    full_path = request.get_full_path()
    way = request.context.get('way','content')
    keyword = request.context.get('keyword','')
    return {
        'navs': navLevels,
        'webUser': webUser,
        'full_path': full_path,
        'showLogin':request.context['showLogin'],
        'way':way,
        'keyword':keyword,
    }


@register.filter
def header_url_in_fullpaths(nav, full_path):
    for nav in nav.subNavs.all():
        if nav.url in full_path:
            return 'my-nav-active'
    return ''



# @register.inclusion_tag('tag/article-nav-left.html')
# def tag_ArticleNavLeft():
#     navLeft1s = NavLeft.objects.filter(level=NavLeft.LEVEL_1)
#     return {'navLeft1s':navLeft1s}
