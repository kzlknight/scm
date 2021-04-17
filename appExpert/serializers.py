from rest_framework import serializers
from appExpert.models import Category, Expert, Rule
from appArticle.models import Article
from aaBase.mymarkdown import mdHtml
from aaBase.search import table_to_datas, datas_to_table
from aaBase.search import search_article
import datetime
from django.utils.timezone import now


# 专家种类
class CategorySerializers(serializers.ModelSerializer):
    class Meta():
        model = Category
        fields = ('name', 'url', 'position', 'brief')


# 一级页面中多条专家数据
class CategoryExpertSerializers(serializers.ModelSerializer):
    class Meta():
        model = Expert
        fields = ('name', 'ppicture', 'brief', 'position',)


class ExpertSerializers(serializers.ModelSerializer):
    content_html = serializers.SerializerMethodField()  # 专家基本信息 从markdown转成的html
    searchs = serializers.SerializerMethodField()  # 搜索的结果 从自定义格式 转成列表字典

    class Meta():
        model = Expert
        fields = ('name', 'brief', 'ppicture', 'content_html', 'searchs')

    def get_content_html(self, expert):
        content = expert.content
        return mdHtml(content)

    def get_searchs(self, expert: Expert):

        # 得到searchResult
        if expert.autoAlter:  # 需要更新
            rule = Rule.objects.all().first()  # 规则
            searchInterval = rule.searchInterval  # 更新时间间隔
            # 无更新时间或者应该被更新
            if not expert.searchDatetime or expert.searchDatetime + datetime.timedelta(
                    hours=searchInterval) >= now():  # 超时时间未更新
                searchDatas: str = search_article(
                    search_text=expert.name,
                    rule=rule,
                    searchNum=expert.searchNum or rule.searchNum,
                )  # [{index:"",title:"",url:""},]
                expert.searchResult = datas_to_table(searchDatas)  # 把搜索的结果变成markdown的table
                expert.searchDatetime = now()  # 更新检索时间
                expert.save()
            else:  # 需要更新但未到更新时间
                pass
        else:  # 不需要更新
            pass

        searchResult = expert.searchResult  # markdown的table
        return table_to_datas(searchResult)
