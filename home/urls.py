from django.urls import path
from django.conf.urls import include, url
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]