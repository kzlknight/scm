from django.template import Library
from django.utils.html import format_html
from appArticle.models import NavLeft
import markdown

register = Library()


@register.inclusion_tag('appArticle/tags/article-nav-left.html')
def tag_ArticleNavLeft(request):
    navLeft1s = NavLeft.objects.filter(level=NavLeft.LEVEL_1)
    full_path = request.get_full_path()
    return {'navLeft1s': navLeft1s,'full_path':full_path}



@register.filter
def mark(text):
    extensions = [
        'markdown.extensions.extra',
        'markdown.extensions.abbr',
        'markdown.extensions.attr_list',
        'markdown.extensions.def_list',
        'markdown.extensions.fenced_code',
        'markdown.extensions.footnotes',
        'markdown.extensions.md_in_html',
        'markdown.extensions.tables',
        'markdown.extensions.admonition',
        'markdown.extensions.codehilite',
        'markdown.extensions.legacy_attrs',
        'markdown.extensions.legacy_em',
        'markdown.extensions.meta',
        'markdown.extensions.nl2br',
        'markdown.extensions.sane_lists',
        'markdown.extensions.smarty',
        'markdown.extensions.toc',
        'markdown.extensions.wikilinks',
    ]
    return format_html(markdown.markdown(text, extensions=extensions))


@register.filter
def join_keywords(keywords):
    if keywords:
        return ','.join(keywords)
    else:
        return ''
