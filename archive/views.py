from django.shortcuts import render

# Create your views here.
def archivepage(request):
    return render(request,'archive/archivepage.html')