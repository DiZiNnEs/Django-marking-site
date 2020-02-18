from django.shortcuts import render
from .models import Notes,Contact, About

def index(request):
    return render(request, 'main/index.html')


def home(request):
    notes = Notes.objects.all()
    return render(request, 'main/home.html', {
        'notes': notes,
    })


def add(request):
    return render(request, 'main/add.html')


def contact(request):
    contacts = Contact.objects.all()
    return render(request, 'main/contact.html', {
        'contacts': contacts,
    })


def about(request):
    abouts_me = About.objects.all()
    return render(request, 'main/about.html', {
        'about_me' : abouts_me
    })
