from django.shortcuts import render, redirect
from .models import Notes, Contact, About
from .forms import EntryNotes
from django.contrib.auth.models import User


def index(request):
    return render(request, 'main/index.html')


def home(request):
    if request.user.is_authenticated:
        notes = Notes.objects.filter(user=request.user).order_by('-pub_date')
        return render(request, 'main/home.html', {
            'notes': notes,
        })
    else:
        return redirect('log_in')


def add(request):
    if request.method == "POST":
        form = EntryNotes(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EntryNotes()

    context = {'form': form}

    return render(request, 'main/add.html', context)


def contact(request):
    contacts = Contact.objects.all()
    return render(request, 'main/contact.html', {
        'contacts': contacts,
    })


def about(request):
    abouts_me = About.objects.all()
    return render(request, 'main/about.html', {
        'about_me': abouts_me
    })


def sign_up(request):
    return render(request, 'allauth/account/signup.html', {

    })


def log_in(reqeust):
    return render(reqeust, 'allauth/account/login.html', {

    })


def error(request):
    return render(request, 'main/error.html', {

    })
