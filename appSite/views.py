from django.shortcuts import redirect,reverse
from django.http import JsonResponse
from django.views import View
from appUser.models import WebUser
from django.http import HttpResponse
from django.shortcuts import render





def page404(request,exception):
    return render(request,'page404.html',request.context)

