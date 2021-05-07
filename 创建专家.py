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
    from appExpert.models import Category, Expert

    expert_names = ['达青文', '种清懿', '弥代玉', '庆静云', '愚骏燕', '幸代蓝', '易绿竹', '盍春雪', '巴怀芹', '齐星', '抗又青', '旁悦人', '郁思柔', '牵熙',
                    '诺奇', '代和顺', '卞萍韵', '粟菱凡', '申屠吉敏', '温俊彦', '柔秋珊', '肇鸿福', '惠鹍', '环子帆', '零清', '本雅琴', '尚鹏鲸', '修邵',
                    '诗冷菱', '胥嘉月', '曾忆柏', '势月天', '荣月华', '朴妍妍', '潘涵衍', '郭谷枫', '寒熙柔', '尹冰真', '有凌寒', '渠映天', '杭倩丽', '甄梦菲',
                    '邰新知', '令依丝', '皇锐达', '辟易绿', '斋咏思', '郁浩慨', '厚宛秋', '弘鸿哲', '连高洁', '郗玉兰', '和令飒', '操夏云', '稽馨欣', '畅胤骞',
                    '游新晴', '姬千叶', '盈静柏', '通芸若', '竹寄蕾', '仙星雨', '郦寻云', '石婉清', '运惜', '宿祥', '冷元瑶', '魏寻桃', '栋明知', '韩玉',
                    '昌博耘', '邵沛槐', '佼骥', '殷山柳', '锁岚', '仇经武', '府天慧', '韦丹彤', '阴新颖', '迟水卉', '书绮', '郝玲琅', '才清心', '潜忻乐',
                    '夹谷若雁', '肖歆', '欧阳欣合', '厉山兰', '功幼菱', '恭稷', '都睿彤', '妫睿聪', '纵帅红', '绍丹蝶', '谬乐容', '帛初蓝', '化华', '苍凌蝶',
                    '高建弼', '展立辉', '东郭格菲', '礼春琳', '龚珹', '东门波光', '贺梓瑶', '籍觅柔', '澄丹彤', '欧佁', '合紫', '伊静枫', '用可佳', '宋莹洁',
                    '颛孙问枫', '隐和璧', '浦艳娇', '藏平和', '溥琼诗', '乌雅旭彬', '蒯宜春', '平安寒', '孟以彤', '毛小谷', '歧曜瑞', '禚慕蕊', '戈竹悦', '乐春娇',
                    '永元芹', '严英毅', '熊诗怀', '绪君丽', '终荃', '子车云溪', '江半烟', '乌孙米琪', '清寄', '宰长', '林盼巧', '兴云蔚', '矫景山', '赫滢滢',
                    '赖丹红', '任晓楠', '哀宛畅', '韶丽华', '开新洁', '焉雅容', '祝妮', '桓雨文', '楚恨之', '边访冬', '芒静', '元妞妞', '崔承', '别问柳',
                    '唐依秋', '乜依琴', '褚绍晖', '随光霁', '来绮晴', '益曲静', '乔痴香', '柯米', '紫春燕', '吾飞槐', '衡熠', '花凡白', '苏冰凡', '夔弘新',
                    '圣清怡', '局忻畅', '侨听春', '金梦菲', '井舒方', '始甘雨', '洛白', '岳曼雁', '端湛蓝', '福幼安', '芮哲思', '隗曼妮', '烟娅', '念若星',
                    '符爰', '豆令雪', '庚和裕', '喻饮香', '陈水丹', '苑濡', '印鸿光', '建夏波', '干天籁', '锺离友易', '隋杨', '钭雅洁', '依弘光', '敛芷珊',
                    '宛乐语', '嵇慧俊', '及昆卉', '初嘉云', '武小溪', '鞠芳菲', '后海荣', '司空芷容', '燕珧', '坚安晏', '盘俊杰', '母经', '宓同光', '肥晗琴',
                    '波向笛', '伟天薇', '许珠雨', '赤沛山', '傅亦', '滑采春', '沙悦欣', '逄炫明', '速颐然', '度溶', '睦彦红', '牟冰', '俟雪晴', '爱思溪',
                    '千宛凝', '古饮', '南门元洲', '匡慧秀', '风华藏', '刘灿', '聂林帆', '独勤', '纪湉湉', '施姮娥', '镇泽恩', '军罡', '麦成礼', '僧光赫',
                    '于喜儿', '袭凝心', '同骏桀', '栾璇子', '释冷雁', '碧鲁红豆', '邬望慕', '柳晶茹', '仪梦桃', '白尔风', '皋寄云', '臧韶美', '贡寄蓉', '愈醉柳',
                    '孛晓昕', '姜春英', '单子萱', '望千风', '声红旭', '席秀颖', '巩诗蕊', '段韵诗', '闳榆', '安妙珍', '华曼云', '琦怜雪', '葛初之', '翠思聪',
                    '狄曼凡', '廉韵梅', '线修齐', '昝书竹', '宝雨竹', '弭许', '羊阳波', '帖沛凝', '庞博延', '纳天曼', '单于秋', '学博艺', '旷书艺', '红敏智',
                    '佘恩霈', '毕紫南', '庾美丽', '丹若云', '历芳洁', '佴朝旭', '钱黎', '剧暮', '钟离骊茹', '腾醉冬', '丘迎南', '莫莹华', '郜雨石', '荤饮月',
                    '淳于高', '贾颖颖', '伏贞婉', '常月', '左曾琪', '简晨', '素阳曦', '鄂祺', '夏梦菲', '兰兴发', '暴书文', '雍怜云', '香瑛', '蔚绮露', '逯代桃',
                    '辉雅琴', '登荫', '范古', '朱听双', '佛陶然', '拓跋晓星', '蔡智敏', '养锐藻', '秘柔丽', '丛香馨', '靳凝思', '须宏深', '赧大', '居永春',
                    '伯思雁', '钟高澹', '劳俊名', '区寄云', '亥夜玉', '蓝正', '陆旭东', '蓬香薇', '竺彬', '权湘君', '布晓枫', '北静枫', '勤和硕', '贯清涵',
                    '祁寿', '碧昆琦', '五森', '谷濮存', '狂佩玉', '淡梦竹', '汝嘉禧', '夙复', '玉碧螺', '祭初夏', '宾曼青', '祈密如', '乌紫雪', '皮魁', '仝白玉',
                    '邶欣然', '范姜飞章', '雀晴虹', '淦新立', '奈元勋', '璩运华', '捷玥', '乐正清雅', '却瑜', '牢新文', '汉庄雅', '商枫', '李安双', '储傲松',
                    '辜以旋', '年安露', '闽梦旋', '鲍弘']
    keywordstag1 = ['网络', '程序员', 'IT', '大数据', '机器学习', '数据库', '分布式', '线程安全', '项目部署', '系统', 'Linux', ]
    keywordstag2 = ['日志', 'Java', '缓存', '架构', '.net', 'ECS', 'Redis', 'Golang']
    keywordstag3 = ['Excel', '神策', 'QuickBI', 'Tableau', 'PowerBi', '统计学', 'Python', 'SPSS']
    keywordstag4 = ['Django', 'Flask', 'Tornado', 'Bottle', 'Vue', 'Bootstrap', 'JQuery', 'CSS']

    keywordstag = keywordstag1 + keywordstag2 + keywordstag3 + keywordstag4
    import random

    categorys = []

    category_names = ['哲学', '经济学', '法学', '教育学', '文学', '历史学', '理学', '工学', '农学', '医学', '军事学', '管理学', '艺术学']

    for index, category_name in enumerate(category_names):
        category = Category(name=category_name, brief='中国特色社会主义的民主政治', position=index + 1)
        category.save()

        for i in range(30):
            en = expert_names.pop()
            Expert(name=en,
                   brief='袁隆平院士是世界著名的杂交水稻专家，是我国杂交水稻研究领域的开创者和带头人，为我国粮食生产和农业科学的发展做出了杰出贡献。他的主要成就表现在杂交水稻的研究、应用与推广方面。',
                   position=i + 1,
                   ppicture='expert_ppicture/1.png',
                   content='',
                   searchKeywords=','.join(random.sample(keywordstag, 2)),
                   category=category,
                   ).save()

    #
    # from appArticle.models import OutsideCategory, PDFCategory, InsideCategory
    # from appArticle.models import OutsideArticle, PDFArticle, InsideArticle
    # import json
    #
    # oc1 = OutsideCategory(name='外部文章1', keywordsTag=','.join(keywordstag1))
    # oc2 = OutsideCategory(name='外部文章2', keywordsTag=','.join(keywordstag2))
    # pc = PDFCategory(name='PDF文章', keywordsTag=','.join(keywordstag3))
    # ic = InsideCategory(name='内部文章', keywordsTag=','.join(keywordstag4))
    #
    # oc1.save()
    # oc2.save()
    # pc.save()
    # ic.save()
    #
    # navOut = Nav(name='外部文章', position=1, level=Nav.LEVEL_1)
    # navOut.save()
    #
    # navOut1 = Nav(name='外部文章1', url=oc1.url, position=1, level=Nav.LEVEL_2, superNav=navOut)
    # navOut2 = Nav(name='外部文章2', url=oc2.url, position=2, level=Nav.LEVEL_2, superNav=navOut)
    # navOut1.save()
    # navOut2.save()
    #
    # navPdf = Nav(name='PDF文章', url=pc.url, position=2, level=Nav.LEVEL_1)
    # navInside = Nav(name='内部文章', url=ic.url, position=3, level=Nav.LEVEL_1)
    # navPdf.save()
    # navInside.save()
    #
    # out1_datas = json.load(open('spider/out1.json', 'r'))
    # out2_datas = json.load(open('spider/out2.json', 'r'))
    # pdf_datas = json.load(open('spider/pdf1.json', 'r'))
    # in_datas = json.load(open('spider/inside1.json', 'r'))
    #
    # for data in out1_datas:
    #     # data['outlink'] = data['href']
    #     # del data['href']
    #     try:
    #         OutsideArticle(category=oc1, **data).save()
    #         print('yes')
    #     except:
    #         print('no')
    #
    # for data in out2_datas:
    #     # data['outlink'] = data['href']
    #     # del data['href']
    #     try:
    #         OutsideArticle(category=oc2, **data).save()
    #         print('yes')
    #     except:
    #         print('no')
    #
    # for data in pdf_datas:
    #     del data['outlink']
    #     try:
    #         PDFArticle(
    #             category=pc,
    #             pdflink='article_pdf/0a5ec255-4607-42ba-8b67-7384e26f1d88.pdf',
    #             **data).save()
    #         print('yes pdf')
    #     except:
    #         print('no pdf')
    #
    # for data in in_datas:
    #     del data['outlink']
    #     try:
    #         InsideArticle(
    #             category=ic,
    #             **data
    #         ).save()
    #         print('yes inside')
    #     except:
    #         print('no inside')
