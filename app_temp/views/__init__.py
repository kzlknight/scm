from django.shortcuts import render,redirect
from app_temp.views.sub import *

# Create your views here.

def article_list(request):
    # return redirect('/admin')
    return render(request,'article_list.html')


