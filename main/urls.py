from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home/', views.index, name='home'),
    path('add/', views.add, name='add'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about')
]

