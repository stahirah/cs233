from django.urls import path
from . import views

app_name = 'locations'

urlpatterns = [
    path('', views.locations_list, name='list'),
    path('<slug>', views.location_detail, name='detail')
]