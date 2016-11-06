from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import FileSpaceForm
from .models import FileSpace, RunSpace
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from guardian.shortcuts import get_objects_for_user, assign_perm
from guardian.decorators import permission_required_or_403

def index(request):
    return render(request, 'prof/plain.html')

@login_required    
def userhome(request):
    runpk=1
    company= RunSpace.objects.get(pk=runpk).CompanyName
    run=RunSpace.objects.get(pk=runpk).RunNo
    return render(request, 'prof/userhome.html', {'runpk': runpk, 'company' : company, 'run': run})
    
@login_required
#@permission_required_or_403('prof.file_owner',(request.user,RunSpace.objects.get(pk=runpk)))  #This does not work, but we need a decorator somehow
def runhome(request,runpk):
    runobject=RunSpace.objects.get(pk=runpk)
    company = runobject.CompanyName
    local_runno=runobject.RunNo
    #if request.method=='POST':
    #    form=FileSpaceForm(request.POST, request.FILES)
    #    if form.is_valid():
    #        newfile = FileSpace(CompanyName=request.POST['CompanyName'], RunNo = request.POST['RunNo'], RunName = request.POST['RunName'], FileType = request.POST['FileType'], TheActualFile=request.FILES['TheActualFile'])
    #        newfile.save()
    #        assign_perm('prof.file_owner',request.user,newfile)  #This is causing some sort of an error, understand how permission assigning in django-guardian works.
    #        return HttpResponseRedirect(reverse('prof:runhome',kwargs={'runid' : runpk}, current_app='prof'))
    #else:
    form=FileSpaceForm() #tab is when reinserting the if statements above
        
    relevant_files=FileSpace.objects.filter(UniqueRunID=runobject)  #get_objects_for_user(request.user,'prof.file_owner').filter(CompanyName=company, RunNo = run)
    pnl_files=relevant_files.filter(FileType='P')
    key_files=relevant_files.filter(FileType='K')
    sales_files=relevant_files.filter(FileType='S')
    
    local_context={'company' : company, 'local_runno' : local_runno, 'form' : form, 'pnl_files' : pnl_files, 'key_files' : key_files, 'sales_files' : sales_files, 'runpk' : runpk }
    return render(request, 'prof/runhome.html',local_context)
