from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    return HttpResponse('<h1>home</h1>')

def about_view(request):
    return HttpResponse('<h1>about</h1>')

def contect_view(request):
    return HttpResponse('<h1>contect</h1>')
