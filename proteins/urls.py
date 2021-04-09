from django.urls import path
from . import views
from .views import SearchResultsView

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'proteins'

urlpatterns = [
    path('', views.proteins_list, name='list'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('<slug>', views.protein_detail, name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#documentations
#SEARCH FUNCTIONALITY https://stackoverflow.com/questions/53364910/django-search-function
#IMAGE DISPLAY https://soshace.com/upload-multiple-images-to-a-django-model-without-plugins/