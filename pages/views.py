from django.shortcuts import render
from django.http import HttpResponse

# pages/views.py

def homePageView(request):
    return HttpResponse("Hello, World!")