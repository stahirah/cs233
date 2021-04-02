from django.urls import path
from . import views

app_name = 'proteins'

urlpatterns = [
    path('', views.proteins_list, name='list'),
    path('(?P<slug>[\w-]+)/$', views.protein_detail, name='detail')
]

#
