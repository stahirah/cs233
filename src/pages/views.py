from django.http import HttpResponse
from django.shortcuts import render


#DJANGO TEMPLATES put HTML codes in templates

# Create your views here.
def home_view(*args, **kwargs):
    print(args, kwargs)
    return render('index.html', {})
