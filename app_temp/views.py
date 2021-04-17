from django.shortcuts import render,redirect

# Create your views here.

def index_handler(request):
    return redirect('/admin')


