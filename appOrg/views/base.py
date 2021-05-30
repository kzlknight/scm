from appOrg.models import Organization
from django.core.paginator import Paginator


class OrgListTool():
    def __init__(self, request, per_page=8):
        self.request = request
        self.per_page = per_page

        self.error_message = ''
        self.query_dict = {}
        self.query_order = None

        self.page = request.GET.get('page', 1)

    def clean(self):
        # 1. 验证Page
        try:
            self.page = int(self.page)
        except:
            self.error_message = 'page' + str(self.page)
            return False
        # 2. 验证范围
        orgs = Organization.objects.all()
        self.paginator = Paginator(orgs,self.per_page)
        if not (self.page >0 and self.page <=self.paginator.num_pages):
            self.error_message = 'page out range'
            return False
        self.instance_page = self.paginator.page(self.page)
        return True

    def get_url(self,page=None):
        if page:
            return self.request.path + '?page=' + str(page)
        else:
            return self.request.path


    def page_data(self,length=5):
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

