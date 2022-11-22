from django.shortcuts import render
from urllib.request import urlopen
import json

url = "https://raw.githubusercontent.com/BigBadWolfPL/Blog-Flask/main/wpisy.json"

with urlopen(url) as res:
    data = json.load(res)



def home(request):
    context = {
        'wpisy': data
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def moja(request):
    return render(request, 'blog/moja.html', {'title': 'Moja'})