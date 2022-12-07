from django.shortcuts import render, redirect
from .forms import VideoForm
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.contrib import messages
from .models import Video

# Create your views here.

def home(request):
    app_name = 'Study Music Videos' 
    return render(request, 'video_collection/home.html', {'app_name': app_name})


def add(request):

    if request.method == 'POST':
        new_video_form = VideoForm(request.POST)
        if new_video_form.is_valid():
            try:
                new_video_form.save()
                # messages.info(request, 'New video saved!')
                # todo redirect to list of videos
                return redirect('video_list')
            except ValidationError:
                messages.warning('request', 'Invalid YouTube URL')
            except IntegrityError:
                messages.warning(request, 'You already added that video')
 
        messages.warning(request, 'Please check the data entered.')
        return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})

    new_video_form = VideoForm()
    return render(request, 'video_collection/add.html', {'new_video_form': new_video_form})


def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video_collection/video_list.html', {'videos': videos})