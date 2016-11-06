from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class RunSpace(models.Model):
    CompanyName = models.CharField(max_length=100, blank=False)
    RunNo = models.IntegerField(blank=False)
    RunName = models.CharField(max_length=20,blank=False)
    RunDescription = models.TextField(blank=True)
    class Meta:
        permissions = (
            ('file_owner', 'File Owner'), 
            ('file_edit_permission', 'File Editing Permission'), 
            ('file_view_permission', 'File Viewing Permission'), 
        )    

    
class FileSpace(models.Model):
    PossibleFileTypes = (('P','P&L File'),('K', 'Key File'),('S', 'Sales Data File'))
    #Owner = models.ForeignKey(User, editable=False)
    UniqueRunID = models.ForeignKey(RunSpace,on_delete=models.CASCADE)
    #CompanyName = models.CharField(max_length=100, blank=False)
    #RunNo = models.IntegerField(blank=False)
    #RunName = models.CharField(max_length=20,blank=True)
    FileType = models.CharField(max_length=1,choices=PossibleFileTypes,blank=False,default='K')
    FileName = models.CharField(max_length=20,blank=False)
    TheActualFile = models.FileField(blank=False)
    FileDescription = models.TextField(blank=True)