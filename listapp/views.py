import requests
from django.shortcuts import render
from bs4 import BeautifulSoup
from . import models

# Create your views here.
def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)

    final_postings = []

    stuff_for_frontend = {
        'search': search,
        'final_postings': final_postings,
    }

    return render(request, 'listapp/new_search.html', stuff_for_frontend)
