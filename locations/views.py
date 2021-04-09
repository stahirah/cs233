from django.shortcuts import render
from .models import Location
# Create your views here.

def locations_list(request):
    locations = Location.objects.all().order_by('location_name')

    return render(request, 'locations/locations_list.html', {'locations':locations})


def location_detail(request, slug):
    # return HttpResponse(slug)
    location = Location.objects.get(slug=slug)
    return render(request, 'locations/result.html', {'location':location})
