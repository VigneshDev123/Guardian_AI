# views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Video
from .forms import VideoUploadForm
import easygui

def first(request):
    return render(request,"index.html")
def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video_file = request.FILES['video']  
            video = Video(file=video_file) 
            video.save()
            easygui.msgbox("Video Uploaded Successfully. Email will be generated in few seconds...","Success")
    else:
        form = VideoUploadForm()
    return render(request, 'index.html', {'form': form})


