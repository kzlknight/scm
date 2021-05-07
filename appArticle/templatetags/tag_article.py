from django.template import Library
from appArticle.models import OutsideCategory,PDFCategory,InsideCategory
from django.utils.html import format_html
from appSite.models import NavLeft
import markdown

register = Library()

# @register.inclusion_tag('tag/article-nav-left.html')
# def tag_articleNavLeft():
#     outsideCategorys = OutsideCategory.objects.all()
#     pdfsideCategorys = PDFCategory.objects.all()
#     insideCategorys = InsideCategory.objects.all()
#     print(outsideCategorys,pdfsideCategorys,insideCategorys)
#     return dict(
#         outsideCategorys = outsideCategorys,
#         pdfsideCategorys = pdfsideCategorys,
#         insideCategorys = insideCategorys
#     )

@register.inclusion_tag('tag/article-nav-left.html')
def tag_ArticleNavLeft():
    navLeft1s = NavLeft.objects.filter(level=NavLeft.LEVEL_1)
    return {'navLeft1s':navLeft1s}


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
    return format_html(markdown.markdown(text,extensions=extensions))


@register.filter
def join_keywords(keywords):
    if keywords:
        return ','.join(keywords)
    else:
        return ''
