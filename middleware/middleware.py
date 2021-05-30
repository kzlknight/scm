from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse
from django.shortcuts import redirect

class ContextMiddleware(MiddlewareMixin):
    # 重写了init方法
    def __init__(self,get_response=None):
        super().__init__(get_response)

    # 1.请求进入中间件后，运行第一个方法
    def process_request(self,request):
        # 返回HttpResponse|None
        request.context = {}
        webUser = request.session.get('webUser',None)
        request.context['showLogin'] = True
        if webUser:
            request.context = {
                'webUser':webUser,
                'showLogin':False,
                'full_path':request.get_full_path(),
            }
        else:
            if request.path.startswith('/admin'):
                return None
            if request.get_full_path() == '/':
                return None
            if request.path == '/login':
                return None
            if request.path.startswith('/static'):
                return None
            if request.path.startswith('/media'):
                return None
            return redirect('/')



