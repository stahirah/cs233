from django.contrib import admin
from .models import Protein, ProteinImage

# Register your models here.



class ProteinImageInline(admin.TabularInline):
    model = ProteinImage
    extra = 3

class ProteinAdmin(admin.ModelAdmin):
    list_display = ("protein_id", "protein_name",)
    inlines = [ProteinImageInline, ]
    class Meta:
        model = Protein


admin.site.register(Protein, ProteinAdmin)
