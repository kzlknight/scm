from appArticle.models import OutsideArticle,PDFArticle,InsideArticle
from django.db.models import Q
import lxml.etree as le
from aaBase.mymarkdown import mdHtml


def datas_to_table(datas, titles=['序号', '标题', '地址']):
    """
    :param datas: [{index:"",title:"",url:""},]
    :return:md_table
    """
    md_text_base = """| 序号 | 标题 | 地址 |\n| :------------ | :------------ | :------------ |\n"""
    if not datas:
        md_text = md_text_base + '|  |  |  |'
    else:
        md_text = md_text_base
        for data in datas:
            md_text += """| {index} | {title} | {url} |\n""".format(
                index=data['index'], title=data['title'], url=data['url'])
    return md_text


# markdown中的table转成datas
def table_to_datas(md_text, titles=['index', 'title', 'url']):
    """
    :param text: markdown中的table字符串
    :param titles:
    :return:[{index:"",title:"",url:""},]
    """
    if not md_text:
        return []
    else:
        htmlx = le.HTML(mdHtml(md_text))
        ret_datas = []
        trs = htmlx.xpath('//tr')[1:]  # 去掉标题
        for tr in trs:
            values = [str(text) for text in tr.xpath('./td/text()')]
            ret_datas.append(dict(zip(titles, values)))
        return ret_datas


def search_article(search_texts:list, rule, searchNum, order_bys=['-clickNum', '-collectNum', '-createDatetime']):
    """
    :param search_text:
    :param rule:
    :param searchNum:
    :param order_bys:
    :return: [{index:"",title:"",url:""},]
    """
    qf = Q()
    if rule.title:
        for st in search_texts:
            qf = qf | Q(title__contains=st)
    if rule.content:
        for st in search_texts:
            qf = qf | Q(content__contains=st)
    if rule.brief:
        for st in search_texts:
            qf = qf | Q(brief__contains=st)
    if rule.author:
        for st in search_texts:
            qf = qf | Q(author__contains=st)
    if rule.origin:
        for st in search_texts:
            qf = qf | Q(origin__contains=st)
    if rule.keywords:
        for st in search_texts:
            qf = qf | Q(keywords__contains=st)

    # 没有搜索文字
    if not search_texts:
        return []
    # 全部禁止
    if not (rule.title) and not (rule.content) and not (rule.brief) and not (rule.author) and not (
    rule.origin) and not (rule.keywords):
        return []
    else:
        outsideArticles = OutsideArticle.objects.filter(qf).order_by(*order_bys)
        pdfArticles = PDFArticle.objects.filter(qf).order_by(*order_bys)
        insideArticles = InsideArticle.objects.filter(qf).order_by(*order_bys)

        searchDatas = []
        articles_objs = [outsideArticles,pdfArticles,insideArticles]
        for articles in articles_objs:
            for index, article in enumerate(articles):
                url = article.url
                title = article.title
                searchDatas.append(
                    {
                        'index': index + 1,
                        'title': title,
                        'url': url,
                    }
                )
        return searchDatas[0:searchNum]

# def search_article_new(searchNum=10):
#     articles = Article.objects.all().order_by('-createDatetime')
#     searchDatas = []
#     for index, article in enumerate(articles[0:searchNum]):
#         url = article.url
#         title = article.title
#         searchDatas.append(
#             {
#                 'index': index + 1,
#                 'title': title,
#                 'url': url,
#             }
#         )
#     return searchDatas
#
# def search_article_hot(searchNum=10):
#     articles = Article.objects.all().order_by('-clickNum')
#     searchDatas = []
#     for index, article in enumerate(articles[0:searchNum]):
#         url = article.url
#         title = article.title
#         searchDatas.append(
#             {
#                 'index': index + 1,
#                 'title': title,
#                 'url': url,
#             }
#         )
#     return searchDatas


