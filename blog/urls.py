from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('gallery/', views.gallery, name='blog-gallery'),
    path('contact/', views.contact, name='blog-contact'),

]