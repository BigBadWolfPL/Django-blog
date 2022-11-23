from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def moja(request):
    return render(request, 'blog/moja.html', {'title': 'Moja'})


def kontakt(request):
    context = {
        'title': 'Kontakt', 
        'dane_kontaktowe': [
            'GitHub: BigBadWolfPL', 
            'LindedIn: Robert Bielicki', 
            'Mail: robertbielickiwet@gmail.com', 
            'Tel: 504-113-035'
            ]
    }
    return render(request, 'blog/kontakt.html', context)

def testowy(request):
    
    context = {
        'title': 'Kontakt', 
        'dane_kontaktowe': [
            'GitHub: BigBadWolfPL', 
            'LindedIn: Robert Bielicki', 
            'Mail: robertbielickiwet@gmail.com', 
            'Tel: 504-113-035'
            ]
    }
    return render(request, 'blog/testowytem.html', context)
