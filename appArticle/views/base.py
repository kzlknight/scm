from copy import deepcopy
from django.core.paginator import Paginator
import datetime
import urllib.parse as up

class ArticleListTool():
    Category: None
    Article: None

    def __init__(self, request, per_page=15):
        self.request = request
        self.per_page = per_page

        self.error_message = ''
        self.query_dict = {}
        self.query_order = None

        self.category_id = request.GET.get('category_id', None)
        self.keyword = request.GET.get('keywords__contains', None)
        self.year = request.GET.get('publishDatetime__year', None)
        self.order_by = request.GET.get('order_by', None)
        self.page = request.GET.get('page', 1)


    def clean(self):
        # 1. category可以为空，且能找到
        if not self.category_id:
            self.error_message = 'no category_id'
            return False
        if not self.Category.objects.filter(id=self.category_id):
            self.error_message = 'not find category'
            return False
        # 2. 关键字
        if self.keyword:
            category = self.Category.objects.get(id=self.category_id)
            # 搜索关键字不在keywordsTag里面
            if not self.keyword in category.keywordsTag:
                self.error_message = 'error keyword'
                return False
        # 3. year
        if self.year:
            try:
                year = int(self.year)
                if not (year >= 0 and year <= 2100):
                    self.error_message = 'error year'
                    return False
            except:
                self.error_message = 'error year'
                return False
        # 4. order_by
        if self.order_by:
            if not self.order_by in ['publishDatetime', 'clickNum', 'collectNum', '-publishDatetime', '-clickNum',
                                     '-collectNum']:
                self.error_message = 'error order_by'
                return False
        # == query_dict
        if self.category_id:
            self.query_dict['category_id'] = self.category_id
        if self.keyword:
            self.query_dict['keywords__contains'] = self.keyword
        if self.year:
            self.query_dict['publishDatetime__year'] = self.year
        # articles
        articles = self.Article.objects.filter(**self.query_dict)
        # order_by
        if self.order_by:
            articles = articles.order_by(self.order_by)

        # 5. page
        # 5.1 判断是否为整数
        try:
            self.page = int(self.page)
        except:
            self.error_message = 'error page'
            return False
        # 5.2 判断是否属于范围
        self.paginator = paginator = Paginator(articles, self.per_page)
        if not (self.page >= 0 and self.page <= paginator.num_pages):
            self.error_message = 'page out off range'
            return False
        self.instance_page = paginator.page(self.page)  # 当前页面的page对象
        return True

    def get_url(self, **kwargs):
        this_query_dict = deepcopy(self.query_dict)
        for key in kwargs.keys():
            value = kwargs[key]
            if value:
                this_query_dict[key] = kwargs[key]
            else:
                if key in this_query_dict.keys():
                    del this_query_dict[key]
        query_str = up.urlencode(this_query_dict)
        full_url = self.request.path + '?' + query_str
        return full_url

    # 用于分页
    def page_data(self, length=5):
        '''
        ret_data = {
            'num_pages':int, # 最大页码
            'first': {'url': 'url', 'name': 'name', 'enable': True},
            'mid': [
                {'url': 'url', 'name': 'name', 'enable': True},
                {'url': 'url', 'name': 'name', 'enable': False},  # 当前页
                {'url': 'url', 'name': 'name', 'enable': True},
            ],
            'last': {'url': 'url', 'name': 'name', 'enable': True},
        }
        '''

        this_first = {
            'url': self.get_url(page=1),
            'name': '首页',
            'enable': True if self.page > 1 else False
        }
        this_last = {
            'url': self.get_url(page=self.paginator.num_pages),
            'name': '尾页',
            'enable': True if self.page < self.paginator.num_pages else False
        }
        this_mids = []
        page_start = max(1, self.page - int(length / 2))
        page_end = min(self.page + int(length / 2), self.paginator.num_pages)
        for page in range(page_start, page_end + 1):
            this_mids.append(
                {
                    'url': self.get_url(page=page),
                    'name': page,
                    'enable': True if self.page != page else False
                }
            )
        ret_data = {
            'num_pages': self.paginator.num_pages,
            'first': this_first,
            'mids': this_mids,
            'last': this_last,
        }

        return ret_data

    def nav_top_data(self):
        '''

        ret_data = {
            'keywords': [{'url': '', 'name': '', 'clicked': True}, ],
            'years': [{'url': '', 'name': '', 'clicked': True}, ],
            'order_bys': [{'url': '', 'name': '', 'clicked': True, }],
        }
        '''

        # keywords:
        keywords = []
        if not self.category_id:
            pass
        else:
            category = self.Category.objects.get(id=self.category_id)
            if not category.keywordsTag:
                pass
            else:
                keyword_names = category.keywordsTag.split(',')
                keywords_nolimit = {
                    'url': self.get_url(keywords__contains=None, page=1),
                    'name': '不限',
                    'clicked': True if not self.keyword else False,
                }
                keywords.append(keywords_nolimit)
                for name in keyword_names:
                    url = self.get_url(keywords__contains=name, page=1)
                    keywords.append({'url': url, 'name': name, 'clicked': True if name == self.keyword else False})
        # years
        years = []
        years_nolimit = {
            'url': self.get_url(publishDatetime__year=None, page=1),
            'name': '不限',
            'clicked': True if not self.year else False,
        }
        years.append(years_nolimit)
        for year in range(datetime.datetime.now().year, 2019, -1):
            url = self.get_url(publishDatetime__year=year, page=1)
            years.append({'url': url, 'name': year, 'clicked': True if str(year) == str(self.year) else False})

        # order_by
        order_bys = [
            {'url': self.get_url(order_by=None, page=1), 'name': '不限', 'clicked': True if not self.order_by else False},
            {'url': self.get_url(order_by='-clickNum', page=1), 'name': '点击量',
             'clicked': True if self.order_by == '-clickNum' else False},
            {'url': self.get_url(order_by='-collectNum', page=1), 'name': '收藏量',
             'clicked': True if self.order_by == '-collectNum' else False},
            {'url': self.get_url(order_by='-publishDatetime', page=1), 'name': '发布时间',
             'clicked': True if self.order_by == '-publishDatetime' else False},
        ]

        ret_data = {
            'keywords': keywords,
            'years': years,
            'order_bys': order_bys
        }
        return ret_data