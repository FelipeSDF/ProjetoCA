from django.db import models

# Create your models here.
class PagesHome(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    link = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name