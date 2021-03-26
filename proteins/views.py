from django.shortcuts import render
from .models import Protein

# Create your views here.
def proteins_list(request):
    proteins = Protein.objects.all().order_by('protein_name')

    return render(request, 'proteins/proteins_list.html', {'proteins':proteins})


