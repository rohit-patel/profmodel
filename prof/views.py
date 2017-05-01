from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import FileSpaceForm
from .models import FileSpace, RunSpace
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from guardian.shortcuts import get_objects_for_user, assign_perm
from guardian.decorators import permission_required_or_403
from django.contrib.auth.models import User
from django.views.generic.edit import DeleteView
from prof.ProcessingFunctions import ProcessTransactionData, generateSamplePnL, updateRunPeriod, processPnLFile


def index(request):
    return render(request, 'prof/plain.html')

@login_required    #This decorator makes sure that a user is logged in
def userhome(request):  #This is the view that processes users home. For now, we are just taking run 1, but will edit to make a full fleged home at some point
    runpk=1
    company= RunSpace.objects.get(pk=runpk).CompanyName
    run=RunSpace.objects.get(pk=runpk).RunNo
    return render(request, 'prof/userhome.html', {'runpk': runpk, 'company' : company, 'run': run})
    
@login_required
@permission_required_or_403('prof.file_owner',(RunSpace, 'pk', 'runpk' ))  #This decorator makes sure that the user that is logged in has 
def runhome(request,runpk):
    runobject=RunSpace.objects.get(pk=runpk)
    company = runobject.CompanyName
    local_runno=runobject.RunNo
    
    if request.method=='POST':
        form=FileSpaceForm(request.POST, request.FILES)
        if form.is_valid():
            newfile = FileSpace(run = RunSpace.objects.get(pk=runpk), FileType = request.POST['FileType'], FileName = request.POST['FileName'], File=request.FILES['File'])
            if newfile.FileType=='T':
                if FileSpace.objects.filter(FileType='T', run=runobject):
                    oldTransactionFile=FileSpace.objects.get(FileType='T', run=runobject)
                    oldTransactionFile.delete()
                    newfile.save()
                    ProcessTransactionData(newfile,runobject)
                else:
                    newfile.save()
                    ProcessTransactionData(newfile,runobject)
                updateRunPeriod(runobject)
                if not(FileSpace.objects.filter(FileType='P', run=runobject)):
                    PnL_sample_file=FileSpace(run=runobject,FileType='P', FileName = 'PnL Sample', FileDescription = 'A sample PnL available for downloas based on uploaded transactions data')
                    PnL_sample_file.File.save('PnL_Sample_run{0}.xlsx'.format(runpk), generateSamplePnL(runobject))
                    assign_perm('prof.file_owner',request.user,PnL_sample_file)
            elif newfile.FileType=='P':
                if FileSpace.objects.filter(FileType='P', run=runobject):
                    oldTransactionFile=FileSpace.objects.get(FileType='P', run=runobject)
                    oldTransactionFile.delete()
                    newfile.save()
                    processPnLFile(newfile, runobject)
                else:
                    newfile.save()
                    processPnLFile(newfile, runobject)
            elif newfile.FileType=='K':
                newfile.save()
            assign_perm('prof.file_owner',request.user,newfile)
            return HttpResponseRedirect(reverse('prof:runhome', kwargs={'runpk' : runpk}, current_app='prof'))
            #return render(request, 'prof/plain.html',{'runpk': runpk})  #Just some test code to see behavior
    else:
        form=FileSpaceForm()
        
    relevant_files=FileSpace.objects.filter(run=runobject)  #get_objects_for_user(request.user,'prof.file_owner').filter(CompanyName=company, RunNo = run)
    pnl_files=relevant_files.filter(FileType='P')
    key_files=relevant_files.filter(FileType='K')
    transactions_files=relevant_files.filter(FileType='T')
    
    local_context={'company' : company, 'local_runno' : local_runno, 'form' : form, 'pnl_files' : pnl_files, 'key_files' : key_files, 'transactions_files' : transactions_files, 'runpk' : runpk }
    return render(request, 'prof/runhome.html',local_context)

#This view is not currently in use
class FileDeleteConfirm(DeleteView):
    model = FileSpace
    runpk=1 #temporary please
    success_url = reverse_lazy('prof:runhome', kwargs={'runpk' : runpk}, current_app='prof')
    
    
