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
    from appArticle.models import Category as ArticleCategory
    from appArticle.models import TagKeyword
    from appArticle.models import Article
    import random

    # 1. article
    # 1.1 article -category 与关键字
    article_category_names = ['Python文章', 'Java文章', '前端语言文章']
    article_category_keywords = [
        ['python', 'selenium', 'scrapy'],
        ['jvm', 'spring', 'jsp'],
        ['html', 'js', 'css'],
    ]
    article_category_objs = []

    for index, ac in enumerate(article_category_names):
        category = ArticleCategory(name=ac, position=index + 1)
        category.save()
        TagKeyword(keywords=','.join(article_category_keywords[index]), category=category).save()
        article_category_objs.append(category)

    # 1.2 article detail
    import os

    filenames = os.listdir('notebook/python')
    for index, filename in enumerate(filenames):
        try:
            filepath = os.path.join('notebook', 'python', filename)
            with open(filepath, 'r') as f:
                content = f.read()  # 正文
                brief = '简短的介绍'
                title = filename[0:-3]
                category = random.choice(article_category_objs)
                position = index + 1
                Article(title=title, brief=brief, content=content, category=category, position=position).save()
        except:
            pass

    # 2 专家
    # 2.1 专家种类
    from appExpert.models import Category as ExpertCategory
    from appExpert.models import Expert

    expert_category_names = ['政治', '生物', '人文', '社会科学', '法律', '工科']
    expert_category_objs = []

    for index, category_name in enumerate(expert_category_names):
        category = ExpertCategory(name=category_name, position=index + 1)
        category.save()
        expert_category_objs.append(category)

    # 2.2 专家详细
    expert_names = ['孙欣悦', '弓飞光', '饶乐人', '孙俊雄', '弘弘量', '班兴平', '居文彦', '屠经纶', '印自强', '幸景明', '红德惠', '邹正祥', '党经业', '籍昊焱',
                    '薛阳平', '扈兴文', '冉丰茂', '弘晗昱', '乌泰河', '钭正浩', '魏建明', '蓬欣德', '邴茂实', '相修永', '谭思源', '翟嘉祯', '韶彭祖', '关元甲',
                    '赖哲彦', '董伟茂', '索和风', '祖飞翮', '段锐翰', '姚成仁', '祖信瑞', '籍奇希', '宦弘伟', '满玉龙', '武阳平', '郗明俊', '巢飞掣', '杨欣可',
                    '利锐志', '罗宏浚', '谭阳焱', '廖旭尧', '屠锐思', '顾天翰', '蓟彭祖', '段元白', '沃明俊', '龚炫明', '慎明杰', '沃奇伟', '盖刚捷', '于宏深',
                    '须博超', '习咏志', '巴正志', '暴丰羽', '罗经义', '满星剑', '许同和', '戌锐逸', '蒯文瑞', '古英耀', '廖志行', '容涵忍', '黄安翔', '魏元白',
                    '濮新立', '麴烨磊', '张昂雄', '蒙鹏云', '咸涵蓄', '文彬彬', '秦宏盛', '阎英卫', '曹高翰', '班弘方', '高嘉致', '慕俊能', '彭鸿信', '阎子昂',
                    '彭子瑜', '越天赋', '高丰茂', '红玉宇', '钱昊苍', '冷宾白', '步星波', '庄乐逸', '国阳云', '黎欣怿', '郑和宜', '胡鹏鲲', '张景胜', '游宾实',
                    '郏斯年', '许雅志', ]
    search_keywords = ['python', 'java', 'c', '案例', '代码']

    for index, name in enumerate(expert_names):
        position = index + 1
        brief = '专家简介实例：Department of Civil and Environmental Engineering, The Hong Kong Polytechnic University, Hong Kong'
        content = 'Department of Civil and Environmental Engineering, The Hong Kong Polytechnic University, Hong Kong'
        keyword = random.choice(search_keywords)
        Expert(name=name, brief=brief, position=position, content=content, searchKeyword=keyword,
               category=random.choice(expert_category_objs)).save()

    # 3 机构
    from appOrg.models import Organization

    org_names = ['机构1', '机构2', '机构3']
    search_keywords = ['FPT', 'module', 'webDriver']
    for index, name in enumerate(org_names):
        keyword = search_keywords[index]
        position = index + 1
        brief = '基于ModelBuilder的垦造水田耕地质量等别评价'
        Organization(name=name,brief=brief, position=position, searchKeyword=keyword).save()
