from django.shortcuts import redirect,reverse,render,get_object_or_404
from django.http import JsonResponse
from django.views import View
from appUser.models import WebUser
from django.http import Http404


class LoginView(View):
    def post(self,request):
        account = request.POST.get('account')
        password = request.POST.get('password')
        try:
            webUser = WebUser.objects.get(account=account,password=password)
            request.session['webUser'] = webUser.toDict()
            return JsonResponse( data={'code':True})
        except:
            return JsonResponse( data={'code':False})


class LogoutView(View):
    def get(self,request):
        request.session['webUser'] = None
        return redirect('/')



class InfoView(View):
    def get(self,request):
        return render(request,'appUser/userInfo.html',request.context)

    def post(self,request):
        return render(request,'appUser/userInfo.html',request.context)


class CollectView(View):
    def get(self,request,category=None):
        """
        :param category: inside | outside | pdf
        :return:
        """
        webUser:WebUser = get_object_or_404(
            WebUser,id=request.session['webUser']['id']
        )

        if category == 'inside':
            articles = webUser.collectedInsideActicles.all()
        elif category == 'outside':
            articles = webUser.collectedOutsideActicles.all()
        elif category == 'pdf':
            articles = webUser.collectedPDFActicles.all()
        else:
            raise Http404('error category')
        request.context['articles'] = articles

        return render(request,'appUser/userCollect.html',request.context)




