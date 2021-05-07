from appExpert.models import Category, Expert
from django.core.paginator import Paginator
from copy import deepcopy
import urllib.parse as up


class ExpertListTool():
    def __init__(self, request, per_page=15):
        self.request = request
        self.per_page = per_page

        self.error_message = ''
        self.query_dict = {}
        self.query_order = None

        self.category_id = request.GET.get('id', None)
        self.page = request.GET.get('page', 1)

    def clean(self):
        # 1.全部的种类
        self.categorys = Category.objects.all()
        # 2.category_id
        # 2.1 如果没有category_id默认点击第一个
        if not self.category_id:
            self.this_category = Category.objects.first()
            self.category_id = self.this_category.id
            print(self.category_id,'----')
        # 2.2 如果有category_id
        else:
            try:
                # 可以查找的到
                self.this_category = Category.objects.get(id=self.category_id)
                print(self.category_id,'====')
            except:
                # 无法查找的到
                self.error_message = 'expertlist:无法查找到category_id' + str(self.category_id)
                return False
        # 3 page
        # 3.1 验证page是否为整数
        try:
            self.page = int(self.page)
        except:
            self.error_message = 'page' + str(self.page)
            return False
        # 3.2 验证范围
        experts = self.this_category.experts.all()
        self.paginator = Paginator(experts, self.per_page)
        if not (self.page > 0 and self.page <= self.paginator.num_pages):
            self.error_message = 'page out of range'
            return False
        self.instance_page = self.paginator.page(self.page)
        # 3.3 query_dict
        self.query_dict['id'] = self.category_id
        self.query_dict['page'] = self.page
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
