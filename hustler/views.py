
import os
from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'hustler/home.html')

def gallery(request):
    return render(request, 'hustler/gallery.html')

def autobot(request):
    return render(request, 'hustler/autobot.html')




def download_file(request):
    file_path = 'hustler\static\hustler\gym_fitness.apk' # Replace with the path to your file
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404("File not found")