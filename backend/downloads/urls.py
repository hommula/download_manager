from django.urls import path
from . import views

urlpatterns = [
    path('queue_downloads', views.add_download_queue),
    path('dir_structure', views.get_directory_structure),
    path('queue', views.get_current_queue),
    path('download_progress', views.get_current_download_progress),
]