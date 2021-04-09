from django.http import HttpResponse
from django.shortcuts import render

def search(request):
    #return HttpResponse('About')
    return render(request, 'search_results.html')


def home(request):
    #return HttpResponse('Homepage')
    return render(request, 'index.html')

