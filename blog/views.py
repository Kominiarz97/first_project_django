from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post



def home(request):
    context={
        'posts':Post.objects.all(),
        'title':'Home'
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})

def gallery(request):
    return render(request,'blog/contact.html',{'title':'Contact'})

def contact(request):
    return render(request,'blog/contact.html',{'title':'Contact'})
