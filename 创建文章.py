#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scm.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
    from appSite.models import Nav
    from appArticle.models import OutsideCategory,PDFCategory,InsideCategory
    from appArticle.models import OutsideArticle,PDFArticle,InsideArticle
    import json
    keywordstag1 = ['网络', '程序员', 'IT', '大数据', '机器学习', '数据库', '分布式', '线程安全', '项目部署', '系统', 'Linux', ]
    keywordstag2 = ['日志', 'Java', '缓存', '架构', '.net', 'ECS', 'Redis', 'Golang']
    keywordstag3 = ['Excel', '神策', 'QuickBI', 'Tableau', 'PowerBi', '统计学', 'Python', 'SPSS']
    keywordstag4 = ['Django', 'Flask', 'Tornado', 'Bottle', 'Vue', 'Bootstrap', 'JQuery', 'CSS']

    oc1 = OutsideCategory(name='企业创新',keywordsTag=','.join(keywordstag1))
    oc2 = OutsideCategory(name='企业管理',keywordsTag=','.join(keywordstag2))
    pc = PDFCategory(name='互联网金融',keywordsTag=','.join(keywordstag3))
    ic = InsideCategory(name='文化展览',keywordsTag=','.join(keywordstag4))

    oc1.save()
    oc2.save()
    pc.save()
    ic.save()

    navOut = Nav(name='社会知识(外部)',position=1,level=Nav.LEVEL_1)
    navOut.save()

    navOut1 = Nav(name='企业创新',url=oc1.url,position=1,level=Nav.LEVEL_2,superNav=navOut)
    navOut2 = Nav(name='企业管理',url=oc2.url,position=2,level=Nav.LEVEL_2,superNav=navOut)
    navOut1.save()
    navOut2.save()

    navPdf = Nav(name='金融(PDF)',url=pc.url,position=2,level=Nav.LEVEL_1)
    navInside = Nav(name='文化(内部）',url=ic.url,position=3,level=Nav.LEVEL_1)
    navPdf.save()
    navInside.save()

    out1_datas = json.load(open('spider/out1.json','r'))
    out2_datas = json.load(open('spider/out2.json','r'))
    pdf_datas = json.load(open('spider/pdf1.json','r'))
    in_datas = json.load(open('spider/inside1.json','r'))

    for data in out1_datas:
        try:
            OutsideArticle(category=oc1,**data).save()
            print('yes')
        except:
            print('no')

    for data in out2_datas:
        try:
            OutsideArticle(category=oc2,**data).save()
            print('yes')
        except:
            print('no')

    for data in pdf_datas:
        del data['outlink']
        try:
            PDFArticle(
            category=pc,
                pdflink='article_pdf/0a5ec255-4607-42ba-8b67-7384e26f1d88.pdf',
                **data).save()
            print('yes pdf')
        except:
            print('no pdf')

    for data in in_datas:
        del data['outlink']
        try:
            InsideArticle(
                category=ic,
                **data
            ).save()
            print('yes inside')
        except:
            print('no inside')




