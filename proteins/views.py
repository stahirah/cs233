from django.shortcuts import render
from .models import Protein
from django.http import HttpResponse

# Create your views here.
def proteins_list(request):
    proteins = Protein.objects.all().order_by('protein_name')

    return render(request, 'proteins/proteins_list.html', {'proteins':proteins})


def protein_detail(request, slug):
    # return HttpResponse(slug)
    protein = Protein.objects.get(slug=slug)
    return render(request, 'proteins/result.html', {'protein':protein})