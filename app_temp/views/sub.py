from django.shortcuts import render, redirect


def sub_header(request):
    return render(request, 'tag/header.html')


def sub_nav_left(request):
    return render(request, 'tag/nav-left.html')


def sub_nav_top(request):
    return render(request, 'tag/nav-top.html')


def sub_content(request):
    return render(request, 'tag/content.html')
