from django.urls import path
from . import views

urlpatterns = [
    path('', views.proteins_list)
]
