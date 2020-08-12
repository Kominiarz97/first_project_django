from django.shortcuts import render
from django.http import HttpResponse

posts=[
    {
        'author':'Maciek',
        'title':'Post 1',
        'content':'First post on the blog',
        'date_posted':'12.08.2020'
    },
    {
        'author':'Maciek',
        'title':'Post 2',
        'content':'Second post on the blog',
        'date_posted':'13.08.2020'
    },
    {
        'author':'Maciek',
        'title':'Post 3',
        'content':'Third post on the blog',
        'date_posted':'14.08.2020'
    },
]



def home(request):
    context={
        'posts':posts,
        'title':'Home'
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})

def gallery(request):
    return render(request,'blog/contact.html',{'title':'Contact'})

def contact(request):
    return render(request,'blog/contact.html',{'title':'Contact'})
