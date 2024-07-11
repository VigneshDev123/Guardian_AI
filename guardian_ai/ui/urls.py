from django.contrib import admin
from django.urls import path
from .views import upload_video, first  # Import the view function

urlpatterns = [
    path('',first),  # Define URL pattern for the root URL
    path('upload/', upload_video, name='upload_video'),
]
