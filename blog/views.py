from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Blog home</h1>')

def about(request):
    return HttpResponse('<h1>About</h1>')

def gallery(request):
    return HttpResponse('<h1>Gallery</h1>')

def contact(request):
    return HttpResponse('<h1>Contact</h1>')
