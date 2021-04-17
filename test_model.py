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
    from appArticle.models import Article
    from appExpert.models import Expert
    from aaBase.mymarkdown import mdHtml
    import lxml.etree as le

    expert = Expert.objects.get(id=1)
    searchResult = expert.searchResult

    # def table_to_datas(text, titles=['index', 'title', 'url']):
    #     """
    #     :param text: markdown中的table字符串
    #     :param titles:
    #     :return:[{index:"",title:"",url:""},]
    #     """
    #     htmlx = le.HTML(mdHtml(text))
    #     ret_datas = []
    #     trs = htmlx.xpath('//tr')[1:] # 去掉标题
    #     for tr in trs:
    #         values = [str(text) for text in tr.xpath('./td/text()')]
    #         ret_datas.append(dict(zip(titles, values)))
    #     return ret_datas
    #
    # a = table_to_datas(searchResult)
    # print(a)

    datas = [
        {'index': 1, 'title': '11111', 'url': '1-1-1'},
        {'index': 2, 'title': '222', 'url': '2-1-1'},
    ]


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


    ret  =datas_to_table(datas=datas)
    print(ret)
    expert.searchResult = ret
    expert.save()
