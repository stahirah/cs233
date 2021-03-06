from django.db import models


# Create your models here.

class Protein(models.Model):
    protein_id = models.CharField(max_length=100)
    protein_name = models.CharField(max_length=1000)
    slug = models.SlugField()
    function = models.TextField()
    locations = models.TextField()
    thumb = models.ImageField(default='default.png', blank=True)

    class Meta:
        verbose_name_plural = "proteins"

    def __str__(self):
        return self.protein_id

    def function_preview(self):
        return self.function[:200] + ' ...'

    def name_preview(self):
        return self.protein_name[:100] + ' ...'


class ProteinImage(models.Model):
    protein_id = models.ForeignKey(Protein, default=None, on_delete=models.CASCADE)
    images = models.ImageField()
