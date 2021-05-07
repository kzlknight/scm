from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse

class ContextMiddleware(MiddlewareMixin):
    # 重写了init方法
    def __init__(self,get_response=None):
        super().__init__(get_response)
    # 1.请求进入中间件后，运行第一个方法
    def process_request(self,request):
        # 返回HttpResponse|None
        webUser = request.session.get('webUser',None)
        request.context = {
            'webUser':webUser
        }


