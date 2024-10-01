from django.urls import path
import archive.views as archives

urlpatterns = [
    path('', archives.archivepage, name='archivepage')
]