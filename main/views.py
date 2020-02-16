from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def add(request):
    return render(request, 'main/add.html')

def contact(request):
    return render(request, 'main/contact.html')

def about(request):
    return render(request, 'main/about.html')
