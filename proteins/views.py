from django.shortcuts import render, get_object_or_404
from .models import Protein, ProteinImage
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.db.models import Q

# Create your views here.
def proteins_list(request):
    proteins = Protein.objects.all().order_by('protein_name')
    return render(request, 'proteins/proteins_list.html', {'proteins':proteins})


def protein_detail(request, slug):
    # return HttpResponse(slug)
    protein = get_object_or_404(Protein, slug=slug)
    photos = ProteinImage.objects.filter(protein_id=protein)
    return render(request, 'proteins/result.html', {'protein':protein, 'photos':photos})

class SearchResultsView(ListView):
    model = Protein
    template_name = 'proteins/search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Protein.objects.filter(
            Q(protein_id__icontains=query) | Q(protein_name__icontains=query)
        )
        return object_list

