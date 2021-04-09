from django.db import models

# Create your models here.

class Location(models.Model):
    location_name = models.CharField(max_length=1000)
    slug = models.SlugField()
    description = models.TextField()
    thumb = models.ImageField(default='default.png', blank=True)

    class Meta:
        verbose_name_plural = "locations"

    def __str__(self):
        return self.location_name

    def function_preview(self):
        return self.description[:400] + ' ...'



