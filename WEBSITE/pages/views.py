from django.http import HttpResponse
from django.shortcuts import render


#DJANGO TEMPLATES put HTML codes in templates

# Create your views here.
def home(*args, **kwargs):
    return HttpResponse(
        "<HTML CODE HERE>  search page"
    )
