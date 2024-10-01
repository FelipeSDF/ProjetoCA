from django.urls import path
import reports.views as reports

urlpatterns = [
    path('', reports.reportpage, name='reportpage')
]