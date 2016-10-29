from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Project
from .forms import userfield, UploadForm


def index(request):
    return render(request, 'prof/plain.html')
    
def login(request):
    usernameform = userfield()
    return render(request, 'prof/login.html', {'form' : usernameform})


def projecthome(request):
    return render(request, 'prof/plain.html', {})
    
def dashboard(request):
    uploadform=UploadForm()
    return render(request, 'prof/dashboard.html', {'uploadform' : uploadform})
    
