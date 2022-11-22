from django.shortcuts import render
from urllib.request import urlopen
import json

posts = [
    {"author": "Robert Bielicki", "title": "Nauka frameworka Django", "content": "Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source. ", "date_posted": "20.11.2022"}, 
    {"author": "Natalia Marcińczyk", "title": "Dywan", "content": "Misia Natalia była bardzo zasmucona dywanem i trzba było go oddać :<", "date_posted": "22.11.2022"}
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def moja(request):
    return render(request, 'blog/moja.html', {'title': 'Moja'})