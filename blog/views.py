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
    }
    return render(request,'blog/home.html',context)

def about(request):
    return HttpResponse('<h1>About</h1>')

def gallery(request):
    return HttpResponse('<h1>Gallery</h1>')

def contact(request):
    return HttpResponse('<h1>Contact</h1>')
