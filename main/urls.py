from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('home/', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('log_up/', views.log_up, name='log_up'),
]
