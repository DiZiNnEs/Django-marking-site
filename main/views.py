from django.shortcuts import render, redirect
from .models import Notes, Contact, About
from .forms import EntryNotes


def index(request):
    return render(request, 'main/index.html')


def home(request):
    notes = Notes.objects.order_by('-pub_date')
    return render(request, 'main/home.html', {
        'notes': notes,
    })


def add(request):
    if request.method == "POST":
        form = EntryNotes(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EntryNotes()

    # form = EntryNotes

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
    signup = ...
    return render (request, 'main/sign_up.html', {

    })


def log_up(reqeust):
    return render(reqeust, 'main/log_up.html',{

    })
