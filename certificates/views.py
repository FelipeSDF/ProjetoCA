from django.shortcuts import render

# Create your views here.
def certificatepage(request):
    return render(request,'certificates/certificatepage.html')