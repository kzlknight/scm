from django.views.generic import ListView,DetailView
from django.shortcuts import get_object_or_404,get_list_or_404
from django.http import Http404
from appArticle.models import OutsideCategory,InsideCategory,PDFCategory
from appArticle.models import OutsideArticle,InsideArticle,PDFArticle

from django import forms


class ArticleListForm(forms.Form):
    Category:OutsideCategory

    category_id = forms.IntegerField()
    keywords__contains = forms.CharField()
    publishDatetime__year = forms.CharField()
    order_by = forms.CharField()
    page = forms.IntegerField()

    def clean(self):
        category_id = self.cleaned_data.get('category_id',None)
        keywords__contains = self.cleaned_data.get('keywords__contains',None)
        publishDatetime__year = self.cleaned_data.get('publishDatetime__year',None)
        order_by = self.cleaned_data.get('order_by',None)
        page = self.cleaned_data.get('page',1)

        # 1. category_id
        if not category_id:
            raise forms.ValidationError('category_id')
        try:
            category = self.Category.objects.get(id=category_id)
        except:
            raise forms.ValidationError('category_id')

        # 2. keywords__contains
        if keywords__contains:
            if not keywords__contains in category.keywordsTag:
                raise forms.ValidationError('keywords__contains')

        # 3. publishDatetime__year
        if publishDatetime__year:
            try:
                publishDatetime__year = int(publishDatetime__year)
                if not (publishDatetime__year >= 0 and publishDatetime__year <= 2100):
                    raise forms.ValidationError('keywords__contains')
            except:
                raise forms.ValidationError('keywords__contains')
        # 4. order_by
        if order_by:
            if not order_by in ['publishDatetime', 'clickNum', 'collectNum', '-publishDatetime', '-clickNum',
                                     '-collectNum']:

                raise forms.ValidationError('order_by')

        return self.cleaned_data



class BaseListView(ListView):
    model = OutsideArticle
    Category = OutsideCategory


    template_name = 'appArticle/articleList.html'
    context_object_name = 'articles'

    paginate_by = 15

    def get_queryset(self):
        af = ArticleListForm(self.request.GET)
        if not af.is_valid():
            raise Http404('valid')




    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



