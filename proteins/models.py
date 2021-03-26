from django.db import models

# Create your models here.

class Protein(models.Model):
    protein_id = models.CharField(max_length=100)
    protein_name = models.CharField(max_length=100)
    slug = models.SlugField()
    function = models.TextField()
    locations = models.TextField()


    def __str__(self):
        return self.protein_id

    def function_preview(self):
        return self.function[:50] + '...'