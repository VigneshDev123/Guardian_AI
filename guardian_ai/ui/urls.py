from django.contrib import admin
from django.urls import path
from ui.views import upload_video, first, send_email,preprocess_frame  # Import the view function

urlpatterns = [
    path('',first),  # Define URL pattern for the root URL
    path('upload/', upload_video, name='upload_video'),
    path('email/',send_email,name='Send_Mail'),
    path('processing/', preprocess_frame, name='Preprocessing')
]
