from django.urls import path
from . import views

urlpatterns = [
    path('api/upload', views.process_file, name='process_file'),
]