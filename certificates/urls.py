from django.urls import path
import certificates.views as certificates

urlpatterns = [
    path('', certificates.certificatepage, name='certificatepage')
]