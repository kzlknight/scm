# from rest_framework import serializers
# from appArticle.models import Article,Category,TagKeyword
# from rest_framework.utils.serializer_helpers import ReturnDict
# from aaBase.mymarkdown import mdHtml
#
#
# class CategoryAricleSerializer(serializers.ModelSerializer):
#     class Meta():
#         model = Article
#         # 去掉content与video
#         fields = ('title','articleType','outlink','url','pdflink','ppicture','brief','author','origin','createDatetime','clickNum','collectNum','position','keywords')
#
#
# class CategoryTagKeywordSerializer(serializers.ModelSerializer):
#     class Meta():
#         model = TagKeyword
#         fields = ('keywords','category')
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     class Meta():
#         model = Category
#         fields = ('name','url','position')
#
#
#
#
# class ArticleSerializer(serializers.ModelSerializer):
#
#     html_content = serializers.SerializerMethodField()
#
#     class Meta():
#         model = Article
#         fields = ('title','ppicture','html_content','brief','author','origin','createDatetime','clickNum','collectNum','video','keywords')
#
#
#     def get_html_content(self,article):
#         content = article.content
#         return mdHtml(content)
#
