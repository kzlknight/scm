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
    from appOrg.models import Organization

    names = ['北京大学', '交通大学', '黑龙江大学', '吉林大学', '辽宁大学', '东北大学', '哈尔滨工业大学', '同济大学', '交通大学', '南京大学', '清华大学', '同济大学',
             '北京航空航天大学', '北京理工大学', '中国政法大学']

    keywordstag1 = ['网络', '程序员', 'IT', '大数据', '机器学习', '数据库', '分布式', '线程安全', '项目部署', '系统', 'Linux', ]
    keywordstag2 = ['日志', 'Java', '缓存', '架构', '.net', 'ECS', 'Redis', 'Golang']
    keywordstag3 = ['Excel', '神策', 'QuickBI', 'Tableau', 'PowerBi', '统计学', 'Python', 'SPSS']
    keywordstag4 = ['Django', 'Flask', 'Tornado', 'Bottle', 'Vue', 'Bootstrap', 'JQuery', 'CSS']

    keywordstag = keywordstag1 + keywordstag2 + keywordstag3 + keywordstag4

    import random

    categorys = []


    for i, name in enumerate(names):
        Organization(name=name,
                     brief='袁隆平院士是世界著名的杂交水稻专家，是我国杂交水稻研究领域的开创者和带头人，为我国粮食生产和农业科学的发展做出了杰出贡献。他的主要成就表现在杂交水稻的研究、应用与推广方面。',
                     position=i + 1,
                     searchKeywords=','.join(random.sample(keywordstag, 2)),
                     ).save()

