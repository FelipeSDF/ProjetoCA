from django.db import models
import datetime
from CertificateProject.settings import BASE_DIR, MEDIA_ROOT

today = datetime.date.today()

# Create your models here.
class Report(models.Model):
    number = models.CharField(max_length=10)
    data = models.DateField(default=today)
    datetime_created = models.DateTimeField(auto_created=True, auto_now_add= True)
    local = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    unidade = models.CharField(max_length=255)
    obs  = models.CharField(max_length=255)
    pavimentation = models.CharField(max_length=255)
    eletricity = models.CharField(max_length=255)
    ilumination = models.CharField(max_length=255)
    quantity_houses = models.CharField(max_length=255)
    photos = models.ImageField(upload_to='report/slogan_images', default='report/404.png')
    Reports = models.CharField(max_length=600, blank=True, default='Não há relatórios')
    
    def __str__(self) -> str:
        return self.number
    