from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return render(request, 'home.html')
    # render h


def about(request):
    return render(request, 'about.html')


def portfolio(request):
    return render(request,'portfolio.html')