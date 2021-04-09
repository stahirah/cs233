from django.contrib import admin
from .models import Location


class LocationAdmin(admin.ModelAdmin):
    list_display = ("location_name", "description")

admin.site.register(Location, LocationAdmin)

# Register your models here.
