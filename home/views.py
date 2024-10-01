from django.shortcuts import render
from .models import PagesHome
from reports.models import Report
import os
from django.conf import settings

# Create your views here.
def homepage(request):
    pages = PagesHome.objects.all()
    last_report = Report.objects.order_by('datetime_created').last()
    


    path = os.path.join(settings.MEDIA_ROOT, 'report/temp_images') 
    dir = os.listdir(path)
                
    if len(dir) > 0:
        for file in dir:
            os.remove(path + f'/{file}')
            
    if last_report != None:
        return render(request, 'home/homepage.html', {'pages':pages, 'last': last_report})
    else:
        report = Report(number='000000')
        report.save()
        last_report = Report.objects.order_by('datetime_created').last()
    
        return render(request, 'home/homepage.html', {'pages':pages, 'last': last_report})