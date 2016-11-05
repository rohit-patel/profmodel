from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import FileSpace
from .forms import userfield, UploadForm


def index(request):
    return render(request, 'prof/plain.html')

@login_required    
def userhome(request):
    company='Test Corp.'  #Temporary only, edit these to define company and run in the view
    run='1'               #Temporary only, edit these to define company and run in the view        
    return render(request, 'prof/userhome.html', {'company': company, 'run' : run})
    
@login_required    
def runhome(request,company,run):
    return render(request, 'prof/runhome.html',{'company' : company, 'run' : run})
