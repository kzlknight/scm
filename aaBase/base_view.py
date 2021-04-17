from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.utils.urls import replace_query_param  # 用于得到指定的页码


class MyBasePagination(PageNumberPagination):
    page_size = 20

    def get_page_link(self, page_number):
        url = self.request.build_absolute_uri()
        return replace_query_param(url, self.page_query_param, page_number)

    def get_paginated_response(self, data):
        data = {
            'links': {
                'first': self.get_page_link(page_number=1),  # 第一页的地址
                'next': self.get_next_link(),  # 下一页的地址
                'previous': self.get_previous_link(),  # 上一页的地址
                'end': self.get_page_link(page_number=self.page.paginator.num_pages)  # 最后一页的地址

            },
            'count': self.page.paginator.count,  # 一共多少条数据
            'num_pages': self.page.paginator.num_pages,  # 一共多少页
            'current_page': self.page.number,  # 当前页码
            'results': data
        }
        return Response(data)

